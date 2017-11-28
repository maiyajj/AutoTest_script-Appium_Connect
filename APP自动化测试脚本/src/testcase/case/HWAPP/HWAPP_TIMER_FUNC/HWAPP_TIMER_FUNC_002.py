# coding=utf-8
from src.testcase.common.WidgetOperation_HW import *


class HWAppTimerFunc2(WidgetOperationHW):
    @case_run(False)
    def run(self):
        self.case_module = u"定时功能(#240)"  # 用例所属模块
        self.case_title = u'普通定时的定时数量检查'  # 用例名称
        self.zentao_id = 2022  # 禅道ID

    # 用例动作
    def case(self):
        self.choose_home_device(conf["MAC"]["HW"][0])

        self.delete_normal_timer()

        self.delete_delay_timer()

        self.set_power("power_off")

        self.widget_click(self.page["control_device_page"]["normal_timer"],
                          self.page["normal_timer_page"]["title"])

        now = time.strftime("%H:%M")

        delay_time_1 = 1
        self.create_normal_timer(now, delay_time_1)

        delay_time_2 = 2
        self.create_normal_timer(now, delay_time_2)

        delay_time_3 = 3
        self.create_normal_timer(now, delay_time_3)

        delay_time_4 = 4
        self.create_normal_timer(now, delay_time_4)

        delay_time_5 = 5
        self.create_normal_timer(now, delay_time_5)

        delay_time_6 = 6
        self.create_normal_timer(now, delay_time_6)

        delay_time_7 = 7
        self.create_normal_timer(now, delay_time_7)

        delay_time_8 = 8
        self.create_normal_timer(now, delay_time_8)

        try:
            self.wait_widget(self.page["normal_timer_page"]["add_timer"])
            raise TimeoutException("can still add normal timer")
        except TimeoutException:
            pass

