# coding=utf-8
from src.testcase.GN_F1331.WidgetOperation import *


class GNF1331KeyMemory3(WidgetOperation):
    @case_run(False)
    def run(self):
        self.case_module = u"远程开关(#18)"  # 用例所属模块
        self.case_title = u'手机APP远程频繁操作分层开关，设备状态检查'  # 用例名称
        self.zentao_id = "192"  # 禅道ID

    # 用例动作
    def case(self):
        self.choose_home_device(conf["MAC"][self.app][self.device_mac])

        self.delete_out_date_timer()

        self.set_power("main_button_off")

        self.input_serial_command("power")

        ##
        self.widget_click(self.page["control_device_page"]["up_button"],
                          self.page["control_device_page"]["main_button_on"])

        self.widget_click(self.page["control_device_page"]["up_button"],
                          self.page["control_device_page"]["main_button_off"])

        self.widget_click(self.page["control_device_page"]["up_button"],
                          self.page["control_device_page"]["main_button_on"])

        self.widget_click(self.page["control_device_page"]["up_button"],
                          self.page["control_device_page"]["main_button_off"])

        self.widget_click(self.page["control_device_page"]["up_button"],
                          self.page["control_device_page"]["main_button_on"])

        self.widget_click(self.page["control_device_page"]["up_button"],
                          self.page["control_device_page"]["main_button_off"])

        self.widget_click(self.page["control_device_page"]["up_button"],
                          self.page["control_device_page"]["main_button_on"])

        self.widget_click(self.page["control_device_page"]["up_button"],
                          self.page["control_device_page"]["main_button_off"])

        self.widget_click(self.page["control_device_page"]["up_button"],
                          self.page["control_device_page"]["main_button_on"])

        #
        self.widget_click(self.page["control_device_page"]["up_button"],
                          self.page["control_device_page"]["main_button_off"])

        self.widget_click(self.page["control_device_page"]["up_button"],
                          self.page["control_device_page"]["main_button_on"])

        self.widget_click(self.page["control_device_page"]["up_button"],
                          self.page["control_device_page"]["main_button_off"])

        self.widget_click(self.page["control_device_page"]["up_button"],
                          self.page["control_device_page"]["main_button_on"])

        self.widget_click(self.page["control_device_page"]["up_button"],
                          self.page["control_device_page"]["main_button_off"])

        self.widget_click(self.page["control_device_page"]["up_button"],
                          self.page["control_device_page"]["main_button_on"])

        self.widget_click(self.page["control_device_page"]["up_button"],
                          self.page["control_device_page"]["main_button_off"])

        self.widget_click(self.page["control_device_page"]["up_button"],
                          self.page["control_device_page"]["main_button_on"])

        self.widget_click(self.page["control_device_page"]["up_button"],
                          self.page["control_device_page"]["main_button_off"])

        ##
        self.widget_click(self.page["control_device_page"]["mid_button"],
                          self.page["control_device_page"]["main_button_on"])

        self.widget_click(self.page["control_device_page"]["mid_button"],
                          self.page["control_device_page"]["main_button_off"])

        self.widget_click(self.page["control_device_page"]["mid_button"],
                          self.page["control_device_page"]["main_button_on"])

        self.widget_click(self.page["control_device_page"]["mid_button"],
                          self.page["control_device_page"]["main_button_off"])

        self.widget_click(self.page["control_device_page"]["mid_button"],
                          self.page["control_device_page"]["main_button_on"])

        self.widget_click(self.page["control_device_page"]["mid_button"],
                          self.page["control_device_page"]["main_button_off"])

        self.widget_click(self.page["control_device_page"]["mid_button"],
                          self.page["control_device_page"]["main_button_on"])

        self.widget_click(self.page["control_device_page"]["mid_button"],
                          self.page["control_device_page"]["main_button_off"])

        self.widget_click(self.page["control_device_page"]["mid_button"],
                          self.page["control_device_page"]["main_button_on"])

        #
        self.widget_click(self.page["control_device_page"]["mid_button"],
                          self.page["control_device_page"]["main_button_off"])

        self.widget_click(self.page["control_device_page"]["mid_button"],
                          self.page["control_device_page"]["main_button_on"])

        self.widget_click(self.page["control_device_page"]["mid_button"],
                          self.page["control_device_page"]["main_button_off"])

        self.widget_click(self.page["control_device_page"]["mid_button"],
                          self.page["control_device_page"]["main_button_on"])

        self.widget_click(self.page["control_device_page"]["mid_button"],
                          self.page["control_device_page"]["main_button_off"])

        self.widget_click(self.page["control_device_page"]["mid_button"],
                          self.page["control_device_page"]["main_button_on"])

        self.widget_click(self.page["control_device_page"]["mid_button"],
                          self.page["control_device_page"]["main_button_off"])

        self.widget_click(self.page["control_device_page"]["mid_button"],
                          self.page["control_device_page"]["main_button_on"])

        self.widget_click(self.page["control_device_page"]["mid_button"],
                          self.page["control_device_page"]["main_button_off"])

        ##
        self.widget_click(self.page["control_device_page"]["down_button"],
                          self.page["control_device_page"]["main_button_on"])

        self.widget_click(self.page["control_device_page"]["down_button"],
                          self.page["control_device_page"]["main_button_off"])

        self.widget_click(self.page["control_device_page"]["down_button"],
                          self.page["control_device_page"]["main_button_on"])

        self.widget_click(self.page["control_device_page"]["down_button"],
                          self.page["control_device_page"]["main_button_off"])

        self.widget_click(self.page["control_device_page"]["down_button"],
                          self.page["control_device_page"]["main_button_on"])

        self.widget_click(self.page["control_device_page"]["down_button"],
                          self.page["control_device_page"]["main_button_off"])

        self.widget_click(self.page["control_device_page"]["down_button"],
                          self.page["control_device_page"]["main_button_on"])

        self.widget_click(self.page["control_device_page"]["down_button"],
                          self.page["control_device_page"]["main_button_off"])

        self.widget_click(self.page["control_device_page"]["down_button"],
                          self.page["control_device_page"]["main_button_on"])

        #
        self.widget_click(self.page["control_device_page"]["down_button"],
                          self.page["control_device_page"]["main_button_off"])

        self.widget_click(self.page["control_device_page"]["down_button"],
                          self.page["control_device_page"]["main_button_on"])

        self.widget_click(self.page["control_device_page"]["down_button"],
                          self.page["control_device_page"]["main_button_off"])

        self.widget_click(self.page["control_device_page"]["down_button"],
                          self.page["control_device_page"]["main_button_on"])

        self.widget_click(self.page["control_device_page"]["down_button"],
                          self.page["control_device_page"]["main_button_off"])

        self.widget_click(self.page["control_device_page"]["down_button"],
                          self.page["control_device_page"]["main_button_on"])

        self.widget_click(self.page["control_device_page"]["down_button"],
                          self.page["control_device_page"]["main_button_off"])

        self.widget_click(self.page["control_device_page"]["down_button"],
                          self.page["control_device_page"]["main_button_on"])

        self.widget_click(self.page["control_device_page"]["down_button"],
                          self.page["control_device_page"]["main_button_off"])

        #####
        btn_state_list = self.check_button_state()  # 开关

        # 开关
        # 100, 000, 100, 000, 100, 000, 100, 000, 100, 000, 100, 000, 100, 000, 100, 000, 100, 000, 010, 000, 010, 000,
        # 010, 000, 010, 000, 010, 000, 010, 000, 010, 000, 010, 000, 010, 000, 001, 000, 001, 000, 001, 000, 001, 000,
        # c001, 000, 001, 000, 001, 000, 001, 000, 001, 000
        btn_state = btn_state_list[0]
        result = [btn_state[1] == "100"]
        if False in result:
            raise TimeoutException("device state error, current: %s" % btn_state)

        btn_state = btn_state_list[1]
        result = [btn_state[1] == "000"]
        if False in result:
            raise TimeoutException("device state error, current: %s" % btn_state)

        btn_state = btn_state_list[2]
        result = [btn_state[1] == "100"]
        if False in result:
            raise TimeoutException("device state error, current: %s" % btn_state)

        btn_state = btn_state_list[3]
        result = [btn_state[1] == "000"]
        if False in result:
            raise TimeoutException("device state error, current: %s" % btn_state)

        btn_state = btn_state_list[4]
        result = [btn_state[1] == "100"]
        if False in result:
            raise TimeoutException("device state error, current: %s" % btn_state)

        btn_state = btn_state_list[5]
        result = [btn_state[1] == "000"]
        if False in result:
            raise TimeoutException("device state error, current: %s" % btn_state)

        btn_state = btn_state_list[6]
        result = [btn_state[1] == "100"]
        if False in result:
            raise TimeoutException("device state error, current: %s" % btn_state)

        btn_state = btn_state_list[7]
        result = [btn_state[1] == "000"]
        if False in result:
            raise TimeoutException("device state error, current: %s" % btn_state)

        btn_state = btn_state_list[8]
        result = [btn_state[1] == "100"]
        if False in result:
            raise TimeoutException("device state error, current: %s" % btn_state)

        btn_state = btn_state_list[9]
        result = [btn_state[1] == "000"]
        if False in result:
            raise TimeoutException("device state error, current: %s" % btn_state)

        btn_state = btn_state_list[10]
        result = [btn_state[1] == "100"]
        if False in result:
            raise TimeoutException("device state error, current: %s" % btn_state)

        btn_state = btn_state_list[11]
        result = [btn_state[1] == "000"]
        if False in result:
            raise TimeoutException("device state error, current: %s" % btn_state)

        btn_state = btn_state_list[12]
        result = [btn_state[1] == "100"]
        if False in result:
            raise TimeoutException("device state error, current: %s" % btn_state)

        btn_state = btn_state_list[13]
        result = [btn_state[1] == "000"]
        if False in result:
            raise TimeoutException("device state error, current: %s" % btn_state)

        btn_state = btn_state_list[14]
        result = [btn_state[1] == "100"]
        if False in result:
            raise TimeoutException("device state error, current: %s" % btn_state)

        btn_state = btn_state_list[15]
        result = [btn_state[1] == "000"]
        if False in result:
            raise TimeoutException("device state error, current: %s" % btn_state)

        btn_state = btn_state_list[16]
        result = [btn_state[1] == "100"]
        if False in result:
            raise TimeoutException("device state error, current: %s" % btn_state)

        btn_state = btn_state_list[17]
        result = [btn_state[1] == "000"]
        if False in result:
            raise TimeoutException("device state error, current: %s" % btn_state)

        btn_state = btn_state_list[18]
        result = [btn_state[1] == "010"]
        if False in result:
            raise TimeoutException("device state error, current: %s" % btn_state)

        btn_state = btn_state_list[19]
        result = [btn_state[1] == "000"]
        if False in result:
            raise TimeoutException("device state error, current: %s" % btn_state)

        btn_state = btn_state_list[20]
        result = [btn_state[1] == "010"]
        if False in result:
            raise TimeoutException("device state error, current: %s" % btn_state)

        btn_state = btn_state_list[21]
        result = [btn_state[1] == "000"]
        if False in result:
            raise TimeoutException("device state error, current: %s" % btn_state)

        btn_state = btn_state_list[22]
        result = [btn_state[1] == "010"]
        if False in result:
            raise TimeoutException("device state error, current: %s" % btn_state)

        btn_state = btn_state_list[23]
        result = [btn_state[1] == "000"]
        if False in result:
            raise TimeoutException("device state error, current: %s" % btn_state)

        btn_state = btn_state_list[24]
        result = [btn_state[1] == "010"]
        if False in result:
            raise TimeoutException("device state error, current: %s" % btn_state)

        btn_state = btn_state_list[25]
        result = [btn_state[1] == "000"]
        if False in result:
            raise TimeoutException("device state error, current: %s" % btn_state)

        btn_state = btn_state_list[26]
        result = [btn_state[1] == "010"]
        if False in result:
            raise TimeoutException("device state error, current: %s" % btn_state)

        btn_state = btn_state_list[27]
        result = [btn_state[1] == "000"]
        if False in result:
            raise TimeoutException("device state error, current: %s" % btn_state)

        btn_state = btn_state_list[28]
        result = [btn_state[1] == "010"]
        if False in result:
            raise TimeoutException("device state error, current: %s" % btn_state)

        btn_state = btn_state_list[29]
        result = [btn_state[1] == "000"]
        if False in result:
            raise TimeoutException("device state error, current: %s" % btn_state)

        btn_state = btn_state_list[30]
        result = [btn_state[1] == "010"]
        if False in result:
            raise TimeoutException("device state error, current: %s" % btn_state)

        btn_state = btn_state_list[31]
        result = [btn_state[1] == "000"]
        if False in result:
            raise TimeoutException("device state error, current: %s" % btn_state)

        btn_state = btn_state_list[32]
        result = [btn_state[1] == "010"]
        if False in result:
            raise TimeoutException("device state error, current: %s" % btn_state)

        btn_state = btn_state_list[33]
        result = [btn_state[1] == "000"]
        if False in result:
            raise TimeoutException("device state error, current: %s" % btn_state)

        btn_state = btn_state_list[34]
        result = [btn_state[1] == "010"]
        if False in result:
            raise TimeoutException("device state error, current: %s" % btn_state)

        btn_state = btn_state_list[35]
        result = [btn_state[1] == "000"]
        if False in result:
            raise TimeoutException("device state error, current: %s" % btn_state)

        btn_state = btn_state_list[36]
        result = [btn_state[1] == "001"]
        if False in result:
            raise TimeoutException("device state error, current: %s" % btn_state)

        btn_state = btn_state_list[37]
        result = [btn_state[1] == "000"]
        if False in result:
            raise TimeoutException("device state error, current: %s" % btn_state)

        btn_state = btn_state_list[38]
        result = [btn_state[1] == "001"]
        if False in result:
            raise TimeoutException("device state error, current: %s" % btn_state)

        btn_state = btn_state_list[39]
        result = [btn_state[1] == "000"]
        if False in result:
            raise TimeoutException("device state error, current: %s" % btn_state)

        btn_state = btn_state_list[40]
        result = [btn_state[1] == "001"]
        if False in result:
            raise TimeoutException("device state error, current: %s" % btn_state)

        btn_state = btn_state_list[41]
        result = [btn_state[1] == "000"]
        if False in result:
            raise TimeoutException("device state error, current: %s" % btn_state)

        btn_state = btn_state_list[42]
        result = [btn_state[1] == "001"]
        if False in result:
            raise TimeoutException("device state error, current: %s" % btn_state)

        btn_state = btn_state_list[43]
        result = [btn_state[1] == "000"]
        if False in result:
            raise TimeoutException("device state error, current: %s" % btn_state)

        btn_state = btn_state_list[44]
        result = [btn_state[1] == "001"]
        if False in result:
            raise TimeoutException("device state error, current: %s" % btn_state)

        btn_state = btn_state_list[45]
        result = [btn_state[1] == "000"]
        if False in result:
            raise TimeoutException("device state error, current: %s" % btn_state)

        btn_state = btn_state_list[46]
        result = [btn_state[1] == "001"]
        if False in result:
            raise TimeoutException("device state error, current: %s" % btn_state)

        btn_state = btn_state_list[47]
        result = [btn_state[1] == "000"]
        if False in result:
            raise TimeoutException("device state error, current: %s" % btn_state)

        btn_state = btn_state_list[48]
        result = [btn_state[1] == "001"]
        if False in result:
            raise TimeoutException("device state error, current: %s" % btn_state)

        btn_state = btn_state_list[49]
        result = [btn_state[1] == "000"]
        if False in result:
            raise TimeoutException("device state error, current: %s" % btn_state)

        btn_state = btn_state_list[50]
        result = [btn_state[1] == "001"]
        if False in result:
            raise TimeoutException("device state error, current: %s" % btn_state)

        btn_state = btn_state_list[51]
        result = [btn_state[1] == "000"]
        if False in result:
            raise TimeoutException("device state error, current: %s" % btn_state)

        btn_state = btn_state_list[52]
        result = [btn_state[1] == "001"]
        if False in result:
            raise TimeoutException("device state error, current: %s" % btn_state)

        btn_state = btn_state_list[53]
        result = [btn_state[1] == "000"]
        if False in result:
            raise TimeoutException("device state error, current: %s" % btn_state)
