#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#
#	Filename:	functional_tests.py
#	Author:		Chen Qinbo
#	Date:		11 8月2015
#	Description:	
'''
module functional_tests.py
'''
#import builtin/3rd party/other ourself
from .base import FunctionalTest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#global variables

#class define

class NewVistorTest(FunctionalTest):

    def test_can_start_a_list_and_retrieve_li_later(self):
        # Edith has heard about a cool new online to-do app. She goes
        # to check out its homepage
        self.browser.get(self.server_url)

        # She notices the page title and header mention to-do lists
        self.assertIn("To-Do", self.browser.title)
        header_text = self.browser.find_element_by_tag_name("h1").text
        self.assertIn("To-Do", header_text)

        # She is invited to enter a to-do item straight away
        inputbox = self.get_item_input_box()
        self.assertEqual(
                inputbox.get_attribute("placeholder"),
                "Enter a to-do item"
                )

        # She types "Buy peacock feathers" into a text box (Edith's hobby
        # is tying fly-fishing lures)
        inputbox.send_keys("Buy peacock feather")

        # When she hits enter, the page updates, and now the page lists
        # "1: Buy peacock feathers" as an item in a to-do list
        inputbox.send_keys(Keys.ENTER)
        edith_list_url = self.browser.current_url
        self.assertRegex(edith_list_url, "/lists/.+")
        self.check_for_row_in_list_table("1:Buy peacock feather")

        # There is still a text box inviting her to add another item. She
        # enters "Use peacock feathers to make a fly" (Edith is very methodical)
        inputbox = self.get_item_input_box()
        inputbox.send_keys("Use peacock feathers to make a fly")
        inputbox.send_keys(Keys.ENTER)

        # The page updates again, and now shows both items on her list
        self.check_for_row_in_list_table("1:Buy peacock feather")
        self.check_for_row_in_list_table("2:Use peacock feathers to make a fly")

        # now for a new user, Francis, comes along to the site
        self.browser.quit()
        self.browser = webdriver.Firefox()

        # Francis visit the home page,  There is no sign of Edith's list
        self.browser.get(self.server_url)
        page_text = self.browser.find_element_by_tag_name("body").text
        self.assertNotIn("Buy peacock feathers", page_text)
        self.assertNotIn("make a fly", page_text)

        # Francis start a new list by entring a new item.
        # He is less interesting then Edith...
        inputbox = self.get_item_input_box()
        inputbox.send_keys("Buy milk")
        inputbox.send_keys(Keys.ENTER)

        # Francis get his own uinique URL
        francis_list_url = self.browser.current_url
        self.assertRegex(francis_list_url, "/lists/.+")
        self.assertNotEqual(francis_list_url, edith_list_url)

        # Again, there is no trace of Edith's list
        page_text = self.browser.find_element_by_tag_name("body").text
        self.assertNotIn("Buy peacock feathers", page_text)
        self.assertNotIn("make a fly", page_text)
        # Edith wonders whether the site will remember her list. Then she sees
        # that the site has generated a unique URL for her -- there is some
        # explanatory text to that effect.
        # She visits that URL - her to-do list is still there.
        # Satisfied, she goes back to sleep


#function define


if __name__ == "__main__":
    #unittest.main(warnings="ignore")
    unittest.main()
