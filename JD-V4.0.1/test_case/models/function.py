# coding=utf-8

import inspect
import logging
import os
import sys
import time

from appium import webdriver
from selenium.common.exceptions import *

sys.path.append("..")
from page_obj.App_Operate_Page import MainPageWidget

__author__ = "maiyajj"
# filename = function.py
'''
文件说明：
本文件包含三大类：
OpenAppInit():打开APP的初始化工作;
ErrDetection():错误处理方法类;
WidgetOperation():所有可控控件的操作方法；
'''


# 打开APP的初始化工作
class OpenAppInit(MainPageWidget):
    # 关于统计数据所有变量的定义
    def __init__(self):
        self.log_text()
        logging.info(u"自动化测试工具启动")
        # 从function文件获取配置时间
        self.get_timeout_time()
        # 测试流程标志位
        self.test_tempo_flag = None
        # 程序运行循环次数
        self.program_loop_time = 0
        # 打开APP失败次数统计
        self.err_open_app_fail_count = 0
        # 搜索设备超时次数统计
        self.err_search_device_timeout_count = 0
        # 操作响应超时次数统计
        self.err_request_timeout_count = 0
        # 设备离线次数统计
        self.err_offline_count = 0
        # 设备已被添加次数统计
        self.bind_device_added_count = 0
        # 绑定设备成功次数统计
        self.bind_device_success_count = 0
        # 设备已被绑定次数统计
        self.bind_device_bind_count = 0
        # 设备绑定失败次数统计
        self.bind_device_fail_count = 0
        # 手机信息定义
        self.desired_caps = {}
        self.desired_caps['driver'] = 'KIW-AL10'
        self.desired_caps['platformName'] = 'Android'
        self.desired_caps['browserName'] = ''
        self.desired_caps["unicodeKeyboard"] = "True"
        self.desired_caps["resetKeyboard"] = "True"
        self.desired_caps['platformVersion'] = '6.0.1'
        self.desired_caps['deviceName'] = 'EMUI 3.1'
        self.desired_caps['appPackage'] = 'com.jd.smart'
        self.desired_caps['appActivity'] = 'com.jd.smart.activity.LoadingActivity'
        self.class_mainpage_init()

    # 打开APP时的操作及错误处理
    def init_open_app(self):
        # 进入当前函数的时间点
        app_old_time = time.time()
        func_name = inspect.stack()[0][3]
        # 打开APP
        logging.info(u"正在打开APP，请稍后...")
        # 运行下述函数的时间点
        self.wait_old_time = time.time()
        while True:
            try:
                # 运行下面语句手机APP将启动
                self.driver = webdriver.Remote('http://localhost:4723/wd/hub', self.desired_caps)
                # 运行完上一条语句的时间点
                self.wait_new_time = time.time()
                # 两个时间点相减得到语句运行时间
                self.wait_time = int(self.wait_new_time - self.wait_old_time)
                logging.info(u"打开APP花费时间：共%sS" % self.wait_time)
                # self.err_screen_shot()
                self.wait_old_time = time.time()
                while True:
                    try:
                        # self.init_check_update()
                        # self.init_check_ads()
                        self.init_open_app_page()
                        break
                    except NoSuchElementException:
                        # self.operate_wait_time为程序执行等待时间，默认0.1S
                        time.sleep(self.operate_wait_time)
                        # 超时打开APP失败统计数据+1
                        self.err_open_app_fail(self.open_app_timeout)
                break
            except NoSuchElementException:
                time.sleep(self.operate_wait_time)
                # 超时打开APP失败统计数据+1
                self.err_open_app_fail(self.open_app_timeout)

        # 函数运行完毕时间点
        app_new_time = time.time()
        logging.debug(u"<%s running time = %s S" % (func_name, (app_new_time - app_old_time)))

    def init_open_app_page(self):
        app_old_time = time.time()
        func_name = inspect.stack()[0][3]
        self.wait_old_time = time.time()
        while True:
            try:
                # 检测页面是否加载成功
                self.driver.find_element_by_name(self.app_home)
                logging.info(u"打开APP成功")
                # self.err_screen_shot()
                break
            except NoSuchElementException:
                # self.operate_wait_time为程序执行等待时间，默认0.1S
                time.sleep(self.operate_wait_time)
                # 超时打开APP失败统计数据+1
                self.err_open_app_fail(self.open_app_timeout)

        app_new_time = time.time()
        logging.debug(u"<%s running time = %s S" % (func_name, (app_new_time - app_old_time)))

    # 打开APP检查APP是否有更新弹窗的处理函数
    def init_check_update(self):
        app_old_time = time.time()
        func_name = inspect.stack()[0][3]
        # 检测更新
        logging.info(u"正在检测首页是否有更新")
        self.wait_old_time = time.time()
        while True:
            try:
                # 取消更新
                self.CHECK_UPDATE = self.driver.find_element_by_id(self.check_update)
                logging.info(u"当前页面有更新，正在取消")
                # self.err_screen_shot()
                self.CHECK_UPDATE.click()
                self.wait_old_time = time.time()
                while True:
                    try:
                        # 检测页面是否加载成功
                        self.driver.find_element_by_name(self.home)
                        logging.info(u"取消更新成功")
                        break
                    except NoSuchElementException:
                        time.sleep(self.operate_wait_time)
                        # 操作响应超时统计数据+1
                        self.err_request_timeout(self.request_timeout)
                break
            except NoSuchElementException:
                try:
                    self.driver.find_element_by_name(self.home)
                    logging.info(u"当前软件不需要更新")
                    break
                except NoSuchElementException:
                    time.sleep(self.operate_wait_time)
                    # 操作响应超时统计数据+1
                    self.err_request_timeout(self.request_timeout)

        app_new_time = time.time()
        logging.debug(u"<%s running time = %s S" % (func_name, (app_new_time - app_old_time)))

    # 打开APP检查首页是否有广告广告的处理函数
    def init_check_ads(self):
        app_old_time = time.time()
        func_name = inspect.stack()[0][3]
        # 检测广告
        logging.info(u"正在检测首页是否有广告")
        self.wait_old_time = time.time()
        while True:
            try:
                # 关闭广告
                self.AD = self.driver.find_element_by_id(self.ad)
                logging.info(u"当前页面有广告，正在关闭")
                # self.err_screen_shot()
                self.AD.click()
                self.wait_old_time = time.time()
                while True:
                    try:
                        # 检测页面是否加载成功
                        self.driver.find_element_by_id(self.add_device_plus)
                        logging.info(u"关闭广告成功")
                        break
                    except NoSuchElementException:
                        time.sleep(self.operate_wait_time)
                        # 操作响应超时统计数据+1
                        self.err_request_timeout(self.request_timeout)
                break
            except NoSuchElementException:
                try:
                    self.driver.find_element_by_id(self.add_device_plus)
                    logging.info(u"当前页面没有广告")
                    break
                except NoSuchElementException:
                    time.sleep(self.operate_wait_time)
                    # 操作响应超时统计数据+1
                    self.err_request_timeout(self.request_timeout)

        app_new_time = time.time()
        logging.debug(u"<%s running time = %s S" % (func_name, (app_new_time - app_old_time)))


# 错误处理方法类
class ErrDetection(OpenAppInit):
    # 打开APP失败错误处理
    def err_open_app_fail(self, wait_time):
        self.wait_new_time = time.time()
        self.wait_time = int(self.wait_new_time - self.wait_old_time)
        if self.wait_time > wait_time:
            logging.warning(u"打开APP超时")
            # self.err_screen_shot()
            self.close_app()
            # 打开APP失败统计数+1
            self.err_open_app_fail_count += 1

    # 操作响应超时错误处理
    def err_request_timeout(self, wait_time):
        self.wait_new_time = time.time()
        self.wait_time = int(self.wait_new_time - self.wait_old_time)
        if self.wait_time > wait_time:
            logging.warning(u"操作响应超时")
            # self.err_screen_shot()
            self.close_app()
            # 操作响应超时统计数据+1
            self.err_request_timeout_count += 1

    # 搜索设备超时错误处理
    def err_search_device_timeout(self, wait_time):
        self.wait_new_time = time.time()
        self.wait_time = int(self.wait_new_time - self.wait_old_time)
        if self.wait_time > wait_time:
            logging.warning(u"搜索设备超时")
            # self.err_screen_shot()
            self.close_app()
            # 搜索设备超时统计数据+1
            self.err_search_device_timeout_count += 1

    # 设备离线不恢复超时错误处理
    def err_offline_timeout(self, wait_time):
        self.wait_new_time = time.time()
        self.wait_time = int(self.wait_new_time - self.wait_old_time)
        if self.wait_time > wait_time:
            logging.warning(u"设备离线")
            # self.err_screen_shot()
            self.close_app()
            # 设备离线不恢复超时统计数据+1
            self.err_offline_count += 1

    # 发生程序异常截图
    def err_screen_shot(self, call=1):
        filename = inspect.stack()[call][3]
        file_time = time.localtime()
        file_time = time.strftime("%Y-%m-%d %H-%M-%S", file_time)
        # filename = sys._getframe().f_code.co_name
        screen_shot_file = os.path.join("report/image/" + "[%s]" % file_time + " %s" % filename + ".png")
        self.driver.get_screenshot_as_file(screen_shot_file)
        logging.info(u"保存%s屏幕截图成功" % filename)
        return filename

    # 关闭APP
    def close_app(self):
        logging.warning(u"正在关闭APP")
        self.driver.close_app()
        time.sleep(0.1)
        self.driver.quit()
        time.sleep(0.1)
        logging.warning(u"关闭APP成功")


class PageDetection(ErrDetection):
    #
    def page_unit(self, id=None, name=None, xpath=None):
        func_name = inspect.stack()[1][3]
        logging.info(u"L_loading...%s " % func_name)
        self.wait_old_time = time.time()
        while True:
            try:
                if id != None:
                    self.driver.find_element_by_id(id)
                elif name != None:
                    self.driver.find_element_by_name(name)
                elif xpath != None:
                    self.driver.find_element_by_xpath(xpath)
                logging.info(u"L_loading...(%s)success" % func_name)
                # self.err_screen_shot(delay)
                break
            except NoSuchElementException:
                time.sleep(self.operate_wait_time)
                self.err_request_timeout(self.request_timeout)

    def page_add_device_list(self):
        self.page_unit(name=self.add_device_method)

    def page_add_outlet_list(self):
        self.page_unit(name=self.add_outlet_list)

    def page_add_specification(self):
        self.page_unit(id=self.add_specification_confirm)

    def page_add_history_list(self):
        self.page_unit(name=self.add_history_list)

    def page_input_wifi_password(self):
        self.page_unit(id=self.confirm_wifi_password)

    def page_search_device_loading(self):
        self.page_unit(xpath=self.search_device_loading)

    def page_batch_add_device(self):
        self.page_unit(name=self.batch_add_device)

    def page_search_device_success(self):
        self.page_unit(xpath=self.search_device_success)

    def page_search_device_fail(self):
        self.page_unit(name=self.search_device_fail)

    def page_bind_device_success(self):
        self.page_unit(name=self.bind_device_success)

    def page_added_device(self):
        self.page_unit(id=self.control_device)

    def page_bind_device(self):
        self.page_unit(name=self.bind_device)

    def page_control_device(self):
        self.page_unit(id=self.control_device)

    def page_device_info(self):
        self.page_unit(name=self.device_info)

    def page_swich_on(self):
        self.page_unit(name=self.power_on)

    def page_swich_off(self):
        self.page_unit(name=self.power_off)

class PopupsDetection(ErrDetection):
    def popups_unit(self, id=None, name=None, xpath=None):
        app_old_time = time.time()
        func_name = inspect.stack()[1][3]
        # 检测+号
        logging.info(u"正在检测是否进入 %s 弹窗" % func_name)
        self.wait_old_time = time.time()
        while True:
            try:
                if id != None:
                    self.driver.find_element_by_id(id)
                elif name != None:
                    self.driver.find_element_by_name(name)
                elif xpath != None:
                    self.driver.find_element_by_xpath(xpath)
                self.driver.find_element_by_id(self.bind_device_fail)
                logging.info(u"出现 %s 弹窗" % func_name)
                # self.err_screen_shot()
                break
            except NoSuchElementException:
                time.sleep(self.operate_wait_time)
                # 操作响应超时统计数据+1
                self.err_request_timeout(self.request_timeout)

        app_new_time = time.time()
        logging.debug(u"<%s running time = %s S" % (func_name, (app_new_time - app_old_time)))

    def popups_bind_device_fail(self):
        self.popups_unit(id=self.bind_device_fail)

    # 解绑设备结果页面的处理函数
    def popups_unbind_device(self):
        self.popups_unit(id=self.unbind_device_confirm)

    # 检查设备是否离线
    def check_offline(self):
        app_old_time = time.time()
        func_name = inspect.stack()[0][3]
        # 控制电源按钮
        logging.info(u"正在检测设备是否在线")
        self.wait_old_time = time.time()
        while True:
            try:
                self.driver.find_element_by_name(self.offline)
                logging.info(u"设备不在线")
                # self.err_screen_shot()
                # 设备离线不恢复超时统计数据+1
                self.err_offline(self.offline_recovery_timeout)
                break
            except NoSuchElementException:
                logging.info(u"设备在线")
                # self.err_screen_shot()
                break

        app_new_time = time.time()
        logging.debug(u"<%s running time = %s S" % (func_name, (app_new_time - app_old_time)))


class WidgetOperation(PageDetection, PopupsDetection):
    # 添加设备按钮控件的操作处理函数
    def widget_edit_input(self, data):
        if data != None:
            logging.info(u"正在输入密码")
            # 29 is the keycode of 'a', 28672 is the keycode of META_CTRL_MASK
            self.driver.press_keycode(29, 28672)
            # KEYCODE_FORWARD_DEL 删除键 112
            self.driver.press_keycode(112)
            # 发送数据
            self.widget.send_keys(data)
            time.sleep(0.5)
            # self.err_screen_shot()

    def widget_click(self,
                     id=None,
                     name=None,
                     xpath=None,
                     CName=None,
                     page=None,
                     data=None,
                     delay=0):
        app_old_time = time.time()
        func_name = inspect.stack()[1][3]
        # 检测+号
        logging.info(u"O_operate...%s" % func_name)
        self.wait_old_time = time.time()
        while True:
            try:
                if id != None:
                    self.widget = self.driver.find_element_by_id(id)
                    time.sleep(delay)
                    self.widget.click()
                    self.widget_edit_input(data)
                elif name != None:
                    self.widget = self.driver.find_element_by_name(name)
                    time.sleep(delay)
                    self.widget.click()
                    self.widget_edit_input(data)
                elif xpath != None:
                    self.widget = self.driver.find_element_by_xpath(xpath)
                    time.sleep(delay)
                    self.widget.click()
                    self.widget_edit_input(data)
                elif CName != None:
                    self.widget = self.driver.find_element_by_class_name(CName)
                    time.sleep(delay)
                    self.widget.click()
                    self.widget_edit_input(data)
                logging.info(u"O_operate...(%s)success" % func_name)
                try:
                    page()
                except:
                    pass
                break
            except NoSuchElementException:
                time.sleep(self.request_timeout)
                # 操作响应超时统计数据+1
                self.err_request_timeout(self.request_timeout)

        app_new_time = time.time()
        logging.debug(u"<%s running time = %s S" % (func_name, (app_new_time - app_old_time)))
        return self.widget

    def widget_slide(self,
                     id=None,
                     name=None,
                     xpath=None,
                     CName=None,
                     page=None,
                     delay=0):
        app_old_time = time.time()
        func_name = inspect.stack()[1][3]
        # 检测插座选项
        logging.info(u"正在操作控件 ： %s " % func_name)
        self.wait_old_time = time.time()
        while True:
            try:
                if id != None:
                    self.widget = self.driver.find_element_by_id(id)
                    time.sleep(delay)
                    self.widget.click()
                    # self.err_screen_shot()
                elif name != None:
                    self.widget = self.driver.find_element_by_name(name)
                    time.sleep(delay)
                    self.widget.click()
                    # self.err_screen_shot()
                elif xpath != None:
                    self.widget = self.driver.find_element_by_xpath(xpath)
                    time.sleep(delay)
                    self.widget.click()
                elif CName != None:
                    self.widget = self.driver.find_element_by_class_name(CName)
                    time.sleep(delay)
                    self.widget.click()
                logging.info(u"操作控件 ： %s 成功" % func_name)
                try:
                    page()
                except:
                    pass
                break
            except NoSuchElementException:
                logging.info(u"操作控件 ： %s 失败，页面向下滑动" % func_name)
                # self.err_screen_shot()
                # 模拟手指向上滑动
                self.driver.swipe(600, 1800, 600, 10, 0)
                time.sleep(self.request_timeout)
                # 操作响应超时统计数据+1
                self.err_request_timeout(self.request_timeout)

        app_new_time = time.time()
        logging.debug(u"<%s running time = %s S" % (func_name, (app_new_time - app_old_time)))
        return self.widget

    def widget_branch(self,
                      mode=None,
                      id=None,
                      name=None,
                      xpath=None,
                      CName=None,
                      choose=None):
        try:
            if choose == "mode":
                if mode == "SORT":
                    self.test_tempo_flag = "SORT"
                elif mode == "HISTORY":
                    self.test_tempo_flag = "HISTORY"
            elif choose == "bind":
                if mode == "BIND_DEVICE_SUCCESS":
                    if id != None:
                        self.driver.find_element_by_id(id)
                    elif name != None:
                        self.driver.find_element_by_name(name)
                    elif xpath != None:
                        self.driver.find_element_by_xpath(xpath)
                    elif CName != None:
                        self.driver.find_element_by_class_name(CName)
                    logging.info(u"设备绑定成功")
                    self.test_tempo_flag = "BIND_DEVICE_SUCCESS"
                elif mode == "BIND_DEVICE_FAIL":
                    if id != None:
                        self.driver.find_element_by_id(id)
                    elif name != None:
                        self.driver.find_element_by_name(name)
                    elif xpath != None:
                        self.driver.find_element_by_xpath(xpath)
                    elif CName != None:
                        self.driver.find_element_by_class_name(CName)
                    logging.info(u"设备绑定失败")
                    self.test_tempo_flag = "BIND_DEVICE_FAIL"
            elif choose == "search":
                if mode == "SEARCH_DEVICE_SUCCESS":
                    if id != None:
                        self.driver.find_element_by_id(id)
                    elif name != None:
                        self.driver.find_element_by_name(name)
                    elif xpath != None:
                        self.driver.find_element_by_xpath(xpath)
                    elif CName != None:
                        self.driver.find_element_by_class_name(CName)
                    logging.info(u"搜索到设备")
                    self.test_tempo_flag = "SEARCH_DEVICE_SUCCESS"
                elif mode == "SEARCH_DEVICE_FAIL":
                    if id != None:
                        self.driver.find_element_by_id(id)
                    elif name != None:
                        self.driver.find_element_by_name(name)
                    elif xpath != None:
                        self.driver.find_element_by_xpath(xpath)
                    elif CName != None:
                        self.driver.find_element_by_class_name(CName)
                    logging.info(u"未搜索到设备")
                    self.test_tempo_flag = "SEARCH_DEVICE_FAIL"
        except NoSuchElementException:
            pass

    def widget_add_device_button(self):
        self.widget_click(id=self.add_device_plus, page=self.page_add_device_list)

    def widget_choose_add_device_mode(self, adding_mode):
        self.widget_branch(choose="mode", mode=adding_mode)

    # 添加设备列表控件的操作处理函数
    def widget_add_device_list(self):
        self.widget_slide(name=self.outlet_option, page=self.page_add_outlet_list)

    # 添加插座列表控件的操作处理函数
    def widget_add_outlet_list(self):
        self.widget_slide(name=self.lgn_y2011dl, page=self.page_add_specification)

    # 设备添加历史按钮控件的操作处理函数
    def widget_add_history_button(self):
        self.widget_click(id=self.add_history, page=self.page_add_history_list)

    # 设备添加历史列表控件的操作处理函数
    def widget_add_history_list(self):
        self.widget_slide(name=self.hgn_y2011dl, page=self.page_add_specification)

    def widget_add_specification(self):
        self.widget_click(id=self.add_specification_confirm, page=self.page_input_wifi_password, delay=5)

    # 添加设备输入WiFi页面控件的操作处理函数
    def widget_input_password_text(self):
        # 检测输入密码页面
        self.widget_click(id=self.wifi_password, data=u"iot123456")

    def widget_input_password_conform(self):
        self.widget_click(id=self.confirm_wifi_password, page=self.page_search_device_loading)

    def widget_search_device_loading(self):
        app_old_time = time.time()
        func_name = inspect.stack()[0][3]
        # 检测搜索设备
        self.wait_old_time = time.time()
        while True:
            try:
                # 确认按钮
                self.wait_old_time = time.time()
                logging.info(u"search device...")
                while True:
                    try:
                        while True:
                            flag = 0
                            for k, v in self.search_device_success.items():
                                try:
                                    self.driver.find_element_by_xpath(k)
                                    self.widget = self.driver.find_element_by_xpath(v)
                                    flag = 1
                                    break
                                except NoSuchElementException:
                                    pass
                            if flag == 1:
                                break
                            else:
                                # 模拟手指向上滑动
                                self.driver.swipe(600, 1100, 600, 900, 0)
                                time.sleep(1)
                        logging.info(u"搜索到设备，等待添加")
                        # self.err_screen_shot()
                        self.test_tempo_flag = "SEARCH_DEVICE_SUCCESS"
                        break
                    except NoSuchElementException:
                        try:
                            self.driver.find_element_by_xpath(self.search_device_fail)
                            logging.info(u"搜索设备超时")
                            # self.err_screen_shot()
                            self.test_tempo_flag = "SEARCH_DEVICE_FAIL"
                            break
                        except NoSuchElementException:
                            time.sleep(self.operate_wait_time)
                            # 搜索设备超时统计数据+1
                            self.err_search_device_timeout(self.search_device_timeout)
                break
            except NoSuchElementException:
                time.sleep(self.operate_wait_time)
                # 搜索设备超时统计数据+1
                self.err_search_device_timeout(self.search_device_timeout)

        app_new_time = time.time()
        logging.debug(u"<%s running time = %s S" % (func_name, (app_new_time - app_old_time)))
        # 搜索设备成功后检测设备状态的处理函数

    def widget_search_device_success(self):
        app_old_time = time.time()
        func_name = inspect.stack()[0][3]
        # 搜索设备成功，检测设备状态
        logging.info(u"正在检测设备当前状态")
        self.wait_old_time = time.time()
        while True:
            try:
                self.widget.click()
                self.wait_old_time = time.time()
                while True:
                    try:
                        # 检测到有添加成功页面确认按钮即为添加成功
                        self.widget_branch(choose="bind", mode="BIND_DEVICE_SUCCESS", CName=self.power_button)
                        break
                    except NoSuchElementException:
                        try:
                            # 检测到设备绑定失败弹窗即为设备绑定失败
                            self.widget_branch(choose="bind", mode="BIND_DEVICE_FAIL", id=self.bind_device_fail)
                            break
                        except NoSuchElementException:
                            time.sleep(self.operate_wait_time)
                            # 操作响应超时统计数据+1
                            self.err_request_timeout(self.request_timeout)
                break
            except NoSuchElementException:
                time.sleep(self.request_timeout)
                # 操作响应超时统计数据+1
                self.err_request_timeout(self.request_timeout)

        app_new_time = time.time()
        logging.debug(u"<%s running time = %s S" % (func_name, (app_new_time - app_old_time)))

    # 搜索设备超时失败的处理函数
    def widget_search_device_fail(self):
        self.err_search_device_timeout_count += 1
        self.close_app()

    # 绑定设备成功页面的处理函数
    def widget_bind_device_success(self):
        self.widget_click(id=self.confirm_button, page=self.page_control_device)
        self.bind_device_success_count += 1

    # 设备已被添加结果的处理函数
    def widget_input_notes(self):
        # 检测输入密码页面
        app_old_time = time.time()
        func_name = inspect.stack()[0][3]
        # 检测+号
        logging.info(u"正在操作控件 ： %s " % func_name)
        self.wait_old_time = time.time()
        while True:
            try:
                # 设置设备备注名
                self.NOTES = self.driver.find_element_by_id(self.notes)
                # self.err_screen_shot()
                self.NOTES.click()
                logging.info(u"正在添加备注")
                # 29 is the keycode of 'a', 28672 is the keycode of META_CTRL_MASK
                self.driver.press_keycode(29, 28672)
                # KEYCODE_FORWARD_DEL 删除键 112
                self.driver.press_keycode(112)
                mac = self.MAC[self.mac_choose_flag].split("-")
                mac = mac[-2] + mac[-1]
                # 发送数据
                self.NOTES.send_keys(mac)
                logging.info(u"操作控件 ： %s 成功" % func_name)
                time.sleep(0.5)
                break
            except NoSuchElementException:
                time.sleep(self.operate_wait_time)
                # 操作响应超时统计数据+1
                self.err_request_timeout(self.request_timeout)

        app_new_time = time.time()
        logging.debug(u"<%s running time = %s S" % (func_name, (app_new_time - app_old_time)))

        # 设备已被添加结果的处理函数

    def widget_added_device(self):
        self.bind_device_added_count += 1

    # 设备已被绑定页面的处理函数
    def widget_bind_device(self):
        self.bind_device_bind_count += 1
        self.close_app()

    # 绑定设备失败弹窗的处理函数
    def widget_bind_device_fail(self):
        self.bind_device_fail_count += 1
        self.close_app()

    # 电源操作函数
    def widget_btn(self, mode=None):
        app_old_time = time.time()
        # func_name = inspect.stack()[0][3]
        # # 控制电源按钮
        # logging.info(u"正在操作控件 ： %s " % func_name)
        # # 开关次数
        # while True:
        #     try:

        #         try:
        #             self.widget_click(CName=self.power_button, page=self.power_on)
        #             self.widget_click(CName=self.power_button, page=self.power_off)
        #             logging.info(u"点击成功")
        #             self.widget_click(name=self.power_off)
        #             logging.info(u"设备电源已关闭")
        #             self.wait_old_time = time.time()
        #             break
        #                 except NoSuchElementException:
        #                     time.sleep(self.operate_wait_time)
        #                     self.wait_new_time = time.time()
        #                     self.wait_time = int(self.wait_new_time - self.wait_old_time)
        #                     if self.wait_time > 5:
        #                         self.POWER_BUTTON.click()
        #                         # 设备离线不恢复超时统计数据+1
        #                         self.err_offline(self.offline_recovery_timeout)
        #         except NoSuchElementException:
        #             try:
        #                 self.driver.find_element_by_name(self.power_off)
        #                 # 点击控件
        #                 self.POWER_BUTTON.click()
        #                 logging.info(u"点击成功")
        #                 self.wait_old_time = time.time()
        #                 while True:
        #                     try:
        #                         self.driver.find_element_by_name(self.power_on)
        #                         logging.info(u"设备电源已开启")
        #                         # # self.err_screen_shot()
        #                         break
        #                     except NoSuchElementException:
        #                         time.sleep(self.operate_wait_time)
        #                         self.wait_new_time = time.time()
        #                         self.wait_time = int(self.wait_new_time - self.wait_old_time)
        #                         if self.wait_time > 5:
        #                             # 点击控件
        #                             self.POWER_BUTTON.click()
        #                             # 设备离线不恢复超时统计数据+1
        #                             self.err_offline(self.offline_recovery_timeout)
        #             except NoSuchElementException:
        #                 time.sleep(self.operate_wait_time)
        #                 # 操作响应超时统计数据+1
        #                 self.err_request_timeout(self.request_timeout)
        #     break
        # except NoSuchElementException:
        #     time.sleep(self.operate_wait_time)
            # 操作响应超时统计数据+1
            # self.err_request_timeout(self.request_timeout)


        # app_new_time = time.time()
        # logging.debug(u"<%s running time = %s S" % (func_name, (app_new_time - app_old_time)))


    def widget_control_power(self):
        app_old_time = time.time()
        func_name = inspect.stack()[0][3]
        # 控制电源按钮
        logging.info(u"正在操作控件 ： %s " % func_name)
        # 开关次数
        while True:
            try:
                self.POWER_BUTTON = self.driver.find_element_by_class_name(self.power_button)
                self.control_time = 2 * 2
                if self.control_time == 0:
                    break
                while self.control_time > 0:
                    self.control_time -= 1
                    try:
                        self.driver.find_element_by_name(self.power_on)
                        self.POWER_BUTTON.click()
                        logging.info(u"点击成功")
                        self.wait_old_time = time.time()
                        while True:
                            try:
                                self.driver.find_element_by_name(self.power_off)
                                logging.info(u"设备电源已关闭")
                                # # self.err_screen_shot()
                                break
                            except NoSuchElementException:
                                time.sleep(self.operate_wait_time)
                                self.wait_new_time = time.time()
                                self.wait_time = int(self.wait_new_time - self.wait_old_time)
                                if self.wait_time > 5:
                                    self.POWER_BUTTON.click()
                                    # 设备离线不恢复超时统计数据+1
                                    self.err_offline(self.offline_recovery_timeout)
                    except NoSuchElementException:
                        try:
                            self.driver.find_element_by_name(self.power_off)
                            # 点击控件
                            self.POWER_BUTTON.click()
                            logging.info(u"点击成功")
                            self.wait_old_time = time.time()
                            while True:
                                try:
                                    self.driver.find_element_by_name(self.power_on)
                                    logging.info(u"设备电源已开启")
                                    # # self.err_screen_shot()
                                    break
                                except NoSuchElementException:
                                    time.sleep(self.operate_wait_time)
                                    self.wait_new_time = time.time()
                                    self.wait_time = int(self.wait_new_time - self.wait_old_time)
                                    if self.wait_time > 5:
                                        # 点击控件
                                        self.POWER_BUTTON.click()
                                        # 设备离线不恢复超时统计数据+1
                                        self.err_offline(self.offline_recovery_timeout)
                        except NoSuchElementException:
                            time.sleep(self.operate_wait_time)
                            # 操作响应超时统计数据+1
                            self.err_request_timeout(self.request_timeout)
                break
            except NoSuchElementException:
                time.sleep(self.operate_wait_time)
                # 操作响应超时统计数据+1
                self.err_request_timeout(self.request_timeout)

        app_new_time = time.time()
        logging.debug(u"<%s running time = %s S" % (func_name, (app_new_time - app_old_time)))


    # APP设备详情页面的操作处理函数
    def widget_device_info(self):
        self.widget_click(id=self.device_info_button, page=self.page_device_info)


    # 解绑设备结果页面的处理函数
    def widget_unbind_device(self):
        app_old_time = time.time()
        func_name = inspect.stack()[0][3]
        # 检测检测设备是否删除成功
        logging.info(u"正在操作控件 ： %s " % func_name)
        self.wait_old_time = time.time()
        while True:
            try:
                self.UNBIND_DEVICE = self.driver.find_element_by_id(self.unbind_device)
                # self.err_screen_shot()
                self.UNBIND_DEVICE.click()
                logging.info(u"操作控件 ： %s 成功" % func_name)
                self.popups_unbind_device()
                self.widget_popups_unbind_device()
                break
            except NoSuchElementException:
                time.sleep(self.operate_wait_time)
                # 操作响应超时统计数据+1
                self.err_request_timeout(self.request_timeout)
        self.close_app()

        app_new_time = time.time()
        logging.debug(u"<%s running time = %s S" % (func_name, (app_new_time - app_old_time)))


    def widget_popups_unbind_device(self):
        app_old_time = time.time()
        func_name = inspect.stack()[0][3]
        logging.info(u"正在操作控件 ： %s " % func_name)
        self.wait_old_time = time.time()
        while True:
            try:
                self.UNBIND_DEVICE_CONFIRM = self.driver.find_element_by_id(self.unbind_device_confirm)
                # self.err_screen_shot()
                self.UNBIND_DEVICE_CONFIRM.click()
                logging.info(u"操作控件 ： %s 成功" % func_name)
                time.sleep(2)
                while True:
                    try:
                        self.driver.find_element_by_name(self.app_home)
                        logging.info(u"设备解除绑定成功")
                        # self.err_screen_shot()
                        break
                    except NoSuchElementException:
                        try:
                            self.driver.find_element_by_id(self.unbind_device)
                            logging.info(u"设备解除绑定失败")
                            # self.err_screen_shot()
                            break
                        except NoSuchElementException:
                            time.sleep(self.operate_wait_time)
                            # 操作响应超时统计数据+1
                            self.err_request_timeout(self.request_timeout)
                break
            except NoSuchElementException:
                time.sleep(self.operate_wait_time)
                # 操作响应超时统计数据+1
                self.err_request_timeout(self.request_timeout)
        app_new_time = time.time()
        logging.debug(u"<%s running time = %s S" % (func_name, (app_new_time - app_old_time)))  # 所有可控控件的操作方法
class Report(WidgetOperation):
    # 测试结果输出处理函数
    def report(self):
        logging.info("&" * 40)
        logging.info(u"测试次数：%s次" % self.program_loop_time)
        logging.info(u"绑定成功次数：%s次" % self.bind_device_success_count)
        logging.info(u"绑定失败次数：%s次" % self.bind_device_fail_count)
        logging.info(u"搜索设备超时次数：%s次" % self.err_search_device_timeout_count)
        logging.info(u"已被添加次数：%s次" % self.bind_device_added_count)
        logging.info(u"已被绑定次数：%s次" % self.bind_device_bind_count)
        logging.info(u"操作超时次数：%s次" % self.err_request_timeout_count)
        logging.info(u"APP打开失败次数：%s次" % self.err_open_app_fail_count)
        logging.info(u"离线次数：%s次" % self.err_offline_count)
        logging.info("&" * 40)
