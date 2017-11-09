# coding=utf-8
from src.testcase.common.WidgetOperation_JD import *


class JDAppModeTimer4(WidgetOperationJD):
    @case_run(False)
    def run(self):
        self.case_module = u"模式定时"  # 用例所属模块
        self.case_title = u'充电保护模式下手动改变设备为开启状态后，定时结束检查设备状态'  # 用例名称
        self.zentao_id = 1083  # 禅道ID
    
    # 用例动作
    def case(self):
        self.choose_home_device(conf["MAC"]["JD"][0])

        self.close_mode_timer()

        self.set_power("power_off")

        self.widget_click(self.page["control_device_page"]["mode_timer"],
                          self.page["mode_timer_page"]["title"])

        self.widget_click(self.page["mode_timer_page"]["piocc_mode"],
                          self.page["piocc_mode_timer_page"]["title"])

        now = time.strftime("%H:%M")

        delay_time_1 = ["delay", "00:05"]
        start_time_1, set_time_1 = self.set_timer_roll(self.page["piocc_mode_timer_page"]["end_h"],
                                                       self.page["piocc_mode_timer_page"]["end_m"],
                                                       self.page["piocc_mode_timer_page"]["end_time_text"],
                                                       delay_time_1, now)

        self.widget_click(self.page["piocc_mode_timer_page"]["end_time"],
                          self.page["piocc_mode_timer_page"]["title"])

        self.launch_mode_timer("piocc_mode_timer_page", False, start_time_1)

        self.widget_click(self.page["mode_timer_page"]["to_return"],
                          self.page["control_device_page"]["title"])

        self.wait_widget(self.page["control_device_page"]["power_on"])

        time.sleep(60)

        self.widget_click(self.page["control_device_page"]["power_on"],
                          self.page["control_device_page"]["power_off"])

        self.widget_click(self.page["control_device_page"]["power_off"],
                          self.page["control_device_page"]["power_on"])

        self.check_timer(start_time_1, set_time_1, u"设备已关闭")

        self.case_over(True)
