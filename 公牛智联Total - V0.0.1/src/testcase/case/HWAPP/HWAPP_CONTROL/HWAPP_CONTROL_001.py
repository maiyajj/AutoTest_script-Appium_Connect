# coding=utf-8
from src.testcase.common.WidgetOperation_HW import *


class HWAppControl1(WidgetOperationHW):
    @case_run_hw(False)
    def run(self):
        self.case_module = u"远程控制(#250)"  # 用例所属模块
        self.case_title = u'在线状态，频繁开关操作后，状态检查'  # 用例名称
        self.zentao_id = 2106  # 禅道ID

    # 用例动作
    def case(self):
        self.choose_home_device(conf["MAC"]["HW"][0])

        self.set_power("power_on")

        self.delete_normal_timer()

        self.delete_delay_timer()

        i = 10
        while i > 0:
            self.widget_click(self.page["control_device_page"]["power_button"],
                              self.page["control_device_page"]["title"])
            i -= 1
        state = self.ac.get_attribute(self.wait_widget(self.page["control_device_page"]["power_state"]), "name")
        if state != u"设备已开启":
            raise TimeoutException("power state is error,current: %s" % [state])

        i = 9
        while i > 0:
            self.widget_click(self.page["control_device_page"]["power_button"],
                              self.page["control_device_page"]["title"])
            i -= 1
        state = self.ac.get_attribute(self.wait_widget(self.page["control_device_page"]["power_state"]), "name")
        if state != u"设备已关闭":
            raise TimeoutException("power state is error,current: %s" % [state])

        self.case_over(True)
