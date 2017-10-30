# -*- coding: utf-8 -*-

from selenium import webdriver
from time import sleep
import time

class Page(object):
     def __init__(self):
     	self.driver = webdriver.Chrome()

     def _open(self, url):
	print "open"
	self.driver.get(url)
	print "open over"
	time.sleep(2)

     def find_element(self, *loc):
	return self.driver.find_element(*loc)

     def find_elements(self, *loc):
        return self.driver.find_elements(*loc)

     def script(self, src):
	return self.driver.execute_script(src)

     def logout(self):
        js_one = "document.querySelector('.logout').click();"
        self.script(js_one)
        time.sleep(2)

     def check(self, obj1, obj2):
	assert (obj1==obj2)
