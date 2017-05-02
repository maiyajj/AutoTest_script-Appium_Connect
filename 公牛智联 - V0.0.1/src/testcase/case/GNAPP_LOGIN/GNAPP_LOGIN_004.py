# coding=utf-8
import os

from src.testcase.case.LaunchApp import *
from src.testcase.case.ToLoginPage import *
from src.utils.ScreenShot import *


class GNAppLogin4(object):
    def __init__(self, device_list, device_name, logger):
        self.device_list = device_list
        self.device_name = device_name
        self.device_info = device_list[device_name]
        self.logger = logger

        self.case_module = u"登录"  # 用例所属模块
        self.case_title = u'登录页面—成功登录后杀掉APP，再次开启APP的状态查看'  # 用例名称
        self.ZenTao_id = 1903  # 禅道ID
        self.basename = os.path.basename(__file__).split(".")[0]  # 获取用例的文件名称:GNAPP_LOGIN_004
        self.logger.info('[GN_INF] <current case> [CASE_ID="%s", CASE_NAME="%s", 禅道ID="%s", CASE_MODULE="%s"]'
                         % (self.basename, self.case_title, self.ZenTao_id, self.case_module))  # 记录log

        if self.ZenTao_id in database[device_name].keys():
            pass
        else:
            database[device_name][self.ZenTao_id] = {}
            database[device_name][self.ZenTao_id]["test_count"] = 0
            database[device_name][self.ZenTao_id]["test_pass"] = 0
            database[device_name][self.ZenTao_id]["test_fail"] = 0
            database[device_name][self.ZenTao_id]["test_error"] = 0
            database[device_name][self.ZenTao_id]["test_wait"] = 0
            database[device_name][self.ZenTao_id]["ZenTao"] = self.ZenTao_id
            database[device_name][self.ZenTao_id]["case_title"] = self.case_title

        try:
            self.driver = launch_app(self.device_info)  # 启动APP
            widget_check_unit = WidgetCheckUnit(self.driver, self.logger)  # 元素初始化
            self.widget_click = widget_check_unit.widget_click  # 初始化self.widget_click
            self.wait_widget = widget_check_unit.wait_widget  # 初始化self.wait_widget
            self.start_time = time.strftime("%Y-%m-%d %H:%M:%S")
            self.logger.info('app start [time=%s]' % self.start_time)  # 记录log，APP打开时间
            self.success = 0
            ToLoginPage(self.driver, self.logger)  # 使APP跳转到登录页面等待

            self.case()
        except WebDriverException:
            self.case_over("unknown")

    # 用例动作
    def case(self):
        try:
            self.widget_click(login_page["title"],
                              login_page["login_button"],
                              device_page["title"],
                              1, 1, 1, 10, 0.5)

            self.driver.quit()  # 退出appium服务
            self.logger.info(u"[APP_INF] APP退出")
            time.sleep(1)

            try:
                self.driver = launch_app(self.device_info)  # 启动APP
                widget_check_unit = WidgetCheckUnit(self.driver, self.logger)  # 元素初始化
                self.widget_click = widget_check_unit.widget_click  # 初始化self.widget_click
                self.wait_widget = widget_check_unit.wait_widget  # 初始化self.wait_widget
            except WebDriverException:
                self.case_over("unknown")

            self.logger.info(u"[APP_INF] APP重新启动")
            while True:
                if self.driver.current_activity == login_popup["activity"][0]:
                    try:
                        self.wait_widget(update_popup["title"], 3, 1)
                        self.logger.info(u"[APP_INF] APP有最新版本，可以更新")
                        self.widget_click(update_popup["title"],
                                          update_popup["cancel"],
                                          god_page["title"],
                                          1, 1, 1, 10, 0.5, 0)
                        self.logger.info(u"[APP_INF] 取消更新")
                    except TimeoutException:
                        pass
                    try:
                        self.wait_widget(login_popup["title"], 3, 1)
                        self.logger.info(u"[APP_INF] APP需要重新登陆，等待重新登录")
                        self.widget_click(login_popup["title"],
                                          login_popup["confirm"],
                                          login_page["title"],
                                          1, 1, 1, 10, 0.5, 0)
                    except TimeoutException:
                        pass

                if self.driver.current_activity == login_page["activity"][0]:
                    self.logger.info(u"[APP_INF] APP当前页面为登录页面， 错误！")
                    raise TimeoutException()

                if self.driver.current_activity == device_page["activity"][0]:
                    self.logger.info(u"[APP_INF] APP当前页面为主页面")
                    break

            self.case_over(True)
        except TimeoutException:
            self.case_over(False)

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

    def result(self):
        if self.success is True:
            self.logger.info('[GN_INF] <current case> [CASE_TITLE="%s"] success!' % self.case_title)  # 记录运行结果
            database[self.device_name][self.ZenTao_id]["test_pass"] += 1
            return "success", self.ZenTao_id, self.case_title, self.start_time
        elif self.success is False:
            self.logger.info('[GN_INF] <current case> [CASE_TITLE="%s"] failed!' % self.case_title)
            database[self.device_name][self.ZenTao_id]["test_fail"] += 1
            return "failed", self.ZenTao_id, self.case_title, self.start_time
        elif self.success == "unknown":
            self.logger.info('[GN_INF] <current case> [CASE_TITLE="%s"] unknown!' % self.case_title)
            database[self.device_name][self.ZenTao_id]["test_error"] += 1
            return "unknown", self.ZenTao_id, self.case_title, self.start_time
