# coding=utf-8
from src.testcase.GN_APP.WidgetOperation import *


class GNAPPLogin1(WidgetOperation):
    @case_run(True)
    def run(self):
        self.case_module = u"登录"  # 用例所属模块
        self.case_title = u'登录页面—新用户注册页面跳转'  # 用例名称
        self.zentao_id = "1889"  # 禅道ID

    def case(self):
        self.widget_click(self.page["login_page"]["to_register"],
                          self.page["register_page"]["title"])
