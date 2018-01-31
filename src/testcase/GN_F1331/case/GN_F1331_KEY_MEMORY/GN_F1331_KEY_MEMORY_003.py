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
        self.widget_click(self.page["control_device_page"]["up_button"])
        self.wait_widget(self.page["control_device_page"]["main_button_on"])
        time_1 = time.time()

        self.widget_click(self.page["control_device_page"]["up_button"])
        self.wait_widget(self.page["control_device_page"]["main_button_off"])
        time_2 = time.time()

        self.widget_click(self.page["control_device_page"]["up_button"])
        self.wait_widget(self.page["control_device_page"]["main_button_on"])
        time_3 = time.time()

        self.widget_click(self.page["control_device_page"]["up_button"])
        self.wait_widget(self.page["control_device_page"]["main_button_off"])
        time_4 = time.time()

        self.widget_click(self.page["control_device_page"]["up_button"])
        self.wait_widget(self.page["control_device_page"]["main_button_on"])
        time_5 = time.time()

        self.widget_click(self.page["control_device_page"]["up_button"])
        self.wait_widget(self.page["control_device_page"]["main_button_off"])
        time_6 = time.time()

        self.widget_click(self.page["control_device_page"]["up_button"])
        self.wait_widget(self.page["control_device_page"]["main_button_on"])
        time_7 = time.time()

        self.widget_click(self.page["control_device_page"]["up_button"])
        self.wait_widget(self.page["control_device_page"]["main_button_off"])
        time_8 = time.time()

        self.widget_click(self.page["control_device_page"]["up_button"])
        self.wait_widget(self.page["control_device_page"]["main_button_on"])
        time_9 = time.time()

        #
        self.widget_click(self.page["control_device_page"]["up_button"])
        self.wait_widget(self.page["control_device_page"]["main_button_off"])
        time_10 = time.time()

        self.widget_click(self.page["control_device_page"]["up_button"])
        self.wait_widget(self.page["control_device_page"]["main_button_on"])
        time_11 = time.time()

        self.widget_click(self.page["control_device_page"]["up_button"])
        self.wait_widget(self.page["control_device_page"]["main_button_off"])
        time_12 = time.time()

        self.widget_click(self.page["control_device_page"]["up_button"])
        self.wait_widget(self.page["control_device_page"]["main_button_on"])
        time_13 = time.time()

        self.widget_click(self.page["control_device_page"]["up_button"])
        self.wait_widget(self.page["control_device_page"]["main_button_off"])
        time_14 = time.time()

        self.widget_click(self.page["control_device_page"]["up_button"])
        self.wait_widget(self.page["control_device_page"]["main_button_on"])
        time_15 = time.time()

        self.widget_click(self.page["control_device_page"]["up_button"])
        self.wait_widget(self.page["control_device_page"]["main_button_off"])
        time_16 = time.time()

        self.widget_click(self.page["control_device_page"]["up_button"])
        self.wait_widget(self.page["control_device_page"]["main_button_on"])
        time_17 = time.time()

        self.widget_click(self.page["control_device_page"]["up_button"])
        self.wait_widget(self.page["control_device_page"]["main_button_off"])
        time_18 = time.time()

        ##
        self.widget_click(self.page["control_device_page"]["mid_button"])
        self.wait_widget(self.page["control_device_page"]["main_button_on"])
        time_19 = time.time()

        self.widget_click(self.page["control_device_page"]["mid_button"])
        self.wait_widget(self.page["control_device_page"]["main_button_off"])
        time_20 = time.time()

        self.widget_click(self.page["control_device_page"]["mid_button"])
        self.wait_widget(self.page["control_device_page"]["main_button_on"])
        time_21 = time.time()

        self.widget_click(self.page["control_device_page"]["mid_button"])
        self.wait_widget(self.page["control_device_page"]["main_button_off"])
        time_22 = time.time()

        self.widget_click(self.page["control_device_page"]["mid_button"])
        self.wait_widget(self.page["control_device_page"]["main_button_on"])
        time_23 = time.time()

        self.widget_click(self.page["control_device_page"]["mid_button"])
        self.wait_widget(self.page["control_device_page"]["main_button_off"])
        time_24 = time.time()

        self.widget_click(self.page["control_device_page"]["mid_button"])
        self.wait_widget(self.page["control_device_page"]["main_button_on"])
        time_25 = time.time()

        self.widget_click(self.page["control_device_page"]["mid_button"])
        self.wait_widget(self.page["control_device_page"]["main_button_off"])
        time_26 = time.time()

        self.widget_click(self.page["control_device_page"]["mid_button"])
        self.wait_widget(self.page["control_device_page"]["main_button_on"])
        time_27 = time.time()

        #
        self.widget_click(self.page["control_device_page"]["mid_button"])
        self.wait_widget(self.page["control_device_page"]["main_button_off"])
        time_28 = time.time()

        self.widget_click(self.page["control_device_page"]["mid_button"])
        self.wait_widget(self.page["control_device_page"]["main_button_on"])
        time_29 = time.time()

        self.widget_click(self.page["control_device_page"]["mid_button"])
        self.wait_widget(self.page["control_device_page"]["main_button_off"])
        time_30 = time.time()

        self.widget_click(self.page["control_device_page"]["mid_button"])
        self.wait_widget(self.page["control_device_page"]["main_button_on"])
        time_31 = time.time()

        self.widget_click(self.page["control_device_page"]["mid_button"])
        self.wait_widget(self.page["control_device_page"]["main_button_off"])
        time_32 = time.time()

        self.widget_click(self.page["control_device_page"]["mid_button"])
        self.wait_widget(self.page["control_device_page"]["main_button_on"])
        time_33 = time.time()

        self.widget_click(self.page["control_device_page"]["mid_button"])
        self.wait_widget(self.page["control_device_page"]["main_button_off"])
        time_34 = time.time()

        self.widget_click(self.page["control_device_page"]["mid_button"])
        self.wait_widget(self.page["control_device_page"]["main_button_on"])
        time_35 = time.time()

        self.widget_click(self.page["control_device_page"]["mid_button"])
        self.wait_widget(self.page["control_device_page"]["main_button_off"])
        time_36 = time.time()

        ##
        self.widget_click(self.page["control_device_page"]["down_button"])
        self.wait_widget(self.page["control_device_page"]["main_button_on"])
        time_37 = time.time()

        self.widget_click(self.page["control_device_page"]["down_button"])
        self.wait_widget(self.page["control_device_page"]["main_button_off"])
        time_38 = time.time()

        self.widget_click(self.page["control_device_page"]["down_button"])
        self.wait_widget(self.page["control_device_page"]["main_button_on"])
        time_39 = time.time()

        self.widget_click(self.page["control_device_page"]["down_button"])
        self.wait_widget(self.page["control_device_page"]["main_button_off"])
        time_40 = time.time()

        self.widget_click(self.page["control_device_page"]["down_button"])
        self.wait_widget(self.page["control_device_page"]["main_button_on"])
        time_41 = time.time()

        self.widget_click(self.page["control_device_page"]["down_button"])
        self.wait_widget(self.page["control_device_page"]["main_button_off"])
        time_42 = time.time()

        self.widget_click(self.page["control_device_page"]["down_button"])
        self.wait_widget(self.page["control_device_page"]["main_button_on"])
        time_43 = time.time()

        self.widget_click(self.page["control_device_page"]["down_button"])
        self.wait_widget(self.page["control_device_page"]["main_button_off"])
        time_44 = time.time()

        self.widget_click(self.page["control_device_page"]["down_button"])
        self.wait_widget(self.page["control_device_page"]["main_button_on"])
        time_45 = time.time()

        #
        self.widget_click(self.page["control_device_page"]["down_button"])
        self.wait_widget(self.page["control_device_page"]["main_button_off"])
        time_46 = time.time()

        self.widget_click(self.page["control_device_page"]["down_button"])
        self.wait_widget(self.page["control_device_page"]["main_button_on"])
        time_47 = time.time()

        self.widget_click(self.page["control_device_page"]["down_button"])
        self.wait_widget(self.page["control_device_page"]["main_button_off"])
        time_48 = time.time()

        self.widget_click(self.page["control_device_page"]["down_button"])
        self.wait_widget(self.page["control_device_page"]["main_button_on"])
        time_49 = time.time()

        self.widget_click(self.page["control_device_page"]["down_button"])
        self.wait_widget(self.page["control_device_page"]["main_button_off"])
        time_50 = time.time()

        self.widget_click(self.page["control_device_page"]["down_button"])
        self.wait_widget(self.page["control_device_page"]["main_button_on"])
        time_51 = time.time()

        self.widget_click(self.page["control_device_page"]["down_button"])
        self.wait_widget(self.page["control_device_page"]["main_button_off"])
        time_52 = time.time()

        self.widget_click(self.page["control_device_page"]["down_button"])
        self.wait_widget(self.page["control_device_page"]["main_button_on"])
        time_53 = time.time()

        self.widget_click(self.page["control_device_page"]["down_button"])
        self.wait_widget(self.page["control_device_page"]["main_button_off"])
        time_54 = time.time()

        #####
        # 开关
        btn_dict = self.check_button_state(time_1, time_2, time_3, time_4, time_5, time_6, time_7, time_8, time_9,
                                           time_10, time_11, time_12, time_13, time_14, time_15, time_16, time_17,
                                           time_18, time_19, time_20, time_21, time_22, time_23, time_24, time_25,
                                           time_26, time_27, time_28, time_29, time_30, time_31, time_32, time_33,
                                           time_34, time_35, time_36, time_37, time_38, time_39, time_40, time_41,
                                           time_42, time_43, time_44, time_45, time_46, time_47, time_48, time_49,
                                           time_50, time_51, time_52, time_53, time_54, t_list=True)

        # 开关
        # 100, 000, 100, 000, 100, 000, 100, 000, 100,
        #  000, 100, 000, 100, 000, 100, 000, 100, 000,
        # 010, 000, 010, 000, 010, 000, 010, 000, 010,
        #  000, 010, 000, 010, 000, 010, 000, 010, 000,
        # 001, 000, 001, 000, 001, 000, 001, 000, 001,
        #  000, 001, 000, 001, 000, 001, 000, 001, 000
        btn = btn_dict[time_1]
        btn_all = btn[1]
        result = [btn_all == "100"]
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
        result = [btn_all == "100"]
        if False in result:
            raise TimeoutException("device state error, current: %s, result: %s" % (btn, result))

        btn = btn_dict[time_6]
        btn_all = btn[1]
        result = [btn_all == "000"]
        if False in result:
            raise TimeoutException("device state error, current: %s, result: %s" % (btn, result))

        btn = btn_dict[time_7]
        btn_all = btn[1]
        result = [btn_all == "100"]
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
        result = [btn_all == "000"]
        if False in result:
            raise TimeoutException("device state error, current: %s, result: %s" % (btn, result))

        btn = btn_dict[time_11]
        btn_all = btn[1]
        result = [btn_all == "100"]
        if False in result:
            raise TimeoutException("device state error, current: %s, result: %s" % (btn, result))

        btn = btn_dict[time_12]
        btn_all = btn[1]
        result = [btn_all == "000"]
        if False in result:
            raise TimeoutException("device state error, current: %s, result: %s" % (btn, result))

        btn = btn_dict[time_13]
        btn_all = btn[1]
        result = [btn_all == "100"]
        if False in result:
            raise TimeoutException("device state error, current: %s, result: %s" % (btn, result))

        btn = btn_dict[time_14]
        btn_all = btn[1]
        result = [btn_all == "000"]
        if False in result:
            raise TimeoutException("device state error, current: %s, result: %s" % (btn, result))

        btn = btn_dict[time_15]
        btn_all = btn[1]
        result = [btn_all == "100"]
        if False in result:
            raise TimeoutException("device state error, current: %s, result: %s" % (btn, result))

        btn = btn_dict[time_16]
        btn_all = btn[1]
        result = [btn_all == "000"]
        if False in result:
            raise TimeoutException("device state error, current: %s, result: %s" % (btn, result))

        btn = btn_dict[time_17]
        btn_all = btn[1]
        result = [btn_all == "100"]
        if False in result:
            raise TimeoutException("device state error, current: %s, result: %s" % (btn, result))

        btn = btn_dict[time_18]
        btn_all = btn[1]
        result = [btn_all == "000"]
        if False in result:
            raise TimeoutException("device state error, current: %s, result: %s" % (btn, result))

        btn = btn_dict[time_19]
        btn_all = btn[1]
        result = [btn_all == "010"]
        if False in result:
            raise TimeoutException("device state error, current: %s, result: %s" % (btn, result))

        btn = btn_dict[time_20]
        btn_all = btn[1]
        result = [btn_all == "000"]
        if False in result:
            raise TimeoutException("device state error, current: %s, result: %s" % (btn, result))

        btn = btn_dict[time_21]
        btn_all = btn[1]
        result = [btn_all == "010"]
        if False in result:
            raise TimeoutException("device state error, current: %s, result: %s" % (btn, result))

        btn = btn_dict[time_22]
        btn_all = btn[1]
        result = [btn_all == "000"]
        if False in result:
            raise TimeoutException("device state error, current: %s, result: %s" % (btn, result))

        btn = btn_dict[time_23]
        btn_all = btn[1]
        result = [btn_all == "010"]
        if False in result:
            raise TimeoutException("device state error, current: %s, result: %s" % (btn, result))

        btn = btn_dict[time_24]
        btn_all = btn[1]
        result = [btn_all == "000"]
        if False in result:
            raise TimeoutException("device state error, current: %s, result: %s" % (btn, result))

        btn = btn_dict[time_25]
        btn_all = btn[1]
        result = [btn_all == "010"]
        if False in result:
            raise TimeoutException("device state error, current: %s, result: %s" % (btn, result))

        btn = btn_dict[time_26]
        btn_all = btn[1]
        result = [btn_all == "000"]
        if False in result:
            raise TimeoutException("device state error, current: %s, result: %s" % (btn, result))

        btn = btn_dict[time_27]
        btn_all = btn[1]
        result = [btn_all == "010"]
        if False in result:
            raise TimeoutException("device state error, current: %s, result: %s" % (btn, result))

        btn = btn_dict[time_28]
        btn_all = btn[1]
        result = [btn_all == "000"]
        if False in result:
            raise TimeoutException("device state error, current: %s, result: %s" % (btn, result))

        btn = btn_dict[time_29]
        btn_all = btn[1]
        result = [btn_all == "010"]
        if False in result:
            raise TimeoutException("device state error, current: %s, result: %s" % (btn, result))

        btn = btn_dict[time_30]
        btn_all = btn[1]
        result = [btn_all == "000"]
        if False in result:
            raise TimeoutException("device state error, current: %s, result: %s" % (btn, result))

        btn = btn_dict[time_31]
        btn_all = btn[1]
        result = [btn_all == "010"]
        if False in result:
            raise TimeoutException("device state error, current: %s, result: %s" % (btn, result))

        btn = btn_dict[time_32]
        btn_all = btn[1]
        result = [btn_all == "000"]
        if False in result:
            raise TimeoutException("device state error, current: %s, result: %s" % (btn, result))

        btn = btn_dict[time_33]
        btn_all = btn[1]
        result = [btn_all == "010"]
        if False in result:
            raise TimeoutException("device state error, current: %s, result: %s" % (btn, result))

        btn = btn_dict[time_34]
        btn_all = btn[1]
        result = [btn_all == "000"]
        if False in result:
            raise TimeoutException("device state error, current: %s, result: %s" % (btn, result))

        btn = btn_dict[time_35]
        btn_all = btn[1]
        result = [btn_all == "010"]
        if False in result:
            raise TimeoutException("device state error, current: %s, result: %s" % (btn, result))

        btn = btn_dict[time_36]
        btn_all = btn[1]
        result = [btn_all == "000"]
        if False in result:
            raise TimeoutException("device state error, current: %s, result: %s" % (btn, result))

        btn = btn_dict[time_37]
        btn_all = btn[1]
        result = [btn_all == "001"]
        if False in result:
            raise TimeoutException("device state error, current: %s, result: %s" % (btn, result))

        btn = btn_dict[time_38]
        btn_all = btn[1]
        result = [btn_all == "000"]
        if False in result:
            raise TimeoutException("device state error, current: %s, result: %s" % (btn, result))

        btn = btn_dict[time_39]
        btn_all = btn[1]
        result = [btn_all == "001"]
        if False in result:
            raise TimeoutException("device state error, current: %s, result: %s" % (btn, result))

        btn = btn_dict[time_40]
        btn_all = btn[1]
        result = [btn_all == "000"]
        if False in result:
            raise TimeoutException("device state error, current: %s, result: %s" % (btn, result))

        btn = btn_dict[time_41]
        btn_all = btn[1]
        result = [btn_all == "001"]
        if False in result:
            raise TimeoutException("device state error, current: %s, result: %s" % (btn, result))

        btn = btn_dict[time_42]
        btn_all = btn[1]
        result = [btn_all == "000"]
        if False in result:
            raise TimeoutException("device state error, current: %s, result: %s" % (btn, result))

        btn = btn_dict[time_43]
        btn_all = btn[1]
        result = [btn_all == "001"]
        if False in result:
            raise TimeoutException("device state error, current: %s, result: %s" % (btn, result))

        btn = btn_dict[time_44]
        btn_all = btn[1]
        result = [btn_all == "000"]
        if False in result:
            raise TimeoutException("device state error, current: %s, result: %s" % (btn, result))

        btn = btn_dict[time_45]
        btn_all = btn[1]
        result = [btn_all == "001"]
        if False in result:
            raise TimeoutException("device state error, current: %s, result: %s" % (btn, result))

        btn = btn_dict[time_46]
        btn_all = btn[1]
        result = [btn_all == "000"]
        if False in result:
            raise TimeoutException("device state error, current: %s, result: %s" % (btn, result))

        btn = btn_dict[time_47]
        btn_all = btn[1]
        result = [btn_all == "001"]
        if False in result:
            raise TimeoutException("device state error, current: %s, result: %s" % (btn, result))

        btn = btn_dict[time_48]
        btn_all = btn[1]
        result = [btn_all == "000"]
        if False in result:
            raise TimeoutException("device state error, current: %s, result: %s" % (btn, result))

        btn = btn_dict[time_49]
        btn_all = btn[1]
        result = [btn_all == "001"]
        if False in result:
            raise TimeoutException("device state error, current: %s, result: %s" % (btn, result))

        btn = btn_dict[time_50]
        btn_all = btn[1]
        result = [btn_all == "000"]
        if False in result:
            raise TimeoutException("device state error, current: %s, result: %s" % (btn, result))

        btn = btn_dict[time_51]
        btn_all = btn[1]
        result = [btn_all == "001"]
        if False in result:
            raise TimeoutException("device state error, current: %s, result: %s" % (btn, result))

        btn = btn_dict[time_52]
        btn_all = btn[1]
        result = [btn_all == "000"]
        if False in result:
            raise TimeoutException("device state error, current: %s, result: %s" % (btn, result))

        btn = btn_dict[time_53]
        btn_all = btn[1]
        result = [btn_all == "001"]
        if False in result:
            raise TimeoutException("device state error, current: %s, result: %s" % (btn, result))

        btn = btn_dict[time_54]
        btn_all = btn[1]
        result = [btn_all == "000"]
        if False in result:
            raise TimeoutException("device state error, current: %s, result: %s" % (btn, result))
