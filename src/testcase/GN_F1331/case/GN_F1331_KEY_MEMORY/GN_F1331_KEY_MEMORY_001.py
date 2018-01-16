# coding=utf-8
from src.testcase.GN_F1331.WidgetOperation import *


class GNF1331KeyMemory1(WidgetOperation):
    @case_run(False)
    def run(self):
        self.case_module = u"开关操作"  # 用例所属模块
        self.case_title = u'开关操作及记忆功能'  # 用例名称
        self.zentao_id = 1216  # 禅道ID

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

        self.widget_click(self.page["control_device_page"]["up_button"],
                          self.page["control_device_page"]["up_button_on"])

        self.widget_click(self.page["control_device_page"]["mid_button"],
                          self.page["control_device_page"]["mid_button_on"])

        self.widget_click(self.page["control_device_page"]["down_button"],
                          self.page["control_device_page"]["down_button_on"])

        self.widget_click(self.page["control_device_page"]["up_button"],
                          self.page["control_device_page"]["up_button_off"])

        self.widget_click(self.page["control_device_page"]["mid_button"],
                          self.page["control_device_page"]["mid_button_off"])

        self.widget_click(self.page["control_device_page"]["down_button"],
                          self.page["control_device_page"]["down_button_off"])

        btn_state_list = self.check_serial_button_state()

        btn_state = btn_state_list[0]
        result = [btn_state[1] == "111"]
        if False in result:
            raise TimeoutException("device state error, current: %s, result: %s" % (btn_state, result))

        btn_state = btn_state_list[1]
        result = [btn_state[1] == "000"]
        if False in result:
            raise TimeoutException("device state error, current: %s, result: %s" % (btn_state, result))

        btn_state = btn_state_list[2]
        result = [btn_state[1] == "100"]
        if False in result:
            raise TimeoutException("device state error, current: %s, result: %s" % (btn_state, result))

        btn_state = btn_state_list[3]
        result = [btn_state[1] == "110"]
        if False in result:
            raise TimeoutException("device state error, current: %s, result: %s" % (btn_state, result))

        btn_state = btn_state_list[4]
        result = [btn_state[1] == "111"]
        if False in result:
            raise TimeoutException("device state error, current: %s, result: %s" % (btn_state, result))

        btn_state = btn_state_list[5]
        result = [btn_state[1] == "011"]
        if False in result:
            raise TimeoutException("device state error, current: %s, result: %s" % (btn_state, result))

        btn_state = btn_state_list[6]
        result = [btn_state[1] == "001"]
        if False in result:
            raise TimeoutException("device state error, current: %s, result: %s" % (btn_state, result))

        btn_state = btn_state_list[7]
        result = [btn_state[1] == "000"]
        if False in result:
            raise TimeoutException("device state error, current: %s, result: %s" % (btn_state, result))
