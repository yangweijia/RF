# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from base import Page
# from models.driver import brower

class Table(Page):
        
    def table_cell(self,row,column):  
        row = row+self.start-1
        xpath = self.path +"/tr[%s]/td[%s]"%(row, column)
        return self.driver.find_element_by_xpath(xpath).text
    
    
    
    
    
    
