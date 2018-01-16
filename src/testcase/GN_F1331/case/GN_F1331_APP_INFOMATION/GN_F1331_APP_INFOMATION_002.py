# coding=utf-8
from src.testcase.GN_F1331.WidgetOperation import *


class GNF1331AppFunction2(WidgetOperation):
    @case_run(False)
    def run(self):
        self.case_module = u"APP检查"  # 用例所属模块
        self.case_title = u'设备详细界面，信息检测'  # 用例名称
        self.zentao_id = 007  # 禅道ID

    # 用例动作
    def case(self):
        self.choose_home_device(conf["MAC"]["JD"][0])

        self.set_power("power_off")

        self.widget_click(self.page["control_device_page"]["mode_timer"],
                          self.page["mode_timer_page"]["title"])

        self.widget_click(self.page["mode_timer_page"]["fish_button"],
                          self.page["mode_timer_page"]["title"])

        self.widget_click(self.page["mode_timer_page"]["to_return"],
                          self.page["control_device_page"]["title"])

        self.wait_widget(self.page["control_device_page"]["power_on"])
