# coding=utf-8
from src.testcase.case.LaunchApp import *


class GNAppAccountSettings8(LaunchApp):
    def run(self):
        self.case_module = u"账户设置"  # 用例所属模块
        self.case_title = u'昵称修改成功，页面信息检查'  # 用例名称
        self.zentao_id = 1949  # 禅道ID
        self.basename = os.path.basename(__file__).split(".")[0]  # 获取用例的文件名称:GNAPP_ACCOUNT_SETTINGS_008
        self.driver = self.return_driver()
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
            self.widget_click(self.page["device_page"]["title"],
                              self.page["device_page"]["user_image"],
                              self.page["personal_settings_page"]["title"],
                              1, 1, 1, 10, 0.5)

            self.widget_click(self.page["personal_settings_page"]["title"],
                              self.page["personal_settings_page"]["account_setting"],
                              self.page["account_setting_page"]["title"],
                              1, 1, 1, 10, 0.5)

            self.widget_click(self.page["account_setting_page"]["title"],
                              self.page["account_setting_page"]["nickname"],
                              self.page["change_nickname_page"]["title"],
                              1, 1, 1, 10, 0.5)

            nickname = self.widget_click(self.page["change_nickname_page"]["title"],
                                         self.page["change_nickname_page"]["nickname"],
                                         self.page["change_nickname_page"]["title"],
                                         1, 1, 1, 10, 0.5)

            # 全选
            nickname.clear()
            nickname.send_keys(u"被修改的昵称")
            self.logger.info(u'[APP_INPUT] ["昵称"] input success')
            time.sleep(0.5)

            self.widget_click(self.page["change_nickname_page"]["title"],
                              self.page["change_nickname_page"]["commit"],
                              self.page["account_setting_page"]["title"],
                              1, 1, 1, 10, 0.5)

            self.widget_click(self.page["account_setting_page"]["title"],
                              self.page["account_setting_page"]["to_return"],
                              self.page["personal_settings_page"]["title"],
                              1, 1, 1, 10, 0.5)

            modified_nickname = self.wait_widget(self.page["personal_settings_page"]["nickname"], 3, 1)
            if modified_nickname != u"被修改的昵称":
                raise TimeoutException()

            self.case_over(True)
        except TimeoutException:
            self.case_over(False)

    def output(self):
        self.run()
        return self.result()
