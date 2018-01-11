# coding=utf-8
from src.testcase.GN_APP.WidgetOperation import *


class GNAPPThemeStyle5(WidgetOperation):
    @case_run(False)
    def run(self):
        self.case_module = u"主题风格"  # 用例所属模块
        self.case_title = u'切换为绿色后，查看风格'  # 用例名称
        self.zentao_id = 1987  # 禅道ID

    # 用例动作
    def case(self):
        self.widget_click(self.page["device_page"]["user_image"],
                          self.page["personal_settings_page"]["title"])

        self.widget_click(self.page["personal_settings_page"]["theme_style"],
                          self.page["theme_style_page"]["title"])

        self.widget_click(self.page["theme_style_page"]["green"],
                          self.page["theme_style_page"]["title"])

        # 截取屏幕信息
        ScreenShot(self.device_info, self.zentao_id, self.basename, self.debug)
