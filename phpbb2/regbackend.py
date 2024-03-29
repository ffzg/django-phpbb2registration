# -*- coding: UTF-8 -*-
from django.conf import settings
from django.contrib.sites.models import RequestSite
from django.contrib.sites.models import Site

from registration import signals
from registration.forms import RegistrationForm
from registration.models import RegistrationProfile

from phpbb2.reg.models import PhpbbUsers, PhpbbDjangoUserLink
import hashlib

class PhpbbBackend(object):

    def register(self, request, **kwargs):

        username, email, password, lang = kwargs['username'], kwargs['email'], kwargs['password1'], kwargs['user_lang']
        if Site._meta.installed:
            site = Site.objects.get_current()
        else:
            site = RequestSite(request)

        new_user = RegistrationProfile.objects.create_inactive_user(username, email,
                                                                    password, site)
       
        # create phpbb2 user
        pass_md5 = hashlib.md5(password).hexdigest()
        phpbb_user = PhpbbUsers.objects.create(username=username, user_password=pass_md5, user_lang=lang, user_email=email)
        phpbb_user.save()
        
        # link users
        PhpbbDjangoUserLink(user=new_user, phpbb_user=phpbb_user).save()

        signals.user_registered.send(sender=self.__class__,
                                     user=new_user,
                                     request=request)
        return new_user

    def activate(self, request, activation_key):
        """
        Given an an activation key, look up and activate the user
        account corresponding to that key (if possible).

        After successful activation, the signal
        ``registration.signals.user_activated`` will be sent, with the
        newly activated ``User`` as the keyword argument ``user`` and
        the class of this backend as the sender.
        
        """
        activated = RegistrationProfile.objects.activate_user(activation_key)

        if activated:
            # get phpbb_user from profile
            phpbb_user = activated.get_profile().phpbb_user
            # todo: make method in models
            phpbb_user.user_active = 1
            phpbb_user.save()
            activated.save()

            signals.user_activated.send(sender=self.__class__,
                                        user=activated,
                                        request=request)
        return activated

    def registration_allowed(self, request):
        """
        Indicate whether account registration is currently permitted,
        based on the value of the setting ``REGISTRATION_OPEN``. This
        is determined as follows:

        * If ``REGISTRATION_OPEN`` is not specified in settings, or is
          set to ``True``, registration is permitted.

        * If ``REGISTRATION_OPEN`` is both specified and set to
          ``False``, registration is not permitted.
        
        """
        return getattr(settings, 'REGISTRATION_OPEN', True)

    def get_form_class(self, request):
        """
        Return the default form class used for user registration.
        
        """
        return RegistrationForm

    def post_registration_redirect(self, request, user):
        """
        Return the name of the URL to redirect to after successful
        user registration.
        
        """
        return ('registration_complete', (), {})

    def post_activation_redirect(self, request, user):
        """
        Return the name of the URL to redirect to after successful
        account activation.
        
        """
        return ('registration_activation_complete', (), {})
