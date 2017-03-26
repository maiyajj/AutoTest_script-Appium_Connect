# coding:utf-8 
import inspect
import time

from data.Database import *
from selenium.common.exceptions import *
from selenium.common.exceptions import TimeoutException
from src.testcase.common.App_init import *
from src.utils.Collect_Log import *
from src.utils.ReadConf import *


class TimeoutError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


class Widget_Check_Unit(Exception):
    def __init__(self, driver):
        print "begin"
        self.driver = driver
        print self.driver

    def wait_widget(self, locate=None, widget=None, timeout=1, interval=1):
        end_time = time.time() + timeout
        element = None
        while True:
            try:
                if locate == "id":
                    element = self.driver.find_element_by_id(widget)
                elif locate == "name":
                    element = self.driver.find_element_by_name(widget)
                elif locate == "CName":
                    element = self.driver.find_element_by_class_name(widget)
                elif locate == "xpath":
                    element = self.driver.find_element_by_xpath(widget)
                elif locate == None:
                    raise KeyError('key must be "id" or "name" or "CName" or "xpath"')
                return element
            except NoSuchElementException:
                time.sleep(interval)
                if time.time() > end_time:
                    raise TimeoutException("Failed to locate element.\n"
                                           "UiSelector[INSTANCE=0, RESOURCE_ID=%s, TIMING_OUT=%sS]\n"
                                           % (widget, timeout))
            except TimeoutException:
                return False

    def widget_click(self, check_page=None, operate_widget=None, wait_page=None,
                     wait_time1=1, wait_time2=1, wait_time3=1, timeout=1, interval=1):
        '''
            Using click operation widgets - 使用点击方式操作控件
            widget_click(self, check_page=None,operate_widget=None,wait_page=None,
                     wait_time1=1,wait_time2=1,wait_time3=1,interval=1,timeout=1)
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
            - timeout - Operate timeout
                        操作超时
            - interval - Polling time
                         轮询时间
                         
        :return FALSE
        '''
        if check_page == None:
            raise KeyError("check_page must be not None!")
        elif operate_widget == None:
            raise KeyError("operate_widget must be not None!")
        elif wait_page == None:
            raise KeyError("wait_page must be not None!")
        end_time = time.time() + timeout
        while True:
            try:
                self.wait_widget(check_page[1], check_page[0], wait_time1, interval)
                time.sleep(0.1)
                self.wait_widget(operate_widget[1], operate_widget[0], wait_time2, interval).click()
                time.sleep(0.1)
                self.wait_widget(wait_page[1], wait_page[0], wait_time3, interval)
                break
            except TimeoutException:
                time.sleep(interval)
                if time.time() > end_time:
                    raise TimeoutError("Failed to operate element." + "\n" +
                                       "UiSelector[INSTANCE=0, RESOURCE_ID=%s, TIMING_OUT=%sS]"
                                       % (operate_widget[0], timeout) + "\n")
            except KeyError:
                return False
            except TimeoutError:
                return False

    def page_unit(self, id=None, name=None, xpath=None):
        driver = database["driver"]
        page = None
        func_name = inspect.stack()[1][3]
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

    def popups_unit(self, locate=None, key=None):
        driver = database["driver"]
        self.driver = driver
        logger.info(u"正在检测是否进入 %s 弹窗" % driver.current_activity)
        print self.wait_widget("id", "com.iotbull.android.superapp:id/loginCommitButton", 5, 1)
        print self.wait_widget("id", "nCommitButton", 5, 1)
