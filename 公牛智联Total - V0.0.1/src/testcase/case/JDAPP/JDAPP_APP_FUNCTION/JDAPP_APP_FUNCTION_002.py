# coding=utf-8
from src.testcase.case.LaunchApp_JD import *


class JDAppAppFunction2(LaunchAppJD):
    @case_run_jd(False)
    def run(self):
        self.case_module = u"APP功能测试"  # 用例所属模块
        self.case_title = u'启动鱼缸模式定时，APP中开关状态检查"'  # 用例名称
        self.zentao_id = 1307  # 禅道ID

    # 用例动作
    def case(self):
        pass

        self.case_over(True)
