# coding:utf-8
import time
import urllib2
from multiprocessing import Process

from appium import webdriver
from data.Database import *
from src.utils.Get_Phone_Info import *
from src.utils.Launch_Appium_Services import *
from src.utils.ReadConf import *

desired_caps = {}
desired_caps['driver'] = '%s' % device.keys()[0]
desired_caps['platformName'] = '%s' % device.values()[0]["platformName"]
desired_caps['browserName'] = ''
desired_caps["unicodeKeyboard"] = "True"
desired_caps["resetKeyboard"] = "True"
desired_caps['platformVersion'] = '%s' % device.values()[0]["platformVersion"]
desired_caps['deviceName'] = '%s' % device.values()[0]["deviceName"]
desired_caps['appPackage'] = '%s' % App["GN"][0]
desired_caps['appActivity'] = '%s' % App["GN"][1]


def open_app():
    Appium = Process(target=Launch_Appium_Services().main)
    Appium.start()
    while True:
        try:
            driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
            break
        except urllib2.URLError:
            time.sleep(1)
    database["driver"] = driver

