# coding=utf-8
from appium import webdriver
from src.testcase.case.ToDevicePage import *
from src.testcase.case.ToLoginPage import *
from src.testcase.common.WidgetCheckUnit import *
from src.utils.ReadConf import *


class LaunchApp(object):
    conf = conf

    def __init__(self, device_list, device_name, logger):
        self.device_list = device_list
        self.device_name = device_name
        self.device_info = device_list[device_name]
        self.logger = logger
        self.debug = self.device_info["debug"]
        self.user = self.device_info["user_and_pwd"]
        self.case_module = ""  # 用例所属模块
        self.case_title = ""  # 用例名称
        self.zentao_id = 0000  # 禅道ID
        self.basename = ""  # 用例自动化文件名称
        self.success = False  # 初始化用例执行结果
        self.start_fail = False  # 初始化APP启动结果
        self.driver = None
        self.widget_click = None
        self.wait_widget = None
        self.start_time = None

    def init_operate(self, driver):
        self.debug.info("driver(init_operate):%s" % self.driver)
        self.driver = driver
        widget_check_unit = WidgetCheckUnit(self.driver, self.logger)  # 元素初始化
        self.widget_click = widget_check_unit.widget_click  # 初始化self.widget_click
        self.wait_widget = widget_check_unit.wait_widget  # 初始化self.wait_widget
        self.start_time = time.strftime("%Y-%m-%d %H:%M:%S")
        self.logger.info('app start [time=%s]' % self.start_time)  # 记录log，APP打开时间
        self.success = False

    def data_statistics(self, zentao_id):
        self.debug.info("zentao_id:%s" % zentao_id)
        if zentao_id in database[self.device_name].keys():
            pass
        else:
            database[self.device_name][zentao_id] = {}
            database[self.device_name][zentao_id]["test_count"] = 0
            database[self.device_name][zentao_id]["test_pass"] = 0
            database[self.device_name][zentao_id]["test_fail"] = 0
            database[self.device_name][zentao_id]["test_error"] = 0
            database[self.device_name][zentao_id]["test_wait"] = 0
            database[self.device_name][zentao_id]["ZenTao"] = zentao_id
            database[self.device_name][zentao_id]["case_title"] = self.case_title
        self.debug.info("%s:%s" % (zentao_id, database[self.device_name][zentao_id]))

    def launch_app(self, page_login, first_time=True):
        self.debug.info("basename:%s" % self.basename)
        self.data_statistics(self.zentao_id)
        self.start_fail = False
        try:
            i = 3
            while i > 0:
                try:
                    self.driver = webdriver.Remote('http://localhost:%s/wd/hub' % self.device_info["port"],
                                                   self.device_info["desired_caps"])  # 启动APP
                    self.start_fail = False  # 缺少此条语句将造成APP启动一直失败原因为第73行
                    self.debug.info("driver(while):%s" % self.driver)
                    break
                except WebDriverException:
                    self.start_fail = True
                    self.debug.error("driver(WebDriverException):%s" % self.start_fail)
                finally:
                    i -= 1
            self.debug.info("driver(over):%s" % self.driver)
            if self.start_fail is True:
                self.debug.error("driver(over):App start failed")
                raise WebDriverException("App start failed")

            self.init_operate(self.driver)

            if page_login is True and first_time is True:
                ToLoginPage(self.driver, self.logger, self.device_info)  # 使APP跳转到登录页面等待
            elif page_login is False and first_time is True:
                ToDevicePage(self.driver, self.logger, self.device_info)  # 使APP跳转到设备主页面等待
        except WebDriverException:
            self.case_over("unknown")
            self.debug.error("case_over:Case launch unknown")
            raise WebDriverException("Case launch unknown")

    def case_over(self, success):
        self.success = success
        time.sleep(1)
        try:
            if self.start_fail is True:
                raise WebDriverException("App start failed")
            self.driver.close_app()  # 关闭APP
            self.driver.quit()  # 退出appium服务
        except WebDriverException:
            self.debug.error("case_over(success):Case launch unknown")
            pass
        self.logger.info('app closed [time=%s]' % time.strftime("%Y-%m-%d %H:%M:%S"))
        database[self.device_name][self.zentao_id]["test_count"] += 1

    # 记录运行结果
    def result(self):
        if self.success is True:
            self.logger.info('[GN_INF] <current case> [CASE_TITLE="%s"] success!' % self.case_title)
            database[self.device_name][self.zentao_id]["test_pass"] += 1
            return "success", self.zentao_id, self.case_title, self.start_time
        elif self.success is False:
            self.logger.info('[GN_INF] <current case> [CASE_TITLE="%s"] failed!' % self.case_title)
            database[self.device_name][self.zentao_id]["test_fail"] += 1
            return "failed", self.zentao_id, self.case_title, self.start_time
        elif self.success == "unknown":
            self.logger.info('[GN_INF] <current case> [CASE_TITLE="%s"] unknown!' % self.case_title)
            database[self.device_name][self.zentao_id]["test_error"] += 1
            return "unknown", self.zentao_id, self.case_title, self.start_time
        elif self.success == "screen":
            self.logger.info('[GN_INF] <current case> [CASE_TITLE="%s"] waiting for review!' % self.case_title)
            database[self.device_name][self.zentao_id]["test_wait"] += 1
            return "wait", self.zentao_id, self.case_title, self.start_time
