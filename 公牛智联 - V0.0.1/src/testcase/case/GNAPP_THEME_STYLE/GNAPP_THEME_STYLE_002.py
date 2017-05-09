# coding=utf-8
from src.testcase.case.LaunchApp import *
from src.utils.ScreenShot import *


class GNAppThemeStyle2(LaunchApp):
    def run(self):
        self.case_module = u"主题风格"  # 用例所属模块
        self.case_title = u'切换为紫色后，查看风格'  # 用例名称
        self.zentao_id = 1990  # 禅道ID
        self.basename = os.path.basename(__file__).split(".")[0]  # 获取用例的文件名称:GNAPP_THEME_STYLE_002
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
            self.widget_click(device_page["title"],
                              device_page["user_image"],
                              personal_settings_page["title"],
                              1, 1, 1, 10, 0.5)

            self.widget_click(personal_settings_page["title"],
                              personal_settings_page["theme_style"],
                              theme_style_page["title"],
                              1, 1, 1, 10, 0.5)

            self.widget_click(theme_style_page["title"],
                              theme_style_page["cyan"],
                              theme_style_page["title"],
                              1, 1, 1, 10, 0.5)

            # 截取屏幕信息
            ScreenShot(self.device_info, self.zentao_id, self.basename, self.logger)

            self.case_over(True)
        except TimeoutException:
            self.case_over(False)

    def output(self):
        self.run()
        return self.result()
