# coding:utf-8
import traceback
from urllib2 import *

from appium import webdriver
from selenium.common.exceptions import *

desired_caps = {'driver': 'KIW-AL10', 'platformName': 'Android', 'unicodeKeyboard': 'True', 'browserName': '',
                'resetKeyboard': 'True', 'platformVersion': '5.1', 'deviceName': 'EMUI 3.1',
                'appPackage': 'com.iotbull.android.superapp',
                'appActivity': 'com.iotbull.android.superapp.activitys.regist_login.SplashActivity'}
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

try:
    i = 1
    while True:
        try:
            try:
                driver.quit()  # 确保appium服务已关闭
            except AttributeError:
                print "AttributeError", traceback.format_exc()
                raise WebDriverException()
        except WebDriverException:
            try:
                print "driver.quit()", traceback.format_exc()
                driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
                print "driver(while):%s" % driver
                break
            except WebDriverException:
                driver.quit()
                print  "driver(WebDriverException):%s times" % i
                i += 1
            except URLError:
                print "URLError", traceback.format_exc()
except WebDriverException:
    print "case_over:%s" % traceback.format_exc()
