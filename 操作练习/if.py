# encoding:utf-8
a = "1"
class tmp(object):
    def __init__(self):
        self.flag = True
        self.a()
    def a(self):
        self.flag = False
        if self.flag == False:
            print self.flag
        self.close()
    def close(self):
        print "close"

tmp()