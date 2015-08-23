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
#global variables

#class define

class LayoutAndStylingTest(FunctionalTest):
    def test_layout_and_styling(self):
        # Edith goes to the home page
        self.browser.get(self.server_url)
        self.browser.set_window_size(1024, 768)

        # She notices the input box is nicely centered
        inputbox = self.browser.find_element_by_id("id_new_item")
        self.assertAlmostEqual(
                inputbox.location["x"] + inputbox.size["width"] / 2,
                512,
                delta=5
                )

        # She starts a new list and sees the input is nicely
        # centered there too
        inputbox.send_keys("testing\n")
        inputbox = self.browser.find_element_by_id("id_new_item")
        self.assertAlmostEqual(
                inputbox.location["x"] + inputbox.size["width"] / 2,
                512,
                delta=5
                )

#function define


if __name__ == "__main__":
    #unittest.main(warnings="ignore")
    unittest.main()
