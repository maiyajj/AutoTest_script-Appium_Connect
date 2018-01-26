# coding=utf-8
from src.testcase.GN_APP.WidgetOperation import *


class GNAPPAccountSettings6(WidgetOperation):
    @case_run(False)
    def run(self):
        self.case_module = u"账户设置"  # 用例所属模块
        self.case_title = u'点击昵称"按钮，功能检查"'  # 用例名称
        self.zentao_id = "1946"  # 禅道ID

    # 用例动作
    def case(self):
        self.widget_click(self.page["device_page"]["user_image"],
                          self.page["personal_settings_page"]["title"])

        self.widget_click(self.page["personal_settings_page"]["account_setting"],
                          self.page["account_setting_page"]["title"])

        self.widget_click(self.page["account_setting_page"]["nickname"],
                          self.page["change_nickname_page"]["title"])

        self.wait_widget(self.page["change_nickname_page"]["nickname"])

        self.wait_widget(self.page["change_nickname_page"]["commit"])

        self.widget_click(self.page["change_nickname_page"]["to_return"],
                          self.page["account_setting_page"]["title"])
