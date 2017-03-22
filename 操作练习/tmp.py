#coding:utf-8
from appium import webdriver
desired_caps = {'unicodeKeyboard': 'True', 'ver': '3.3.2', 'deviceName': 'MIUI 8 6.8.11', 'driver': 'xiaomi4', 'browserName': '', 'version': '6.0.1', 'resetKeyboard': 'True', 'appPackage': 'com.jd.smart', 'platformName': 'Android', 'appActivity': 'com.jd.smart.activity.LoadingActivity'}
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

ListView = "//android.widget.ListView"
LinearLayout = "/android.widget.LinearLayout"
LinearLayout1 = "/android.widget.LinearLayout[1]"
TextView = "/android.widget.TextView"
TextValue = "[@text='%s']" % "C4-11-E0-00-46-26"

search_device_mac = "".join((ListView,LinearLayout1, LinearLayout, LinearLayout, TextView, TextValue))
driver.find_element_by_xpath(search_device_mac)

TextView = "/android.widget.TextView"
TextValue = "[@text='%s']" % u"使用"
search_device_success = "".join((ListView,LinearLayout1, LinearLayout, TextView, TextValue))
driver.find_element_by_xpath(search_device_success)

driver.find_element_by_class_name("android.widget.Button").click()



search_device_mac = "C4-11-E0-00-46-26"
ListView = "//android.widget.ListView"
LinearLayout = "/android.widget.LinearLayout"
TextView = "/android.widget.TextView"
TextValue = "[@text='%s']" % search_device_mac
search_device_success = {}
for i in xrange(1, 6):
    LinearLayout1 = "/android.widget.LinearLayout[%s]" % i
    mac = "".join((ListView, LinearLayout1, LinearLayout,
                   LinearLayout, TextView, TextValue))
    text = "".join((ListView, LinearLayout1, LinearLayout, TextView))
    search_device_success[mac] = text

search_device_success = {"//android.widget.ListView/android.widget.LinearLayout[5]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.TextView[@text='C4-11-E0-00-46-26']": '//android.widget.ListView/android.widget.LinearLayout[5]/android.widget.LinearLayout/android.widget.TextView', "//android.widget.ListView/android.widget.LinearLayout[4]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.TextView[@text='C4-11-E0-00-46-26']": '//android.widget.ListView/android.widget.LinearLayout[4]/android.widget.LinearLayout/android.widget.TextView', "//android.widget.ListView/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.TextView[@text='C4-11-E0-00-46-26']": '//android.widget.ListView/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.TextView', "//android.widget.ListView/android.widget.LinearLayout[3]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.TextView[@text='C4-11-E0-00-46-26']": '//android.widget.ListView/android.widget.LinearLayout[3]/android.widget.LinearLayout/android.widget.TextView', "//android.widget.ListView/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.TextView[@text='C4-11-E0-00-46-26']": '//android.widget.ListView/android.widget.LinearLayout[2]/android.widget.LinearLayout/android.widget.TextView'}
from selenium.common.exceptions import *
while True:
    flag = 0
    for k, v in search_device_success.items():
        try:
            driver.find_element_by_xpath(k)
            widget = driver.find_element_by_xpath(v)
            widget.click()
            flag = 1
            break
        except NoSuchElementException:
            pass
    if flag == 1:
        break
    else:
        driver.swipe(600, 1100, 600, 900, 0)