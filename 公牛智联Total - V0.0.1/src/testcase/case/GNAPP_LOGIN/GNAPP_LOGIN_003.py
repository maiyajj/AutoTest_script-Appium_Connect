# coding=utf-8
from src.testcase.case.LaunchApp import *


class GNAppLogin3(LaunchApp):
    @case_run
    def run(self):
        self.case_module = u"登录"  # 用例所属模块
        self.case_title = u'登录页面—登录功能检查'  # 用例名称
        self.zentao_id = 1891  # 禅道ID


    # 用例动作
    def case(self):

        try:
            user_name = self.widget_click(self.page["login_page"]["title"],
                                          self.page["login_page"]["username"],
                                          self.page["login_page"]["title"],
                                          1, 1, 1, 10, 0.5)

            # 发送数据
            data = conf["user_and_pwd"][self.user]["user_name"]
            data = str(data).decode('hex').replace(" ", "")
            user_name.clear()
            self.ac.send_keys(user_name, data)
            self.logger.info(u'[APP_INPUT] ["用户名"] input success')
            time.sleep(0.5)

            login_pwd = self.widget_click(self.page["login_page"]["title"],
                                          self.page["login_page"]["password"],
                                          self.page["login_page"]["title"],
                                          1, 1, 1, 10, 0.5)

            data = conf["user_and_pwd"][self.user]["login_pwd"]
            data = str(data).decode('hex').replace(" ", "")
            self.show_pwd(self.wait_widget(self.page["login_page"]["check_box"]))
            login_pwd.clear()
            self.ac.send_keys(login_pwd, data)
            self.logger.info(u'[APP_INPUT] ["密码"] input success')
            time.sleep(0.5)

            self.widget_click(self.page["login_page"]["title"],
                              self.page["login_page"]["login_button"],
                              self.page["device_page"]["title"],
                              1, 1, 1, 10, 0.5)

            self.case_over(True)
        except TimeoutException:
            self.case_over(False)

