# coding=utf-8
import os

from src.testcase.case.LaunchApp import *
from src.testcase.case.ToDevicePage import *


class GNAppVersion1(object):
    def __init__(self, device_list, device_name, logger):
        self.device_list = device_list
        self.device_name = device_name
        self.device_info = device_list[device_name]
        self.logger = logger

        self.case_module = u"版本信息"  # 用例所属模块
        self.case_title = u'版本信息-当前版本为最新版本，页面信息检查'  # 用例名称
        self.ZenTao_id = 1992  # 禅道ID
        self.basename = os.path.basename(__file__).split(".")[0]  # 获取用例的文件名称:GNAPP_VERSION_001
        self.logger.info('[GN_INF] <current case> [CASE_ID="%s", CASE_NAME="%s", 禅道ID="%s", CASE_MODULE="%s"]'
                         % (self.basename, self.case_title, self.ZenTao_id, self.case_module))  # 记录log

        try:
            self.driver = launch_app(self.device_info)  # 启动APP
            widget_check_unit = WidgetCheckUnit(self.driver, self.logger)  # 元素初始化
            self.widget_click = widget_check_unit.widget_click  # 初始化self.widget_click
            self.wait_widget = widget_check_unit.wait_widget  # 初始化self.wait_widget
            self.start_time = time.strftime("%Y-%m-%d %H:%M:%S")
            self.logger.info('app start [time=%s]' % self.start_time)  # 记录log，APP打开时间
            self.success = 0
            ToDevicePage(self.driver, self.logger)  # 使APP跳转到设备主页面等待

            self.case()
        except WebDriverException:
            self.case_over("unknown")

    # 用例动作
    def case(self):
        try:
            self.widget_click(device_page["title"],
                              device_page["user_image"],
                              personal_settings_page["title"],
                              1, 1, 1, 10, 0.5)

            self.widget_click(personal_settings_page["title"],
                              personal_settings_page["version_info"],
                              upgrade_page["title"],
                              1, 1, 1, 10, 0.5)

            current_version = self.wait_widget(upgrade_page["current_version"], 3, 1).get_attribute("name")[-10:]

            new_version = self.wait_widget(upgrade_page["new_version"], 3, 1).get_attribute("name")[-10:]

            btn_state = self.wait_widget(upgrade_page["upgrade_button"], 3, 1).get_attribute("enabled")

            if current_version == new_version and btn_state != "false":
                raise TimeoutException()

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

    def result(self):
        if self.success is True:
            self.logger.info('[GN_INF] <current case> [CASE_TITLE="%s"] success!' % self.case_title)  # 记录运行结果
            return "success", self.case_title, self.start_time
        elif self.success is False:
            self.logger.info('[GN_INF] <current case> [CASE_TITLE="%s"] failed!' % self.case_title)
            return "failed", self.case_title, self.start_time
        elif self.success == "unknown":
            self.logger.info('[GN_INF] <current case> [CASE_TITLE="%s"] unknown!' % self.case_title)
            return "unknown", self.case_title, self.start_time
