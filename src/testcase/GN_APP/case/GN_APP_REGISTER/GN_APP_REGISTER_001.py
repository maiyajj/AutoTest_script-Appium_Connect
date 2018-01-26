# coding=utf-8
from src.testcase.GN_APP.WidgetOperation import *


class GNAPPRegister1(WidgetOperation):
    @case_run(True)
    def run(self):
        self.case_module = u"注册"  # 用例所属模块
        self.case_title = u'注册页面-已有账户登录按钮，跳转页面检查'  # 用例名称
        self.zentao_id = "1888"  # 禅道ID

    # 用例动作
    def case(self):
        self.widget_click(self.page["login_page"]["to_register"],
                          self.page["register_page"]["title"])

        self.widget_click(self.page["register_page"]["to_login"],
                          self.page["login_page"]["title"])
