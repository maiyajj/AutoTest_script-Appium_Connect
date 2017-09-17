# coding=utf-8
import time
import traceback

from selenium.common.exceptions import *

from data.Database import *


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
        self.index = None

    def wait_widget(self, main_widget, timeout=3.0, interval=1.0, driver="find_element_in_driver"):
        plural = False
        if driver == "find_element_in_driver":
            parent_element = self.driver
        else:
            parent_element = driver
        if not isinstance(main_widget, list):
            raise TypeError("main_widget must be list! [widget, locate method...]")
        locate = main_widget[1]
        widget = main_widget[0]
        popup_text = "None"
        try:
            if isinstance(widget, dict):
                plural = True
            keys = main_widget[3].keys()
            if "text" in keys:
                popup_text = main_widget[3]["text"]
        except IndexError:
            pass
        end_time = time.time() + timeout
        while True:
            try:
                time.sleep(0.5)
                if locate == "id":
                    element = parent_element.find_element_by_id(widget)
                elif locate == "name":
                    element = parent_element.find_element_by_name(widget)
                elif locate == "class":
                    element = parent_element.find_element_by_class_name(widget)
                elif locate == "xpath":
                    if plural is False:
                        element = parent_element.find_element_by_xpath(widget)
                    else:
                        element = {}
                        for k, v in widget.items():
                            try:
                                element[k] = parent_element.find_element_by_xpath(v)
                            except NoSuchElementException:
                                pass
                elif locate == "activity":
                    element = parent_element.wait_activity(widget)
                elif locate == "accessibility_id":
                    element = parent_element.find_element_by_accessibility_id(widget)
                else:
                    raise KeyError('find_element_by_%s must in'
                                   '["id", "name", "class", "xpath", "activity", "accessibility_id"' % locate)
                if popup_text != "None":
                    if element.get_attribute("name") == popup_text:
                        pass
                    else:
                        raise TimeoutException()
                return element
            except NoSuchElementException:
                time.sleep(interval)
                if time.time() > end_time:
                    raise TimeoutException()

    def widget_click(self, operate_widget=None, wait_page=None, wait_time1=3, wait_time2=3, timeout=6, interval=1,
                     log_record=1, operate_driver="find_element_in_driver", wait_driver="find_element_in_driver"):
        """
            Using click operation widgets - 使用点击方式操作控件
            widget_click(self, operate_widget=None, wait_page=None, wait_time1=1, wait_time2=1, timeout=6, interval=1,
                         log_record=1, operate_driver="find_element_in_driver", wait_driver="find_element_in_driver")
        Args:
            :param operate_widget: To control operation
                               待操作的控件
            :param wait_page: Check whether the widgets operation is successful
                          检查控件是否操作成功
            :param wait_time1: operate_widget——wait_time
                           operate_widget操作等待时间，超时报错
            :param wait_time2: wait_page——wait_time
                           wait_page操作等待时间，超时报错
            :param interval: Polling time
                         轮询时间
            :param timeout: Operate timeout
                        操作超时
            :param log_record: The flag of record the log
                        是否记录log
            :param operate_driver: not app drier,is node parent's driver
                        不是启动APP时的driver，是节点的父节点的driver
            :param wait_driver: 
                        the same
        :return element
        """
        if not isinstance(operate_widget, list):
            raise TypeError("operate_widget must be list! [widget_id, type(widget_id)]")
        elif not isinstance(wait_page, list):
            raise TypeError("wait_page must be list! [widget_id, type(widget_id)]")
        end_time = time.time() + timeout
        flag = 0
        while True:
            try:
                flag = 0
                widget = self.wait_widget(operate_widget, wait_time1, interval, driver=operate_driver)
                widget.click()
                while True:
                    try:
                        self.wait_widget(self.page["loading_popup"]["title"], 0.2, 0.1)
                    except TimeoutException:
                        break
                if log_record != 0:
                    self.logger.info('[APP_CLICK] operate_widget ["%s"] success' % operate_widget[2])
                time.sleep(0.1)
                flag = 1
                self.wait_widget(wait_page, wait_time2, interval, driver=wait_driver)
                return widget
            except TimeoutException:
                time.sleep(interval)
                if time.time() > end_time:
                    if flag == 0 and log_record != 0:
                        self.logger.info('[APP_CLICK] operate_widget ["%s"] error' % operate_widget[2])
                    elif flag == 1 and log_record != 0:
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
                self.logger.error(traceback.format_exc())
                return traceback.format_exc()
