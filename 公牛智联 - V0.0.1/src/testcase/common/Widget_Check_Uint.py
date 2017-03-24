# coding:utf-8 
import inspect
import time

from data.Database import *
from selenium.common.exceptions import *
from selenium.common.exceptions import TimeoutException
from src.testcase.common.App_init import *
from src.utils.Collect_Log import *
from src.utils.ReadConf import *


class Widget_Check_Uint(Exception):
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
