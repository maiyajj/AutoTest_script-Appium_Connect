# coding=utf-8
import os

from src.testcase.case.LaunchApp import *
from src.utils.ScreenShot import *


class GNAppFeedBack1(LaunchApp):
    def run(self):
        self.case_module = u"意见反馈"  # 用例所属模块
        self.case_title = u'版本信息-当前版本为最新版本，页面信息检查'  # 用例名称
        self.ZenTao_id = 1992  # 禅道ID
        self.basename = os.path.basename(__file__).split(".")[0]  # 获取用例的文件名称:GNAPP_FEED_BACK_001

        self.launch_app(Login_page=False)  # 启动APP
        self.case()

    # 用例动作
    def case(self):
        try:
            self.widget_click(device_page["title"],
                              device_page["user_image"],
                              personal_settings_page["title"],
                              1, 1, 1, 10, 0.5)

            self.widget_click(personal_settings_page["title"],
                              personal_settings_page["version_info"],
                              upgrade_page["title"],
                              1, 1, 1, 10, 0.5)

            current_version = self.wait_widget(upgrade_page["current_version"], 3, 1).get_attribute("name")[-10:]

            new_version = self.wait_widget(upgrade_page["new_version"], 3, 1).get_attribute("name")[-10:]

            btn_state = self.wait_widget(upgrade_page["upgrade_button"], 3, 1).get_attribute("enabled")

            if current_version == new_version and btn_state != "false":
                raise TimeoutException()

            self.case_over(True)
        except TimeoutException:
            self.case_over(False)

    def output(self):
        self.run()
        return self.result()
