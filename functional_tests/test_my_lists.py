#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
#	Filename:	test_my_lists.py
#	Author:		Chen Qinbo
#	Date:		05 9月2015
#	Description:	
'''
module test_my_lists.py
'''
#import builtin/3rd party/other ourself
from django.conf import settings
from django.contrib.auth import BACKEND_SESSION_KEY, SESSION_KEY, get_user_model


from django.contrib.sessions.backends.db import SessionStore
from .base import FunctionalTest
#global variables

User = get_user_model()
#class define

class MyListTest(FunctionalTest):

    def create_pre_authenticated_session(self, email):
        user = User.objects.create(email=email)
        session = SessionStore()
        session[SESSION_KEY] = user.pk
        session[BACKEND_SESSION_KEY] = settings.AUTHENTICATION_BACKENDS[0]
        session.save()

        self.browser.get(self.server_url + "/404_no_such_url/")
        self.browser.add_cookies(dict(
            name = settings.SESSION_COOKIE_NAME,
            value = session.session_key,
            path = "/",
        ))

