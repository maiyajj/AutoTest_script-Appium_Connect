# coding:utf-8
import time
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
desired_caps['appPackage'] = '%s' % App["JD"][0]
desired_caps['appActivity'] = '%s' % App["JD"][1]


def run_app():
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    database["driver"] = driver
    database["open_app_flag"] = 1

def open_app():
    Appium = Process(target=Launch_Appium_Services().main)
    Appium.start()
    time.sleep(5)
    run_app()
