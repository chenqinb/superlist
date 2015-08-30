#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
#	Filename:	forms.py
#	Author:		Chen Qinbo
#	Date:		27 8月2015
#	Description:	
'''
module forms.py
'''
#import builtin/3rd party/other ourself
from django import forms
from lists.models import Item

#global variables
EMPTY_ITEM_ERROR = "You can't have an empty list item"

#class define
class ItemForm(forms.models.ModelForm):
    class Meta:
        model = Item
        fields = ("text", )
        widgets = {
                "text": forms.fields.TextInput(attrs={
                    "placeholder": "Enter a to-do item",
                    "class": "form-control input-lg",
                    }),
                }
        error_messages = {
                "text":{"required": EMPTY_ITEM_ERROR}
                }


#function define
