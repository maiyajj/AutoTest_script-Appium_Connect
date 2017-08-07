# coding=utf-8
from src.testcase.case.LaunchApp import *


class GNAppMessageClassify4(LaunchApp):
    @case_run
    def run(self):
        self.case_module = u"消息"  # 用例所属模块
        self.case_title = u'消息设置页面信息检查'  # 用例名称
        self.zentao_id = 1925  # 禅道ID


    # 用例动作
    def case(self):
        try:
            self.widget_click(self.page["device_page"]["title"],
                              self.page["device_page"]["message_table"],
                              self.page["home_message_page"]["title"],
                              1, 1, 1, 10, 0.5)

            self.widget_click(self.page["home_message_page"]["title"],
                              self.page["home_message_page"]["setting"],
                              self.page["message_setting_page"]["title"],
                              1, 1, 1, 10, 0.5)

            self.wait_widget(self.page["message_setting_page"]["title"], 3, 1)

            self.wait_widget(self.page["message_setting_page"]["to_return"], 3, 1)

            self.wait_widget(self.page["message_setting_page"]["clear_activity"], 3, 1)

            self.wait_widget(self.page["message_setting_page"]["clear_device"], 3, 1)

            self.case_over(True)
        except TimeoutException:
            self.case_over(False)

