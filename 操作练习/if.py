# encoding:utf-8

print "iot123456".encode('hex')
import time

print type(time.strftime("%H"))

class a(object):
    def __init__(self):
        print "sdafasdfasdf"
        self.b()

    def b(self):
        print "hhg"
        self.flag = 1

    def c(self):
        print "bb"
        return self.flag, "jj"


def write_report(case):
    CASE = case
    report = u"[CASE_TITLE=%s, RESULT=%s]" % \
             (CASE[1], CASE[0])
    return report

