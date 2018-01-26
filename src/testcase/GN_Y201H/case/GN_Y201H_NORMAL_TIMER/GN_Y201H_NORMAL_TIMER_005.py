# coding=utf-8
from src.testcase.GN_Y201H.WidgetOperation import *


class GNY201HNormalTimer5(WidgetOperation):
    @case_run(False)
    def run(self):
        self.case_module = u"普通定时(#246)"  # 用例所属模块
        self.case_title = u'在线状态，4组开与4组关单次执行的定时执行状态检查'  # 用例名称
        self.zentao_id = "2061"  # 禅道ID

    # 用例动作
    def case(self):
        self.choose_home_device(conf["MAC"]["HW"][0])

        self.delete_normal_timer()

        self.delete_delay_timer()

        self.set_power("power_off")

        self.widget_click(self.page["control_device_page"]["normal_timer"],
                          self.page["normal_timer_page"]["title"])

        now = time.strftime("%H:%M")
        # 本体120S + 2个定时 * (最多滑动59+23次) * 每次滑动耗时1S
        delay_s = 120 + 2 * ((59 + 23) * 1)

        time_1 = 1
        start_time_1, set_time_1, cycle1 = self.create_normal_timer(now, time_on=time_1, delay_s=delay_s)

        time_2 = 2
        start_time_2, set_time_2, cycle2 = self.create_normal_timer(now, time_off=time_2, delay_s=delay_s)

        self.widget_click(self.page["normal_timer_page"]["to_return"],
                          self.page["control_device_page"]["title"])

        self.check_timer(start_time_1, set_time_1, u"电源已开启", cycle1)
        self.check_timer(start_time_2, set_time_2, u"电源已关闭", cycle2)

        self.widget_click(self.page["control_device_page"]["normal_timer"],
                          self.page["normal_timer_page"]["title"])

        now = time.strftime("%H:%M")
        delay_s = 120 + 6 * ((59 + 23) * 1)

        time_3 = 2
        start_time_3, set_time_3, cycle3 = self.create_normal_timer(now, time_on=time_3, delay_s=delay_s)

        time_4 = 4
        start_time_4, set_time_4, cycle4 = self.create_normal_timer(now, time_off=time_4, delay_s=delay_s)

        time_5 = 6
        start_time_5, set_time_5, cycle5 = self.create_normal_timer(now, time_on=time_5, delay_s=delay_s)

        time_6 = 8
        start_time_6, set_time_6, cycle6 = self.create_normal_timer(now, time_off=time_6, delay_s=delay_s)

        time_7 = 10
        start_time_7, set_time_7, cycle7 = self.create_normal_timer(now, time_on=time_7, delay_s=delay_s)

        time_8 = 12
        start_time_8, set_time_8, cycle8 = self.create_normal_timer(now, time_off=time_8, delay_s=delay_s)

        self.widget_click(self.page["normal_timer_page"]["to_return"],
                          self.page["control_device_page"]["title"])

        self.check_timer(start_time_3, set_time_3, u"电源已开启", cycle3)
        self.check_timer(start_time_4, set_time_4, u"电源已关闭", cycle4)
        self.check_timer(start_time_5, set_time_5, u"电源已开启", cycle5)
        self.check_timer(start_time_6, set_time_6, u"电源已关闭", cycle6)
        self.check_timer(start_time_7, set_time_7, u"电源已开启", cycle7)
        self.check_timer(start_time_8, set_time_8, u"电源已关闭", cycle8)
