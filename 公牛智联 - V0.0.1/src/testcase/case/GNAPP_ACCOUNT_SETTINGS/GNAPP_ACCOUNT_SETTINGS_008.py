# coding=utf-8
from src.testcase.case.LaunchApp import *
from src.utils.ScreenShot import *


class GNAppAccountSettings8(LaunchApp):
    def run(self):
        self.case_module = u"账户设置"  # 用例所属模块
        self.case_title = u'昵称修改成功，页面信息检查'  # 用例名称
        self.zentao_id = 1949  # 禅道ID
        self.basename = os.path.basename(__file__).split(".")[0]  # 获取用例的文件名称:GNAPP_ACCOUNT_SETTINGS_008
        self.logger.info('[GN_INF] <current case> [CASE_ID="%s", CASE_NAME="%s", 禅道ID="%s", CASE_MODULE="%s"]'
                         % (self.basename, self.case_title, self.zentao_id, self.case_module))  # 记录log

        try:
            self.launch_app(False)  # 启动APP
            self.case()
        except WebDriverException:
            pass  # Message: ***

    # 用例动作
    def case(self):
        try:
            self.widget_click(device_page["title"],
                              device_page["user_image"],
                              personal_settings_page["title"],
                              1, 1, 1, 10, 0.5)

            self.widget_click(personal_settings_page["title"],
                              personal_settings_page["account_setting"],
                              account_setting_page["title"],
                              1, 1, 1, 10, 0.5)

            self.widget_click(account_setting_page["title"],
                              account_setting_page["nickname"],
                              change_nickname_page["title"],
                              1, 1, 1, 10, 0.5)

            nickname = self.widget_click(change_nickname_page["title"],
                                         change_nickname_page["nickname"],
                                         change_nickname_page["title"],
                                         1, 1, 1, 10, 0.5)

            # 全选
            self.driver.press_keycode(29, 28672)
            # KEYCODE_FORWARD_DEL 删除键 112
            self.driver.press_keycode(112)
            nickname.send_keys(u"被修改的昵称")
            self.logger.info(u'[APP_INPUT] ["昵称"] input success')
            time.sleep(0.5)

            self.widget_click(change_nickname_page["title"],
                              change_nickname_page["commit"],
                              account_setting_page["title"],
                              1, 1, 1, 10, 0.5)

            self.widget_click(account_setting_page["title"],
                              account_setting_page["to_return"],
                              personal_settings_page["title"],
                              1, 1, 1, 10, 0.5)

            modified_nickname = self.wait_widget(personal_settings_page["nickname"], 3, 1)
            if modified_nickname != u"被修改的昵称":
                raise TimeoutException()

            self.case_over(True)
        except TimeoutException:
            self.case_over(False)

    def output(self):
        self.run()
        return self.result()
