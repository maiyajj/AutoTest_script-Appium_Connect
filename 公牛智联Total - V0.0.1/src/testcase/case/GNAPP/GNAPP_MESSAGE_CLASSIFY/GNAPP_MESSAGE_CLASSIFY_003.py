# coding=utf-8
from src.testcase.case.LaunchApp_GN import *


class GNAppMessageClassify3(LaunchAppGN):
    @case_run_gn(False)
    def run(self):
        self.case_module = u"消息"  # 用例所属模块
        self.case_title = u'消息设置页面，清空设备历时消息功能检查'  # 用例名称
        self.zentao_id = 1927  # 禅道ID

    # 用例动作
    def case(self):
        try:
            self.widget_click(self.page["device_page"]["message_table"],
                              self.page["home_message_page"]["title"])

            self.widget_click(self.page["home_message_page"]["setting"],
                              self.page["message_setting_page"]["title"])

            self.widget_click(self.page["message_setting_page"]["clear_activity"],
                              self.page["clear_activity_popup"]["title"])

            self.widget_click(self.page["clear_activity_popup"]["confirm"],
                              self.page["home_message_page"]["title"])

            self.widget_click(self.page["home_message_page"]["message_activity"],
                              self.page["home_message_page"]["title"])

            element = self.wait_widget(self.page["home_message_page"]["message_activity"])
            state = self.ac.get_attribute(element, "checked")
            self.logger.info(u"[PAGE_INFO]内容为：[%s], 长度为：[%s]" % (state, len(state)))
            if state is True:
                self.wait_widget(self.page["home_message_page"]["no_message"])
            else:
                self.widget_click(self.page["home_message_page"]["message_activity"],
                                  self.page["home_message_page"]["title"])

            self.case_over(True)
        except TimeoutException:
            self.case_over(False)
