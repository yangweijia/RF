# -*- coding: utf-8 -*-
'''
Created on 20161011

@author: yangweijia
'''

from base import Page
from selenium.webdriver.common.by import By
import time


class goodsApprovePage(Page):
    url=''
    ########################################定位############################
    #商品ID输入框
    goodsId_loc = (By.NAME,"goods_id")
    #搜索按钮
    search_loc = (By.XPATH,"//button")
    #审核列表第一行的通过按钮
    pass_loc = (By.XPATH,"//span[11]/button")
    #通过弹窗的确认按钮
    confirmOfPass_loc = (By.LINK_TEXT,u"确认")
    #无更多数据的提示
    tip_loc = (By.XPATH,"/html/body/div[7]/div")
    ########################################操作############################
    #输入商品ID
    def goodsIdInput(self,goodsId):
        self.find_element(*self.goodsId_loc).send_keys(goodsId)
        time.sleep(2)
    
    #点击搜索按钮
    def searchButton(self):
        self.find_element(*self.search_loc).click()
        time.sleep(2) 
        
    #点击审核列表第一行的通过按钮
    def passButton(self):
        self.find_element(*self.pass_loc).click()
        time.sleep(2) 
        
    #点击通过弹窗的确认按钮
    def confirmOfPassButton(self):
        self.find_element(*self.confirmOfPass_loc).click()
        time.sleep(2) 
        
    #获取无更多数据的提示
    def getTip(self):
        return self.find_element(*self.tip_loc).text
    
    
    
    
