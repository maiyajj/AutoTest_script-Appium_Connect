# coding:utf-8
import time,re
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


def run_app():
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    database["driver"] = driver
    database["open_app_flag"] = 1

def follow(thefile):
    thefile.seek(0,2)
    while True:
        line = thefile.readline()
        if not line:
            time.sleep(0.1)
            continue
        yield line
def log():
    with open('../log/myapp.log', 'r') as logfile:
        loglines = follow(logfile)
        for line in loglines:
            tmp = re.findall(r".+localhost", line)
            if tmp == []:
                with open('../log/report.log', 'a') as files:
                    files.write(loglines)
            else:
                pass

def open_app():
    Appium = Process(target=Launch_Appium_Services().main)
    Appium.start()
    del_log = Process(target=log)
    del_log.start()
    time.sleep(10)
    run_app()