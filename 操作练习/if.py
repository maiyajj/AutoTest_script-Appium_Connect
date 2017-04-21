# coding=utf-8
import os
from multiprocessing import Process

from appium import webdriver

command = "taskkill /f /t /im adb.exe"
os.system(command)
device = {'8681_M02':
              {'deviceName': '8681-M02', 'udid': '8681-M02-0xa0a151df',
               'desired_caps':
                   {'unicodeKeyboard': 'True',
                    'deviceName': '8681-M02',
                    # 'udid': '8681-M02-0xa0a151df',
                    'driver': '8681_M02',
                    'browserName': '',
                    'resetKeyboard': 'True',
                    'platformVersion': '5.1',
                    'appPackage': 'com.iotbull.android.superapp', 'platformName': 'Android',
                    'appActivity': 'com.iotbull.android.superapp.activitys.regist_login.SplashActivity'},
               'platformVersion': '5.1', 'platformName': 'Android', 'port': 4725,
               'dpi': ['1080', '1920']},
          'MX5':
              {'deviceName': 'MX5', 'udid': '85GABMN9UDD2',
               'desired_caps':
                   {'unicodeKeyboard': 'True',
                    'deviceName': 'MX5',
                    # 'udid': '85GABMN9UDD2',
                    'driver': 'MX5',
                    'browserName': '',
                    'resetKeyboard': 'True',
                    'platformVersion': '5.1',
                    'appPackage': 'com.iotbull.android.superapp',
                    'platformName': 'Android',
                    'appActivity': 'com.iotbull.android.superapp.activitys.regist_login.SplashActivity'},
               'platformVersion': '5.1', 'platformName': 'Android',
               'port': 4726, 'dpi': ['1080', '1920']}}


def launch(devices):
    driver = webdriver.Remote('http://localhost:%s/wd/hub' % device[devices]["port"], device[devices]["desired_caps"])


def app_init_launch_appium():
    process = []
    for key in device.keys():
        process.append(Process(target=launch, args=(key,)))

    for i in process:
        i.start()


if __name__ == '__main__':
    app_init_launch_appium()
