# coding=utf-8
from src.testcase.case.LaunchApp import *


class GNAppAccountSettings2(LaunchApp):
    @case_run(False)
    def run(self):
        self.case_module = u"账户设置"  # 用例所属模块
        self.case_title = u'密码修改后页面跳转确认'  # 用例名称
        self.zentao_id = 1972  # 禅道ID


    # 用例动作
    def case(self):
        try:
            self.widget_click(self.page["device_page"]["title"],
                              self.page["device_page"]["user_image"],
                              self.page["personal_settings_page"]["title"])

            self.widget_click(self.page["personal_settings_page"]["title"],
                              self.page["personal_settings_page"]["account_setting"],
                              self.page["account_setting_page"]["title"])

            self.widget_click(self.page["account_setting_page"]["title"],
                              self.page["account_setting_page"]["change_pwd"],
                              self.page["change_pwd_page"]["title"])

            old_pwd = self.widget_click(self.page["change_pwd_page"]["title"],
                                        self.page["change_pwd_page"]["old_pwd"],
                                        self.page["change_pwd_page"]["title"])

            data = conf["user_and_pwd"][self.user]["login_pwd"]
            data = str(data).decode('hex').replace(" ", "")
            old_pwd.clear()
            self.ac.send_keys(old_pwd, data, self.driver)
            self.logger.info(u'[APP_INPUT] ["旧密码"] input success')
            time.sleep(0.5)

            new_pwd = self.widget_click(self.page["change_pwd_page"]["title"],
                                        self.page["change_pwd_page"]["new_pwd"],
                                        self.page["change_pwd_page"]["title"])

            data = conf["user_and_pwd"][self.user]["new_pwd"]
            data = str(data).decode('hex').replace(" ", "")
            new_pwd.clear()
            self.ac.send_keys(new_pwd, data, self.driver)
            self.logger.info(u'[APP_INPUT] ["新密码"] input success')
            time.sleep(0.5)

            conform_pwd = self.widget_click(self.page["change_pwd_page"]["title"],
                                            self.page["change_pwd_page"]["conform_pwd"],
                                            self.page["change_pwd_page"]["title"])

            data = conf["user_and_pwd"][self.user]["new_pwd"]
            data = str(data).decode('hex').replace(" ", "")
            conform_pwd.clear()
            self.ac.send_keys(conform_pwd, data, self.driver)
            self.logger.info(u'[APP_INPUT] ["确认新密码"] input success')
            time.sleep(0.5)

            old_pwd = conf["user_and_pwd"][self.user]["login_pwd"]
            new_pwd = conf["user_and_pwd"][self.user]["new_pwd"]
            conf["user_and_pwd"][self.user]["login_pwd"], conf["user_and_pwd"][self.user]["new_pwd"] = new_pwd, old_pwd
            modified_conf(conf)

            self.widget_click(self.page["change_pwd_page"]["title"],
                              self.page["change_pwd_page"]["commit"],
                              self.page["login_page"]["title"])

            self.case_over(True)
        except TimeoutException:
            self.case_over(False)

