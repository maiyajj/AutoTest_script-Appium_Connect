# coding=utf-8
import time

from appium import webdriver
from selenium.common.exceptions import *

desired_caps = {'driver': 'KIW-AL10', 'platformName': 'Android', 'unicodeKeyboard': 'True', 'browserName': '',
                'resetKeyboard': 'True', 'platformVersion': '5.1.1', 'deviceName': 'EMUI 3.1',
                'appPackage': 'com.iotbull.android.superapp',
                'appActivity': 'com.iotbull.android.superapp.activitys.regist_login.SplashActivity',
                'waitappActivity': 'com.iotbull.android.superapp/.activitys.regist_login.LoginActivity'}
while True:
    try:
        driver = webdriver.Remote('http://localhost:4725/wd/hub', desired_caps)
        break
    except WebDriverException:
        pass
print "first launch success"
i = 1
while True:
    print "run times %s !" % i
    driver.close_app()
    print "APP 关闭成功 %s" % time.strftime("%Y-%m-%d %H:%M:%S")
    while True:
        try:
            driver.launch_app()
            print "APP 打开成功 %s" % time.strftime("%Y-%m-%d %H:%M:%S")
            break
        except WebDriverException:
            print "retry"
    i += 1
