#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
#	Filename:	test_models.py
#	Author:		Chen Qinbo
#	Date:		04 9月2015
#	Description:	
'''
module test_models.py
'''
#import builtin/3rd party/other ourself

from django.test import TestCase
from django.contrib.auth import get_user_model
User = get_user_model()
#global variables

#class define
class UserModelTest(TestCase):

    def test_user_is_valid_with_email_only(self):
        user = User(email="a@b.com")
        user.full_clean()

    def test_email_is_primary_key(self):
        user = User()
        self.assertFalse(hasattr(user, "id"))

    def test_is_authenticated(self):
        user = User()
        self.assertTrue(user.is_authenticated())
