# coding=utf-8
from src.testcase.common.WidgetOperation_JD import *


class JDAppElectricityMeter1(WidgetOperationJD):
    @case_run(False)
    def run(self):
        self.case_module = u"电量计量"  # 用例所属模块
        self.case_title = u'电量统计2H功能及精度检查'  # 用例名称
        self.zentao_id = 1117  # 禅道ID

    # 用例动作
    def case(self):
        self.choose_home_device(conf["MAC"]["JD"][0])

