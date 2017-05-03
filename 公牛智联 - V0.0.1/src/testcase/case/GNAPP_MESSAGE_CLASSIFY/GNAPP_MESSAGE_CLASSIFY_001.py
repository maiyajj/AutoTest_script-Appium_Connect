# coding=utf-8
import os

from src.testcase.case.LaunchApp import *
from src.utils.ScreenShot import *


class GNAppMessageClassify1(LaunchApp):
    def run(self):
        self.case_module = u"消息"  # 用例所属模块
        self.case_title = u'消息分类页面信息检查'  # 用例名称
        self.ZenTao_id = 1922  # 禅道ID
        self.basename = os.path.basename(__file__).split(".")[0]  # 获取用例的文件名称:GNAPP_MESSAGE_CLASSIFY_001

        self.launch_app(Login_page=False)  # 启动APP
        self.case()

    # 用例动作
    def case(self):
        try:
            self.widget_click(device_page["title"],
                              device_page["message_table"],
                              home_message_page["title"],
                              1, 1, 1, 10, 0.5)

            self.widget_click(home_message_page["title"],
                              home_message_page["classify"],
                              message_classify_page["title"],
                              1, 1, 1, 10, 0.5)

            self.widget_click(message_classify_page["title"],
                              message_classify_page["all_device"],
                              home_message_page["title"],
                              1, 1, 1, 10, 0.5)
            self.widget_click(home_message_page["title"],
                              home_message_page["classify"],
                              message_classify_page["title"],
                              1, 1, 1, 10, 0.5)
            result = self.wait_widget(message_classify_page["all_device"],
                                      3, 1).get_attribute("checked")
            if result != "true":
                raise TimeoutException()

            self.widget_click(message_classify_page["title"],
                              message_classify_page["experience_data"],
                              home_message_page["title"],
                              1, 1, 1, 10, 0.5)
            self.widget_click(home_message_page["title"],
                              home_message_page["classify"],
                              message_classify_page["title"],
                              1, 1, 1, 10, 0.5)
            result = self.wait_widget(message_classify_page["experience_data"],
                                      3, 1).get_attribute("checked")
            if result != "true":
                raise TimeoutException()

            self.widget_click(message_classify_page["title"],
                              message_classify_page["A2"],
                              home_message_page["title"],
                              1, 1, 1, 10, 0.5)
            self.widget_click(home_message_page["title"],
                              home_message_page["classify"],
                              message_classify_page["title"],
                              1, 1, 1, 10, 0.5)
            result = self.wait_widget(message_classify_page["A2"],
                                      3, 1).get_attribute("checked")
            if result != "true":
                raise TimeoutException()

            self.widget_click(message_classify_page["title"],
                              message_classify_page["A3"],
                              home_message_page["title"],
                              1, 1, 1, 10, 0.5)
            self.widget_click(home_message_page["title"],
                              home_message_page["classify"],
                              message_classify_page["title"],
                              1, 1, 1, 10, 0.5)
            result = self.wait_widget(message_classify_page["A3"],
                                      3, 1).get_attribute("checked")
            if result != "true":
                raise TimeoutException()

            self.widget_click(message_classify_page["title"],
                              message_classify_page["A4"],
                              home_message_page["title"],
                              1, 1, 1, 10, 0.5)
            self.widget_click(home_message_page["title"],
                              home_message_page["classify"],
                              message_classify_page["title"],
                              1, 1, 1, 10, 0.5)
            result = self.wait_widget(message_classify_page["A4"],
                                      3, 1).get_attribute("checked")
            if result != "true":
                raise TimeoutException()

            self.widget_click(message_classify_page["title"],
                              message_classify_page["A5"],
                              home_message_page["title"],
                              1, 1, 1, 10, 0.5)
            self.widget_click(home_message_page["title"],
                              home_message_page["classify"],
                              message_classify_page["title"],
                              1, 1, 1, 10, 0.5)
            result = self.wait_widget(message_classify_page["A5"],
                                      3, 1).get_attribute("checked")
            if result != "true":
                raise TimeoutException()
            self.case_over(True)
        except TimeoutException:
            self.case_over(False)

    def output(self):
        self.run()
        return self.result()
