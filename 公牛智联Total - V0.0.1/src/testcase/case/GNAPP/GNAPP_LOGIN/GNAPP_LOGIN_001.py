# coding=utf-8
from src.testcase.common.WidgetOperation_GN import *


class GNAppLogin1(WidgetOperationGN):
    @case_run_gn(True)
    def run(self):
        self.case_module = u"登录"  # 用例所属模块
        self.case_title = u'登录页面—新用户注册页面跳转'  # 用例名称
        self.zentao_id = 1889  # 禅道ID

    def case(self):
        self.widget_click(self.page["login_page"]["to_register"],
                          self.page["register_page"]["title"])

        self.case_over(True)
