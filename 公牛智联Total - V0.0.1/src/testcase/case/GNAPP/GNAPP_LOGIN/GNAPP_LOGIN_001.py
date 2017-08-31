# coding=utf-8
from src.testcase.case.LaunchApp_GN import *


class GNAppLogin1(LaunchAppGN):
    @case_run_gn(True)
    def run(self):
        self.case_module = u"登录"  # 用例所属模块
        self.case_title = u'登录页面—新用户注册页面跳转'  # 用例名称
        self.zentao_id = 1889  # 禅道ID

    def case(self):
        try:
            self.widget_click(self.page["login_page"]["title"],
                              self.page["login_page"]["to_register"],
                              self.page["register_page"]["title"])

            self.case_over(True)
        except TimeoutException:
            self.case_over(False)
