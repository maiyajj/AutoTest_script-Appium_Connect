# coding=utf-8
from src.testcase.common.WidgetOperation_HW import *


class HWAppTest1(WidgetOperationHW):
    @case_run(False)
    def run(self):
        self.case_module = u"用例脚本调试专用"  # 用例所属模块
        self.case_title = u'用例脚本调试用例'  # 用例名称
        self.zentao_id = 999999  # 禅道ID

    # 用例动作
    def case(self):
        pass

