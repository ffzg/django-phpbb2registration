# -*- coding: UTF-8 -*-
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from models import PhpbbDjangoUserLink
from phpbb2.reg.models import *

admin.site.unregister(User)

class PhpbbDjangoUserLinkInline(admin.StackedInline):
    model = PhpbbDjangoUserLink

class PhpbbDjangoUserLinkAdmin(UserAdmin):
    inlines = [ PhpbbDjangoUserLinkInline, ]

class PhpbbUsersAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'username', 'user_email')
    search_fields = ['user_email']

admin.site.register(User, PhpbbDjangoUserLinkAdmin)
admin.site.register(PhpbbUsers, PhpbbUsersAdmin)


