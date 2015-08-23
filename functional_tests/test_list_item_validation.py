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

class ItemValidtionTest(FunctionalTest):
    def test_cannot_add_empty_list_items(self):

        # Edith goes to the home page and accidentally tries to submit
        # an empty list item. She hits Enter on the empty input box

        # The home page refreshes, and there is an error message saying
        # that list items cannot be blank

        # She tries again with some text for the item, which now works

        # Perversely, she now decides to submit a second blank list item

        # She receives a similar warning on the list page

        # And she can correct it by filling some text in
        # Edith goes to the home page 

        self.fail("Finish the test!")

#function define


if __name__ == "__main__":
    #unittest.main(warnings="ignore")
    unittest.main()
