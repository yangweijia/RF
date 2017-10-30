# -*- coding: utf-8 -*-
'''
Created on 20161021

@author: yangweijia
'''
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from base import Page
from selenium.webdriver.common.by import By
import time
from time import sleep
from pdb import post_mortem

class orderReturnMsPage(Page):
    #退货
    refund_loc = (By.XPATH,"//span[11]/button")
    #确认
    confrim_loc = (By.LINK_TEXT,u"知道了")
    #提示
    tip_loc = (By.XPATH,"/html/body/div[3]/div/div/div[1]/span")
    
    #点击退货
    def refundButton(self):
        self.find_element(*self.refund_loc).click()
        time.sleep(2)
        
    #点击确认
    def confirmButton(self):
        self.find_element(*self.confrim_loc).click()
        time.sleep(2)   

    #获取提示
    def getTipText(self):
        return self.find_element(*self.tip_loc).text