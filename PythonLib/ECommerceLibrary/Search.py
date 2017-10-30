# -*- coding: utf-8 -*-
'''
Created on 20161019

@author: yangweijia
'''
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from base import Page
from selenium.webdriver.common.by import By
import time
from time import sleep
from pdb import post_mortem

class Search(Page):
    #订单状态
    orderState_loc = (By.NAME,"sf[order_state]")
    #订单邮寄类型
    mailType_loc = (By.NAME,"sf[mail_type]")
    #订单ID
    orderId_loc = (By.NAME,"order_id")
    #商品ID或者超级商品ID
    goodsId_loc = (By.NAME,"goods_id")
    #收货人
    receiver_loc = (By.NAME,"receiver")
    #咕咚昵称
    userNick_loc = (By.NAME,"user_nick")
    #联系方式
    tel_loc = (By.NAME,"tel")
    #搜索按钮
    search_loc = (By.XPATH,"//button[@type='submit']")
    
    #输入订单ID
    def orderIdInput(self,id):
        self.find_element(*self.orderId_loc).clear()
        self.find_element(*self.orderId_loc).send_keys(id)
        time.sleep(2)
    
    #输入商品ID或者超级商品ID
    def goodsIdInput(self,id):
        self.find_element(*self.goodsId_loc).clear()
        self.find_element(*self.goodsId_loc).send_keys(id)
        time.sleep(2)
        
    #点击搜索按钮
    def searchButton(self):
        self.find_element(*self.search_loc).click()
        time.sleep(2)