# coding=utf-8
from src.testcase.case.LaunchApp_GN import *


class GNAppRegister3(LaunchAppGN):
    @case_run_gn(True)
    def run(self):
        self.case_module = u"注册"  # 用例所属模块
        self.case_title = u'注册页面-正确的用户名和密码，验证码大于6位，注册验证'  # 用例名称
        self.zentao_id = 1884  # 禅道ID

    # 用例动作
    def case(self):
        self.widget_click(self.page["login_page"]["to_register"],
                          self.page["register_page"]["title"])  # 点击“新用户注册按钮”

        user_name = self.widget_click(self.page["register_page"]["username"],
                                      self.page["register_page"]["title"])  # 点击用户名输入框

        # 发送数据
        data = self.user["user_name"]
        data = str(data).decode('hex').replace(" ", "")
        user_name.clear()
        self.ac.send_keys(user_name, data, self.driver)
        self.logger.info(u'[APP_INPUT] ["用户名"] input success')
        time.sleep(0.5)

        self.show_pwd(self.wait_widget(self.page["register_page"]["check_box"]))
        pwd = self.widget_click(self.page["register_page"]["password"],
                                self.page["register_page"]["title"])  # 点击密码输入框

        data = self.user["login_pwd"]
        data = str(data).decode('hex').replace(" ", "")
        pwd.clear()
        self.ac.send_keys(pwd, data, self.driver)
        self.logger.info(u'[APP_INPUT] ["密码"] input success')
        time.sleep(0.5)

        check_code = self.widget_click(self.page["register_page"]["check_code"],
                                       self.page["register_page"]["title"])  # 点击验证码输入框

        data = "1234567"  # 传入超过6位的验证码
        check_code.clear()
        self.ac.send_keys(check_code, data, self.driver)
        self.logger.info(u'[APP_INPUT] ["注册验证码"] input success')
        time.sleep(0.5)

        element = self.page["register_page"]["check_code"]
        check_code = self.ac.get_attribute(self.wait_widget(element), "name")
        self.logger.info(u"[PAGE_INFO]内容为：[%s], 长度为：[%s]" % (check_code, len(check_code)))
        check_code = check_code.replace(element[3]["default_text"], "")
        if len(check_code) != 6:  # 检测验证码长度
            raise TimeoutException()

        self.case_over(True)
