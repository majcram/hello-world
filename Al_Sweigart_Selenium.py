# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 15:18:06 2020

@author: Other
"""

from selenium import webdriver
browser = webdriver.Chrome()
browser.get('https://automatetheboringstuff.com')

elem = browser.find_element_by_css_selector('body > div.main > div:nth-child(1) > div:nth-child(2) > a')

elem
elem.text