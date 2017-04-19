# coding=utf-8
from appium import webdriver
from src.testcase.common.WidgetCheckUnit import *


def launch_app():
    try:
        driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)  # 启动APP
    except WebDriverException:
        try:
            driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        except WebDriverException:
            try:
                driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
            except WebDriverException:
                raise WebDriverException()
    return driver
