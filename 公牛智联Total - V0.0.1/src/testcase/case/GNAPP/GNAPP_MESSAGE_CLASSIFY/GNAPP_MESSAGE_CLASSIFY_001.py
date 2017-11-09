# coding=utf-8
from src.testcase.common.WidgetOperation_GN import *


class GNAppMessageClassify1(WidgetOperationGN):
    @case_run(False)
    def run(self):
        self.case_module = u"消息"  # 用例所属模块
        self.case_title = u'消息分类页面信息检查'  # 用例名称
        self.zentao_id = 1922  # 禅道ID

    # 用例动作
    def case(self):
        self.widget_click(self.page["device_page"]["message_table"],
                          self.page["home_message_page"]["title"])

        self.widget_click(self.page["home_message_page"]["classify"],
                          self.page["message_classify_page"]["title"])

        self.widget_click(self.page["message_classify_page"]["all_device"],
                          self.page["home_message_page"]["title"])

        self.widget_click(self.page["home_message_page"]["classify"],
                          self.page["message_classify_page"]["title"])

        element = self.wait_widget(self.page["message_classify_page"]["all_device"])
        result = self.ac.get_attribute(element, "checked")
        self.logger.info(u"[PAGE_INFO]内容为：[%s], 长度为：[%s]" % (result, len(result)))
        if result != "true":
            raise TimeoutException("all device state is not true, current is %s" % result)

        self.widget_click(self.page["message_classify_page"]["experience_data"],
                          self.page["home_message_page"]["title"])

        self.widget_click(self.page["home_message_page"]["classify"],
                          self.page["message_classify_page"]["title"])

        element = self.wait_widget(self.page["message_classify_page"]["experience_data"])
        result = self.ac.get_attribute(element, "checked")
        self.logger.info(u"[PAGE_INFO]内容为：[%s], 长度为：[%s]" % (result, len(result)))
        if result != "true":
            raise TimeoutException("experience data state is not true, current is %s" % result)

        self.widget_click(self.page["message_classify_page"]["A2"],
                          self.page["home_message_page"]["title"])

        self.widget_click(self.page["home_message_page"]["classify"],
                          self.page["message_classify_page"]["title"])

        element = self.wait_widget(self.page["message_classify_page"]["A2"])
        result = self.ac.get_attribute(element, "checked")
        self.logger.info(u"[PAGE_INFO]内容为：[%s], 长度为：[%s]" % (result, len(result)))
        if result != "true":
            raise TimeoutException("A2 state is not true, current is %s" % result)

        self.widget_click(self.page["message_classify_page"]["A3"],
                          self.page["home_message_page"]["title"])

        self.widget_click(self.page["home_message_page"]["classify"],
                          self.page["message_classify_page"]["title"])

        element = self.wait_widget(self.page["message_classify_page"]["A3"])
        result = self.ac.get_attribute(element, "checked")
        self.logger.info(u"[PAGE_INFO]内容为：[%s], 长度为：[%s]" % (result, len(result)))
        if result != "true":
            raise TimeoutException("A3 state is not true, current is %s" % result)

        self.widget_click(self.page["message_classify_page"]["A4"],
                          self.page["home_message_page"]["title"])

        self.widget_click(self.page["home_message_page"]["classify"],
                          self.page["message_classify_page"]["title"])

        element = self.wait_widget(self.page["message_classify_page"]["A4"])
        result = self.ac.get_attribute(element, "checked")
        self.logger.info(u"[PAGE_INFO]内容为：[%s], 长度为：[%s]" % (result, len(result)))
        if result != "true":
            raise TimeoutException("A4 state is not true, current is %s" % result)

        self.widget_click(self.page["message_classify_page"]["A5"],
                          self.page["home_message_page"]["title"])

        self.widget_click(self.page["home_message_page"]["classify"],
                          self.page["message_classify_page"]["title"])

        element = self.wait_widget(self.page["message_classify_page"]["A5"])
        result = self.ac.get_attribute(element, "checked")
        self.logger.info(u"[PAGE_INFO]内容为：[%s], 长度为：[%s]" % (result, len(result)))
        if result != "true":
            raise TimeoutException("A5 state is not true, current is %s" % result)

        self.case_over(True)
