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
PERSONA_VERIFY_URL = "https://verifier.login.persona.org/verify"
DOMAIN = "localhost"
#global variables

#class define
class PersonaAuthenticationBackend(object):

    def authenticate(self, assertion):
        requests.post(
                PERSONA_VERIFY_URL,
                data={"assertion":assertion, "audience":DOMAIN}
        )

