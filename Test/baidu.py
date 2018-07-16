

from utiity.log import log
class test():
    def __init__(self):
        self.log = log()
    def dd(self):
        self.log.info('dd')
    def aa(self):
        self.log.info('aa')

if __name__ == '__main__':
    c = test()
    c.aa()
    c.dd()
    c.dd()
        
  