# encoding:utf-8
from appium import webdriver
desired_caps = {'driver':'KIW-AL10','platformName':'Android','unicodeKeyboard':'True','browserName':'',
                'resetKeyboard':'True','platformVersion':'5.1.1','deviceName':'EMUI 3.1',
                'appPackage':'com.iotbull.android.superapp','appActivity':'com.iotbull.android.superapp.activitys.regist_login.SplashActivity'}
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
driver.get('http://release.thy360.com/o2o_weixin/index.html#/tab/platformHome')
driver.implicitly_wait(30)
driver.switch_to.context('WEBVIEW_1')