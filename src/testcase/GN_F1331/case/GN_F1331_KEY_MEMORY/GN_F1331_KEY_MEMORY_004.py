# coding=utf-8
from src.testcase.GN_F1331.WidgetOperation import *


class GNF1331KeyMemory4(WidgetOperation):
    @case_run(False)
    def run(self):
        self.case_module = u"远程开关(#18)"  # 用例所属模块
        self.case_title = u'手机APP远程分层开关功能检查'  # 用例名称
        self.zentao_id = "191"  # 禅道ID

    # 用例动作
    def case(self):
        self.choose_home_device(conf["MAC"][self.app][self.device_mac])

        self.delete_out_date_timer()

        self.set_power("main_button_off")

        self.input_serial_command("power")

        ##
        self.widget_click(self.page["control_device_page"]["main_button"])
        self.wait_widget(self.page["control_device_page"]["main_button_on"])

        self.wait_widget(self.page["control_device_page"]["up_button_on"])

        self.wait_widget(self.page["control_device_page"]["mid_button_on"])

        self.wait_widget(self.page["control_device_page"]["down_button_on"])
        time_1 = time.time()

        ##
        self.widget_click(self.page["control_device_page"]["main_button"])
        self.wait_widget(self.page["control_device_page"]["main_button_off"])

        self.wait_widget(self.page["control_device_page"]["up_button_off"])

        self.wait_widget(self.page["control_device_page"]["mid_button_off"])

        self.wait_widget(self.page["control_device_page"]["down_button_off"])
        time_2 = time.time()

        #####
        # 开关
        btn_dict = self.check_button_state(time_1, time_2, t_list=True)

        # 开关
        # 111, 000
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
