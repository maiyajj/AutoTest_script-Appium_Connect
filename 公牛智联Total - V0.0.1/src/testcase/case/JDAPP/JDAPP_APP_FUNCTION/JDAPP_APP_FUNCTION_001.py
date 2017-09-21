# coding=utf-8
from src.testcase.case.LaunchApp_JD import *


class JDAppAppFunction1(LaunchAppJD):
    @case_run_jd(False)
    def run(self):
        self.case_module = u"APP功能测试"  # 用例所属模块
        self.case_title = u'定时记录删除是否成功"'  # 用例名称
        self.zentao_id = 1170  # 禅道ID

    # 用例动作
    def case(self):
        self.widget_click(self.page["app_home_page"]["add_device"],
                          self.page["add_device_method_page"]["title"])

        self.case_over(True)
