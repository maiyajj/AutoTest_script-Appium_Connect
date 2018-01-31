# coding=utf-8
from src.testcase.GN_F1331.WidgetOperation import *


class GNF1331KeyMemory2(WidgetOperation):
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
        self.widget_click(self.page["control_device_page"]["main_button"])
        self.wait_widget(self.page["control_device_page"]["main_button_on"])
        time_1 = time.time()

        self.widget_click(self.page["control_device_page"]["main_button"])
        self.wait_widget(self.page["control_device_page"]["main_button_off"])
        time_2 = time.time()

        ##
        self.widget_click(self.page["control_device_page"]["up_button"])
        self.wait_widget(self.page["control_device_page"]["main_button_on"])
        time_3 = time.time()

        self.widget_click(self.page["control_device_page"]["main_button"])
        self.wait_widget(self.page["control_device_page"]["main_button_off"])
        time_4 = time.time()

        #
        self.widget_click(self.page["control_device_page"]["mid_button"])
        self.wait_widget(self.page["control_device_page"]["main_button_on"])
        time_5 = time.time()

        self.widget_click(self.page["control_device_page"]["main_button"])
        self.wait_widget(self.page["control_device_page"]["main_button_off"])
        time_6 = time.time()

        #
        self.widget_click(self.page["control_device_page"]["down_button"])
        self.wait_widget(self.page["control_device_page"]["main_button_on"])
        time_7 = time.time()

        self.widget_click(self.page["control_device_page"]["main_button"])
        self.wait_widget(self.page["control_device_page"]["main_button_off"])
        time_8 = time.time()

        ##
        self.widget_click(self.page["control_device_page"]["up_button"])
        self.wait_widget(self.page["control_device_page"]["main_button_on"])
        time_9 = time.time()

        self.widget_click(self.page["control_device_page"]["mid_button"])
        self.wait_widget(self.page["control_device_page"]["main_button_on"])
        time_10 = time.time()

        self.widget_click(self.page["control_device_page"]["main_button"])
        self.wait_widget(self.page["control_device_page"]["main_button_off"])
        time_11 = time.time()

        #
        self.widget_click(self.page["control_device_page"]["up_button"])
        self.wait_widget(self.page["control_device_page"]["main_button_on"])
        time_12 = time.time()

        self.widget_click(self.page["control_device_page"]["down_button"])
        self.wait_widget(self.page["control_device_page"]["main_button_on"])
        time_13 = time.time()

        self.widget_click(self.page["control_device_page"]["main_button"])
        self.wait_widget(self.page["control_device_page"]["main_button_off"])
        time_14 = time.time()

        #
        self.widget_click(self.page["control_device_page"]["mid_button"])
        self.wait_widget(self.page["control_device_page"]["main_button_on"])
        time_15 = time.time()

        self.widget_click(self.page["control_device_page"]["down_button"])
        self.wait_widget(self.page["control_device_page"]["main_button_on"])
        time_16 = time.time()

        self.widget_click(self.page["control_device_page"]["main_button"])
        self.wait_widget(self.page["control_device_page"]["main_button_off"])
        time_17 = time.time()

        #####
        #  开关
        btn_dict = self.check_button_state(time_1, time_2, time_3, time_4, time_5, time_6, time_7, time_8, time_9,
                                           time_10, time_11, time_12, time_13, time_14, time_15, time_16, time_17,
                                           t_list=True)

        # 开关
        # 111, 000, 100, 000, 010, 000, 001, 000, 100, 110, 000, 100, 101, 000, 010, 011, 000
        btn = btn_dict[time_1]
        btn_all = btn[1]
        result = [btn_all == "111"]
        if False in result:
            raise TimeoutException("device state error, current: %s, result: %s" % (btn, result))

        btn = btn_dict[time_2]
        btn_all = btn[1]
        result = [btn_all == "000"]
        if False in result:
            raise TimeoutException("device state error, current: %s, result: %s" % (btn, result))

        btn = btn_dict[time_3]
        btn_all = btn[1]
        result = [btn_all == "100"]
        if False in result:
            raise TimeoutException("device state error, current: %s, result: %s" % (btn, result))

        btn = btn_dict[time_4]
        btn_all = btn[1]
        result = [btn_all == "000"]
        if False in result:
            raise TimeoutException("device state error, current: %s, result: %s" % (btn, result))

        btn = btn_dict[time_5]
        btn_all = btn[1]
        result = [btn_all == "010"]
        if False in result:
            raise TimeoutException("device state error, current: %s, result: %s" % (btn, result))

        btn = btn_dict[time_6]
        btn_all = btn[1]
        result = [btn_all == "000"]
        if False in result:
            raise TimeoutException("device state error, current: %s, result: %s" % (btn, result))

        btn = btn_dict[time_7]
        btn_all = btn[1]
        result = [btn_all == "001"]
        if False in result:
            raise TimeoutException("device state error, current: %s, result: %s" % (btn, result))

        btn = btn_dict[time_8]
        btn_all = btn[1]
        result = [btn_all == "000"]
        if False in result:
            raise TimeoutException("device state error, current: %s, result: %s" % (btn, result))

        btn = btn_dict[time_9]
        btn_all = btn[1]
        result = [btn_all == "100"]
        if False in result:
            raise TimeoutException("device state error, current: %s, result: %s" % (btn, result))

        btn = btn_dict[time_10]
        btn_all = btn[1]
        result = [btn_all == "110"]
        if False in result:
            raise TimeoutException("device state error, current: %s, result: %s" % (btn, result))

        btn = btn_dict[time_11]
        btn_all = btn[1]
        result = [btn_all == "000"]
        if False in result:
            raise TimeoutException("device state error, current: %s, result: %s" % (btn, result))

        btn = btn_dict[time_12]
        btn_all = btn[1]
        result = [btn_all == "100"]
        if False in result:
            raise TimeoutException("device state error, current: %s, result: %s" % (btn, result))

        btn = btn_dict[time_13]
        btn_all = btn[1]
        result = [btn_all == "101"]
        if False in result:
            raise TimeoutException("device state error, current: %s, result: %s" % (btn, result))

        btn = btn_dict[time_14]
        btn_all = btn[1]
        result = [btn_all == "000"]
        if False in result:
            raise TimeoutException("device state error, current: %s, result: %s" % (btn, result))

        btn = btn_dict[time_15]
        btn_all = btn[1]
        result = [btn_all == "010"]
        if False in result:
            raise TimeoutException("device state error, current: %s, result: %s" % (btn, result))

        btn = btn_dict[time_16]
        btn_all = btn[1]
        result = [btn_all == "011"]
        if False in result:
            raise TimeoutException("device state error, current: %s, result: %s" % (btn, result))

        btn = btn_dict[time_17]
        btn_all = btn[1]
        result = [btn_all == "000"]
        if False in result:
            raise TimeoutException("device state error, current: %s, result: %s" % (btn, result))
