# coding=utf-8
from src.testcase.GN_F1331.WidgetOperation import *


class GNF1331KeyMemory1(WidgetOperation):
    @case_run(False)
    def run(self):
        self.case_module = u"远程开关(#18)"  # 用例所属模块
        self.case_title = u'手机APP远程频繁操作总开关，设备状态检查'  # 用例名称
        self.zentao_id = "194"  # 禅道ID

    # 用例动作
    def case(self):
        self.choose_home_device(conf["MAC"][self.app][self.device_mac])

        self.delete_out_date_timer()

        self.set_power("main_button_off")

        self.input_serial_command("power")

        self.widget_click(self.page["control_device_page"]["main_button"],
                          self.page["control_device_page"]["main_button_on"])

        self.widget_click(self.page["control_device_page"]["main_button"],
                          self.page["control_device_page"]["main_button_off"])

        self.widget_click(self.page["control_device_page"]["main_button"],
                          self.page["control_device_page"]["main_button_on"])

        self.widget_click(self.page["control_device_page"]["main_button"],
                          self.page["control_device_page"]["main_button_off"])

        self.widget_click(self.page["control_device_page"]["main_button"],
                          self.page["control_device_page"]["main_button_on"])

        self.widget_click(self.page["control_device_page"]["main_button"],
                          self.page["control_device_page"]["main_button_off"])

        self.widget_click(self.page["control_device_page"]["main_button"],
                          self.page["control_device_page"]["main_button_on"])

        self.widget_click(self.page["control_device_page"]["main_button"],
                          self.page["control_device_page"]["main_button_off"])

        self.widget_click(self.page["control_device_page"]["main_button"],
                          self.page["control_device_page"]["main_button_on"])

        btn_state_list = self.check_button_state()  # 开关

        btn_state = btn_state_list[-1]
        result = [btn_state[1] == "111"]
        if False in result:
            raise TimeoutException("device state error, current: %s" % btn_state)

        self.input_serial_command("power")

        self.widget_click(self.page["control_device_page"]["main_button"],
                          self.page["control_device_page"]["main_button_off"])

        self.widget_click(self.page["control_device_page"]["main_button"],
                          self.page["control_device_page"]["main_button_on"])

        self.widget_click(self.page["control_device_page"]["main_button"],
                          self.page["control_device_page"]["main_button_off"])

        self.widget_click(self.page["control_device_page"]["main_button"],
                          self.page["control_device_page"]["main_button_on"])

        self.widget_click(self.page["control_device_page"]["main_button"],
                          self.page["control_device_page"]["main_button_off"])

        self.widget_click(self.page["control_device_page"]["main_button"],
                          self.page["control_device_page"]["main_button_on"])

        self.widget_click(self.page["control_device_page"]["main_button"],
                          self.page["control_device_page"]["main_button_off"])

        self.widget_click(self.page["control_device_page"]["main_button"],
                          self.page["control_device_page"]["main_button_on"])

        self.widget_click(self.page["control_device_page"]["main_button"],
                          self.page["control_device_page"]["main_button_off"])

        #####
        btn_state_list = self.check_button_state()  # 开关

        # 开关
        # ...,000
        btn_state = btn_state_list[-1]
        result = [btn_state[1] == "000"]
        if False in result:
            raise TimeoutException("device state error, current: %s" % btn_state)
