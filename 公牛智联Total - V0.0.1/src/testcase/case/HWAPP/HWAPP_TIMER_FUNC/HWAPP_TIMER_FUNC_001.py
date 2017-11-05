# coding=utf-8
from src.testcase.common.WidgetOperation_HW import *


class HWAppTimerFunc1(WidgetOperationHW):
    @case_run_hw(False)
    def run(self):
        self.case_module = u"定时功能(#240)"  # 用例所属模块
        self.case_title = u'延时定时的定时数量检查'  # 用例名称
        self.zentao_id = 2023  # 禅道ID

    # 用例动作
    def case(self):
        self.choose_home_device(conf["MAC"]["HW"][0])

        self.set_power("power_off")

        self.delete_delay_timer()

        self.widget_click(self.page["control_device_page"]["delay_timer"],
                          self.page["delay_timer_roll_popup"]["title"])

        now = time.strftime("%H:%M")

        delay_time_1 = 1
        self.set_timer_roll(self.page["delay_timer_roll_popup"]["roll_h"],
                            self.page["delay_timer_roll_popup"]["roll_m"],
                            now, delay_time_1)

        self.widget_click(self.page["control_device_page"]["delay_timer"],
                          self.page["delay_timer_roll_popup"]["title"])

        self.wait_widget(self.page["delay_timer_roll_popup"]["stop"])

        self.case_over(True)
