# coding=utf-8
from src.testcase.common.WidgetOperation_GN import *


class GNAppMessageClassify2(WidgetOperationGN):
    @case_run(False)
    def run(self):
        self.case_module = u"消息"  # 用例所属模块
        self.case_title = u'消息设置页面，清空活动历时消息功能检查'  # 用例名称
        self.zentao_id = 1926  # 禅道ID

    # 用例动作
    def case(self):
        self.widget_click(self.page["device_page"]["message_table"],
                          self.page["home_message_page"]["title"])

        self.widget_click(self.page["home_message_page"]["setting"],
                          self.page["message_setting_page"]["title"])

        self.widget_click(self.page["message_setting_page"]["clear_device"],
                          self.page["clear_device_popup"]["title"])

        self.widget_click(self.page["clear_device_popup"]["confirm"],
                          self.page["home_message_page"]["title"])

        self.widget_click(self.page["home_message_page"]["device"],
                          self.page["home_message_page"]["title"])

        element = self.wait_widget(self.page["home_message_page"]["device"])
        state = self.ac.get_attribute(element, "checked")
        self.logger.info(u"[PAGE_INFO]内容为：[%s], 长度为：[%s]" % (state, len(state)))
        if state is True:
            self.wait_widget(self.page["home_message_page"]["no_message"])
        else:
            self.widget_click(self.page["home_message_page"]["device"],
                              self.page["home_message_page"]["title"])

        self.case_over(True)
