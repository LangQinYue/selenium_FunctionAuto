#!/usr/bin/env python
#coding:utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException,NoAlertPresentException
import os,datetime,time,xlrd
from selenium.webdriver.support.select import Select
from utiity import conf
from selenium.webdriver.common.by import By
from readYaml import readYaml
from utiity.log import log
from selenium.webdriver.support.expected_conditions import presence_of_element_located, visibility_of_element_located

from selenium.common.exceptions import NoSuchFrameException,NoAlertPresentException,NoSuchWindowException
from utiity.readXml import xmlUtils
import sys
reload(sys)
sys.getdefaultencoding()
class base(object):
    flag = False
    def __init__(self,driver,baseurl,filename):
        #self.driver = driver
        self.driver = driver
        self.baseurl = baseurl
        self.B_DIR = os.path.dirname(os.path.dirname(__file__))
        self.yaml_dict = readYaml(filename).readYaml()
        self.readXml = xmlUtils()
        self.log = log()
        if 'HTTP_PROXY'in os.environ: 
            del os.environ['HTTP_PROXY']
            
    def openBaseUrl(self,pagetitle):
        self.driver.get(self.baseurl)
        self.driver.maximize_window()
        #assert self.getUrlTital(pagetitle), u"打开开页面失败 %s" % self.baseurl
   
    #检查窗口是否打开 通过title验证
    def onPageTitle(self,pagetitle):
        return pagetitle in self.driver.title
    

    

    def getby(self,by):
        getby_dict = {'ID':By.ID,
             'CLASS_NAME':By.CLASS_NAME,
             'CSS_SELECTOR':By.CSS_SELECTOR,
             'LINK_TEXT':By.LINK_TEXT,
             'NAME':By.NAME,
             'PARTIAL_LINK_TEXT':By.PARTIAL_LINK_TEXT,
             'TAG_NAME':By.TAG_NAME,
             'XPATH':By.XPATH
             }
        try:
            if by.upper() in getby_dict:
                self.bytype = getby_dict[by.upper()]
            return self.bytype
        except Exception:
            print by+'not found'
    
    #获取元素   
    def find_element(self,by,value): 
        by = self.getby(by)
        try:
            WebDriverWait(self.driver, 10).until(lambda driver:driver.find_element(by,value))
            conf.flag = True
        except Exception,e:
            pass
        if conf.flag:
            return self.driver.find_element(by,value)
    
    #获取一组元素
    def find_elements(self,by,value):
        #return self.driver.find_element(*loc)
        by = self.getby(by)
        try:
            WebDriverWait(self.driver,10).until(lambda driver:driver.find_elements(by,value))
            conf.flag = True
        except Exception:
            pass
        if conf.flag:
            return self.driver.find_elements(by,value)
   
    #获取当前页面的title
    def getTital(self,):
        return self.driver.title
    
    #获取当前页面地址
    def getUrl(self,):
        return self.driver.current_url

    def readkey(self,key):
        key = key.decode('utf-8')
        return self.yaml_dict[key].split(',')[0],self.yaml_dict[key].split(',')[1]
    
    #鼠标悬浮
    def elementMoveTo(self,key):
#         try:
#             element = self.find_element(*locat)
#         except Exception:
#             self.saveScreenshot(locat, conf.flag) 
#         ActionChains(self.driver).move_to_element(element).perform()
        (by,value) = self.readkey(key)
        element = self.find_element(by,value)
        if conf.flag:
            ActionChains(self.driver).move_to_element(element).perform()
            conf.flag = False
        else:
            self.saveScreenshot(key, False)
    #鼠标单击
    def elemenClick(self,key):
        (by,value) = self.readkey(key)
        #(by,value) = self.readXml.readXml(key)
        element = self.find_element(by,value)
        if conf.flag:
            element.click()
            conf.flag = False
        else:
            self.saveScreenshot(key, conf.flag)
            self.log.errorInfo(key)

    #鼠标双击
    def elementDoubleClick(self,key):
        (by,value) = self.readkey(key)
        element = self.find_element(by,value)
        if conf.flag:
            ActionChains(self.driver).double_click(element).perform()
            conf.flag = False
        else:
            self.saveScreenshot(key, conf.flag)
            self.log.errorInfo(key)
  
    #鼠标右击
    def elementContextClick(self,key):
        (by,value) = self.readkey(key)
        element = self.find_element(by,value)
        if conf.flag:
            ActionChains(self.driver).context_click(element).perform()
            conf.flag = False
        else:
            self.saveScreenshot(key, conf.flag)
            self.log.errorInfo(key)   
    #输入数据
    def elementSendkeys(self,input,key):
#         try:
#             if click:
#                 self.find_element(*locat).click()
#             if clear:
#                 self.find_element(*locat).clear()
#             self.find_element(*locat).send_keys(input)
#         except NoSuchElementException:
#             self.saveScreenshot(locat, conf.flag)
        (by,value) = self.readkey(key)
        element = self.find_element(by,value)
        if conf.flag:
            element.send_keys(input)
            conf.flag = False
        else:
            self.saveScreenshot(key, conf.flag)
            self.log.errorInfo(key)
    #清掉输入框数据
    def elementClear(self,key):
        (by,value) = self.readkey(key)
        element = self.find_element(by,value)
        if conf.flag:
            element.clear()
            conf.flag = False
        else:
            self.saveScreenshot(key, conf.flag)
            self.log.errorInfo(key)
    #获取元素属性
    def elementGetAttribute(self,key,type):
        (by,value) = self.readkey(key)
        element = self.find_element(by,value)
        if conf.flag:
            attr = element.get_attribute(type)
            conf.flag = False
            return attr
        else:
            self.saveScreenshot(key, conf.flag)
            self.log.errorInfo(key)

    #发送文件
    def sendFile(self,file,key):
        (by,value) = self.readkey(key)
        element = self.find_element(by,value)

        if conf.flag:
            element.send_keys(file)
            conf.flag = False
        else:
            self.saveScreenshot(key, conf.flag)
            self.log.errorInfo(key)
            
    #切换到新窗口
    def switchToWindow(self,):
        curr_window = self.driver.current_window_handle
        #print curr_window+'3333'
        handles = self.driver.window_handles
        #print handles
        for handle in handles:
            if handle != curr_window:
                self.driver.switch_to_window(handle)
                #print handle+'111111111'
                
    def switchToFrameById(self,FrameId):
        try:
            self.driver.switch_to_frame(FrameId)
        except NoSuchFrameException,e:
            self.log.errorInfo(e,0)
            self.log.errorInfo(FrameId)
  
    def switchToFrameByIndex(self,IndexId):
        try:
            self.driver.switch_to_frame(IndexId)
        except NoSuchFrameException,e:
            self.log.errorInfo(e,0)
            self.log.errorInfo(IndexId)
    def switchToDefaultFrame(self):
        self.driver.switch_to_default_content()
 
    #对话框 点击确定 回到主窗口
    def alertAccept(self):
        #self.driver.switch_to_alert().accept()
        self.waitTime(3)
        try:
            self.driver.switch_to_alert().accept()
        except NoAlertPresentException,e:
            self.saveScreenshot('alert', False)
            self.log.errorInfo(e, 0)
#         try:
#             self.driver.switch_to_default_content()
#         except:
#             pass
    #对话框 点击取消 回到主窗口
    def alertDismiss(self):
        self.waitTime(3)
        try:
            self.driver.switch_to_alert().dismiss()
        except NoAlertPresentException,e:
            self.saveScreenshot('alert', False)
            self.log.errorInfo(e, 0)
    #获取对话框文本内容
    def alertText(self):
        self.waitTime(3)
        try:
            return self.driver.switch_to_alert().text()
        except NoAlertPresentException,e:
            self.log.errorInfo(e, 0)
        
  #刷新页面
    def refresh(self):
        self.driver.refresh()
 
    def quitWindow(self):
        self.driver.quit()

    def closeWindow(self):
        self.driver.close()
    
    #执行JS语句
    def excuteScript(self,script):
        self.driver.execute_script(script)

    def checkboxAll(self,elements,key):
        (by,value) = self.readkey(key)
        elements = self.find_elements(by,value)
        if conf.flag:
            for element in elements:
                if element.GetAttribute('type') =='checkbox':
                    element.click()
        else:
            self.saveScreenshot(key, False)
            self.log.errorInfo(key)
 
    def selectByText(self,text,key):
#         try:
#             select =Select( self.find_element(*locat) )
#             select.select_by_visible_text(text)
#         except NoSuchElementException,e:
#             print e
        (by,value) = self.readkey(key)
        element = self.find_element(by,value)
        if conf.flag:
            select = Select(element)
            select.select_by_visible_text(text)
        else:
            
            self.saveScreenshot(key, False)
            self.log.errorInfo(key)
  
    def selectByValue(self,value,key):
        (by,value) = self.readkey(key)
        element = self.find_element(by,value)
        if conf.flag:
            select = Select(element)
            select.select_by_value(value)
        else:
            self.saveScreenshot(key, False)
            self.log.errorInfo(key)
            
    def selectByIndex(self,index,key):
        (by,value) = self.readkey(key)
        element = self.find_element(by,value)
        if conf.flag:
            select = Select(element)
            select.select_by_index(index)
        else:
            self.saveScreenshot(key, False)
            self.log.errorInfo(key)
    #获取当前系统时间
    def getSystemTime(self):
        return datetime.datetime.now().__format__('%Y-%m-%d %H-%M-%S')
    
    # 生成截图文件名
    def savePngName(self,name):
        day = time.strftime('%Y-%m-%d',time.localtime(time.time()))
        fp = 'result\\' + day + '\\image'
        tm = self.getSystemTime()
        type = '.png'
        if os.path.exists(fp):
            filename = str(fp) + '\\' +str(tm) + str('_') +str(name) +str(type)
            return filename
        else:
            os.makedirs(fp)
            filename = str(fp) + '\\' +str(tm) + str('_') +str(name) +str(type)
            return filename
    def saveScreenshot(self,name,isSucceed):
        if isSucceed:
            pass
        else :
            self.driver.save_screenshot(self.savePngName(name))
            #self.quitWindow()
    def waitTime(self,seccond):
        time.sleep(seccond)
    def is_element_present(self, key):
        (by,value) = self.readkey(key)
#         try: 
#             self.find_element(by, value)
#         except NoSuchElementException: 
#             return False
#         return True
        element = self.find_element(by, value)
        if element:
            return True
        else:
            return False
    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException:
            return False
        return True
		# 判断jQuery是否加载 
	def jQueryLoad(self): 
		res = False
		try:
			res = self.driver.execute_script('return jQuery()!=null')
		except Exception, e:
			res = False

	return res

	# 注入jQuery 
	def injectJQuery(self): 
		jqueryLibJs = '''
		var headID = document.getElementsByTagName("head")[0];
		var newScript = document.createElement("script");
		newScript.type = "text/javascript";
		newScript.src = "http://code.jquery.com/jquery-1.11.1.min.js";
		headID.appendChild(newScript);
		'''

		self.driver.execute_script(jqueryLibJs)


	#判断是否有必要注入jquery 
	def injectJQueryIfNeed(self): 
	if not jQueryLoad(driver):
		print 'inject jQuery ...'
		injectJQuery(self.driver)
	else:
		print 'no need to inject jquery...'

	def wait_for_ajax(driver, timeout=5, increment=0.4): 
		timeSum = 0

		while 1:
			print 'check jQuery status ....'
			res = self.driver.execute_script('return jQuery.active == 0')
			print 'check jQuery status return....'
			if res:
				break
    def setTable(self,filepath,sheetname):
        try:
            data = xlrd.open_workbook(filepath)
        except:
            print u'打开文件出错'
        table = data.sheet_by_name(sheetname)
        return table
    #读取xls表格 使用生成器
    def getTabledata(self,filepath,sheetname):
        table = self.setTable(filepath, sheetname)
        for args in range(1,table.nrows):
            yield table.row_values(args)
    def getcelldata(self,filepath,sheetname,RowNum,ColNum):
        table = self.setTable(filepath, sheetname)
        celldata = table.cell_value(RowNum,ColNum)
        return celldata
    '''
    def scroll_to_element(self, *locator):
        """Scroll to element"""
        el = self.selenium.find_element(*locator)
        self.selenium.execute_script("window.scrollTo(0, %s)" % (el.location['y'] + el.size['height']))
    '''
    def switch_to_window(self, partial_url='', partial_title=''):
        '''切换窗口
            如果窗口数<3,不需要传入参数，切换到当前窗口外的窗口；
            如果窗口数>=3，则必须传入参数来确定要跳转到哪个窗口
        '''
        all_windows = self.driver.window_handles
        flag = 0
        if len(all_windows) == 1:
            print 'only 1 window!'
        elif len(all_windows) == 2:
            other_window = all_windows[1-all_windows.index(self.current_window)]
            self.driver.switch_to.window(other_window)
            flag = 1
        else:
            for window in all_windows:
                self.driver.switch_to.window(window)
                if not partial_url and not partial_title:
                    raise ParameterError('窗口多于三个，请传入参数定位window！')
                elif partial_url and partial_title and partial_url in self.driver.current_url and partial_title in self.driver.title:
                    flag = 1
                    break
                elif not partial_title and partial_url in self.driver.current_url:
                    flag = 1
                    break
                elif not partial_url and partial_title in self.driver.title:
                    flag = 1
                    break
        if flag:
            print self.driver.current_url, self.driver.title
        else:
            raise ParameterError('并无匹配的窗口，请检查传入参数！')
    
    
