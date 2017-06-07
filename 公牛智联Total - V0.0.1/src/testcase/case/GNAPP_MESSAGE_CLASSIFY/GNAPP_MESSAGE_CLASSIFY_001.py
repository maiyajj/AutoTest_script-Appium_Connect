# coding=utf-8
from src.testcase.case.LaunchApp import *


class GNAppMessageClassify1(LaunchApp):
    def run(self):
        self.case_module = u"消息"  # 用例所属模块
        self.case_title = u'消息分类页面信息检查'  # 用例名称
        self.zentao_id = 1922  # 禅道ID
        self.basename = os.path.basename(__file__).split(".")[0]  # 获取用例的文件名称:GNAPP_MESSAGE_CLASSIFY_001
        self.driver = self.return_driver()
        self.logger.info('[GN_INF] <current case> [CASE_ID="%s", CASE_NAME="%s", 禅道ID="%s", CASE_MODULE="%s"]'
                         % (self.basename, self.case_title, self.zentao_id, self.case_module))  # 记录log

        try:
            self.launch_app(False)  # 启动APP
            self.case()
        except WebDriverException:
            self.debug.error(traceback.format_exc())  # Message: ***

    # 用例动作
    def case(self):
        try:
            self.widget_click(self.page["device_page"]["title"],
                              self.page["device_page"]["message_table"],
                              self.page["home_message_page"]["title"],
                              1, 1, 1, 10, 0.5)

            self.widget_click(self.page["home_message_page"]["title"],
                              self.page["home_message_page"]["classify"],
                              self.page["message_classify_page"]["title"],
                              1, 1, 1, 10, 0.5)

            self.widget_click(self.page["message_classify_page"]["title"],
                              self.page["message_classify_page"]["all_device"],
                              self.page["home_message_page"]["title"],
                              1, 1, 1, 10, 0.5)
            self.widget_click(self.page["home_message_page"]["title"],
                              self.page["home_message_page"]["classify"],
                              self.page["message_classify_page"]["title"],
                              1, 1, 1, 10, 0.5)
            result = self.wait_widget(self.page["message_classify_page"]["all_device"],
                                      3, 1).get_attribute("checked")
            if result != "true":
                raise TimeoutException()

            self.widget_click(self.page["message_classify_page"]["title"],
                              self.page["message_classify_page"]["experience_data"],
                              self.page["home_message_page"]["title"],
                              1, 1, 1, 10, 0.5)
            self.widget_click(self.page["home_message_page"]["title"],
                              self.page["home_message_page"]["classify"],
                              self.page["message_classify_page"]["title"],
                              1, 1, 1, 10, 0.5)
            result = self.wait_widget(self.page["message_classify_page"]["experience_data"],
                                      3, 1).get_attribute("checked")
            if result != "true":
                raise TimeoutException()

            self.widget_click(self.page["message_classify_page"]["title"],
                              self.page["message_classify_page"]["A2"],
                              self.page["home_message_page"]["title"],
                              1, 1, 1, 10, 0.5)
            self.widget_click(self.page["home_message_page"]["title"],
                              self.page["home_message_page"]["classify"],
                              self.page["message_classify_page"]["title"],
                              1, 1, 1, 10, 0.5)
            result = self.wait_widget(self.page["message_classify_page"]["A2"],
                                      3, 1).get_attribute("checked")
            if result != "true":
                raise TimeoutException()

            self.widget_click(self.page["message_classify_page"]["title"],
                              self.page["message_classify_page"]["A3"],
                              self.page["home_message_page"]["title"],
                              1, 1, 1, 10, 0.5)
            self.widget_click(self.page["home_message_page"]["title"],
                              self.page["home_message_page"]["classify"],
                              self.page["message_classify_page"]["title"],
                              1, 1, 1, 10, 0.5)
            result = self.wait_widget(self.page["message_classify_page"]["A3"],
                                      3, 1).get_attribute("checked")
            if result != "true":
                raise TimeoutException()

            self.widget_click(self.page["message_classify_page"]["title"],
                              self.page["message_classify_page"]["A4"],
                              self.page["home_message_page"]["title"],
                              1, 1, 1, 10, 0.5)
            self.widget_click(self.page["home_message_page"]["title"],
                              self.page["home_message_page"]["classify"],
                              self.page["message_classify_page"]["title"],
                              1, 1, 1, 10, 0.5)
            result = self.wait_widget(self.page["message_classify_page"]["A4"],
                                      3, 1).get_attribute("checked")
            if result != "true":
                raise TimeoutException()

            self.widget_click(self.page["message_classify_page"]["title"],
                              self.page["message_classify_page"]["A5"],
                              self.page["home_message_page"]["title"],
                              1, 1, 1, 10, 0.5)
            self.widget_click(self.page["home_message_page"]["title"],
                              self.page["home_message_page"]["classify"],
                              self.page["message_classify_page"]["title"],
                              1, 1, 1, 10, 0.5)
            result = self.wait_widget(self.page["message_classify_page"]["A5"],
                                      3, 1).get_attribute("checked")
            if result != "true":
                raise TimeoutException()
            self.case_over(True)
        except TimeoutException:
            self.case_over(False)

    def output(self):
        self.run()
        return self.result()
