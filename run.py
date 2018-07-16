#!/usr/bin/env python
#coding:utf-8
import unittest
import HTMLTestRunner
import os ,time,datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
baseDir = os.path.dirname(os.path.abspath(__file__))
testDir = os.path.join(baseDir+'\\testCase')
reportDir = os.path.join(baseDir+'\\log')
#=============定义发送邮件==========
def sentmail(file_new):
    #发信邮箱
    mail_from='langqinyue@letshare.com.cn'
    #收信邮箱
    mail_to='zhweds@yeah.net'
    #定义正文
    f = open(file_new, 'rb')
    mail_body = f.read()
    f.close()
    msg=MIMEText(mail_body,_subtype='html',_charset='utf-8')
    #定义标题 汤绍
    msg['Subject']=u"百度测试报告"
    #定义发送时间（不定义的可能有的邮件客户端会不显示发送时间）
    msg['date']=time.strftime('%a, %d %b %Y %H:%M:%S %z')
    smtp=smtplib.SMTP()
    #连接 SMTP 服务器，此处用的126的 SMTP 服务器
    smtp.connect('smtp.idccenter.net')
    #用户名密码
    smtp.login('langqinyue@letshare.com.cn','@88888')
    smtp.sendmail(mail_from,mail_to,msg.as_string())
    smtp.quit()
    print 'email has send out !'
#======查找测试报告目录，找到最新生成的测试报告文件====
def sendreport():
    #result_dir = 'D:\\selenium_python\\report'
    lists=os.listdir(reportDir)
    lists.sort(key=lambda fn: os.path.getmtime(reportDir+"\\"+fn) if not
    os.path.isdir(reportDir+"\\"+fn) else 0)
    #print (u'最新测试生成的报告： '+lists[-1])
    #找到最新生成的文件
    file_new = os.path.join(reportDir,lists[-1])
    #print file_new
    #调用发邮件模块
    sentmail(file_new)
#============测试用例组装测试套件=========
def creatsuit():
    testunit = unittest.TestSuite()
    discover =  unittest.defaultTestLoader.discover(testDir, pattern='*.py', top_level_dir=None)
    for testsuit in discover:
        for testcase in testsuit:
            testunit.addTest(testcase)
    return testunit
	'''
	unittest.TestLoader().loadTestsFromName(testCase)

	testCase 如  "user.UserTestCase.test_login"  则执行user文件里面UserTestCase类里面的test_login方法

	看下unittest即可
	'''
	
#==========定义并生成测试报告========

if __name__ == "__main__":
    now = time.strftime(' %Y-%m-%d-%H-%M-%S ',time.localtime(time.time()))
    filename = os.path.join(reportDir,now+'report.html')
    fp = file(filename,'wb')
    runner = HTMLTestRunner.HTMLTestRunner(
    stream=fp,
    title=u'百度测试报告',
    description =u'用例执行情况' )
    #执行测试用例
    runner.run(creatsuit())
    fp.close() #关闭生成的报告
    #执行发邮件
    #sendreport()
		'''
		# 指定测试用例为当前文件夹下的 interface 目录
		test_dir = './interface'
		discover = unittest.defaultTestLoader.discover(test_dir, pattern='*_test.py')


		if __name__ == "__main__":
		    test_data.init_data() # 初始化接口测试数据

		    now = time.strftime("%Y-%m-%d %H_%M_%S")
		    filename = './report/' + now + '_result.html'
		    fp = open(filename, 'wb')
		    runner = HTMLTestRunner(stream=fp,
		                            title='Guest Manage System Interface Test Report',
		                            description='Implementation Example with: ')
		    runner.run(discover)
		    fp.close()
		'''
    
    
