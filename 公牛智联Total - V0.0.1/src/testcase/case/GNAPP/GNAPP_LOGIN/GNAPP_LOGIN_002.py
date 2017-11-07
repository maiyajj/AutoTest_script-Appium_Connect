# coding=utf-8
from src.testcase.common.WidgetOperation_GN import *


class GNAppLogin2(WidgetOperationGN):
    @case_run_gn(True)
    def run(self):
        self.case_module = u"登录"  # 用例所属模块
        self.case_title = u'登录页面—忘记密码页面跳转'  # 用例名称
        self.zentao_id = 1890  # 禅道ID

    # 用例动作
    def case(self):
        self.widget_click(self.page["login_page"]["to_find_password"],
                          self.page["find_password_page"]["title"])

        self.case_over(True)
