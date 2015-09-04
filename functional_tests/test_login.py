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

    def wait_for_element_with_id(self, element_id):
        WebDriverWait(self.browser, timeout=30).until(
                lambda b: b.find_element_by_id(element_id)
                )

    def test_login_with_persona(self):
        self.browser.get(self.server_url)
        self.browser.find_element_by_id("id_login").click()

        self.switch_to_new_window("Mozilla persona")

        self.browser.find_element_by_id(
                "authentication_email"
                ).send_keys("pingfanrenweilai@null.com")

        self.browser.find_element_by_tag_name("button").click()
        self.switch_to_new_window("To-Do")

        self.wait_for_element_with_id("id_logout")
        navbar = self.browser.find_element_by_css_selector(".navbar")
        self.assertIn("pingfanrenweilai@null.com", navbar.text)

#function define

