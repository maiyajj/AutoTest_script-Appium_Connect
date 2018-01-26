# coding=utf-8
from src.testcase.GN_Y201J.WidgetOperation import *


class GNY201JOverDay1(WidgetOperation):
    @case_run(False)
    def run(self):
        self.case_module = u"模式定时"  # 用例所属模块
        self.case_title = u'热水器模式设置每日循环'  # 用例名称
        self.zentao_id = "1299"  # 禅道ID

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

        time_1, time_2 = 1, 5
        tmp, cycle = self.create_water_mode_timer(now, time_1, time_2, u"每天")
        start_time_1, set_time_1 = tmp[0]
        start_time_2, set_time_2 = tmp[1]

        self.widget_click(self.page["mode_timer_page"]["to_return"],
                          self.page["control_device_page"]["title"])

        self.wait_widget(self.page["control_device_page"]["power_off"])

        self.check_timer(start_time_1, set_time_1, u"设备已开启", cycle)

        self.check_timer(start_time_2, set_time_2, u"设备已关闭", cycle)
