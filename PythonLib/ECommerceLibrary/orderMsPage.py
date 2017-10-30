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

class orderMsPage(Page):
    #退款或者退货
    refund_loc = (By.XPATH,"//span[8]/button")
    #选择数量
    refundNum_loc = (By.CSS_SELECTOR,"select.base-unit.select-refund-num")
    #退货公司
    mailCompany_loc = (By.NAME,"mail_company")
    #快递单号
    mailNum_loc = (By.NAME,"mail_num")
    #退款金额
    refundFee_loc = (By.NAME,"refund_fee")
    #退款原因
    refundReason_loc = (By.NAME,"reason")
    
    #完整退款确认退款
    confirmOfRefundComplete_loc = (By.XPATH,"//div[6]/button[2]")
    #部分退款确认退款
    confirmOfRefundPart_loc = (By.XPATH,"//div[7]/button[2]")
    
    #完整退款确认退货
    confirmOfReturnComplete_loc = (By.XPATH,"//div[8]/button[2]")
    #部分退款确认退货
    confirmOfReturnPart_loc = (By.XPATH,"//div[9]/button[2]")
    
    #提示
    tip_loc = (By.XPATH,"/html/body/div[3]/div/div/div[1]/span")
    #点击退款
    def refundButton(self):
        self.find_element(*self.refund_loc).click()
        time.sleep(2)
    #选择数量
    def refundNumSelec(self,*numbers):
        n = 1
        for num in numbers:
            if n==1:
                Select(self.find_element(*self.refundNum_loc)).select_by_visible_text(num)
                time.sleep(2)
            else:
                path = "//div["+str(n)+"]/div/span[8]/select"
                Select(self.driver.find_element_by_xpath(path)).select_by_visible_text(num)
                time.sleep(2)
            n=n+1
                
            
    #输入退款金额
    def refundFeeInput(self,fee):
        self.find_element(*self.refundFee_loc).send_keys(fee)
        time.sleep(2)
    #输入退款原因
    def refundReasonInput(self,reason):
        self.find_element(*self.refundReason_loc).send_keys(reason)
        time.sleep(2)
        
    #输入物流公司
    def mailCompanyInput(self,mailCompany):
        self.find_element(*self.mailCompany_loc).send_keys(mailCompany)
        time.sleep(2) 
    
    #输入退货单号
    def mailNumInput(self,mailNum):
        self.find_element(*self.mailNum_loc).send_keys(mailNum)
        time.sleep(2)  
        
    #点击确认退款
    def confirmOfRefundButton(self,completeRefund):
        if completeRefund == True:
            self.find_element(*self.confirmOfRefundComplete_loc).click()
        else:
            self.find_element(*self.confirmOfRefundPart_loc).click()           
        time.sleep(2)
    
    #点击确认退货
    def confirmOfReturnButton(self,completeRefund):
        if completeRefund == True:
            self.find_element(*self.confirmOfReturnComplete_loc).click()
        else:
            self.find_element(*self.confirmOfReturnPart_loc).click()           
        time.sleep(2)
        
    #获取提示
    def getTipText(self):
        return self.find_element(*self.tip_loc).text
    