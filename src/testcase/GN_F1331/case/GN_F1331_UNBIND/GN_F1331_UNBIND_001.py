# coding=utf-8
from src.testcase.GN_F1331.WidgetOperation import *


class GNF1331Unbind1(WidgetOperation):
    @case_run(False)
    def run(self):
        self.case_module = u"解绑功能(#13)"  # 用例所属模块
        self.case_title = u'带负载APP端解绑功能检查'  # 用例名称
        self.zentao_id = "167"  # 禅道ID

    # 用例动作
    def case(self):
        self.choose_home_device(conf["MAC"][self.app][self.device_mac])

        self.set_power("main_button_on")

        self.input_serial_command("power")

        self.widget_click(self.page["control_device_page"]["device_setting"],
                          self.page["device_setting_page"]["title"])

        self.widget_click(self.page["device_setting_page"]["unbind"],
                          self.page["unbind_device_popup"]["title"])

        self.widget_click(self.page["unbind_device_popup"]["confirm"],
                          self.page["control_device_page"]["title"])

        v = self.get_index(conf["MAC"][self.app][self.device_mac], self.page["app_home_page"]["device"])
        if not v:
            raise TimeoutException()

        btn_list = self.check_button_state(wait=True)
        time_1 = time.time()

        btn = self.get_last_device_state(btn_list, time_1)
        btn_all = btn[1]
        result = [btn_all == "111"]
        if False in result:
            raise TimeoutException("device state error, current: %s, result: %s" % (btn, result))
