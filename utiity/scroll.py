#!/usr/bin/env python
#coding:utf-8
class scroll():
    def __init__(self,driver):
        self.driver = driver
        #拖动滚动条到底部
    @classmethod
    def setScrollBotton(self):
        self.driver.execute_script('document.documentElement.scrollTop=10000')
   
    #拖动滚到条到顶部
    @classmethod
    def setScrollTop(self):
        self.driver.execute_script('document.documentElement.scrollTop=0')

