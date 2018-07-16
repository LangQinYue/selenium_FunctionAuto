#!coding=utf-8
'''
Created on 2016年6月30日

@author: lx-lang.qinyue
'''
# import sys 
# reload(sys)
# sys.setdefaultencoding("utf-8")
from utiity.log import log
import unittest
class testt(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        super(testt, cls).setUpClass()
        global logg
        logg = log()
    @classmethod
    def tearDownClass(cls):
        super(testt, cls).tearDownClass()
        print 'end'
    def setUp(self):
        #self.logg = log()
        pass

    def testloginout(self):

        logg.msgInfo('out begin')
        print '------ddd-----------'
        logg.msgInfo('out end')
    def testloginin(self):
        logg.msgInfo(' 111')
        logg.msgInfo('222')

    def testlogin(self):
        logg.msgInfo('begin test')
        logg.msgInfo('end test')
    def tearDown(self):
        pass
if __name__ == '__main__':
    ids = [1,4,3,3,4,2,3,4,5,6,1]
    func = lambda x,y:x if y in x else x + [y]
    ids = reduce(func, [[], ] + ids)
    print ids


