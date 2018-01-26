# coding=utf-8
from src.testcase.GN_Y201J.WidgetOperation import *


class GNY201JNormalTimer3(WidgetOperation):
    @case_run(False)
    def run(self):
        self.case_module = u"模式定时"  # 用例所属模块
        self.case_title = u'普通定时最大组数设定_设置12组'  # 用例名称
        self.zentao_id = "1164"  # 禅道ID

    # 用例动作
    def case(self):
        self.choose_home_device(conf["MAC"]["JD"][0])

        self.close_mode_timer()

        self.set_power("power_off")

        self.widget_click(self.page["control_device_page"]["normal_timer"],
                          self.page["normal_timer_page"]["title"])
        self.delete_normal_timer()

        now = time.strftime("%H:%M")

        time_1 = 1
        start_time_1, set_time_1, cycle1 = self.create_normal_timer(now, time_1, "power_on", u"执行一次")

        time_2 = 2
        start_time_2, set_time_2, cycle2 = self.create_normal_timer(now, time_2, "power_off", u"执行一次")

        time_3 = 3
        start_time_3, set_time_3, cycle3 = self.create_normal_timer(now, time_3, "power_on", u"执行一次")

        time_4 = 4
        start_time_4, set_time_4, cycle4 = self.create_normal_timer(now, time_4, "power_off", u"执行一次")

        time_5 = 5
        start_time_5, set_time_5, cycle5 = self.create_normal_timer(now, time_5, "power_on", u"执行一次")

        time_6 = 6
        start_time_6, set_time_6, cycle6 = self.create_normal_timer(now, time_6, "power_off", u"执行一次")

        time_7 = 7
        start_time_7, set_time_7, cycle7 = self.create_normal_timer(now, time_7, "power_on", u"执行一次")

        time_8 = 8
        start_time_8, set_time_8, cycle8 = self.create_normal_timer(now, time_8, "power_off", u"执行一次")

        time_9 = 9
        start_time_9, set_time_9, cycle9 = self.create_normal_timer(now, time_9, "power_on", u"执行一次")

        time_10 = 10
        start_time_10, set_time_10, cycle10 = self.create_normal_timer(now, time_10, "power_off", u"执行一次")

        time_11 = 11
        start_time_11, set_time_11, cycle11 = self.create_normal_timer(now, time_11, "power_on", u"执行一次")

        time_12 = 12
        start_time_12, set_time_12, cycle12 = self.create_normal_timer(now, time_12, "power_off", u"执行一次")

        self.widget_click(self.page["normal_timer_page"]["to_return"],
                          self.page["control_device_page"]["title"])

        self.wait_widget(self.page["control_device_page"]["power_off"])

        self.check_timer(start_time_1, set_time_1, u"设备已开启")
        self.check_timer(start_time_2, set_time_2, u"设备已关闭")
        self.check_timer(start_time_3, set_time_3, u"设备已开启")
        self.check_timer(start_time_4, set_time_4, u"设备已关闭")
        self.check_timer(start_time_5, set_time_5, u"设备已开启")
        self.check_timer(start_time_6, set_time_6, u"设备已关闭")
        self.check_timer(start_time_7, set_time_7, u"设备已开启")
        self.check_timer(start_time_8, set_time_8, u"设备已关闭")
        self.check_timer(start_time_9, set_time_9, u"设备已开启")
        self.check_timer(start_time_10, set_time_10, u"设备已关闭")
        self.check_timer(start_time_11, set_time_11, u"设备已开启")
        self.check_timer(start_time_12, set_time_12, u"设备已关闭")
