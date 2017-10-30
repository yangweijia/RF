# -*- coding: utf-8 -*-
'''
Created on 20170107

@author: yangweijia
'''
from base import Page
import time

class Element(Page):

    def go_to_url(self,url):
        self.driver.get(url)
        time.sleep(2)

    def max_wind(self):
        self.driver.maximize_window()
        time.sleep(1)
