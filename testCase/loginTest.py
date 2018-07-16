#!/usr/bin/env python
#coding:utf-8
import unittest

from utiity.seleniumDrive import seleniumDrive
from utiity.base import base
from utiity import conf
from utiity.log import log


class loginCase(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.logg = log()
        
    def setUp(self):
        
        self.driver = seleniumDrive('chrome').GetDrive()
        self.testbaidu = base(self.driver,conf.BaseUrl,'TestDate.yaml')

        
    def tearDown(self):
        pass
        #self.logg.info('test end')
        #self.testbaidu.quitWindow()
        #self.log.info('testlogin end')
    def testlogin(self):
        self.logg.
        self.testbaidu.openBaseUrl('百度一下 你就知道')
        self.testbaidu.elemenClick('登录')
        self.testbaidu.elementSendkeys('zhweds@163.com', 'user')
        self.testbaidu.elementSendkeys('jiangshu', 'password')
        self.testbaidu.elemenClick('登录按钮')
        self.testbaidu.waitTime(10)
        self.testbaidu.elemenClick('close')

if __name__ == '__main__':
    unittest.main()
    