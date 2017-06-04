# coding=utf-8
import traceback
from urllib2 import URLError

from appium import webdriver

from src.testcase.case.ToDevicePage import *
from src.testcase.case.ToLoginPage import *
from src.testcase.common.WidgetCheckUnit import *
from src.utils.ScreenShot import *

class LaunchApp(object):
    conf = conf

    def __init__(self, device_list, device_name, logger, sc):
        self.device_list = device_list
        self.device_name = device_name
        self.device_info = device_list[device_name]
        self.logger = logger
        self.sc = sc
        self.debug = self.device_info["debug"]
        self.user = self.device_name
        self.case_module = ""  # 用例所属模块
        self.case_title = ""  # 用例名称
        self.zentao_id = 0000  # 禅道ID
        self.basename = ""  # 用例自动化文件名称
        self.success = False  # 初始化用例执行结果
        # self.start_fail = False  # 初始化APP启动结果
        self.widget_click = None
        self.wait_widget = None
        self.start_time = None

    def init_app(self):
        global driver
        try:
            i = 1
            ii = 1
            while True:
                try:
                    self.debug.warn("init_app driver(ready launch)")
                    driver = webdriver.Remote('http://localhost:%s/wd/hub' % self.device_info["port"],
                                              self.device_info["desired_caps"])  # 启动APP
                    self.debug.info("init_app driver(launch success):%s" % driver)
                    driver.close_app()
                    self.debug.info("init_app driver(close_app success):%s" % driver)
                    break
                except WebDriverException:
                    self.debug.error("init_app driver(WebDriverException):%s times" % i)
                    i += 1
                    time.sleep(1)
                except URLError:
                    self.debug.error("init_app driver(URLError):%s times" % ii)
                    ii += 1
                    while True:
                        try:
                            self.sc.find_proc_and_pid_by_port(self.device_info["port"])[0]
                        except IndexError:
                            time.sleep(1)
                        else:
                            self.debug.error(
                                "init_app Appium Sever Restart Success! %s" % time.strftime("%Y-%m-%d %H:%M:%S"))
                            break

        except BaseException:
            self.debug.error(traceback.format_exc())

    def init_operate(self):
        self.debug.info("driver(init_operate):%s" % driver)
        widget_check_unit = WidgetCheckUnit(driver, self.logger)  # 元素初始化
        self.widget_click = widget_check_unit.widget_click  # 初始化self.widget_click
        self.wait_widget = widget_check_unit.wait_widget  # 初始化self.wait_widget

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

    def launch_app(self, page_login):
        global driver
        self.debug.info("basename:%s" % self.basename)
        self.data_statistics(self.zentao_id)
        try:
            i = 1
            ii = 1
            iii = 1
            while True:
                try:
                    self.debug.warn("launch_app driver(ready launch)")
                    driver.close_app()
                    self.debug.info("launch_app driver(close_app success):%s" % driver)
                    driver.launch_app()
                    self.debug.info("launch_app driver(launch_app success):%s" % driver)
                    break
                except WebDriverException, e:
                    if "A new session could not be created" not in e:
                        self.debug.error("launch_app driver(WebDriverException):%s times" % i)
                        i += 1
                        time.sleep(1)
                    else:
                        try:
                            pid = self.sc.find_proc_and_pid_by_port(5037)  # 判断5037端口是否被占用
                            for i in pid:
                                self.sc.kill_proc_by_pid(i[1])
                                self.debug.error(u"appium重启后关闭%s进程" % i[0])
                        except IndexError:
                            self.debug.error(u"appium重启后没有程序占用5037端口")
                            
                except URLError:
                    self.debug.error("launch_app driver(URLError):%s times" % ii)
                    ii += 1
                    while True:
                        try:
                            self.sc.find_proc_and_pid_by_port(self.device_info["port"])[0]
                        except IndexError:
                            time.sleep(1)
                        else:
                            self.debug.error(
                                "launch_app Appium Sever Restart Success! %s" % time.strftime("%Y-%m-%d %H:%M:%S"))
                            while True:
                                try:
                                    driver = webdriver.Remote('http://localhost:%s/wd/hub' % self.device_info["port"],
                                                              self.device_info["desired_caps"])  # 启动APP
                                    break
                                except WebDriverException:
                                    self.debug.error("URLError driver(WebDriverException):%s times" % iii)
                                    iii += 1
                            break

            self.init_operate()
            self.start_time = time.strftime("%Y-%m-%d %H:%M:%S")
            self.logger.info('app start [time=%s]' % self.start_time)  # 记录log，APP打开时间
            self.success = False

            if page_login is True:
                ToLoginPage(driver, self.logger, self.device_info)  # 使APP跳转到登录页面等待
            elif page_login is False:
                ToDevicePage(driver, self.logger, self.device_info)  # 使APP跳转到设备主页面等待
        except BaseException:
            self.case_over("unknown")
            self.debug.error("case_over:%s" % traceback.format_exc())
            raise WebDriverException("Case launch unknown")

    # def launch_app(self, page_login, first_time=True):
    #     self.debug.info("basename:%s" % self.basename)
    #     self.data_statistics(self.zentao_id)
    #     self.start_fail = False
    #     try:
    #         i = 1
    #         while i <= 3:
    #             try:
    #                 while True:
    #                     try:
    #                         try:
    #                             driver.quit()  # 确保appium服务已关闭
    #                         except AttributeError:
    #                             raise WebDriverException()
    #                     except WebDriverException:
    #                         driver = webdriver.Remote('http://localhost:%s/wd/hub' % self.device_info["port"],
    #                                                        self.device_info["desired_caps"])  # 启动APP
    #                         self.start_fail = False  # 缺少此条语句将造成APP启动一直失败原因为第73行
    #                         self.debug.info("driver(while):%s" % driver)
    #                         break
    #                 break
    #             except WebDriverException:
    #                 self.start_fail = True
    #                 i += 1
    #                 self.debug.error("driver(WebDriverException):%s,%s" % (self.start_fail, i))
    #
    #         self.debug.info("driver(over):%s" % driver)
    #         if self.start_fail is True:
    #             self.debug.error("driver(over):App start failed")
    #             raise WebDriverException("App start failed")
    #
    #         self.debug.warn("self.start_fail:%s" % self.start_fail)
    #         self.init_operate(driver)
    #
    #         if page_login is True and first_time is True:
    #             ToLoginPage(driver, self.logger, self.device_info)  # 使APP跳转到登录页面等待
    #         elif page_login is False and first_time is True:
    #             ToDevicePage(driver, self.logger, self.device_info)  # 使APP跳转到设备主页面等待
    #     except WebDriverException:
    #         self.case_over("unknown")
    #         self.debug.error("case_over:Case launch unknown")
    #         raise WebDriverException("Case launch unknown")
    def return_driver(self):
        return driver

    def case_over(self, success):
        self.success = success
        time.sleep(1)
        try:
            driver.close_app()  # 关闭APP
            self.debug.warn("(%s)driver.close_app() App close" % self.basename)
        except WebDriverException:
            self.debug.error("case_over(success):Case launch unknown")
            self.debug.error(traceback.format_exc())

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
