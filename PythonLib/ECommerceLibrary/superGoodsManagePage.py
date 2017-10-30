# -*- coding: utf-8 -*-
'''
Created on 20161009

@author: yangweijia
'''
from selenium.webdriver.support.ui import Select
from base import Page
from selenium.webdriver.common.by import By
import time
from time import sleep
from pdb import post_mortem

class superGoodsManagePage(Page):
    url=''
    #定位
    #超级商品编辑页面的商品长名称
    supGoodsLNameOfEdit_loc = (By.NAME,"name")
    #超级商品列表的搜索输入框
    searCont_loc = (By.NAME,"sf[search]")
    #三方Boss、小Boss搜索按钮
    searchA_loc = (By.XPATH,"//button")
    #三方商户、自营管理员搜索按钮
    searchB_loc = (By.XPATH,"//form/div/button")
    #超级商品列表的生效
    effect_loc = (By.XPATH,"//button[2]")
    #确认生效
    confirmOfEffect_loc = (By.LINK_TEXT,u"确认")
    #获取超级商品编辑页面的商品长名称
    def getSupGoodsLNameOfEdit(self):
	return self.find_element(*self.supGoodsLNameOfEdit_loc).get_attribute("value")
    
    #输入搜索内容
    def searContInput(self,cont):
        self.find_element(*self.searCont_loc).clear()
        self.find_element(*self.searCont_loc).send_keys(cont)
        time.sleep(2)
          
    #点击搜索按钮
    def searchButton(self,role):
        if role == "thirdBoss" or role == "subThirdBoss":
            self.find_element(*self.searchA_loc).click()
        else:
            self.find_element(*self.searchB_loc).click()
        time.sleep(2) 
        
    #点击商品列表第一行的生效
    def effectButton(self):
        self.find_element(*self.effect_loc).click()
        time.sleep(2) 
    
    #获取商品列表第一行的生/失效的文案
    def geteffectText(self):
        return self.find_element(*self.effect_loc).text
    
    #确认生效
    def confirmOfEffect(self):
        self.find_element_by_link_text(u"确认").click()
        time.sleep(2) 
        
