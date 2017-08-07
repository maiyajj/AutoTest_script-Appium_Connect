# coding=utf-8
from src.testcase.case.LaunchApp import *


class GNAppThemeStyle4(LaunchApp):
    def run(self):
        self.case_module = u"主题风格"  # 用例所属模块
        self.case_title = u'切换为红色后，查看风格'  # 用例名称
        self.zentao_id = 1988  # 禅道ID
        self.basename = os.path.basename(__file__).split(".")[0]  # 获取用例的文件名称:GNAPP_THEME_STYLE_004
        self.logger.info('[GN_INF] <current case> [CASE_ID="%s", CASE_NAME="%s", 禅道ID="%s", CASE_MODULE="%s"]'
                         % (self.basename, self.case_title, self.zentao_id, self.case_module))  # 记录log

        try:
            self.launch_app(False)  # 启动APP
            self.case()
        except BaseException:
            self.debug.error(traceback.format_exc())  # Message: ***
            self.case_over("unknown")

    # 用例动作
    def case(self):
        try:
            self.widget_click(self.page["device_page"]["title"],
                              self.page["device_page"]["user_image"],
                              self.page["personal_settings_page"]["title"],
                              1, 1, 1, 10, 0.5)

            self.widget_click(self.page["personal_settings_page"]["title"],
                              self.page["personal_settings_page"]["theme_style"],
                              self.page["theme_style_page"]["title"],
                              1, 1, 1, 10, 0.5)

            self.widget_click(self.page["theme_style_page"]["title"],
                              self.page["theme_style_page"]["red"],
                              self.page["theme_style_page"]["title"],
                              1, 1, 1, 10, 0.5)

            # 截取屏幕信息
            ScreenShot(self.device_info, self.zentao_id, self.basename, self.logger)

            self.case_over(True)
        except TimeoutException:
            self.case_over(False)

    def output(self):
        self.run()
        return self.result()
