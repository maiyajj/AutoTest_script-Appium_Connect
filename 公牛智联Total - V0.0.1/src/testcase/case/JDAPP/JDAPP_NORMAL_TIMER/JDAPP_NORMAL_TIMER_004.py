# coding=utf-8
from src.testcase.common.WidgetOperation_JD import *


class JDAppNormalTimer4(WidgetOperationJD):
    @case_run(False)
    def run(self):
        self.case_module = u"模式定时"  # 用例所属模块
        self.case_title = u'普通定时_设置13组'  # 用例名称
        self.zentao_id = 1174  # 禅道ID
    
    # 用例动作
    def case(self):
        self.choose_home_device(conf["MAC"]["JD"][0])

        self.close_mode_timer()

        self.set_power("power_off")

        self.widget_click(self.page["control_device_page"]["normal_timer"],
                          self.page["normal_timer_page"]["title"])
        self.delete_normal_timer()

        now = time.strftime("%H:%M")

        delay_time_1 = 1
        self.create_normal_timer(now, delay_time_1, "power_on", u"执行一次")

        delay_time_2 = 2
        self.create_normal_timer(now, delay_time_2, "power_off", u"执行一次")

        delay_time_3 = 3
        self.create_normal_timer(now, delay_time_3, "power_on", u"执行一次")

        delay_time_4 = 4
        self.create_normal_timer(now, delay_time_4, "power_off", u"执行一次")

        delay_time_5 = 5
        self.create_normal_timer(now, delay_time_5, "power_on", u"执行一次")

        delay_time_6 = 6
        self.create_normal_timer(now, delay_time_6, "power_off", u"执行一次")

        delay_time_7 = 7
        self.create_normal_timer(now, delay_time_7, "power_on", u"执行一次")

        delay_time_8 = 8
        self.create_normal_timer(now, delay_time_8, "power_off", u"执行一次")

        delay_time_9 = 9
        self.create_normal_timer(now, delay_time_9, "power_on", u"执行一次")

        delay_time_10 = 10
        self.create_normal_timer(now, delay_time_10, "power_off", u"执行一次")

        delay_time_11 = 11
        self.create_normal_timer(now, delay_time_11, "power_on", u"执行一次")

        delay_time_12 = 12
        self.create_normal_timer(now, delay_time_12, "power_off", u"执行一次")

        try:
            delay_time_13 = 13
            self.create_normal_timer(now, delay_time_13, "power_on", u"执行一次")
        except TimeoutException:
            self.logger.info(u"[APP_TIMER]第13个定时设置失败: %s[%s]" % (time.strftime("%X"), time.time()))

        self.widget_click(self.page["normal_timer_page"]["to_return"],
                          self.page["control_device_page"]["title"])

        self.wait_widget(self.page["control_device_page"]["power_off"])

        self.case_over(True)
