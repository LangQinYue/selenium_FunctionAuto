#!/usr/bin/env python
#coding:utf-8
from selenium import webdriver
import os
import sys
from webbrowser import Chrome 
reload(sys)
#sys.setprofile('function')   htmlrunner pytest nose pyunit
class seleniumDrive():
    drive = None
    def __init__(self,driveType):
        self.driveType = driveType
        self.__SetDrive()
    def __SetDrive(self,):
        if self.driveType.upper() == 'IE':
            self.drive = webdriver.Ie()
#             iedriver = "C:/Program Files/Internet Explorer/iexplore.exe"
#             os.environ['webdriver.ie.driver'] = iedriver
#             self.drive = webdriver.Ie(iedriver)
        if self.driveType.upper() == 'FIREFOX':
            B_DIR = os.path.dirname(os.path.dirname(__file__))
            fp = webdriver.FirefoxProfile()
            fp.add_extension(os.path.join(B_DIR+'\\tool','firebug-1.8.4.xpi'))#加载插件
            fp.set_preference("browser.download.folderList",2)#加载配置
            fp.set_preference("browser.download.manager.showWhenStarting",False)
            #profiles = webdriver.FirefoxProfile("C:/Documents and Settings/Administrator/Application Data/Mozilla/Firefox/Profiles/rhw9fq7m.default")
            #driver = webdriver.Firefox(profiles)
            #用于指定你所下载文件的目录
            fp.set_preference("browser.download.dir", os.getcwd())
            #下载文件类型 上面配置的都是下载文件的
            fp.set_preference("browser.helperApps.neverAsk.saveToDisk","application/octet-stream")
            self.drive = webdriver.Firefox(firefox_profile=fp)
        if self.driveType.upper() == 'CHROME':
            '''
            chromedriver = 'C:/Program Files (x86)/Google/Chrome/Application/chromedriver.exe'
            os.environ['webdriver.chrome.driver'] = chromedriver
            options = webdriver.ChromeOptions()
            options.add_argument("--user-data-dir=C:\Users\lx-lang.qinyue\AppData\Local\Google\Chrome\User Data\default")
            self.drive = webdriver.Chrome(chromedriver,chrome_options=options)
            '''
            self.drive = webdriver.Chrome()
    def GetDrive(self):
        return self.drive