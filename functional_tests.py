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
from selenium import webdriver
#global variables

#class define

#function define

def main():
    browser = webdriver.Firefox()
    browser.get("http://localhost:8000")

    assert "Django" in browser.title


if __name__ == "__main__":
    main()
