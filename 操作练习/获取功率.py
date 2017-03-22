#coding:utf-8

# 京东：'appPackage':'com.jd.smart','appActivity':'com.jd.smart.activity.LoadingActivity'
# 公牛智联：'appPackage':'com.iotbull.android.superapp','appActivity':'com.iotbull.android.superapp.activitys.regist_login.SplashActivity'

from appium import webdriver
desired_caps = {'driver':'KIW-AL10','platformName':'Android','unicodeKeyboard':'True','browserName':'',
                'resetKeyboard':'True','platformVersion':'5.1.1','deviceName':'EMUI 3.1',
                'appPackage':'com.iotbull.android.superapp','appActivity':'com.iotbull.android.superapp.activitys.regist_login.SplashActivity'}
# desired_caps = {'driver':'ViVo Y51A','platformName':'Android','unicodeKeyboard':'True','browserName':'',
#                 'resetKeyboard':'True','platformVersion':'5.1.1','deviceName':'Funtouch OS_2.5.1',
#                 'appPackage':'com.iotbull.android.superapp','appActivity':'com.iotbull.android.superapp.activitys.regist_login.SplashActivity'}
# desired_caps = {'driver':'MI5','platformName':'Android','unicodeKeyboard':'True','browserName':'',
#                 'resetKeyboard':'True','platformVersion':'7.0','deviceName':'MIUI 8.2.1.0',
#                 'appPackage':'com.jd.smart','appActivity':'com.jd.smart.activity.LoadingActivity'}
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
# driver.swipe(270, 900, 270, 100, 0)
def get_name(num):
    b = []
    for x in xrange(3, 31):
        WebView = "//android.webkit.WebView"
        ListView = "/android.widget.ListView[%s]"%x
        View1 = "/android.view.View"
        search_device_mac1 = "".join((WebView, WebView, ListView, View1))
        View2 = "/android.view.View[2]"
        search_device_mac2 = "".join((WebView, WebView, ListView, View2))
        b.append(driver.find_element_by_xpath(search_device_mac2).get_attribute("name")[:-num]+"\n")
        b.append("\n")
        b.append("\n")
        b.append("\n")
    with open(r"Z:/text.log","w") as files:
        for i in b:
            file = files.write(i)
#获取电量
#获取电费
get_name(4)
# get_name(1)