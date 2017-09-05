# coding=utf-8
from src.testcase.case.LaunchApp_GN import *


class GNAppLogin2(LaunchAppGN):
    @case_run_gn(True)
    def run(self):
        self.case_module = u"登录"  # 用例所属模块
        self.case_title = u'登录页面—忘记密码页面跳转'  # 用例名称
        self.zentao_id = 1890  # 禅道ID

    # 用例动作
    def case(self):
        try:
            self.widget_click(self.page["login_page"]["to_find_password"],
                              self.page["find_password_page"]["title"])

            self.case_over(True)
        except TimeoutException:
            self.case_over(False)
