from django.conf.urls import patterns, include, url
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.views.generic.simple import direct_to_template

from registration.views import register, activate
from reg.forms import *
import phpbb2.regbackend

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/register/$', 
        register, {'backend': 'phpbb2.regbackend.PhpbbBackend','form_class': PhpbbUsersForm}, 
        name='registration_register'),
     url(r'^accounts/activate/complete/$',
        direct_to_template,
        {'template': 'registration/activation_complete.html'},
        name='registration_activation_complete'),
    url(r'^accounts/activate/(?P<activation_key>\w+)/$', 
        activate, {'backend': 'phpbb2.regbackend.PhpbbBackend'},
        name='registration_activate'),
    url(r'^accounts/password/change/$',
        auth_views.password_change,
        {'password_change_form': PhpbbPasswordChangeForm},
        name='auth_password_change'),
    url(r'^accounts/password/reset/$',
        auth_views.password_reset,
        {'password_reset_form': PhpbbPasswordResetForm},
        name='auth_password_reset'),
    url(r'^accounts/password/reset/confirm/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$',
        auth_views.password_reset_confirm,
        {'set_password_form': PhpbbSetPasswordForm},
        name='auth_password_reset_confirm'),
    (r'^accounts/', include('registration.backends.default.urls')),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
   )
