# coding=utf-8
from appium import webdriver
from src.testcase.common.WidgetCheckUnit import *


def launch_app(device_info):
    try:
        driver = webdriver.Remote('http://localhost:%s/wd/hub' % device_info["port"],
                                  device_info["desired_caps"])  # 启动APP
    except WebDriverException:
        try:
            driver = webdriver.Remote('http://localhost:%s/wd/hub' % device_info["port"],
                                      device_info["desired_caps"])
        except WebDriverException:
            try:
                driver = webdriver.Remote('http://localhost:%s/wd/hub' % device_info["port"],
                                          device_info["desired_caps"])
            except WebDriverException:
                raise WebDriverException()
    return driver
