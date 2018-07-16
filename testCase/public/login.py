#!/usr/bin/env python
#coding:utf-8
from utiity.seleniumDrive import seleniumDrive
from utiity.base import base
from utiity import conf
class login():
    def __init__(self,dr):
        #drive = seleniumDrive('chrome').GetDrive()
        self.d = dr
    

    def login(self):
        self.d.openBaseUrl('d')
        self.d.openBaseUrl('百度一下 你就知道')
        self.d.elemenClick('loginbutton')
        self.d.elementSendkeys('zhweds@163.com', 'user')
        self.d.elementSendkeys('jiangshu', 'password')
        self.d.elemenClick('登录按钮')
        self.d.elemenClick('close')
        self.d.waitTime(3)
if __name__ == '__main__':
    a = login()
    a.login()
        