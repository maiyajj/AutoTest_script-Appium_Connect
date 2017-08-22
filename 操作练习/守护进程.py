# coding=utf-8
import multiprocessing
import psutil
import time
def dafe(p):
    while True:
        print p
        time.sleep(1)
def run(var):
    a = 1
    b = 1
    while True:
        if a == 1:
            appium = multiprocessing.Process(target=dafe, args=("dsf",), name="adfasdf")
            appium.start()
            print "appium run"
            a = 0
        if b == 1:
            appium1 = multiprocessing.Process(target=dafe, args=("sss",), name="sss")
            appium1.start()
            print "appium1 run"
            b = 0
        print appium.pid,appium1.pid
        while True:
            if appium.is_alive() is False:
                a = 1
                print appium.name, appium.pid
                break
            elif appium1.is_alive() is False:
                b = 1
                print appium1.name, appium1.pid
                break
            else:
                time.sleep(1)
p = multiprocessing.Process(target=run, args=('var',))
p.start()

# 'authkey',
# 'daemon',
# 'exitcode',
# 'ident',
# 'is_alive',
# 'join',
# 'name',
# 'pid',
# 'run',
# 'start',
# 'terminate']