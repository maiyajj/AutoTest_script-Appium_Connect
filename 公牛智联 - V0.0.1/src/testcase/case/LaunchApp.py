# coding=utf-8
from appium import webdriver
from src.testcase.common.WidgetCheckUnit import *


def launch_app(devices):
    try:
        driver = webdriver.Remote('http://localhost:%s/wd/hub' % device[devices]["port"],
                                  device[devices]["desired_caps"])  # 启动APP
    except WebDriverException:
        try:
            driver = webdriver.Remote('http://localhost:%s/wd/hub' % device[devices]["port"],
                                      device[devices]["desired_caps"])
        except WebDriverException:
            try:
                driver = webdriver.Remote('http://localhost:%s/wd/hub' % device[devices]["port"],
                                          device[devices]["desired_caps"])
            except WebDriverException:
                raise WebDriverException()
    device[devices]["driver"] = driver
    return driver
