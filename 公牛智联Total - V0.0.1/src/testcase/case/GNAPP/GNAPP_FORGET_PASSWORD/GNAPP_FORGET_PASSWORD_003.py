# coding=utf-8
from src.testcase.common.WidgetOperation_GN import *


class GNAppForgetPassword3(WidgetOperationGN):
    @case_run(True)
    def run(self):
        self.case_module = u"忘记密码"  # 用例所属模块
        self.case_title = u'忘记密码页面-点击返回登入界面按钮，页面检查'  # 用例名称
        self.zentao_id = 1907  # 禅道ID

    # 用例动作
    def case(self):
        self.widget_click(self.page["login_page"]["to_find_password"],
                          self.page["find_password_page"]["title"])

        self.widget_click(self.page["find_password_page"]["to_return"],
                          self.page["login_page"]["title"])

        self.case_over(True)
