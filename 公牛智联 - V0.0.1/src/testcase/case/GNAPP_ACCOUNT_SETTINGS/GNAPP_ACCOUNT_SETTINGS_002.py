# coding=utf-8
from src.testcase.case.LaunchApp import *


class GNAppAccountSettings2(LaunchApp):
    def run(self):
        self.case_module = u"账户设置"  # 用例所属模块
        self.case_title = u'密码修改后页面跳转确认'  # 用例名称
        self.zentao_id = 1972  # 禅道ID
        self.basename = os.path.basename(__file__).split(".")[0]  # 获取用例的文件名称:GNAPP_ACCOUNT_SETTINGS_002
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
            self.widget_click(device_page["title"],
                              device_page["user_image"],
                              personal_settings_page["title"],
                              1, 1, 1, 10, 0.5)

            self.widget_click(personal_settings_page["title"],
                              personal_settings_page["account_setting"],
                              account_setting_page["title"],
                              1, 1, 1, 10, 0.5)

            self.widget_click(account_setting_page["title"],
                              account_setting_page["change_pwd"],
                              change_pwd_page["title"],
                              1, 1, 1, 10, 0.5)

            old_pwd = self.widget_click(change_pwd_page["title"],
                                        change_pwd_page["old_pwd"],
                                        change_pwd_page["title"],
                                        1, 1, 1, 10, 0.5)
            data = str(conf["user_and_pwd"][self.user][1]).decode('hex')
            old_pwd.send_keys(data)
            self.logger.info(u'[APP_INPUT] ["旧密码"] input success')
            time.sleep(0.5)

            new_pwd = self.widget_click(change_pwd_page["title"],
                                        change_pwd_page["new_pwd"],
                                        change_pwd_page["title"],
                                        1, 1, 1, 10, 0.5)
            data = str(conf["user_and_pwd"][self.user][2]).decode('hex')
            new_pwd.send_keys(data)
            self.logger.info(u'[APP_INPUT] ["新密码"] input success')
            time.sleep(0.5)

            conform_pwd = self.widget_click(change_pwd_page["title"],
                                            change_pwd_page["conform_pwd"],
                                            change_pwd_page["title"],
                                            1, 1, 1, 10, 0.5)
            data = str(conf["user_and_pwd"][self.user][2]).decode('hex')
            conform_pwd.send_keys(data)
            self.logger.info(u'[APP_INPUT] ["确认新密码"] input success')
            time.sleep(0.5)

            conf["user_and_pwd"][self.user][1], conf["user_and_pwd"][self.user][2] = \
                str(conf["user_and_pwd"][self.user][2]), str(conf["user_and_pwd"][self.user][1])
            # conf["user_and_pwd"][self.user][1] = conf["user_and_pwd"][self.user][2]
            # conf["user_and_pwd"][self.user][2] = conf["user_and_pwd"][self.user][1]

            modified_conf(conf)

            self.widget_click(change_pwd_page["title"],
                              change_pwd_page["commit"],
                              login_page["title"],
                              1, 1, 1, 10, 0.5)

            self.case_over(True)
        except TimeoutException:
            self.case_over(False)

    def output(self):
        self.run()
        return self.result()
