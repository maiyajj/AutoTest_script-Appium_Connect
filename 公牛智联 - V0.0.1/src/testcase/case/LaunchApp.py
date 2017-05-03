# coding=utf-8
from appium import webdriver
from src.testcase.case.ToDevicePage import *
from src.testcase.case.ToLoginPage import *
from src.testcase.common.WidgetCheckUnit import *


class LaunchApp(object):
    def __init__(self, device_list, device_name, logger):
        self.device_list = device_list
        self.device_name = device_name
        self.device_info = device_list[device_name]
        self.logger = logger

    def init_operate(self, driver):
        self.driver = driver
        widget_check_unit = WidgetCheckUnit(self.driver, self.logger)  # 元素初始化
        self.widget_click = widget_check_unit.widget_click  # 初始化self.widget_click
        self.wait_widget = widget_check_unit.wait_widget  # 初始化self.wait_widget
        self.start_time = time.strftime("%Y-%m-%d %H:%M:%S")
        self.logger.info('app start [time=%s]' % self.start_time)  # 记录log，APP打开时间
        self.success = False

    def data_statistics(self, ZenTao_id):
        self.logger.info('[GN_INF] <current case> [CASE_ID="%s", CASE_NAME="%s", 禅道ID="%s", CASE_MODULE="%s"]'
                         % (self.basename, self.case_title, ZenTao_id, self.case_module))  # 记录log

        if ZenTao_id in database[self.device_name].keys():
            pass
        else:
            database[self.device_name][ZenTao_id] = {}
            database[self.device_name][ZenTao_id]["test_count"] = 0
            database[self.device_name][ZenTao_id]["test_pass"] = 0
            database[self.device_name][ZenTao_id]["test_fail"] = 0
            database[self.device_name][ZenTao_id]["test_error"] = 0
            database[self.device_name][ZenTao_id]["test_wait"] = 0
            database[self.device_name][ZenTao_id]["ZenTao"] = ZenTao_id
            database[self.device_name][ZenTao_id]["case_title"] = self.case_title

    def launch_app(self, Login_page):
        self.data_statistics(self.ZenTao_id)
        try:
            i = 3
            while i > 0:
                try:
                    self.driver = webdriver.Remote('http://localhost:%s/wd/hub' % self.device_info["port"],
                                                   self.device_info["desired_caps"])  # 启动APP
                    break
                except WebDriverException:
                    self.driver = "WebDriverException"
                finally:
                    i -= 1
            if self.driver == "WebDriverException":
                raise WebDriverException()

            self.init_operate(self.driver)

            if Login_page is True:
                ToLoginPage(self.driver, self.logger)  # 使APP跳转到登录页面等待
            elif Login_page is False:
                ToDevicePage(self.driver, self.logger)  # 使APP跳转到设备主页面等待

        except WebDriverException:
            self.case_over("unknown")

    def case_over(self, success):
        self.success = success
        time.sleep(1)
        try:
            self.driver.close_app()  # 关闭APP
            self.driver.quit()  # 退出appium服务
        except WebDriverException:
            pass
        self.logger.info('app closed [time=%s]' % time.strftime("%Y-%m-%d %H:%M:%S"))
        database[self.device_name][self.ZenTao_id]["test_count"] += 1

    # 记录运行结果
    def result(self):
        if self.success is True:
            self.logger.info('[GN_INF] <current case> [CASE_TITLE="%s"] success!' % self.case_title)
            database[self.device_name][self.ZenTao_id]["test_pass"] += 1
            return "success", self.ZenTao_id, self.case_title, self.start_time
        elif self.success is False:
            self.logger.info('[GN_INF] <current case> [CASE_TITLE="%s"] failed!' % self.case_title)
            database[self.device_name][self.ZenTao_id]["test_fail"] += 1
            return "failed", self.ZenTao_id, self.case_title, self.start_time
        else:
            self.logger.info('[GN_INF] <current case> [CASE_TITLE="%s"] unknown!' % self.case_title)
            database[self.device_name][self.ZenTao_id]["test_error"] += 1
            return "unknown", self.ZenTao_id, self.case_title, self.start_time
