# coding=utf-8
from src.testcase.common.WidgetOperation_GN import *


class GNAppMessageClassify5(WidgetOperationGN):
    @case_run_gn(False)
    def run(self):
        self.case_module = u"消息"  # 用例所属模块
        self.case_title = u'消息分类页面，选择多个设备后的消息内容检查'  # 用例名称
        self.zentao_id = 1924  # 禅道ID

    # 用例动作
    def case(self):
        self.widget_click(self.page["device_page"]["message_table"],
                          self.page["home_message_page"]["title"])

        self.widget_click(self.page["home_message_page"]["setting"],
                          self.page["message_setting_page"]["title"])

        self.wait_widget(self.page["message_setting_page"]["title"])

        self.wait_widget(self.page["message_setting_page"]["to_return"])

        self.wait_widget(self.page["message_setting_page"]["clear_activity"])

        self.wait_widget(self.page["message_setting_page"]["clear_device"])

        self.case_over(True)
