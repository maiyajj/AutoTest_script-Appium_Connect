# coding=utf-8
from src.testcase.case.LaunchApp import *


class GNAppUsingHelp1(LaunchApp):
    @case_run
    def run(self):
        self.case_module = u"使用帮助"  # 用例所属模块
        self.case_title = u'返回按钮功能确认'  # 用例名称
        self.zentao_id = 1975  # 禅道ID


    # 用例动作
    def case(self):
        try:
            self.widget_click(self.page["device_page"]["title"],
                              self.page["device_page"]["user_image"],
                              self.page["personal_settings_page"]["title"],
                              1, 1, 1, 10, 0.5)

            self.widget_click(self.page["personal_settings_page"]["title"],
                              self.page["personal_settings_page"]["using_help"],
                              self.page["app_help_page"]["title"],
                              1, 1, 1, 10, 0.5)

            self.widget_click(self.page["app_help_page"]["title"],
                              self.page["app_help_page"]["to_return"],
                              self.page["personal_settings_page"]["title"],
                              1, 1, 1, 10, 0.5)

            self.case_over(True)
        except TimeoutException:
            self.case_over(False)

