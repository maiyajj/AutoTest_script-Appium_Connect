# coding=utf-8
from src.testcase.case.LaunchApp import *


class GNAppAccountSettings3(LaunchApp):
    def run(self):
        self.case_module = u"账户设置"  # 用例所属模块
        self.case_title = u'退出当前账号后，取消按钮功能检查'  # 用例名称
        self.zentao_id = 1973  # 禅道ID
        self.basename = os.path.basename(__file__).split(".")[0]  # 获取用例的文件名称:GNAPP_ACCOUNT_SETTINGS_003
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
                              self.page["personal_settings_page"]["account_setting"],
                              self.page["account_setting_page"]["title"],
                              1, 1, 1, 10, 0.5)

            self.widget_click(self.page["account_setting_page"]["title"],
                              self.page["account_setting_page"]["logout"],
                              self.page["logout_popup"]["title"],
                              1, 1, 1, 10, 0.5)

            self.widget_click(self.page["logout_popup"]["title"],
                              self.page["logout_popup"]["cancel"],
                              self.page["account_setting_page"]["title"],
                              1, 1, 1, 10, 0.5)

            self.widget_click(self.page["account_setting_page"]["title"],
                              self.page["account_setting_page"]["logout"],
                              self.page["logout_popup"]["title"],
                              1, 1, 1, 10, 0.5)

            x = self.driver.get_window_size()['width']
            y = self.driver.get_window_size()['height']
            x = int(x * 0.1)
            y = int(y * 0.1)
            self.driver.tap([(x, y)])
            self.widget_click(self.page["account_setting_page"]["title"],
                              self.page["account_setting_page"]["title"],
                              self.page["account_setting_page"]["title"],
                              1, 1, 1, 10, 0.5)

            self.case_over(True)
        except TimeoutException:
            self.case_over(False)

    def output(self):
        self.run()
        return self.result()
