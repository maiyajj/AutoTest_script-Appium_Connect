# coding:utf-8 
import inspect
import time

from data.Database import *
from selenium.common.exceptions import *
from src.testcase.common.App_init import *
from src.utils.ReadConf import *


def page_unit(id=None, name=None, xpath=None):
    driver = database["driver"]
    page = None
    func_name = inspect.stack()[1][3]
    # logging.info(u"L_loading...%s " % func_name)
    # wait_old_time = time.time()
    while True:
        try:
            if id != None:
                page = driver.find_element_by_id(id)
            elif name != None:
                page = driver.find_element_by_name(name)
            elif xpath != None:
                page = driver.find_element_by_xpath(xpath)
            # logging.info(u"L_loading...(%s)success" % func_name)
            # err_screen_shot(delay)
            break
        except NoSuchElementException:
            time.sleep(operate_wait_time)
            # err_request_timeout(request_timeout)
    return page


def popups_unit(id=None, name=None, xpath=None):
    driver = database["driver"]
    page = None
    app_old_time = time.time()
    func_name = inspect.stack()[1][3]
    # 检测+号
    logging.info(u"正在检测是否进入 %s 弹窗" % func_name)
    wait_old_time = time.time()
    while True:
        try:
            if id != None:
                page = driver.find_element_by_id(id)
            elif name != None:
                page = driver.find_element_by_name(name)
            elif xpath != None:
                page = driver.find_element_by_xpath(xpath)
            # page = driver.find_element_by_id(bind_device_fail)
            logging.info(u"出现 %s 弹窗" % func_name)
            # err_screen_shot()
            break
        except NoSuchElementException:
            time.sleep(operate_wait_time)
            # 操作响应超时统计数据+1
            # err_request_timeout(request_timeout)
    return page
