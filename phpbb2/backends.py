# -*- coding: UTF-8 -*-
# This file is part of django-phpbb, integration between Django and phpBB
# Copyright (C) 2007-2008  Maciej Bliziński
# Modifyed for phpbb2 by Luka Blašković

import logging
from django.contrib.auth.models import User
from phpbb2.reg.models import PhpbbUsers, PhpbbDjangoUserLink
from django.utils.encoding import smart_unicode
import hashlib

from django.conf import settings

logging.basicConfig(level=logging.DEBUG)
logging.debug(str(getattr(settings, 'DEBUG', True)))
if getattr(settings, 'DEBUG', True):
    logging_level = logging.DEBUG
else:
    logging_level = logging.FATAL
logging.basicConfig(level=logging_level)

class PhpbbBackend:

    def authenticate(self, username=None, password=None):
        """Authenticate user against phpBB2 database.
        
        Check if the user exists in Django users. If not, create it.
        Then authenticate."""

        logging.debug(u"PhpbbBackend::authenticate()")
        user = None
        # phpbb 2.x encodes passwords as plain md5 hashes, no salt
        pass_md5 = hashlib.md5(password.encode("cp1250")).hexdigest()

        try:
            phpbb_user = PhpbbUsers.objects.get(username = username)
        except PhpbbUsers.DoesNotExist:
            # The user does not exist in phpBB. Bailing out.
            logging.info(u"User '%s' doesn't exist." % username)
            return None

        if phpbb_user.user_password == pass_md5:
            logging.debug(u"User %s successfully authenticated "
                         "with phpBB database." % username)
        else:
            # Invalid password
            logging.info(u"Wrong password for user %s" % username)
            return None
        # At this point we have successfully checked phpBB user password.
        # Now we're getting and returning Django user. If necessary, we're
        # creating the user on the fly.
        try:
            user = User.objects.get(username = username)
        except User.DoesNotExist:
  #          logging.info(u"Creating new Django user '%s'" % username)
            if username:
                user = User(username = smart_unicode(username, encoding="utf-8"), password = "")
                user.is_staff = False
                user.is_superuser = False
                user.email = phpbb_user.user_email
                user.save()
                PhpbbDjangoUserLink(user=user, phpbb_user=phpbb_user).save()
            else:
                logging.warning(u"User name empty. Not creating.")
                return None
        # In case the phpBB password has changed, we're updating user's
        # Django password. Django password is necessary when user wants to log
        # in to the admin interface.
        user.set_password(password)
        user.save()
        logging.debug(u"Returning user '%s'" % user)
        return user

    def get_user(self, user_id):
        user = User.objects.get(pk = user_id)
 #       logging.debug(u"get_user(): Returning user '%s'" % user)
        return user
