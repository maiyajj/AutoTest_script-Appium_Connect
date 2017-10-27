# coding=utf-8
from src.testcase.common.WidgetOperation_AL import *


class ALAppCrossTimer1(WidgetOperationAL):
    @case_run_al(True)
    def run(self):
        self.case_module = u"FUT_CROSSTIMER_各种定时交叉执行(#45)"  # 用例所属模块
        self.case_title = u'FUT_CROSSTIMER_普通定时、循环定时、延时定时交叉设置后定时执行'  # 用例名称
        self.zentao_id = 519  # 禅道ID

    # 用例动作
    def case(self):
        device = conf["MAC"]["AL"][0]
        self.set_power(device, "power_off")

        self.choose_home_device(device)

        self.close_mode_timer()

        self.close_general_timer()

        self.widget_click(self.page["control_device_page"]["normal_timer"],
                          self.page["normal_timer_page"]["title"])

        now = time.strftime("%H:%M")

        delay_time_1 = 5
        start_time_1, set_time_1 = self.create_normal_timer(now, delay_time_1, "power_on", u"执行一次", delay_s=240)

        delay_time_2 = 10
        start_time_2, set_time_2 = self.create_normal_timer(now, delay_time_2, "power_on", u"执行一次", delay_s=240)

        delay_time_3 = 15
        start_time_3, set_time_3 = self.create_normal_timer(now, delay_time_3, "power_off", u"执行一次", delay_s=240)

        delay_time_4 = 20
        start_time_4, set_time_4 = self.create_normal_timer(now, delay_time_4, "power_off", u"执行一次", delay_s=240)

        self.widget_click(self.page["normal_timer_page"]["to_return"],
                          self.page["control_device_page"]["title"])

        self.widget_click(self.page["control_device_page"]["delay_timer"],
                          self.page["delay_timer_page"]["title"])

        delay_time_5 = 10
        start_time_5, set_time_5 = self.create_delay_timer(now, delay_time_5, "power_on", 150)

        self.widget_click(self.page["delay_timer_page"]["to_return"],
                          self.page["control_device_page"]["title"])

        self.ac.swipe(0.5, 0.6, 0.5, 0.4, 0, self.driver)
        self.widget_click(self.page["control_device_page"]["cycle_timer"],
                          self.page["cycle_timer_page"]["title"])

        delay_time_6, delay_time_7 = 3, 3
        tmp = self.create_cycle_timer("cycle_timer_page", now, delay_time_6, delay_time_7, u"4次", 210)
        start_time_6, set_time_6, start_time_7, set_time_7 = tmp[0]
        start_time_8, set_time_8, start_time_9, set_time_9 = tmp[1]
        start_time_10, set_time_10, start_time_11, set_time_11 = tmp[2]
        start_time_12, set_time_12, start_time_13, set_time_13 = tmp[3]
        start_time_14, set_time_14, start_time_15, set_time_15 = tmp[4]

        self.widget_click(self.page["cycle_timer_page"]["to_return"],
                          self.page["control_device_page"]["title"])

        self.widget_click(self.page["control_device_page"]["to_return"],
                          self.page["app_home_page"]["title"])

        self.check_timer(device, start_time_6, set_time_6, u"设备已关闭")
        self.check_timer(device, start_time_1, set_time_1, u"设备已开启")
        self.check_timer(device, start_time_7, set_time_7, u"设备已开启", True)
        self.check_timer(device, start_time_5, set_time_5, u"设备已开启", True)
        self.check_timer(device, start_time_8, set_time_8, u"设备已关闭")
        self.check_timer(device, start_time_2, set_time_2, u"设备已关闭", True)
        self.check_timer(device, start_time_9, set_time_9, u"设备已开启")
        self.check_timer(device, start_time_10, set_time_10, u"设备已关闭")
        self.check_timer(device, start_time_3, set_time_3, u"设备已开启")
        self.check_timer(device, start_time_11, set_time_11, u"设备已开启", True)

        self.choose_home_device(device)
        self.widget_click(self.page["control_device_page"]["delay_timer"],
                          self.page["delay_timer_page"]["title"])

        delay_time_16 = 10
        start_time_16, set_time_16 = self.create_delay_timer(set_time_5, delay_time_16, "power_off", 150, True)

        self.widget_click(self.page["delay_timer_page"]["to_return"],
                          self.page["control_device_page"]["title"])

        self.widget_click(self.page["control_device_page"]["to_return"],
                          self.page["app_home_page"]["title"])

        self.check_timer(device, start_time_16, set_time_16, u"设备已关闭")
        self.check_timer(device, start_time_4, set_time_4, u"设备已关闭", True)
        self.check_timer(device, start_time_12, set_time_12, u"设备已关闭", True)
        self.check_timer(device, start_time_13, set_time_13, u"设备已开启")
        self.check_timer(device, start_time_14, set_time_14, u"设备已关闭")
        self.check_timer(device, start_time_15, set_time_15, u"设备已开启")

        self.case_over(True)
