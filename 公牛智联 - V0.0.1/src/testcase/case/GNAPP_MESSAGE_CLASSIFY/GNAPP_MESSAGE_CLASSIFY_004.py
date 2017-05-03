# coding=utf-8
import os

from src.testcase.case.LaunchApp import *
from src.utils.ScreenShot import *


class GNAppMessageClassify4(LaunchApp):
    def run(self):
        self.case_module = u"消息"  # 用例所属模块
        self.case_title = u'消息设置页面信息检查'  # 用例名称
        self.ZenTao_id = 1925  # 禅道ID
        self.basename = os.path.basename(__file__).split(".")[0]  # 获取用例的文件名称:GNAPP_MESSAGE_CLASSIFY_004

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
                              home_message_page["setting"],
                              message_setting_page["title"],
                              1, 1, 1, 10, 0.5)

            self.wait_widget(message_setting_page["title"], 3, 1)

            self.wait_widget(message_setting_page["to_return"], 3, 1)

            self.wait_widget(message_setting_page["clear_activity"], 3, 1)

            self.wait_widget(message_setting_page["clear_device"], 3, 1)

            self.case_over(True)
        except TimeoutException:
            self.case_over(False)

    def output(self):
        self.run()
        return self.result()
