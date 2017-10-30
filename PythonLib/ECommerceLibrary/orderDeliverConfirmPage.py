# -*- coding: utf-8 -*-
'''
Created on 20161018

@author: yangweijia
'''
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from base import Page
from selenium.webdriver.common.by import By
import time
from time import sleep
from pdb import post_mortem

class orderDeliverConfirmPage(Page):
    #订单ID
    orderIdOfSearch_loc = (By.NAME,"order_id")
    #商品ID或者超级商品ID输入框
    goodsIdOfSearch_loc = (By.NAME,"goods_id")
    #搜索按钮
    search_loc = (By.XPATH,"//button[@type='submit']")
    #批量订单确认
    batchConfirm_loc = (By.XPATH,"//button")
    #确认批量订单
    confirmOfBatch_loc = (By.LINK_TEXT,u"确认")
    #提示
    tip_loc = (By.XPATH,"/html/body/div[3]/div/div/div[1]/span")
    #单个确认订单
    singleConfirm_loc = (By.XPATH,"//span[8]/button")
    
    #输入订单ID
    def orderIdOfSearchInput(self,id):
        self.find_element(*self.orderIdOfSearch_loc).clear()
        self.find_element(*self.orderIdOfSearch_loc).send_keys(id)
        time.sleep(2)
    
    #输入商品ID或者超级商品ID
    def goodsIdOfSearchInput(self,id):
        self.find_element(*self.goodsIdOfSearch_loc).clear()
        self.find_element(*self.goodsIdOfSearch_loc).send_keys(id)
        time.sleep(2)
        
    #点击搜索按钮
    def searchButton(self):
        self.find_element(*self.search_loc).click()
        time.sleep(2)
        
    #点击批量订单确认
    def batchConfirmButton(self):
        self.find_element(*self.batchConfirm_loc).click()
        time.sleep(2)
        
    #点击确认批量订单按钮
    def confirmOfBatchButton(self):
        self.find_element(*self.confirmOfBatch_loc).click()
        time.sleep(2)
    
    #获取提示
    def getTipText(self):
        return self.find_element(*self.tip_loc).text
    
    #点击单个确认订单
    def singleConfirmButton(self):
        self.find_element(*self.singleConfirm_loc).click()
        time.sleep(2)
    
    #获取单个确认订单的文案
    def getsingleConfirmText(self):
        return self.find_element(*self.singleConfirm_loc).text
    
    