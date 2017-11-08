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


# 元素操作API，将find_element进行再封装
class WidgetCheckUnit(Exception):
    copy = copy  # 初始化copy函数，避免import copy函数未使用被自动删除

    def __init__(self, driver, page_element, logger):
        self.driver = driver
        self.logger = logger
        self.page = page_element
        self.px = None

    # 等待元素出现，同于find_element_*
    def wait_widget(self, main_widget, timeout=3.0, interval=1.0, log_record=1):
        self.px = plural = False  # 元素在屏幕的像素坐标
        if not isinstance(main_widget, list):
            raise TypeError("main_widget must be list! [widget, locate method...]")
        locate = main_widget[1]  # page函数中的元素查找名称，例："//XCUIElementTypeTextField","btn_skip"，etc
        widget = main_widget[0]  # page函数中的元素查找方式，例："xpath","name","id"，etc
        try:
            if isinstance(widget, dict):
                plural = "dict"
            keys = main_widget[3]  # 读取页面元素的附加属性，包含index索引；px参考系为指定元素的坐标；pxw，参考系为屏幕分辨率；
            key = keys.keys()
            if "px" in key:
                self.px = [keys["px"], "px"]  # 待控元素像素对参考元素坐标的比例关系
            elif "pxw" in key:
                self.px = [keys["pxw"], "pxw"]  # 待控元素像素对屏幕分辨率的比例关系
            if "index" in key:
                index = int(keys["index"])  # 采用find_elements后的元素列表索引来定位元素
                plural = True  # 采用find_elements定位
        except IndexError:
            pass
        end_time = time.time() + timeout  # 设定元素查找超时时间
        while True:
            try:
                time.sleep(0.5)
                # 元素定位方式
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
                    # 当页面同类型元素很多或者页面元素不确定是否会出现时，单一判断依据已失效，
                    # 使用xpath轮询的方式来查找出所有同类元素，再根据待查找元素的指定特征再进行判断；
                    if plural is False:
                        element = self.driver.find_element_by_xpath(widget)
                    elif plural is True:
                        element = self.driver.find_elements_by_xpath(widget)[index]
                    else:
                        # 返回元素字典
                        # 输入→//XCUIElementTypeTextField[1] 输出→type(driver.WebElement...[1])
                        #      //XCUIElementTypeTextField[2]      type(driver.WebElement...[2])
                        #      ...                                ...
                        # return element:{0:WebElement, 1:WebElement...}
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
                    raise KeyError('find_element_by_%s must in ["id", "name", "class", "xpath", "activity", '
                                   '"accessibility_id"' % locate)
                # 根据需要开启log日志记录
                if log_record != 0:
                    self.logger.info('[APP_INFO] wait_widget ["%s"] success' % main_widget[2])

                return element
            except NoSuchElementException:
                if time.time() > end_time:
                    raise TimeoutException()
                time.sleep(interval)

    # 点击元素，同于element.click()
    def widget_click(self, operate_widget=None, wait_page=None, wait_time1=3, wait_time2=3,
                     times=1, interval=1, log_record=1):
        """
            Using click operation widgets - 使用点击方式操作元素
            widget_click(self, operate_widget=None, wait_page=None, wait_time1=1, wait_time2=1, timeout=6, interval=1,
                         log_record=1, operate_driver="find_element_in_driver", wait_driver="find_element_in_driver")
        Args:
            :param operate_widget: To control operation
                               待操作的元素
            :param wait_page: Check whether the widgets operation is successful
                          检查元素是否操作成功
            :param wait_time1: operate_widget——wait_time
                           operate_widget操作等待时间，超时报错
            :param wait_time2: wait_page——wait_time
                           wait_page操作等待时间，超时报错
            :param times: Operate times
                        元素操作次数
            :param interval: Polling time
                         轮询时间
            :param log_record: The flag of record the log
                        是否记录log
        :return element
        """
        if not isinstance(operate_widget, list):
            raise TypeError("operate_widget must be list! [widget_id, type(widget_id)]")
        elif not isinstance(wait_page, list):
            raise TypeError("wait_page must be list! [widget_id, type(widget_id)]")
        run_times = times  # 操作元素的次数，不使用时间，需要元素操作次数场合使用时间不确定性太大。
        flag = 0  # 元素操作失败步骤标志位
        click_flag = True
        widget = None  # 初始化widget，避免Local variable 'widget' might be referenced before assignment错误；
        while True:
            try:
                # 点击待控元素
                if click_flag is True:
                    flag = 0
                    widget = self.wait_widget(operate_widget, wait_time1, interval, 0)
                    if self.px is False:  # 元素附属属性没有px/pxw，使用正常操作点击元素
                        widget.click()
                    elif self.px[1] == "px":  # 使用px方式点击元素坐标
                        px = self.px[0]
                        lc, sz = widget.location, widget.size
                        pxx, pxy = int(lc["x"] + px[0] * sz["width"]), int(lc["y"] + px[1] * sz["height"])
                        try:
                            self.driver.tap([(pxx, pxy)])
                        except WebDriverException:
                            raise TimeoutException()
                    else:  # 使用pxw方式点击屏幕坐标
                        px = self.px[0]
                        ws = self.driver.get_window_size()
                        pxx, pxy = int(ws["width"] * px[0]), int(ws["height"] * px[1])
                        try:
                            self.driver.tap([(pxx, pxy)])
                        except WebDriverException:
                            raise TimeoutException()

                    # 点击元素后会有页面跳转加载动画，等待页面加载完成
                    while True:
                        try:
                            for k in self.page["loading_popup"].keys():
                                self.wait_widget(self.page["loading_popup"][k], 0.2, 0.1)
                        except TimeoutException:
                            break
                    # 根据需要开启log日志记录
                    if log_record != 0:
                        self.logger.info('[APP_CLICK] operate_widget ["%s"] success' % operate_widget[2])
                    time.sleep(0.1)
                # 点击元素后等待页面加载
                # 如果wait_page为None，则跳过此检测
                if wait_page is not None:
                    flag = 1
                    self.wait_widget(wait_page, wait_time2, interval, 0)
                return widget
            except TimeoutException:
                run_times -= 1
                if run_times <= 0:
                    if flag == 0:  # 点击操作未完成
                        error_info = ("[ERROR]Failed to operate element.UiSelector[INSTANCE=0, RESOURCE_ID=%s,"
                                      " RUN_TIMES=%sS]" % (operate_widget[0], run_times))
                        logger_info = '[APP_CLICK] operate_widget ["%s"] error' % operate_widget[2]
                    else:  # 完成点击操作，等待页面加载失败
                        error_info = ("[ERROR]Failed to wait element.UiSelector[INSTANCE=0, RESOURCE_ID=%s,"
                                      " RUN_TIMES=%sS]" % (wait_page[0], run_times))
                        logger_info = '[APP_CLICK] wait_page ["%s"] error' % wait_page[2]

                    if log_record != 0:
                        self.logger.info(logger_info)
                        database["err_request_timeout_count"] += 1

                    raise TimeoutException(error_info)
                else:  # 第一次元素操作未完成
                    try:  # 若页面仍停留在待点击元素页面
                        self.wait_widget(operate_widget, wait_time1, interval, 0)
                        click_flag = True
                    except TimeoutException:
                        try:  # 页面已跳转
                            self.wait_widget(wait_page, wait_time2, interval, 0)
                            click_flag = False  # 若页面已跳转，则下次操作不会再点击元素
                        except TimeoutException:
                            raise TimeoutException(self.driver.page_source)
            except TypeError:  # 判断输入是否正确
                self.logger.error(traceback.format_exc())
                return traceback.format_exc()
