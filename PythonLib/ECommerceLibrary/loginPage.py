# -*- coding: utf-8 -*-

from base import Page
from selenium.webdriver.common.by import By
import time

class loginPage(Page):

    #定位
    login_username_loc =(By.NAME,"login[name]")
    login_password_loc =(By.NAME,"login[pwd]")
    login_submit_loc =(By.CSS_SELECTOR,"button.llv-submit")
    
    #输入用户名
    def login_username(self,username):
        self.find_element(*self.login_username_loc).clear()
        self.find_element(*self.login_username_loc).send_keys(username)
    
    #输入密码
    def login_password(self,password):
        self.find_element(*self.login_password_loc).clear()
        self.find_element(*self.login_password_loc).send_keys(password)
        
    #登录按钮
    def login_button(self):
        self.find_element(*self.login_submit_loc).click()
    
    #登录操作
    def login(self,username,pwd,url="https://admin.codoon.com/admin/html/index.html"): 
        self._open(url)
        time.sleep(2)
        self.login_username(username)
        time.sleep(2)
        self.login_password(pwd)
        time.sleep(2)      
        self.login_button()
        time.sleep(2)
        if url == "https://admin.codoon.com/admin/html/item-creator-test.html#!new":          
            self._open(url)
        
        
        
        
