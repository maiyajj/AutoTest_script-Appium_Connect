# coding:utf-8

from appium import webdriver

device = {'8681_M02': {'udid': '8681-M02-0xa0a151df', 'platformVersion': '5.1', 'platformName': 'Android',
                       'deviceName': '5.1.085.P2.160128.8681_M02'}}
desired_caps = {}
desired_caps['driver'] = '%s' % device.keys()[0]
desired_caps['platformName'] = '%s' % device.values()[0]["platformName"]
desired_caps['browserName'] = ''
desired_caps["unicodeKeyboard"] = "True"
desired_caps["resetKeyboard"] = "True"
desired_caps['platformVersion'] = '%s' % device.values()[0]["platformVersion"]
desired_caps['deviceName'] = '%s' % device.values()[0]["deviceName"]
desired_caps['appPackage'] = 'com.iotbull.android.superapp'
desired_caps['appActivity'] = "com.iotbull.android.superapp.activitys.regist_login.SplashActivity"
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
