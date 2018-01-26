# coding=utf-8
from src.testcase.GN_Y201J.WidgetOperation import *


class GNY201JModeTimer6(WidgetOperation):
    @case_run(False)
    def run(self):
        self.case_module = u"模式定时"  # 用例所属模块
        self.case_title = u'鱼缸模式开启1分钟，关闭1分钟定时是否正确执行'  # 用例名称
        self.zentao_id = "1103"  # 禅道ID

    # 用例动作
    def case(self):
        self.choose_home_device(conf["MAC"]["JD"][0])

        self.close_mode_timer()

        self.set_power("power_off")

        self.widget_click(self.page["control_device_page"]["mode_timer"],
                          self.page["mode_timer_page"]["title"])

        self.widget_click(self.page["mode_timer_page"]["fish_mode"],
                          self.page["fish_mode_timer_page"]["title"])

        now = time.strftime("%H:%M")

        time_1, time_2 = ["delay", "00:01"], ["delay", "00:01"]
        tmp = self.create_fish_timer(now, time_1, time_2, u"永久循环")
        start_time_1, set_time_1 = tmp[0]
        start_time_2, set_time_2 = tmp[1]

        self.widget_click(self.page["mode_timer_page"]["to_return"],
                          self.page["control_device_page"]["title"])

        self.wait_widget(self.page["control_device_page"]["power_on"])

        self.check_timer(start_time_1, set_time_1, u"设备已关闭")

        self.check_timer(start_time_2, set_time_2, u"设备已开启")
