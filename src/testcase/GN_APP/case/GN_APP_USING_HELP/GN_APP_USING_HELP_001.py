# coding=utf-8
from src.testcase.GN_APP.WidgetOperation import *


class GNAPPUsingHelp1(WidgetOperation):
    @case_run(False)
    def run(self):
        self.case_module = u"使用帮助"  # 用例所属模块
        self.case_title = u'返回按钮功能确认'  # 用例名称
        self.zentao_id = 1975  # 禅道ID

    # 用例动作
    def case(self):
        self.widget_click(self.page["device_page"]["user_image"],
                          self.page["personal_settings_page"]["title"])

        self.widget_click(self.page["personal_settings_page"]["using_help"],
                          self.page["app_help_page"]["title"])

        self.widget_click(self.page["app_help_page"]["to_return"],
                          self.page["personal_settings_page"]["title"])
