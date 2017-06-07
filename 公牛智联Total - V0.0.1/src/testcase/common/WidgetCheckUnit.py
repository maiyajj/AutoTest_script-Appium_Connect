# coding=utf-8
import time

from data.Database import *
from selenium.common.exceptions import *


class TimeoutError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


class WidgetCheckUnit(Exception):
    def __init__(self, driver, page_element, logger):
        self.driver = driver
        self.logger = logger
        self.page = page_element

    def wait_widget(self, main_widget=None, timeout=1.0, interval=1.0):
        locate = main_widget[1]
        widget = main_widget[0]
        end_time = time.time() + timeout
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
                elif locate == "accessibility_id":
                    element = self.driver.find_element_by_accessibility_id(widget)
                else:
                    raise KeyError('find_element_by_%s must in'
                                   '["id", "name", "class", "xpath", "activity", "accessibility_id"' % locate)
                try:
                    popup_text = main_widget[3]
                    if element.get_attribute("name") == popup_text:
                        pass
                    else:
                        raise TimeoutException()
                except IndexError:
                    pass
                return element
            except NoSuchElementException:
                time.sleep(interval)
                if time.time() > end_time:
                    raise TimeoutException()

    def widget_click(self, check_page=None, operate_widget=None, wait_page=None,
                     wait_time1=1, wait_time2=1, wait_time3=1, timeout=1,
                     interval=1, log_record=1):
        """
            Using click operation widgets - 使用点击方式操作控件
            widget_click(self, check_page=None, operate_widget=None, wait_page=None,
                         wait_time1=1, wait_time2=1, wait_time3=1, timeout=1,
                         interval=1, log_record=1, data=None)
        Args:
            :param check_page: Operating widgets before check whether to enter the widgets pages
                           操作控件前检查是否进入该控件所在页面
            :param operate_widget: To control operation
                               待操作的控件
            :param wait_page: Check whether the widgets operation is successful
                          检查控件是否操作成功
            :param wait_time1: check_page——wait_time
                           check_page操作等待时间，超时报错
            :param wait_time2: operate_widget——wait_time
                           operate_widget操作等待时间，超时报错
            :param wait_time3: wait_page——wait_time
                           wait_page操作等待时间，超时报错
            :param interval: Polling time
                         轮询时间
            :param timeout: Operate timeout
                        操作超时
            :param log_record: The flag of record the log
                        是否记录log

        :return FALSE
        """
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
                # self.logger.info('[APP_CLICK] check_page ["%s"] success' % check_page[2])
                time.sleep(0.1)
                flag = 1
                widget = self.wait_widget(operate_widget, wait_time2, interval)
                widget.click()
                while True:
                    try:
                        self.wait_widget(self.page["loading_popup"]["title"], 0.2, 0.1)
                    except TimeoutException:
                        break
                if log_record != 0:
                    self.logger.info('[APP_CLICK] operate_widget ["%s"] success' % operate_widget[2])
                time.sleep(0.1)
                flag = 2
                self.wait_widget(wait_page, wait_time3, interval)
                # self.logger.info('[APP_CLICK] wait_page ["%s"] success' % wait_page[2])
                return widget
            except TimeoutException:
                time.sleep(interval)
                if time.time() > end_time:
                    if flag == 0 and log_record != 0:
                        self.logger.info('[APP_CLICK] check_page ["%s"] error' % check_page[2])
                    elif flag == 1 and log_record != 0:
                        self.logger.info('[APP_CLICK] operate_widget ["%s"] error' % operate_widget[2])
                    elif flag == 2 and log_record != 0:
                        self.logger.info('[APP_CLICK] wait_page ["%s"] error' % wait_page[2])
                    database["err_request_timeout_count"] += 1
                    if log_record != 0:
                        self.logger.error("[ERROR]Failed to operate element.UiSelector"
                                          "[INSTANCE=0, RESOURCE_ID=%s, TIMING_OUT=%sS]"
                                          % (operate_widget[0], timeout))
                    raise TimeoutException("[ERROR]Failed to operate element.UiSelector"
                                           "[INSTANCE=0, RESOURCE_ID=%s, TIMING_OUT=%sS]"
                                           % (operate_widget[0], timeout))
            except TypeError:
                return False
