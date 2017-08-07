# coding=utf-8
from src.testcase.case.LaunchApp import *


class GNAppMessageClassify2(LaunchApp):
    @case_run
    def run(self):
        self.case_module = u"消息"  # 用例所属模块
        self.case_title = u'消息设置页面，清空活动历时消息功能检查'  # 用例名称
        self.zentao_id = 1926  # 禅道ID


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

            self.widget_click(self.page["message_setting_page"]["title"],
                              self.page["message_setting_page"]["clear_device"],
                              self.page["clear_device_popup"]["title"],
                              1, 1, 1, 10, 0.5)

            self.widget_click(self.page["clear_device_popup"]["title"],
                              self.page["clear_device_popup"]["confirm"],
                              self.page["home_message_page"]["title"],
                              1, 1, 1, 10, 0.5)

            self.widget_click(self.page["home_message_page"]["title"],
                              self.page["home_message_page"]["device"],
                              self.page["home_message_page"]["title"],
                              1, 1, 1, 10, 0.5)

            state = self.wait_widget(self.page["home_message_page"]["device"], 3, 1).get_attribute("checked")
            if state is True:
                self.wait_widget(self.page["home_message_page"]["no_message"], 3, 1)
            else:
                self.widget_click(self.page["home_message_page"]["title"],
                                  self.page["home_message_page"]["device"],
                                  self.page["home_message_page"]["title"],
                                  1, 1, 1, 10, 0.5)

            self.case_over(True)
        except TimeoutException:
            self.case_over(False)

