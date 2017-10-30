# -*- coding: utf-8 -*-
from selenium import webdriver
from base import Page
from selenium.webdriver.common.by import By
import time
from time import sleep

class brandManagePage(Page):
    url=''
    #定位
    brandManage_newBrand_loc =(By.XPATH,"//button")
    brandManage_brandName_loc =(By.XPATH,"//input[@value='']")
    brandManage_uploadPic_loc =(By.ID,"idi_pic")
    brandManage_brandNick_loc =(By.XPATH,"(//input[@value=''])[2]")
    brandManage_AddbrandNick_loc = (By.XPATH,"//div[2]/button")
    brandManage_save_loc = (By.CSS_SELECTOR,"div.cf_i.action_sec > button.btn.btn-default")
    
    brandManage_newBrand_success_hint_loc = (By.XPATH,"/html/body/div[3]/div/div/div[1]/span")
    #点击新建品牌
    def brandManage_newBrand(self):
        self.find_element(*self.brandManage_newBrand_loc).click()
        sleep(2)
    
    #输入品牌名   
    def brandManage_brandName(self,brandName):
        self.find_element(*self.brandManage_brandName_loc).clear()
        self.find_element(*self.brandManage_brandName_loc).send_keys(brandName)
    
    #上传品牌配图
    def brandManage_uploadPic(self,pic):
        js="var q=document.getElementById('idi_pic').style.display='block'; "
        self.script(js)
        self.find_element(*self.brandManage_uploadPic_loc).send_keys(pic)
        time.sleep(8)
        
    #输入品牌别名
    def brandManage_brandNick(self,nick):
        self.find_element(*self.brandManage_brandNick_loc).clear()
        self.find_element(*self.brandManage_brandNick_loc).send_keys(nick)
        time.sleep(5)
    
    #添加品牌别名
    def brandManage_AddbrandNick(self): 
        self.find_element(*self.brandManage_AddbrandNick_loc).click()
        time.sleep(2)
        
    #点击保存
    def brandManage_save(self): 
        self.find_element(*self.brandManage_save_loc).click()
        time.sleep(2)
        
    #创建成功提示
    def  brandManage_newBrand_success(self):
        return self.find_element(*self.brandManage_newBrand_success_hint_loc).text
        
        