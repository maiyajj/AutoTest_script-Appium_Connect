# coding=utf-8
from src.testcase.case.LaunchApp import *


class GNAppRegister6(LaunchApp):
    @case_run(True)
    def run(self):
        self.case_module = u"注册"  # 用例所属模块
        self.case_title = u'注册页面-验证码为特殊字符时，提示信息检查'  # 用例名称
        self.zentao_id = 1881  # 禅道ID


    # 用例动作
    def case(self):
        try:
            self.widget_click(self.page["login_page"]["title"],
                              self.page["login_page"]["to_register"],
                              self.page["register_page"]["title"],
                              1, 1, 1, 10, 0.5)

            self.show_pwd(self.wait_widget(self.page["register_page"]["check_box"]))
            check_code = self.widget_click(self.page["register_page"]["title"],
                                           self.page["register_page"]["check_code"],
                                           self.page["register_page"]["title"],
                                           1, 1, 1, 10, 0.5)

            data = u"△▽○◇"
            check_code.clear()
            self.ac.send_keys(check_code, data)
            self.logger.info(u'[APP_INPUT] ["注册验证码"] input success')
            time.sleep(0.5)

            element = self.wait_widget(self.page["register_page"]["check_code"], 1, 0.5)
            check_code = self.ac.get_attribute(element, "name")
            if len(check_code) != 0:
                raise TimeoutException()

            self.case_over(True)
        except TimeoutException:
            self.case_over(False)

