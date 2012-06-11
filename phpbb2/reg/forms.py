# -*- coding: UTF-8 -*-
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordResetForm, SetPasswordForm, AdminPasswordChangeForm
from django.utils.translation import ugettext as _

from registration.forms import RegistrationForm
from captcha.fields import ReCaptchaField
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Fieldset, Div

from phpbb2.reg.models import PhpbbUsers, PhpbbDjangoUserLink
import hashlib

class HoneyPotMix(RegistrationForm):
    honeypot = forms.CharField(
        label=_(u'Extra'), max_length=250, required=False,
        help_text=_(u'<strong>Please, do not fill in this field if you can see this message</strong>.'),
    )
    captcha = ReCaptchaField()

    def clean_honeypot(self):
        if self.cleaned_data['honeypot']:
            raise forms.ValidationError(_(u'Please leave this field blank.'))
        return self.cleaned_data['honeypot']

class PhpbbUsersForm(HoneyPotMix):

    user_lang = forms.ChoiceField(
        label=_('Language'), required=True,
        choices=PhpbbUsers.LANGUAGE,
    )

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_class = 'well form-horizontal'
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Fieldset(
                _(u'Registration form'),
                'username',
                'email',
                'password1',
                'password2',
                'user_lang',
                'captcha',
            ),
            Submit('submit', _(u'Register'), css_class='btn btn-primary'),
            Div('honeypot', css_class="sweet-field")
        )
        
        super(PhpbbUsersForm, self).__init__(*args, **kwargs)

    def clean_username(self):

        existing = PhpbbUsers.objects.filter(username__iexact=self.cleaned_data['username'])
        if existing.exists():
            raise forms.ValidationError(_("A user with that username already exists."))
        else:
            return self.cleaned_data['username']


class PhpbbPasswordResetForm(PasswordResetForm):

    def __init__(self, *args, **kwargs):

        self.helper = FormHelper()
        self.helper.form_class = 'well form-horizontal'
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', _(u'Reset Password'), css_class='btn btn-inverse'))
        super(PhpbbPasswordResetForm, self).__init__(*args, **kwargs)

    
    def clean_email(self):
        
        email = self.cleaned_data["email"]
        self.phpbb_users_cache = PhpbbUsers.objects.filter(user_email__iexact=email,
                                               user_active=1)

        if not len(self.phpbb_users_cache):
            raise forms.ValidationError(self.error_messages['unknown'])
            
        user_link = PhpbbDjangoUserLink.objects.filter(phpbb_user=self.phpbb_users_cache[0])
        
        if not len(user_link):
             user = User(username = self.phpbb_users_cache.username, password = "")
             user.is_staff = False
             user.is_superuser = False
             user.email = self.phpbb_users_cache.user_email
             user.save()
             PhpbbDjangoUserLink(user=user, phpbb_user=phpbb_user).save()

        # ugly stuff
        self.users_cache = User.objects.filter(email__iexact=email,
                                        is_active=True)
        return email


class PhpbbSetPasswordForm(SetPasswordForm):

    def __init__(self, *args, **kwargs):

        self.helper = FormHelper()
        self.helper.form_class = 'well form-horizontal'
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', _(u'Change password'), css_class='btn btn-danger'))
        super(PhpbbSetPasswordForm, self).__init__(*args, **kwargs)

    def save(self):

        new_user = super(PhpbbSetPasswordForm, self).save(commit=False)

        password = self.cleaned_data['new_password1']
        phpbb_user = new_user.get_profile().phpbb_user

        pass_md5 = hashlib.md5(password).hexdigest()
        phpbb_user.user_password = pass_md5
        # is this nessesary ?
        phpbb_user.save()
        # commit again
        new_user.save()        
        
        return new_user


class PhpbbPasswordChangeForm(PhpbbSetPasswordForm):
    """
    TODO: monkey patch this class, not c/p form auth

    A form that lets a user change his/her password by entering
    their old password.
    """
    error_messages = dict(SetPasswordForm.error_messages, **{
        'password_incorrect': _("Your old password was entered incorrectly. "
                                "Please enter it again."),
    })
    old_password = forms.CharField(label=_("Old password"),
                                   widget=forms.PasswordInput)

    def clean_old_password(self):
        """
        Validates that the old_password field is correct.
        """
        old_password = self.cleaned_data["old_password"]
        if not self.user.check_password(old_password):
            raise forms.ValidationError(
                self.error_messages['password_incorrect'])
        return old_password

PhpbbPasswordChangeForm.base_fields.keyOrder = ['old_password', 'new_password1',
                                           'new_password2']


class PhpbbAdminPasswordChangeForm(AdminPasswordChangeForm):
    """
    TODO
    """
    pass


class PhpbbProfile(forms.Form):
    """
    TODO: Profile form
    """
    user_attachsig = forms.ChoiceField(
        label=_('Potpis'), required=False,
        choices=PhpbbUsers.YES_NO,
        initial="Ne",
        help_text=_("Uvijek dodaj moj potpis")
    )
    user_allowhtml = forms.ChoiceField(
        label=_('HTML'), required=False,
        choices=PhpbbUsers.YES_NO,
        help_text=_("Uvijek dozvoli HTML")
    )
    user_allowbbcode = forms.ChoiceField(
        label=_('BBCode'), required=False,
        choices=PhpbbUsers.YES_NO,
        help_text=_("Uvijek dozvoli BBCode")
    )
    user_allowsmile = forms.ChoiceField(
        label=_('Smajlici'), required=False,
        choices=PhpbbUsers.YES_NO,
        help_text=_("Uvijek dozvoli Smajlice")
    )
    user_notify_pm = forms.ChoiceField(
        label=_('Privatne Poruke'), required=False,
        choices=PhpbbUsers.YES_NO,
        help_text=_("Obavijesti me kada dobijem privatnu poruku")
    )
    user_notify = forms.ChoiceField(
        label=_('Obavijesti me o odgovorima'), required=False,
        choices=PhpbbUsers.YES_NO,
        help_text=_("Kada netko odgovori na temu u kojoj (i) Vi sudjelujete, stici ce Vam e-mail")
    )
