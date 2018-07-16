#!/usr/bin/env python
#coding:utf-8
import unittest
from utiity.seleniumDrive import seleniumDrive
from utiity.base import base
from utiity import conf
from mock import DEFAULT
from unittest.loader import defaultTestLoader
import HTMLTestRunner

class TestCase(unittest.TestCase):

    def setUp(self):
        self.d = seleniumDrive('chrome').GetDrive()
        self.driver = base(self.d,conf.BaseUrl,'TestDate.yaml')
    def tearDown(self):
        self.driver.quitWindow()

    def testMet1(self):
        u'''baidu搜索'''
        self.driver.openBaseUrl('pagetitle')
        self.driver.elemenClick('登录链接')
#         try:
#             self.assertTrue(self.driver.is_element_present('close'),'fail')
#         except AssertionError,e:
#             print e
        #self.assertTrue(self.driver.is_element_present('close'),'fail')
def suit():
    '''
#         suite = unittest.TestSuite()
#         suite.addTest(TestCase('testMet1'))
#         return suite
        #第二种
        #return unittest.makeSuite(TestCase, "test")#要测试的方法名都以test开头
    '''
    testunit = unittest.TestSuite()
    testunit.addTest(unittest.makeSuite(TestCase.testMet1))
if __name__ == '__main__':
    #第一种
    #unittest.main() #要测试的方法名都以test开头
    #第二种
    #unittest.main(defaultTest = 'suit')
    '''
            另一种执行方式：
    suite = unittest.TestSuite()
    suite.addTest(Mytest("test_add"))
    suite.addTest(Mytest("test_add2"))
    suite.addTest(Mytest("test_add3"))
    # 执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)
    '''
    testunit = unittest.TestSuite()
    testunit.addTest(unittest.makeSuite(TestCase.testMet1))
    run = unittest.TextTestRunner()
    run.run(testunit)
    '''
    filename = 'D:\\eclipsworkdir\\lang\\testCase\\report.html'
    fp = file(filename,'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
        stream=fp,
        title=u'百度搜素报告',
        description =u'用例执行情况' )
    runner.run(testunit)
    fp.close()
    '''