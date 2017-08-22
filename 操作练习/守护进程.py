# coding=utf-8
import multiprocessing
import psutil
import time
def dafe(p):
    while True:
        print p
        time.sleep(1)
def run(var):
    print('.')
    while True:
        appium = multiprocessing.Process(target=dafe, args=("dsf",), name="adfasdf")
        appium.start()
        print  appium.pid
        while True:
            if appium.is_alive() is False:
                # appium.join()
                print appium.name, appium.pid
                # del appium
                print "appium is death"
                time.sleep(1)
                break
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