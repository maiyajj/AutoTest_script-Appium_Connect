# encoding:utf-8
from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def find_toast(self, message):
    '''''判断toast信息'''
    try:
        element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, message)))
        return True
    except:
        return False
