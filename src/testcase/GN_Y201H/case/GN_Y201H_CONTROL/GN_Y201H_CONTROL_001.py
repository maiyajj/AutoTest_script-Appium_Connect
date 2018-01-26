# coding=utf-8
from src.testcase.GN_Y201H.WidgetOperation import *


class GNY201HControl1(WidgetOperation):
    @case_run(False)
    def run(self):
        self.case_module = u"远程控制(#250)"  # 用例所属模块
        self.case_title = u'在线状态，频繁开关操作后，状态检查'  # 用例名称
        self.zentao_id = "2106"  # 禅道ID

    # 用例动作
    def case(self):
        self.choose_home_device(conf["MAC"]["HW"][0])

        self.delete_normal_timer()

        self.delete_delay_timer()

        self.set_power("power_on")

        i = 10
        while i > 0:
            self.widget_click(self.page["control_device_page"]["power_button"])
            i -= 1
        state = self.ac.get_attribute(self.wait_widget(self.page["control_device_page"]["power_state"]), "name")
        if state != u"电源已开启":
            raise TimeoutException("power state is error,current: %s" % [state])

        i = 9
        while i > 0:
            self.widget_click(self.page["control_device_page"]["power_button"])
            i -= 1
        state = self.ac.get_attribute(self.wait_widget(self.page["control_device_page"]["power_state"]), "name")
        if state != u"电源已关闭":
            raise TimeoutException("power state is error,current: %s" % [state])
