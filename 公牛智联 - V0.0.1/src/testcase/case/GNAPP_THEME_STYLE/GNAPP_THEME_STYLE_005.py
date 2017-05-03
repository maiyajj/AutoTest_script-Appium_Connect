# coding=utf-8
import os

from src.testcase.case.LaunchApp import *
from src.utils.ScreenShot import *


class GNAppThemeStyle5(LaunchApp):
    def run(self):
        self.case_module = u"主题风格"  # 用例所属模块
        self.case_title = u'切换为绿色后，查看风格'  # 用例名称
        self.ZenTao_id = 1987  # 禅道ID
        self.basename = os.path.basename(__file__).split(".")[0]  # 获取用例的文件名称:GNAPP_THEME_STYLE_005

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
                              personal_settings_page["theme_style"],
                              theme_style_page["title"],
                              1, 1, 1, 10, 0.5)

            self.widget_click(theme_style_page["title"],
                              theme_style_page["green"],
                              theme_style_page["title"],
                              1, 1, 1, 10, 0.5)

            # 截取屏幕信息
            ScreenShot(self.device_info, self.ZenTao_id, self.basename, self.logger)

            self.case_over(True)
        except TimeoutException:
            self.case_over(False)

    def output(self):
        self.run()
        return self.result()
