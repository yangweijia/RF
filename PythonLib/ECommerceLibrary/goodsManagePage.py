# -*- coding: utf-8 -*-
from selenium.webdriver.support.ui import Select
from base import Page
from selenium.webdriver.common.by import By
import time

class goodsManagePage(Page):
    url=''
    #定位
    #快熟新增商品
    newGoodsButton_loc =(By.CSS_SELECTOR,"button.llv-submit")
    #商品名称
    goodsName_loc = (By.NAME,"l_name")
    #商品描述
    goodsDesc_loc = (By.NAME,"s_name")
    #广告
    goodsAdv_loc = (By.NAME,"adv_name")
    #SKU属性的名称
    skuDesc_loc = (By.NAME,"sku_desc")
    #每个ID限购个数
    limitCount_loc = (By.NAME,"limit_count")
    #市场价
    marketPrice_loc = (By.NAME,"market_price")
    
    #促销规则可用是
    promoteRulesTrue_loc =(By.NAME,"promote_rules")
    #促销规则可用否
    promoteRulesFalse_loc =(By.XPATH,"//div[7]/div/input[2]")
    
    #显示正品保证是
    showQualityTure_loc = (By.NAME,"show_quality")
    #显示正品保证否
    showQualityFalse_loc = (By.XPATH,"(//input[@name='show_quality'])[2]")
    
    #可用优惠券
    couponTrue_loc = (By.NAME,"can_use_coupon")
    #不可用优惠券
    couponFalse_loc = (By.XPATH,"//div[10]/div/input[2]")
    
    #新增关联
    newAssociate_loc = (By.LINK_TEXT,u"新增关联")
    
    #上传商品配图
    picUpload_loc = (By.ID,"idi_pic")
    
    #编辑详情
    detailEdit_loc = (By.LINK_TEXT,"编辑")
    
    #分类下拉框
    firstClass_loc = (By.NAME,"class_name") 
    
    #二级分类下拉框
    secondClass_loc = (By.NAME,"second_class_name")
    
    #品牌
    brand_loc = (By.XPATH,"//div[@id='J_brand_query']/input")
    
    
    
    
    
    ####SKU构建
    #SKU一级属性名
    firstAttrNam_loc = (By.NAME,"f_attr")
    #添加一级属性按钮
    addFAttr_loc = (By.ID,"addFName")
    #SKU二级属性名
    secondAttrNam_loc = (By.NAME,"s_attr")
    #添加二级属性按钮
    addSAttr_loc = (By.ID,"addSName")
    
    #要邮寄
    postTrue_loc = (By.NAME,"post")
    #不邮寄
    postFalse_loc = (By.XPATH,"//input[2]")
    
    #邮费
    postPrice_loc = (By.NAME,"post_price")
    #结算商户下拉框
    vendor_loc = (By.XPATH,"//div[2]/div/div/div[2]/div")

    
    
    #支持退回
    refundTrue_loc = (By.NAME,"can_refund")
    #三方商户不支持退货
    refundFalseThird_loc = (By.XPATH,"//div[8]/div[2]/input[2]")
    #自营商户不支持退货
    refundFalseSelf_loc = (By.XPATH,"//div[9]/div[2]/input[2]")
    
    #需要结算
    settleTrue_loc = (By.NAME,"settle_type")
    #三方商户不需要结算
    settleFalseThird_loc = (By.XPATH,"//div[9]/div[2]/input[2]")
    #自营商户不需要结算
    settleFalseSelf_loc = (By.XPATH,"//div[10]/div[2]/input[2]")    
    
    #下一步
    nextSkuConfig_loc = (By.LINK_TEXT,u"下一步")
    ################商品编辑：配置sku#####################
    #所有sku价格相同
    skuInfoBatchPrice_All_loc = (By.NAME,"price")
    #同一级属性sku价格相同
    skuInfoBatchPrice_FirAttr_loc = (By.XPATH,"//label[3]/input")
    #同二级属性sku价格相同
    skuInfoBatchPrice_SecAttr_loc = (By.XPATH,"//label[4]/input") 
    #所有sku数量相同
    skuInfoBatchNum_All_loc = (By.NAME,"num")
    #同一级属性sku数量相同
    skuInfoBatchNum_FirAttr_loc = (By.XPATH,"//div[3]/label[3]/input")
    #同二级属性sku数量相同
    skuInfoBatchNum_SecAttr_loc = (By.XPATH,"//div[3]/label[4]/input")
    
    #所有sku成本相同
    skuInfoBatchCost_All_loc = (By.NAME,"cost")
    #同一级属性sku成本相同
    skuInfoBatchCost_FirAttr_loc = (By.XPATH,"//div[4]/label[3]/input")
    #同二级属性sku成本相同
    skuInfoBatchCost_SecAttr_loc = (By.XPATH,"//div[4]/label[4]/input")
     
    #所有sku扣点相同
    skuInfoBatchRebate_All_loc = (By.NAME,"rebate")
    #同一级属性sku扣点相同
    skuInfoBatchRebate_FirAttr_loc = (By.XPATH,"//div[5]/label[3]/input")
    #同二级属性sku扣点相同
    skuInfoBatchRebate_SecAttr_loc = (By.XPATH,"//div[5]/label[4]/input")
    
    #需要结算的清空
    skuInfoBatchClear_loc = (By.XPATH,"//div[6]/span[3]")
    #需要结算的取消
    skuInfoBatchCancel_loc = (By.XPATH,"//div[6]/span[2]")
    #需要结算的确认
    skuInfoBatchConfirm_loc = (By.XPATH,"//div[6]/span") 
    #不需要结算的清空
    skuInfoBatchClearNSett_loc = (By.XPATH,"//div[4]/span[3]")
    #不需要结算的取消
    skuInfoBatchCancelNSett_loc = (By.XPATH,"//div[4]/span[2]")
    #不需要结算的确认
    skuInfoBatchConfirmNSett_loc = (By.XPATH,"//div[4]/span")
    
    #配置完毕
    ConfirmEnd_loc = (By.XPATH,"//div[3]/span")
    
    ################商品列表#####################
    #商品ID输入框
    goodsId_loc = (By.NAME,"goods_id")
    #商品长名称
    goodsLName_loc = (By.NAME,"goods_desc")
    #搜索按钮
    search_loc = (By.XPATH,"//form/div/div/button")
    #商品列表第一行的商品ID
    goodsInfoId_loc = (By.XPATH,"//p[2]/a")
    #商品列表第一行的商品长名称
    goodsInfoLName_loc = (By.XPATH,"//p")
    
    #商品列表第一行的上架
    up_loc = (By.XPATH,"//span[11]/button")
    #商品列表第一行的提交审核
    submit_loc = (By.XPATH,"//span[9]/button")
    #上架弹窗的确定
    upEnsure_loc = (By.ID,"up-ensure")
    #操作提示
    upSuc_loc = (By.XPATH,"/html/body/div[3]/div/div/div[1]/p")
    ################商品编辑页面#####################
    #商品编辑页面的商品名称
    goodsLNameOfEdit_loc = (By.NAME,"goods_name")
    #商品编辑页面的商品ID
    goodsIdOfEdit_loc = (By.CSS_SELECTOR,"div.cf_tip")
    
    
    
    
    
    

            
            
    

    
    #操作
    #点击快速新增商品
    def newGoodsButton(self):
        self.driver.find_element_by_css_selector("button.llv-submit").click()
        time.sleep(2)
        self.find_element(*self.newGoodsButton_loc).click()
        time.sleep(2)   
   
    #输入商品名称
    def goodsNameInput(self,goodsName):
        self.find_element(*self.goodsName_loc).clear()
        self.find_element(*self.goodsName_loc).send_keys(goodsName)
        time.sleep(2)
        
    #输入商品描述
    def goodsDescInput(self,goodsDesc):
        self.find_element(*self.goodsDesc_loc).clear()
        self.find_element(*self.goodsDesc_loc).send_keys(goodsDesc)
        time.sleep(2)
    
    #输入广告
    def goodsAdvInput(self,goodsAdv):
        self.find_element(*self.goodsAdv_loc).clear()
        self.find_element(*self.goodsAdv_loc).send_keys(goodsAdv)
        time.sleep(2)
        
    #输入SKU属性的名称
    def skuDescInput(self,skuDesc):
        self.find_element(*self.skuDesc_loc).clear()
        self.find_element(*self.skuDesc_loc).send_keys(skuDesc)
        time.sleep(2)
    
    #输入每个ID限购个数
    def limitCountInput(self,limitCount):
        self.find_element(*self.limitCount_loc).clear()
        self.find_element(*self.limitCount_loc).send_keys(limitCount)
        time.sleep(2)
    
    #输入市场价
    def marketPriceInput(self,marketPrice):
        self.find_element(*self.marketPrice_loc).clear()
        self.find_element(*self.marketPrice_loc).send_keys(marketPrice)
        time.sleep(2)
        
    #单选卡币规则是否可用
    def promoteRulesRadio(self,promoteRules):
        if promoteRules == False:
            pass
        else:
            self.find_element(*self.promoteRulesTrue_loc).click()
        time.sleep(2)
    
    #单选是否显示正品保证
    def showQualityRadio(self,showQuality):
        if showQuality == False:
            pass
        else:
            self.find_element(*self.showQualityTure_loc).click()
        time.sleep(2)

    #单选是否可用优惠券
    def couponRadio(self,coupon):
        if coupon == True:
            pass
        else:
            self.find_element(*self.couponFalse_loc).click()           
        time.sleep(2)    
    
    #上传m张商品配图
    def picUploadButtom(self,m,*pics):
        js="var q=document.getElementById('idi_pic').style.display='block'; "
        self.script(js)
        for pic in pics:
            self.find_element(*self.picUpload_loc).send_keys(pic)
            time.sleep(2)
            
    #配置图文详情
    def detailEditButtom(self):
        self.find_element(*self.detailEdit_loc).click()
        time.sleep(2)
    
    #编辑图文详情
    def detailEdit(self, picPath):
        driver = self.driver
        GoodsInfoWindown=driver.current_window_handle
        self.detailEditButtom()

        for handle in driver.window_handles:
            if handle !=GoodsInfoWindown:  
                driver.switch_to_window(handle)
                driver.switch_to_frame(driver.find_element_by_xpath("//div[6]/div/div/div/div/iframe"))
                driver.find_element_by_xpath("/html/body/div/form/input").send_keys(picPath)
                time.sleep(2)
                driver.switch_to_default_content()
                driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/button")
                driver.close()
                time.sleep(2)
                        
        driver.switch_to_window(GoodsInfoWindown)
    
    #下拉框选择商品一级分类
    def firstClassSelect(self,firstClass):
        Select(self.find_element(*self.firstClass_loc)).select_by_visible_text(firstClass)
        time.sleep(2)

    #下拉框选择商品二级分类
    def secondClassSelect(self,secondClass):
        Select(self.find_element(*self.secondClass_loc)).select_by_visible_text(secondClass)
        time.sleep(2)
    
    #输入商品品牌
    def brandInput(self,brand):
        self.find_element(*self.brand_loc).send_keys(brand)   
        time.sleep(2)    
    
    #新增关联按钮
    def newAssociateButtom(self):
        self.find_element(*self.newAssociate_loc).click()
        time.sleep(2)
        
    #输入一级属性名称
    def firstAttrNamInput(self,firstAttrNam):
        self.find_element(*self.firstAttrNam_loc).send_keys(firstAttrNam)
        time.sleep(2)
          
    #添加SKU一级属性
    def firstAttrAdd(self,*firstAttr):
        n=1
        for attr in firstAttr:
            self.find_element(*self.addFAttr_loc).click()
            time.sleep(1)
            if n == 1:              
                self.driver.find_element_by_xpath("//span/input").clear()
                self.driver.find_element_by_xpath("//span/input").send_keys(attr)
                time.sleep(1)
            else:
                firstAttr_loc = "//span["+str(n)+"]/input"
                self.driver.find_element_by_xpath(firstAttr_loc).clear()
                self.driver.find_element_by_xpath(firstAttr_loc).send_keys(attr) 
                time.sleep(1) 
            n=n+1              

    #输入二级属性名称
    def secondAttrNamInput(self,secondAttrNam):
        self.find_element(*self.secondAttrNam_loc).send_keys(secondAttrNam)
        time.sleep(2)
        
    #添加SKU二级属性
    def secondAttrAdd(self,*secondAttr):
        n=1
        for attr in secondAttr:
            self.find_element(*self.addSAttr_loc).click()
            time.sleep(1)
            if n == 1:              
                self.driver.find_element_by_xpath("//div[5]/div/div/span/input").clear()
                self.driver.find_element_by_xpath("//div[5]/div/div/span/input").send_keys(attr)
                time.sleep(1)
            else:
                secondAttr_loc = "//div[5]/div/div/span["+str(n)+"]/input"
                self.driver.find_element_by_xpath(secondAttr_loc).clear()
                self.driver.find_element_by_xpath(secondAttr_loc).send_keys(attr) 
                time.sleep(1) 
            n=n+1 
    
    #单选是否邮寄
    def postRadio(self,post):
        if post == True:
            pass
        else:
            self.find_element(*self.postFalse_loc).click()           
        time.sleep(2) 
        
    #输入邮费
    def postPriceInput(self,postPrice):
        self.find_element(*self.postPrice_loc).clear()
        self.find_element(*self.postPrice_loc).send_keys(postPrice) 
        time.sleep(4)
        
    #下拉框选择结算商户
    def vendorSelect(self,vendor):
        self.driver.find_element_by_xpath("//div[2]/div/div/div[2]/div[1]").click()
        time.sleep(2)
        vend = "'"+vendor+"'"
        js_one="var vendors=document.querySelectorAll('span.label');for(var i = 0;i < vendors.length;i++){if(vendors[i].innerHTML == "+vend+"){vendors[i].click();}};"   
        self.script(js_one)
        time.sleep(2)
        
        
        
    #单选是否支持退货
    def refundRadio(self,refund,role):
        if refund == True:
            pass
        else:
            if role == "thirdManage":              
                self.find_element(*self.refundFalseThird_loc).click()  
            elif role == "selfManage":
                self.find_element(*self.refundFalseSelf_loc).click()                           
        time.sleep(2)
        
    #单选是否结算
    def settleRadio(self,settle,role):
        if settle == True:
            pass
        else:
            if role == "thirdManage":              
                self.find_element(*self.settleFalseThird_loc).click()  
            elif role == "selfManage":
                self.find_element(*self.settleFalseSelf_loc).click()          
        time.sleep(2)
    
    #下一步到SKU配置按钮
    def nextSkuConfigButton(self):
        self.find_element(*self.nextSkuConfig_loc).click() 
        time.sleep(2)
        
#     #配置某个sku的价格
#     def skuPriceInput(self,firAttrNum,secAttrNum,price):
#         if firAttrNum==1 & secAttrNum==1:
#             locate = (By.XPATH,"//input")
#         elif 
            
    
    #配置某一个sku
    def skuInfoInput(self,firAttrNum,firAttrTotalNum,secAttrNum,secAttrTotalNum,price,num,skuCode,settle,cost,point):
        #普通商品
        if settle == True:
            rownum=5
        else:
            rownum=3  
        if secAttrTotalNum==0:
            if firAttrNum==1:
                self.driver.find_element_by_xpath("//input[@value='']").clear()
                self.driver.find_element_by_xpath("//input[@value='']").send_keys(price)
                time.sleep(1)

                self.driver.find_element_by_xpath("(//input[@value=''])[2]").clear()
                self.driver.find_element_by_xpath("(//input[@value=''])[2]").send_keys(num)   
                time.sleep(1)
                
                if skuCode!=None:
                    self.driver.find_element_by_xpath("(//input[@value=''])[3]").clear()
                    self.driver.find_element_by_xpath("(//input[@value=''])[3]").send_keys(skuCode) 
                    time.sleep(1)
                    
                if cost!=None:
                    self.driver.find_element_by_xpath("(//input[@value=''])[4]").clear()
                    self.driver.find_element_by_xpath("(//input[@value=''])[4]").send_keys(cost) 
                    time.sleep(1)                          
                
                if point!=None:
                    self.driver.find_element_by_xpath("(//input[@value=''])[5]").clear()
                    self.driver.find_element_by_xpath("(//input[@value=''])[5]").send_keys(point)
                    time.sleep(1)
            else:
                row = (firAttrNum-1)*rownum
                self.driver.find_element_by_xpath("(//input[@value=''])["+str(row+1)+"]").clear()
                self.driver.find_element_by_xpath("(//input[@value=''])["+str(row+1)+"]").send_keys(price)
                time.sleep(1)

                self.driver.find_element_by_xpath("(//input[@value=''])["+str(row+2)+"]").clear()
                self.driver.find_element_by_xpath("(//input[@value=''])["+str(row+2)+"]").send_keys(num) 
                time.sleep(1)  
                
                if skuCode!=None:
                    self.driver.find_element_by_xpath("(//input[@value=''])["+str(row+3)+"]").clear()
                    self.driver.find_element_by_xpath("(//input[@value=''])["+str(row+3)+"]").send_keys(skuCode) 
                    time.sleep(1)
                    
                if cost!=None:
                    self.driver.find_element_by_xpath("(//input[@value=''])["+str(row+4)+"]").clear()
                    self.driver.find_element_by_xpath("(//input[@value=''])["+str(row+4)+"]").send_keys(cost)                           
                    time.sleep(1)
                    
                if point!=None:
                    self.driver.find_element_by_xpath("(//input[@value=''])["+str(row+5)+"]").clear()
                    self.driver.find_element_by_xpath("(//input[@value=''])["+str(row+5)+"]").send_keys(point)
                    time.sleep(1)
    
        #超级商品
        else:
            if firAttrNum==1 and secAttrNum==1:
                self.driver.find_element_by_xpath("//input[@value='']").clear()
                self.driver.find_element_by_xpath("//input[@value='']").send_keys(price)
                time.sleep(1)

                self.driver.find_element_by_xpath("(//input[@value=''])[2]").clear()
                self.driver.find_element_by_xpath("(//input[@value=''])[2]").send_keys(num)   
                time.sleep(1)
                
                if skuCode!=None:
                    self.driver.find_element_by_xpath("(//input[@value=''])[3]").clear()
                    self.driver.find_element_by_xpath("(//input[@value=''])[3]").send_keys(skuCode) 
                    time.sleep(1)
                    
                if cost!=None:
                    self.driver.find_element_by_xpath("(//input[@value=''])[4]").clear()
                    self.driver.find_element_by_xpath("(//input[@value=''])[4]").send_keys(cost) 
                    time.sleep(1)                          
                
                if point!=None:
                    self.driver.find_element_by_xpath("(//input[@value=''])[5]").clear()
                    self.driver.find_element_by_xpath("(//input[@value=''])[5]").send_keys(point)
                    time.sleep(1)
            else:
                row = (firAttrNum-1)*secAttrTotalNum*rownum+(secAttrNum-1)*rownum
                self.driver.find_element_by_xpath("(//input[@value=''])["+str(row+1)+"]").clear()
                self.driver.find_element_by_xpath("(//input[@value=''])["+str(row+1)+"]").send_keys(price)
                time.sleep(1)

                self.driver.find_element_by_xpath("(//input[@value=''])["+str(row+2)+"]").clear()
                self.driver.find_element_by_xpath("(//input[@value=''])["+str(row+2)+"]").send_keys(num) 
                time.sleep(1)  
                
                if skuCode!=None:
                    self.driver.find_element_by_xpath("(//input[@value=''])["+str(row+3)+"]").clear()
                    self.driver.find_element_by_xpath("(//input[@value=''])["+str(row+3)+"]").send_keys(skuCode) 
                    time.sleep(1)
                    
                if cost!=None:
                    self.driver.find_element_by_xpath("(//input[@value=''])["+str(row+4)+"]").clear()
                    self.driver.find_element_by_xpath("(//input[@value=''])["+str(row+4)+"]").send_keys(cost)                           
                    time.sleep(1)
                    
                if point!=None:
                    self.driver.find_element_by_xpath("(//input[@value=''])["+str(row+5)+"]").clear()
                    self.driver.find_element_by_xpath("(//input[@value=''])["+str(row+5)+"]").send_keys(point)
                    time.sleep(1)
    
    #打开批量配置sku弹窗
    def skuInfoBatchButton(self,firAttrNum,firAttrTotalNum,secAttrNum,secAttrTotalNum,settle):
        if settle == True:
            rownum=7
        else:
            rownum=5  
        if  secAttrNum==0 and firAttrNum==1:
            self.driver.find_element_by_xpath("//td["+str(rownum)+"]/span").click()
            time.sleep(2)
        elif firAttrNum==1 and secAttrNum==1:
            self.driver.find_element_by_xpath("//td["+str(rownum+1)+"]/span").click()
            time.sleep(2)           
        else:
            if secAttrNum==0:
                self.driver.find_element_by_xpath("//tr["+str(firAttrNum)+"]/td["+str(rownum)+"]/span").click()
                time.sleep(2)
            else:
                row=(firAttrNum-1)*secAttrTotalNum+secAttrNum
                if secAttrNum==1:
                    self.driver.find_element_by_xpath("//tr["+str(row)+"]/td["+str(rownum+1)+"]/span").click()
                    time.sleep(2)
                else:
                    self.driver.find_element_by_xpath("//tr["+str(row)+"]/td["+str(rownum)+"]/span").click()
                    time.sleep(2)
    
    #批量配置sku价格：所有SKU价格相同
    def skuInfoBatchPrice_All(self):
        self.find_element(*self.skuInfoBatchPrice_All_loc).click()
        time.sleep(2)
        
    #批量配置sku价格：一级属性相同SKU价格相同
    def skuInfoBatchPrice_FirAttr(self):
        self.find_element(*self.skuInfoBatchPrice_FirAttr_loc).click()
        time.sleep(2)
        
    #批量配置sku价格：二级属性相同SKU价格相同
    def skuInfoBatchPrice_SecAttr(self):
        self.find_element(*self.skuInfoBatchPrice_SecAttr_loc).click()
        time.sleep(2)
    
    #批量配置sku数量：所有SKU数量相同
    def skuInfoBatchNum_All(self):
        self.find_element(*self.skuInfoBatchNum_All_loc).click()
        time.sleep(2)
        
    #批量配置sku数量：一级属性相同SKU数量相同
    def skuInfoBatchNum_FirAttr(self):
        self.find_element(*self.skuInfoBatchNum_FirAttr_loc).click()
        time.sleep(2)
        
    #批量配置sku数量：二级属性相同SKU数量相同
    def skuInfoBatchNum_SecAttr(self):
        self.find_element(*self.skuInfoBatchNum_SecAttr_loc).click()
        time.sleep(2)
    
    #批量配置sku成本：所有SKU成本相同
    def skuInfoBatchCost_All(self):
        self.find_element(*self.skuInfoBatchCost_All_loc).click()
        time.sleep(2)
        
    #批量配置sku成本：一级属性相同SKU成本相同
    def skuInfoBatchCost_FirAttr(self):
        self.find_element(*self.skuInfoBatchCost_FirAttr_loc).click()
        time.sleep(2)
        
    #批量配置sku成本：二级属性相同SKU成本相同
    def skuInfoBatchCost_SecAttr(self):
        self.find_element(*self.skuInfoBatchCost_SecAttr_loc).click()
        time.sleep(2)
    
    #批量配置sku扣点：所有SKU扣点相同
    def skuInfoBatchRebate_All(self):
        self.find_element(*self.skuInfoBatchRebate_All_loc).click()
        time.sleep(2)
        
    #批量配置sku扣点：一级属性相同SKU扣点相同
    def skuInfoBatchRebate_FirAttr(self):
        self.find_element(*self.skuInfoBatchRebate_FirAttr_loc).click()
        time.sleep(2)
        
    #批量配置sku扣点：二级属性相同SKU扣点相同
    def skuInfoBatchRebate_SecAttr(self):
        self.find_element(*self.skuInfoBatchRebate_SecAttr_loc).click()
        time.sleep(2)
    
    #批量配置sku:清空
    def skuInfoBatchClear(self,settle=True):
        if settle==False:
            self.find_element(*self.skuInfoBatchClearNSett_loc).click()
        else:
            self.find_element(*self.skuInfoBatchClear_loc).click()
        time.sleep(2)
        
    #批量配置sku:取消
    def skuInfoBatchCancel(self,settle=True):
        if settle==False:
            self.find_element(*self.skuInfoBatchCancelNSett_loc).click()
        else:
            self.find_element(*self.skuInfoBatchCancel_loc).click()
        time.sleep(2)
        
    #批量配置sku:确认
    def skuInfoBatchConfirm(self,settle=True):
        if settle==False:
            self.find_element(*self.skuInfoBatchConfirmNSett_loc).click()
        else:
            self.find_element(*self.skuInfoBatchConfirm_loc).click()
        time.sleep(2)
   
    #点击配置完毕按钮
    def ConfirmEndButton(self):
        self.find_element(*self.ConfirmEnd_loc).click()
        time.sleep(3)      
    
    ################商品编辑页面#####################
    #获取商品编辑页面的商品名称
    def getGoodsLNameOfEdit(self):
        return self.find_element(*self.goodsLNameOfEdit_loc).get_attribute("value")
    #获取商品编辑页面的商品ID
    def getGoodsIdOfEdit(self):
        return self.find_element(*self.goodsIdOfEdit_loc).text
    
    ################商品列表#####################
    #输入商品ID
    def goodsIdInput(self,goodsId):
        self.find_element(*self.goodsId_loc).send_keys(goodsId)
        time.sleep(2)
        
    #输入商品长名称
    def goodsLNameInput(self,goodsLName):
        self.find_element(*self.goodsLName_loc).send_keys(goodsLName)
        time.sleep(2)
        
    #点击搜索按钮
    def searchButton(self):
        self.find_element(*self.search_loc).click()
        time.sleep(2)    
        
    #获取商品列表第一行的商品ID  
    def getGoodsInfoId(self):
        return self.find_element(*self.goodsInfoId_loc).text
        
    #获取商品列表第一行的商品长名称
    def getGoodsInfoLName(self):
        return self.find_element(*self.goodsInfoLName_loc).text
    
    #点击商品列表第一行的上架
    def upButton(self):
        self.find_element(*self.up_loc).click()
        time.sleep(2)
    
    #点击商品列表第一行的提交审核
    def submitButton(self):
        self.find_element(*self.submit_loc).click()
        time.sleep(2)
           
    #点击上架弹窗的确定
    def upEnsureButton(self):
        self.find_element(*self.upEnsure_loc).click()
        time.sleep(2)
        
    #获取提示文案
    def upSecText(self):
        return self.find_element(*self.upSuc_loc).text
