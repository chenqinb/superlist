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
from lists.forms import (DUMPLICATE_ITEM_ERROR, EMPTY_ITEM_ERROR,
        ExistingListItemForm, ItemForm)
from lists.models import Item, List

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
        self.assertEqual( form.errors["text"], [EMPTY_ITEM_ERROR])

    def test_form_save_handles_saving_to_a_list(self):
        list_ = List.objects.create()
        form = ItemForm(data = {"text":"do me"})
        new_item = form.save(for_list = list_)
        self.assertEqual(new_item, Item.objects.first())
        self.assertEqual(new_item.text, "do me")
        self.assertEqual(new_item.list, list_)

class ExistingListItemFormText(TestCase):
    
    def test_form_renders_item_text_input(self):
        list_ = List.objects.create()
        form = ExistingListItemForm(for_list = list_)
        self.assertIn('placeholder="Enter a to-do item"', form.as_p())

    def test_form_validation_for_blank_items(self):
        list_ = List.objects.create()
        form = ExistingListItemForm(for_list=list_, data={"text":""})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors["text"], [EMPTY_ITEM_ERROR])

    def test_form_validation_for_duplicate_items(self):
        list_ = List.objects.create()
        Item.objects.create(list=list_, text="no twins!")
        form = ExistingListItemForm(for_list=list_, data={"text":"no twins!"})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors["text"], [DUMPLICATE_ITEM_ERROR])
#function define
