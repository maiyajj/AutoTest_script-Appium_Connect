# coding=utf-8
from src.testcase.case.LaunchApp_JD import *


class JDAppElectricityMeter1(LaunchAppJD):
    @case_run_jd(False)
    def run(self):
        self.case_module = u"APP功能测试"  # 用例所属模块
        self.case_title = u'定时记录删除是否成功"'  # 用例名称
        self.zentao_id = 1170  # 禅道ID

    # 用例动作
    def case(self):
        pass

        self.case_over(True)
