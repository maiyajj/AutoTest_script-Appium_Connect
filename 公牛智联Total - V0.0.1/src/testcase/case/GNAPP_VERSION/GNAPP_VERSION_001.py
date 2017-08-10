# coding=utf-8
from src.testcase.case.LaunchApp import *


class GNAppVersion1(LaunchApp):
    @case_run(False)
    def run(self):
        self.case_module = u"版本信息"  # 用例所属模块
        self.case_title = u'当前版本为最新版本，页面信息检查'  # 用例名称
        self.zentao_id = 1992  # 禅道ID


    # 用例动作
    def case(self):
        try:
            self.widget_click(self.page["device_page"]["title"],
                              self.page["device_page"]["user_image"],
                              self.page["personal_settings_page"]["title"],
                              1, 1, 1, 10, 0.5)

            self.widget_click(self.page["personal_settings_page"]["title"],
                              self.page["personal_settings_page"]["version_info"],
                              self.page["upgrade_page"]["title"],
                              1, 1, 1, 10, 0.5)

            element = self.wait_widget(self.page["upgrade_page"]["current_version"], 3, 1)
            current_version = self.ac.get_attribute(element, "name")[-10:]

            element = self.wait_widget(self.page["upgrade_page"]["new_version"], 3, 1)
            new_version = self.ac.get_attribute(element, "name")[-10:]

            element = self.wait_widget(self.page["upgrade_page"]["upgrade_button"], 3, 1)
            btn_state = self.ac.get_attribute(element, "enabled")

            if current_version == new_version and btn_state != "false":
                raise TimeoutException()

            self.case_over(True)
        except TimeoutException:
            self.case_over(False)

