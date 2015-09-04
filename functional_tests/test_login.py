#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
#	Filename:	test_login.py
#	Author:		Chen Qinbo
#	Date:		03 9月2015
#	Description:	
'''
module test_login.py
'''
#import builtin/3rd party/other ourself
import time
from selenium.webdriver.support.ui import WebDriverWait
from .base import FunctionalTest

#global variables
TEST_EMAIL = "pingfanrenweilai@126.com"

#class define
class classTest(FunctionalTest):

    
    def switch_to_new_window(self, text_in_title):
        retries = 60
        while retries > 0:
            for handle in self.browser.window_handles:
                self.browser.switch_to_window(handle)
                if text_in_title in self.browser.title:
                    return
            retries -= 1
            time.sleep(0.5)
        self.fail("could not find window")


    def test_login_with_persona(self):
        self.browser.get(self.server_url)
        self.browser.find_element_by_id("id_login").click()

        self.switch_to_new_window("Mozilla Persona")

        self.browser.find_element_by_id(
                "authentication_email"
                ).send_keys(TEST_EMAIL)

        # self.browser.find_element_by_id(
                # "authentication_password"
                # ).send_keys("x")

        self.browser.find_element_by_tag_name("button").click()
        self.switch_to_new_window("To-Do")

        self.wait_to_be_logged_in(TEST_EMAIL)

        self.browser.refresh()

        self.wait_to_be_logged_in(TEST_EMAIL)

        self.browser.find_element_by_id("id_logout").click()
        self.wait_to_be_logged_out(TEST_EMAIL)
        self.browser.refresh()
        self.wait_to_be_logged_out(TEST_EMAIL)
#function define

