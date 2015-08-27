#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
#	Filename:	test_forms.py
#	Author:		Chen Qinbo
#	Date:		27 8月2015
#	Description:	
'''
module test_forms.py
'''
#import builtin/3rd party/other ourself
from django.test import TestCase
from lists.forms import ItemForm, EMPTY_LIST_ERROR

#global variables

#class define
class ItemForTest(TestCase):
    
    def test_form_renders_item_text_input(self):
        form = ItemForm()
        self.assertIn('placeholder="Enter a to-do item"', form.as_p())
        self.assertIn('class="form-control input-lg"', form.as_p())

    def test_form_validation_for_blank_items(self):
        form = ItemForm(data={"text": ""})
        self.assertFalse(form.is_valid())
        self.assertEqual( form.errors["text"], [EMPTY_LIST_ERROR])
#function define
