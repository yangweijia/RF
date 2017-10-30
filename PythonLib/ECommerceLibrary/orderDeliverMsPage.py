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

class orderDeliverMsPage(Page):
    #订单ID
    orderIdOfSearch_loc = (By.NAME,"order_id")
    #商品ID或者超级商品ID输入框
    goodsIdOfSearch_loc = (By.NAME,"goods_id")
    #搜索按钮
    search_loc = (By.XPATH,"//button[@type='submit']")
    #批量发货导出
    batchDeliver_loc = (By.XPATH,"//button")
    #确认批量发货导出
    confirmOfBatch_loc = (By.XPATH,"/html/body/div[3]/div/div/div[2]/a[2]")
    #导出
    export_loc = (By.XPATH,"//button[2]")
    #发货按钮
    deliver_loc = (By.XPATH,"//span[8]/button")
    #选择数量
    numSelect_loc = (By.CSS_SELECTOR,"select.base-unit.select-deliver-num")
    #快递公司
    mailCompany_loc = (By.NAME,"mail_company")
    #快递费用
    mailCost_loc = (By.NAME,"mail_cost")
    #快递单号
    mailCode_loc = (By.NAME,"mail_code")
    #确认按钮
    confirmOfDeliver_loc = (By.XPATH,"//p[5]/button")
    #提示
    tip_loc = (By.ID,"J_tip")
    
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
        
    #点击批量发货导出
    def batchConfirmButton(self):
        self.find_element(*self.batchDeliver_loc).click()
        time.sleep(2)
        
    #点击导出
    def exportButton(self):
        self.find_element(*self.export_loc).click()
        time.sleep(2)
        
    #点击确认批量订单按钮
    def confirmOfBatchButton(self):
        self.find_element(*self.confirmOfBatch_loc).click()
        time.sleep(2)
        
    #点击发货按钮
    def deliverButton(self):
        self.find_element(*self.deliver_loc).click()
        time.sleep(2)
    
    #选择数量
    def numSelect(self,num):
        Select(self.find_element(*self.numSelect_loc)).select_by_visible_text(str(num))
        time.sleep(2)
        
    #输入快递公司
    def mailCompanyInput(self,mailCompany):
        self.find_element(*self.mailCompany_loc).clear()
        self.find_element(*self.mailCompany_loc).send_keys(mailCompany)
        time.sleep(2)
    
    #输入快递费用
    def mailCostInput(self,mailCost):
        self.find_element(*self.mailCost_loc).clear()
        self.find_element(*self.mailCost_loc).send_keys(mailCost)
        time.sleep(2)
    
    #输入快递单号
    def mailCodeInput(self,mailCode):
        self.find_element(*self.mailCode_loc).clear()
        self.find_element(*self.mailCode_loc).send_keys(mailCode)
        time.sleep(2)
        
    def confirmOfDeliverButton(self):
        #点击确认按钮
        self.find_element(*self.confirmOfDeliver_loc).click()
        time.sleep(2)
        
    
    def getTipText(self):
        #获取提示文案
        return self.find_element(*self.tip_loc).text