# coding=utf-8
from src.testcase.common.WidgetOperation_AL import *


class ALAppSwitch1(WidgetOperationAL):
    @case_run(False)
    def run(self):
        self.case_module = u"FUT_NTIMER_普通定时(#48)"  # 用例所属模块
        self.case_title = u'FUT_NTIMER_冲突定时设置'  # 用例名称
        self.zentao_id = 517  # 禅道ID

    # 用例动作
    def case(self):
        device = conf["MAC"]["AL"][0]
        self.set_power(device, "power_off")

        self.choose_home_device(device)

        for i in xrange(2):
            self.widget_click(self.page["control_device_page"]["power_button"],
                              self.page["control_device_page"]["title"])

        self.case_over(True)
