# coding=utf-8
from src.testcase.case.LaunchApp_GN import *


class GNAppRegister9(LaunchAppGN):
    @case_run_gn(True)
    def run(self):
        self.case_module = u"注册"  # 用例所属模块
        self.case_title = u'注册页面-密码长度大于16位，注册检查'  # 用例名称
        self.zentao_id = 1866  # 禅道ID

    # 用例动作
    def case(self):
        try:
            self.widget_click(self.page["login_page"]["to_register"],
                              self.page["register_page"]["title"])

            user_name = self.widget_click(self.page["register_page"]["username"],
                                          self.page["register_page"]["title"])

            # 发送数据
            data = self.user["user_name"]
            data = str(data).decode('hex').replace(" ", "")
            user_name.clear()
            self.ac.send_keys(user_name, data, self.driver)
            self.logger.info(u'[APP_INPUT] ["用户名"] input success')
            time.sleep(0.5)

            self.show_pwd(self.wait_widget(self.page["register_page"]["check_box"]))
            check_code = self.widget_click(self.page["register_page"]["check_code"],
                                           self.page["register_page"]["title"])

            data = "1234"
            check_code.clear()
            self.ac.send_keys(check_code, data, self.driver)
            self.logger.info(u'[APP_INPUT] ["注册验证码"] input success')
            time.sleep(0.5)

            pwd = self.widget_click(self.page["register_page"]["password"],
                                    self.page["register_page"]["title"])

            data = "12345678901234567"
            pwd.clear()
            self.ac.send_keys(pwd, data, self.driver)
            self.logger.info(u'[APP_INPUT] ["密码"] input success')
            time.sleep(0.5)

            element = self.page["register_page"]["check_code"]
            pwd = self.ac.get_attribute(self.wait_widget(element), "name")
            self.logger.info(u"[PAGE_INFO]内容为：[%s], 长度为：[%s]" % (pwd, len(pwd)))
            pwd = pwd.replace(element[3]["default_text"], "")
            if len(pwd) != 0:
                raise TimeoutException()

            self.case_over(True)
        except TimeoutException:
            self.case_over(False)
