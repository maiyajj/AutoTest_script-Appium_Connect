# coding=utf-8
from src.testcase.common.WidgetOperation_GN import *


class GNAppThemeStyle1(WidgetOperationGN):
    @case_run(False)
    def run(self):
        self.case_module = u"主题风格"  # 用例所属模块
        self.case_title = u'返回按钮功能检查'  # 用例名称
        self.zentao_id = 1986  # 禅道ID

    # 用例动作
    def case(self):
        self.widget_click(self.page["device_page"]["user_image"],
                          self.page["personal_settings_page"]["title"])

        self.widget_click(self.page["personal_settings_page"]["theme_style"],
                          self.page["theme_style_page"]["title"])

        self.widget_click(self.page["theme_style_page"]["to_return"],
                          self.page["personal_settings_page"]["title"])

        self.case_over(True)
