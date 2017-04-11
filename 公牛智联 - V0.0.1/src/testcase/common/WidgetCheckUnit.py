# coding:utf-8 
import time
import urllib2

from AppInit import *
from appium import webdriver
from data.Database import *
from selenium.common.exceptions import *
from src.utils.CollectLog import *
from src.utils.ReadAPPElement import *
from src.utils.ReadConf import *


class TimeoutError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


class WidgetCheckUnit(Exception):
    def __init__(self, driver):
        self.driver = driver
        database["driver"] = driver

    def wait_widget(self, main_widget=None, timeout=1, interval=1):
        locate = main_widget[1]
        widget = main_widget[0]
        if main_widget == None or locate not in ["id", "name", "class", "xpath", "activity"]:
            raise KeyError('[%s][1] must be "id" or "name" or "class" or "xpath"' % main_widget)
        end_time = time.time() + timeout
        element = None
        while True:
            try:
                if locate == "id":
                    element = self.driver.find_element_by_id(widget)
                elif locate == "name":
                    element = self.driver.find_element_by_name(widget)
                elif locate == "class":
                    element = self.driver.find_element_by_class_name(widget)
                elif locate == "xpath":
                    element = self.driver.find_element_by_xpath(widget)
                elif locate == "activity":
                    element = self.driver.wait_activity(widget)
                return element
            except NoSuchElementException:
                time.sleep(interval)
                if time.time() > end_time:
                    raise TimeoutException()

    def widget_click(self, check_page=None, operate_widget=None, wait_page=None,
                     wait_time1=1, wait_time2=1, wait_time3=1, timeout=1, interval=1, log=1):
        '''
            Using click operation widgets - 使用点击方式操作控件
            widget_click(self, check_page=None,operate_widget=None,wait_page=None,
                     wait_time1=1,wait_time2=1,wait_time3=1,timeout=1,interval=1,log=1)
        Args:
            - check_page - Operating widgets before check whether to enter the widgets pages
                           操作控件前检查是否进入该控件所在页面
            - operate_widget - To control operation
                               待操作的控件
            - wait_page - Check whether the widgets operation is successful
                          检查控件是否操作成功
            - wait_time1 - check_page——wait_time
                           check_page操作等待时间，超时报错
            - wait_time2 - operate_widget——wait_time
                           operate_widget操作等待时间，超时报错
            - wait_time3 - wait_page——wait_time
                           wait_page操作等待时间，超时报错
            - interval - Polling time
                         轮询时间
            - timeout - Operate timeout
                        操作超时
            - log - The flag of record the log
                        是否记录log
                         
        :return FALSE
        '''
        if not isinstance(check_page, list):
            raise TypeError("check_page must be list! [widget_id, type(widget_id)]")
        elif not isinstance(operate_widget, list):
            raise TypeError("operate_widget must be list! [widget_id, type(widget_id)]")
        elif not isinstance(wait_page, list):
            raise TypeError("wait_page must be list! [widget_id, type(widget_id)]")
        end_time = time.time() + timeout
        flag = 0
        while True:
            try:
                flag = 0
                self.wait_widget(check_page, wait_time1, interval)
                # logger.info('[APP_CLICK] check_page ["%s"] success' % check_page[2])
                time.sleep(0.1)
                flag = 1
                widget = self.wait_widget(operate_widget, wait_time2, interval)
                widget.click()
                if log != 0:
                    logger.info('[APP_CLICK] operate_widget ["%s"] success' % operate_widget[2])
                time.sleep(0.1)
                flag = 2
                self.wait_widget(wait_page, wait_time3, interval)
                # logger.info('[APP_CLICK] wait_page ["%s"] success' % wait_page[2])
                return widget
            except TimeoutException:
                time.sleep(interval)
                if time.time() > end_time:
                    if flag == 0 and log != 0:
                        logger.info('[APP_CLICK] check_page ["%s"] error' % check_page[2])
                    elif flag == 1 and log != 0:
                        logger.info('[APP_CLICK] operate_widget ["%s"] error' % operate_widget[2])
                    elif flag == 2 and log != 0:
                        logger.info('[APP_CLICK] wait_page ["%s"] error' % wait_page[2])
                    database["err_request_timeout_count"] += 1
                    if log != 0:
                        logger.error("[ERROR]Failed to operate element.UiSelector"
                                     "[INSTANCE=0, RESOURCE_ID=%s, TIMING_OUT=%sS]"
                                     % (operate_widget[0], timeout))
                    raise TimeoutException("[ERROR]Failed to operate element.UiSelector"
                                           "[INSTANCE=0, RESOURCE_ID=%s, TIMING_OUT=%sS]"
                                           % (operate_widget[0], timeout))
            except TypeError:
                return False
                # except AttributeError:
                #     raise TimeoutException()

    def page_unit(self, id=None, name=None, xpath=None):
        driver = database["driver"]
        page = None
        logger.info(u"L_loading...%s " % func_name)
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
