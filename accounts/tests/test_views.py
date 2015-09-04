#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
#	Filename:	test_views.py
#	Author:		Chen Qinbo
#	Date:		04 9月2015
#	Description:	
'''
module test_views.py
'''
#import builtin/3rd party/other ourself
from django.test import TestCase
from unittest.mock import patch

#global variables

#class define
class LoginViewTest(TestCase):
    
    @patch("accounts.views.authenticate")
    def test_calls_authenticate_with_assertion_from_post(self, mock_authenticate):
        mock_authenticate.return_value = None
        self.client.post("/accounts/login", {"assertion":"assert this"})
        mock_authenticate.assert_called_once_with(assertion="assert this")

#function define
