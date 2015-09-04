#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
#	Filename:	test_authentication.py
#	Author:		Chen Qinbo
#	Date:		04 9月2015
#	Description:	
'''
module test_authentication.py
'''
#import builtin/3rd party/other ourself
from unittest.mock import patch
from django.test import TestCase

from accounts.authentication import (
        PERSONA_VERIFY_URL, DOMAIN, PersonaAuthenticationBackend
)

@patch ("accounts.authentication.requests.post")
class AuthenticateTest(TestCase):
    
    def setUp(self):
        self.backend = PersonaAuthenticationBackend()

    def test_send_assertion_to_mozilla_with_domain(self, mock_post):
        self.backend.authenticate("an assertion")
        mock_post.assert_called_once_with(
                PERSONA_VERIFY_URL,
                data={"assertion": "an assertion", "audience":DOMAIN}
        )

    def test_returns_none_if_response_errors(self, mock_post):
        mock_post.return_value.ok = False
        backend = PersonaAuthenticationBackend()
        user = self.backend.authenticate("an assertion")
        self.assertIsNone(user)
