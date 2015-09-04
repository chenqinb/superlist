#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
#	Filename:	authentication.py
#	Author:		Chen Qinbo
#	Date:		04 9月2015
#	Description:	
'''
module authentication.py
'''
#import builtin/3rd party/other ourself
import requests
from django.contrib.auth import get_user_model
User = get_user_model()
PERSONA_VERIFY_URL = "https://verifier.login.persona.org/verify"
DOMAIN = "localhost"
#global variables

#class define
class PersonaAuthenticationBackend(object):

    def authenticate(self, assertion):
        response = requests.post(
                PERSONA_VERIFY_URL,
                data={"assertion":assertion, "audience":DOMAIN}
        )
        if response.ok and  response.json()["status"] == "okay":
            email = response.json()["email"]
            try:
                return User.objects.get(email=email)
            except User.DoesNotExist:
                return User.objects.create(email=email)

    def get_user(self, email):

        try:
            return User.objects.get(email=email)
        except User.DoesNotExist:
            return None
