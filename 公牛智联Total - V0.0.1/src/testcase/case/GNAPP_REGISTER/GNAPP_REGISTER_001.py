# coding=utf-8
from src.testcase.case.LaunchApp import *


class GNAppRegister1(LaunchApp):
    @case_run
    def run(self):
        self.case_module = u"注册"  # 用例所属模块
        self.case_title = u'注册页面-已有账户登录按钮，跳转页面检查'  # 用例名称
        self.zentao_id = 1888  # 禅道ID


    # 用例动作
    def case(self):
        try:
            self.widget_click(self.page["login_page"]["title"],
                              self.page["login_page"]["to_register"],
                              self.page["register_page"]["title"],
                              1, 1, 1, 10, 0.5)

            self.widget_click(self.page["register_page"]["title"],
                              self.page["register_page"]["to_login"],
                              self.page["login_page"]["title"],
                              1, 1, 1, 10, 0.5)

            self.case_over(True)
        except TimeoutException:
            self.case_over(False)

