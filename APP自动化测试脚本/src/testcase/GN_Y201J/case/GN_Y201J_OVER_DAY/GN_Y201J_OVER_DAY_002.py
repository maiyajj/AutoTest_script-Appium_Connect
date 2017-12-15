# coding=utf-8
from src.testcase.GN_Y201J.WidgetOperation import *


class GNY201JOverDay2(WidgetOperation):
    @case_run(False)
    def run(self):
        self.case_module = u"模式定时"  # 用例所属模块
        self.case_title = u'热水器模式在跨天循环下的跨天执行'  # 用例名称
        self.zentao_id = 1300  # 禅道ID

    # 用例动作
    def case(self):
        self.choose_home_device(conf["MAC"]["JD"][0])

        self.close_mode_timer()

        self.set_power("power_off")

        self.widget_click(self.page["control_device_page"]["mode_timer"],
                          self.page["mode_timer_page"]["title"])

        self.widget_click(self.page["mode_timer_page"]["water_mode"],
                          self.page["water_mode_timer_page"]["title"])

        now = time.strftime("%H:%M")

        delay_time_1, delay_time_2 = ["point", "17:00"], ["point", "01:00"]
        now = time.strftime("%A").lower()
        date_1 = ["monday", "wednesday", "friday"]
        if now in date_1:
            date_2 = [u"周一", u"周三", u"周五"]
        else:
            date_2 = [u"周二", u"周四", u"周六"]
        tmp, cycle = self.create_water_mode_timer(now, delay_time_1, delay_time_2, date_2)
        start_time_1, set_time_1 = tmp[0]
        start_time_2, set_time_2 = tmp[1]

        self.widget_click(self.page["mode_timer_page"]["to_return"],
                          self.page["control_device_page"]["title"])

        self.wait_widget(self.page["control_device_page"]["power_off"])

        self.check_timer(start_time_1, set_time_1, u"设备已开启", cycle)

        self.check_timer(start_time_2, set_time_2, u"设备已关闭", cycle)
