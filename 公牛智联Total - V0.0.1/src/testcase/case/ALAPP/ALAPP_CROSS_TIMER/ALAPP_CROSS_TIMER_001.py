# coding=utf-8
from src.testcase.common.WidgetOperation_AL import *


class ALAppCrossTimer1(WidgetOperationAL):
    @case_run_al(True)
    def run(self):
        self.case_module = u"FUT_CROSSTIMER_各种定时交叉执行"  # 用例所属模块
        self.case_title = u'FUT_CROSSTIMER_普通定时、循环定时、延时定时交叉设置后定时执行'  # 用例名称
        self.zentao_id = 519  # 禅道ID

    # 用例动作
    def case(self):
        self.set_power(conf["MAC"]["AL"][0], "power_off")

        self.choose_home_device(conf["MAC"]["AL"][0])

        self.close_mode_timer()

        self.close_general_timer()

        self.widget_click(self.page["control_device_page"]["normal_timer"],
                          self.page["normal_timer_page"]["title"])

        now = time.strftime("%H:%M")

        delay_time_1 = 5
        start_time_1, set_time_1 = self.create_normal_timer(now, delay_time_1, "power_on", u"执行一次", leave_time=4)

        delay_time_2 = 10
        start_time_2, set_time_2 = self.create_normal_timer(now, delay_time_2, "power_on", u"执行一次", leave_time=4)

        delay_time_3 = 15
        start_time_3, set_time_3 = self.create_normal_timer(now, delay_time_3, "power_off", u"执行一次", leave_time=4)

        delay_time_4 = 20
        start_time_4, set_time_4 = self.create_normal_timer(now, delay_time_4, "power_off", u"执行一次", leave_time=4)

        self.widget_click(self.page["normal_timer_page"]["to_return"],
                          self.page["control_device_page"]["title"])

        self.widget_click(self.page["control_device_page"]["delay_timer"],
                          self.page["delay_timer_page"]["title"])

        delay_time_5 = 10
        start_time_5, set_time_5 = self.create_delay_timer(now, delay_time_5, "power_off", True)

        self.widget_click(self.page["delay_timer_page"]["to_return"],
                          self.page["control_device_page"]["title"])

        delay_time_5 = 10
        start_time_5, set_time_5 = self.create_delay_timer(now, delay_time_5, "power_off", True)

        self.check_timer(start_time_1, set_time_1, u"设备已开启")
        self.check_timer(start_time_2, set_time_2, u"设备已开启", True)
        self.check_timer(start_time_3, set_time_3, u"设备已关闭")
        self.check_timer(start_time_4, set_time_4, u"设备已关闭", True)

        self.case_over(True)
