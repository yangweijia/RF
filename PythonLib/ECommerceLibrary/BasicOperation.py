# -*- coding: utf-8 -*-
from base import Page
import time

class BasicOperation(Page):
        
    def stock_sku(self,mail,skuId,skunum):
        #入库
        #库存管理
        driver = self.driver
        driver.find_element_by_xpath("//a[2]/span").click()
        time.sleep(2)      
        if mail == True:
            #要邮寄SKU库存
            driver.find_element_by_xpath("/html/body/div[4]/div[2]/a[1]/span").click()
            time.sleep(2)
            #搜索
            driver.find_element_by_name("sf[search]").send_keys(skuId)
            time.sleep(1)
            driver.find_element_by_xpath("//*[@id='j-sf-form']/div[1]/button").click()
            time.sleep(3)       
            #入库
            driver.find_element_by_xpath("//td[12]/button").click()
            time.sleep(1)
            driver.find_element_by_name("num").clear()
            driver.find_element_by_name("num").send_keys(skunum)
            time.sleep(1)
            driver.find_element_by_xpath("//button[@type='button']").click()
            time.sleep(3) 
        else:
            #不邮寄SKU库存
            driver.find_element_by_xpath("/html/body/div[4]/div[2]/a[2]/span").click()
            time.sleep(2) 
            #搜索
            driver.find_element_by_name("sf[search]").send_keys(skuId)
            time.sleep(1)               
            driver.find_element_by_xpath("//*[@id='j-sf-form']/div[1]/button").click()
            time.sleep(3)        
            #入库                                                                              
            driver.find_element_by_xpath("//*[@id='j-stock-main']/tbody/tr/td[12]/button[1]").click()
            time.sleep(1)
            driver.find_element_by_name("num").clear()
            driver.find_element_by_name("num").send_keys(skunum)
            time.sleep(1)
            driver.find_element_by_xpath("//button[@type='button']").click()
            time.sleep(3)  
        
    def new_sku(self,goods_lname,goods_sname,limit_count,market_price,product_guarantee,sku_desc,pic,detail,*sku):
        driver = self.driver
        driver.find_element_by_xpath("//a[3]/span").click()
        
        time.sleep(2)
        driver.find_element_by_xpath("/html/body/div[5]/div[2]/a[1]/span").click()
        time.sleep(2)
        driver.find_element_by_xpath("/html/body/div[1]/div/a[1]/button").click()
        time.sleep(2)
        
        driver.find_element_by_css_selector("textarea.pgoods-setting-long-name.base-unit").clear()
        driver.find_element_by_css_selector("textarea.pgoods-setting-long-name.base-unit").send_keys(goods_lname)
        time.sleep(2)
        
        driver.find_element_by_css_selector("textarea.base-unit.pgoods-setting-short-name").clear()
        driver.find_element_by_css_selector("textarea.base-unit.pgoods-setting-short-name").send_keys(goods_sname)
        time.sleep(2)
        #每个ID限购次数
        driver.find_element_by_xpath("/html/body/div[1]/div/textarea[3]").clear()
        driver.find_element_by_xpath("/html/body/div[1]/div/textarea[3]").send_keys(limit_count)
        time.sleep(2)
        #市场价
        driver.find_element_by_xpath("(//textarea[@id=''])[4]").clear()
        driver.find_element_by_xpath("(//textarea[@id=''])[4]").send_keys(market_price)
        time.sleep(2)
        #是否显示正品保证
        if product_guarantee == True:
            driver.find_element_by_xpath("/html/body/div[1]/div/input[1]").click()
            time.sleep(1)
        else:
            pass
        #关联SKU
        for item in sku:
            driver.find_element_by_xpath("//button").click()
            time.sleep(2)
            driver.find_element_by_name("sku_id").clear()
            driver.find_element_by_name("sku_id").send_keys(item)
            driver.find_element_by_xpath("//button[@type='button']").click()
            time.sleep(2)
        #商品SKU描述文案
        driver.find_element_by_css_selector("input.base-unit").clear()
        driver.find_element_by_css_selector("input.base-unit").send_keys(sku_desc)
        #商品配图
        js_string="var q=document.getElementById('upload').style.display='block'"
        driver.execute_script(js_string)
        driver.find_element_by_id("upload").clear()
        driver.find_element_by_id("upload").send_keys(pic)
        time.sleep(4)
        #图文详情
        if detail == False:
            pass
        else:
            windownbefore=driver.window_handles
            driver.find_element_by_xpath("//div[12]/a/button").click()
            time.sleep(4)
            
            for handle in driver.window_handles:
                driver.switch_to_window(handle)
                if driver.title == u'商品管理':
                    pass
                    time.sleep(2)
                else:     
                    driver.switch_to_frame(driver.find_element_by_xpath("//div[6]/div/div/div/div/iframe"))
                    driver.find_element_by_xpath("/html/body/div/form/input").send_keys(u"C:\\Users\\yangweijia\\Pictures\\jpg\\6619393151235890154.jpg")
                    time.sleep(2)
                    driver.switch_to_default_content()
                    driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/button")
                    driver.close()
                    time.sleep(5)
        
            driver.switch_to_window(driver.window_handles)
            
        driver.find_element_by_xpath("/html/body/div[1]/div/div[12]/button[1]").click()
        time.sleep(5)
    
    def add_list_num(self,goodsId,addNum):
        #补充上架数量
        
        driver = self.driver
        driver.find_element_by_css_selector("a.goods_ms > span").click()
        time.sleep(1)                     
        driver.find_element_by_xpath("//div[2]/a[1]/span").click()
        time.sleep(1)
        driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/input[2]").send_keys(goodsId)
        time.sleep(1)
        driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/button").click()
        time.sleep(1)
        
        driver.find_element_by_xpath("//td[11]/a/button").click()
        time.sleep(2)
        driver.find_element_by_xpath("//button[2]").click()
        time.sleep(1)
        driver.find_element_by_name("update_count").send_keys(addNum)
        time.sleep(1)
        driver.find_element_by_xpath("//button[@type='button']").click()
        time.sleep(4)
        driver.find_element_by_xpath("//div[12]/button").click()
        time.sleep(3)    
    
    def goods_search(self,goodsId):
        driver = self.driver
        #商品管理
        driver.find_element_by_xpath("//a[3]/span").click()
        time.sleep(2)
        #商品
        driver.find_element_by_xpath("//div[2]/a/span").click()
        time.sleep(2)
        #输入商品ID                   
        driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/input[2]").send_keys(goodsId)
        time.sleep(1)
        #搜索                                                                          
        driver.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/button").click()
        time.sleep(2)
        
    def sku_search(self,skuId):
        driver = self.driver
        driver.find_element_by_xpath("//a[3]/span").click()
        time.sleep(2)
        driver.find_element_by_xpath("//div[2]/a[2]/span").click()
        time.sleep(2)
        driver.find_element_by_id("sku_id").send_keys(skuId)
        time.sleep(1)
        driver.find_element_by_xpath("//button").click()
        time.sleep(2)
