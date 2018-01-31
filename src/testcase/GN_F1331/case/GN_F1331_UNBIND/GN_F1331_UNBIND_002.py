# coding=utf-8
from src.testcase.GN_F1331.WidgetOperation import *


class GNF1331Unbind2(WidgetOperation):
    @case_run(False)
    def run(self):
        self.case_module = u"远程开关(#18)"  # 用例所属模块
        self.case_title = u'手机APP远程总开关功能检查'  # 用例名称
        self.zentao_id = "193"  # 禅道ID

    # 用例动作
    def case(self):
        self.choose_home_device(conf["MAC"][self.app][self.device_mac])

        self.delete_out_date_timer()

        self.set_power("main_button_off")

        self.input_serial_command("power")

        ##
        self.widget_click(self.page["control_device_page"]["main_button"],
                          self.page["control_device_page"]["main_button_on"])

        self.widget_click(self.page["control_device_page"]["main_button"],
                          self.page["control_device_page"]["main_button_off"])

        ##
        self.widget_click(self.page["control_device_page"]["up_button"],
                          self.page["control_device_page"]["main_button_on"])

        self.widget_click(self.page["control_device_page"]["main_button"],
                          self.page["control_device_page"]["main_button_off"])

        #
        self.widget_click(self.page["control_device_page"]["mid_button"],
                          self.page["control_device_page"]["main_button_on"])

        self.widget_click(self.page["control_device_page"]["main_button"],
                          self.page["control_device_page"]["main_button_off"])

        #
        self.widget_click(self.page["control_device_page"]["down_button"],
                          self.page["control_device_page"]["main_button_on"])

        self.widget_click(self.page["control_device_page"]["main_button"],
                          self.page["control_device_page"]["main_button_off"])

        ##
        self.widget_click(self.page["control_device_page"]["up_button"],
                          self.page["control_device_page"]["main_button_on"])

        self.widget_click(self.page["control_device_page"]["mid_button"],
                          self.page["control_device_page"]["main_button_on"])

        self.widget_click(self.page["control_device_page"]["main_button"],
                          self.page["control_device_page"]["main_button_off"])

        #
        self.widget_click(self.page["control_device_page"]["up_button"],
                          self.page["control_device_page"]["main_button_on"])

        self.widget_click(self.page["control_device_page"]["down_button"],
                          self.page["control_device_page"]["main_button_on"])

        self.widget_click(self.page["control_device_page"]["main_button"],
                          self.page["control_device_page"]["main_button_off"])

        #
        self.widget_click(self.page["control_device_page"]["mid_button"],
                          self.page["control_device_page"]["main_button_on"])

        self.widget_click(self.page["control_device_page"]["down_button"],
                          self.page["control_device_page"]["main_button_on"])

        self.widget_click(self.page["control_device_page"]["main_button"],
                          self.page["control_device_page"]["main_button_off"])

        time.sleep(10)

        #####
        btn_list = self.check_button_state()  # 开关

        # 开关
        # 111, 000, 100, 000, 010, 000, 001, 000, 100, 110, 000, 100, 101, 000, 010, 011, 000
        btn = btn_list[0]
        btn_all = btn[1]
        result = [btn_all == "111"]
        if False in result:
            raise TimeoutException("device state error, current: %s" % btn)

        btn = btn_list[1]
        btn_all = btn[1]
        result = [btn_all == "000"]
        if False in result:
            raise TimeoutException("device state error, current: %s" % btn)

        btn = btn_list[2]
        btn_all = btn[1]
        result = [btn_all == "100"]
        if False in result:
            raise TimeoutException("device state error, current: %s" % btn)

        btn = btn_list[3]
        btn_all = btn[1]
        result = [btn_all == "000"]
        if False in result:
            raise TimeoutException("device state error, current: %s" % btn)

        btn = btn_list[4]
        btn_all = btn[1]
        result = [btn_all == "010"]
        if False in result:
            raise TimeoutException("device state error, current: %s" % btn)

        btn = btn_list[5]
        btn_all = btn[1]
        result = [btn_all == "000"]
        if False in result:
            raise TimeoutException("device state error, current: %s" % btn)

        btn = btn_list[6]
        btn_all = btn[1]
        result = [btn_all == "001"]
        if False in result:
            raise TimeoutException("device state error, current: %s" % btn)

        btn = btn_list[7]
        btn_all = btn[1]
        result = [btn_all == "000"]
        if False in result:
            raise TimeoutException("device state error, current: %s" % btn)

        btn = btn_list[9]
        btn_all = btn[1]
        result = [btn_all == "110"]
        if False in result:
            raise TimeoutException("device state error, current: %s" % btn)

        btn = btn_list[10]
        btn_all = btn[1]
        result = [btn_all == "000"]
        if False in result:
            raise TimeoutException("device state error, current: %s" % btn)

        btn = btn_list[12]
        btn_all = btn[1]
        result = [btn_all == "101"]
        if False in result:
            raise TimeoutException("device state error, current: %s" % btn)

        btn = btn_list[13]
        btn_all = btn[1]
        result = [btn_all == "000"]
        if False in result:
            raise TimeoutException("device state error, current: %s" % btn)

        btn = btn_list[15]
        btn_all = btn[1]
        result = [btn_all == "011"]
        if False in result:
            raise TimeoutException("device state error, current: %s" % btn)

        btn = btn_list[16]
        btn_all = btn[1]
        result = [btn_all == "000"]
        if False in result:
            raise TimeoutException("device state error, current: %s" % btn)
