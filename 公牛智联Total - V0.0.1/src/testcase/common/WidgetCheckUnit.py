# coding=utf-8
import copy
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

    def copy(self):
        copy.copy("init for copy")

    def wait_widget(self, main_widget, timeout=3.0, interval=1.0, log_record=1):
        self.px = plural = False
        if not isinstance(main_widget, list):
            raise TypeError("main_widget must be list! [widget, locate method...]")
        locate = main_widget[1]
        widget = main_widget[0]
        popup_text = "None"
        try:
            if isinstance(widget, dict):
                plural = True
            keys = main_widget[3]
            key = keys.keys()
            if "text" in key:
                popup_text = keys["text"]
            if "index" in key:
                index = int(keys["index"])
            if "px" in key:
                self.px = [keys["px"], "px"]
            if "pxw" in key:
                self.px = [keys["pxw"], "pxw"]
        except IndexError:
            pass
        end_time = time.time() + timeout
        while True:
            try:
                time.sleep(0.5)
                if locate == "id":
                    if plural is False:
                        element = self.driver.find_element_by_id(widget)
                    else:
                        element = self.driver.find_elements_by_id(widget)[index]
                elif locate == "accessibility_id":
                    if plural is False:
                        element = self.driver.find_element_by_accessibility_id(widget)
                    else:
                        element = self.driver.find_elements_by_accessibility_id(widget)[index]
                elif locate == "xpath":
                    if plural is False:
                        element = self.driver.find_element_by_xpath(widget)
                    elif plural is False:
                        element = self.driver.find_elements_by_xpath(widget)[index]
                    else:
                        element = {}
                        for k, v in widget.items():
                            try:
                                element[k] = self.driver.find_element_by_xpath(v)
                            except NoSuchElementException:
                                element[k] = None
                elif locate == "class":
                    if plural is False:
                        element = self.driver.find_element_by_class_name(widget)
                    else:
                        element = self.driver.find_elements_by_class_name(widget)[index]
                elif locate == "name":
                    if plural is False:
                        element = self.driver.find_element_by_name(widget)
                    else:
                        element = self.driver.find_elements_by_name(widget)[index]
                elif locate == "activity":
                    element = self.driver.wait_activity(widget)
                else:
                    raise KeyError('find_element_by_%s must in'
                                   '["id", "name", "class", "xpath", "activity", "accessibility_id"' % locate)
                if popup_text != "None":
                    if element.get_attribute("name") == popup_text:
                        pass
                    else:
                        raise TimeoutException()
                if log_record != 0:
                    self.logger.info('[APP_INFO] wait_widget ["%s"] success' % main_widget[2])
                return element
            except NoSuchElementException:
                time.sleep(interval)
                if time.time() > end_time:
                    raise TimeoutException()

    def widget_click(self, operate_widget=None, wait_page=None, wait_time1=3, wait_time2=3,
                     times=1, interval=1, log_record=1):
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
        :return element
        """
        if not isinstance(operate_widget, list):
            raise TypeError("operate_widget must be list! [widget_id, type(widget_id)]")
        elif not isinstance(wait_page, list):
            raise TypeError("wait_page must be list! [widget_id, type(widget_id)]")
        run_times = times
        flag = 0
        while True:
            try:
                flag = 0
                widget = self.wait_widget(operate_widget, wait_time1, interval, 0)
                if self.px is False:
                    widget.click()
                elif self.px[1] == "px":
                    self.px = self.px[0]
                    lc, sz = widget.location, widget.size
                    x, y = lc["x"] + self.px[0] * sz["width"], lc["y"] + self.px[1] * sz["height"]
                    pxx, pxy = int(x), int(y)
                    try:
                        self.driver.tap([(pxx, pxy)])
                    except WebDriverException:
                        raise TimeoutException()
                else:
                    self.px = self.px[0]
                    ws = self.driver.get_window_size()
                    wsx, wsy = ws["width"], ws["height"]
                    pxx, pxy = int(wsx * self.px[0]), int(wsy * self.px[1])
                    try:
                        self.driver.tap([(pxx, pxy)])
                    except WebDriverException:
                        raise TimeoutException()
                while True:
                    try:
                        for k in self.page["loading_popup"].keys():
                            self.wait_widget(self.page["loading_popup"][k], 0.2, 0.1)
                    except TimeoutException:
                        break
                if log_record != 0:
                    self.logger.info('[APP_CLICK] operate_widget ["%s"] success' % operate_widget[2])
                time.sleep(0.1)
                flag = 1
                self.wait_widget(wait_page, wait_time2, interval, 0)
                return widget
            except TimeoutException:
                run_times -= 1
                if run_times <= 0:
                    if flag == 0:
                        error_info = "[ERROR]Failed to operate element.UiSelector[INSTANCE=0, RESOURCE_ID=%s," \
                                     " RUN_TIMES=%sS]" % (operate_widget[0], run_times)
                        logger_info = '[APP_CLICK] operate_widget ["%s"] error' % operate_widget[2]
                    else:
                        error_info = "[ERROR]Failed to wait element.UiSelector[INSTANCE=0, RESOURCE_ID=%s," \
                                     " RUN_TIMES=%sS]" % (wait_page[0], run_times)
                        logger_info = '[APP_CLICK] wait_page ["%s"] error' % wait_page[2]

                    if log_record != 0:
                        self.logger.info(logger_info)
                        database["err_request_timeout_count"] += 1

                    raise TimeoutException(error_info)
            except TypeError:
                self.logger.error(traceback.format_exc())
                return traceback.format_exc()
