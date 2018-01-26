# coding=utf-8
from src.testcase.GN_Y201H.WidgetOperation import *


class GNY201HTimerFunc2(WidgetOperation):
    @case_run(False)
    def run(self):
        self.case_module = u"定时功能(#240)"  # 用例所属模块
        self.case_title = u'普通定时的定时数量检查'  # 用例名称
        self.zentao_id = "2022"  # 禅道ID

    # 用例动作
    def case(self):
        self.choose_home_device(conf["MAC"]["HW"][0])

        self.delete_normal_timer()

        self.delete_delay_timer()

        self.set_power("power_off")

        self.widget_click(self.page["control_device_page"]["normal_timer"],
                          self.page["normal_timer_page"]["title"])

        now = time.strftime("%H:%M")

        time_1 = 1
        self.create_normal_timer(now, time_1)

        time_2 = 2
        self.create_normal_timer(now, time_2)

        time_3 = 3
        self.create_normal_timer(now, time_3)

        time_4 = 4
        self.create_normal_timer(now, time_4)

        time_5 = 5
        self.create_normal_timer(now, time_5)

        time_6 = 6
        self.create_normal_timer(now, time_6)

        time_7 = 7
        self.create_normal_timer(now, time_7)

        time_8 = 8
        self.create_normal_timer(now, time_8)

        try:
            self.wait_widget(self.page["normal_timer_page"]["add_timer"])
            raise TimeoutException("can still add normal timer")
        except TimeoutException:
            pass
