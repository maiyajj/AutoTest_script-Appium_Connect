# coding=utf-8
from src.testcase.common.WidgetOperation_AL import *


class ALAppEem1(WidgetOperationAL):
    @case_run_al(False)
    def run(self):
        self.case_module = u"FUT_EEM_电量计量(#61)"  # 用例所属模块
        self.case_title = u'电量统计2H功能及精度检查'  # 用例名称
        self.zentao_id = 559  # 禅道ID

    # 用例动作
    def case(self):
        device = conf["MAC"]["AL"][0]
        self.set_power(device, "power_off")

        self.choose_home_device(device)

        self.close_mode_timer()

        self.close_general_timer()

        self.case_over(True)
