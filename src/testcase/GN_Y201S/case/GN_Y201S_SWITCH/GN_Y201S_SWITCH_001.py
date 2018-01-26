# coding=utf-8
from src.testcase.GN_Y201S.WidgetOperation import *


class GNY201SSwitch1(WidgetOperation):
    @case_run(False)
    def run(self):
        self.case_module = u"FUT_SWITCH_开关操作及记忆功能(#46)"  # 用例所属模块
        self.case_title = u'FUT_SWITCH_手机和插座在相同网络下能否正常控制设备'  # 用例名称
        self.zentao_id = "516"  # 禅道ID

    # 用例动作
    def case(self):
        device = conf["MAC"]["AL"][0]
        self.set_power(device, "power_off")

        self.choose_home_device(device)

        for i in xrange(2):
            self.widget_click(self.page["control_device_page"]["power_button"])
