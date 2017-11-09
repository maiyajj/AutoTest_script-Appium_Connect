# coding=utf-8
from src.testcase.common.WidgetOperation_HW import *


class HWAppDelayTimer3(WidgetOperationHW):
    @case_run(False)
    def run(self):
        self.case_module = u"延时定时(#249)"  # 用例所属模块
        self.case_title = u'在线状态，1组单开的延时定时执行状态检查'  # 用例名称
        self.zentao_id = 2098  # 禅道ID

    # 用例动作
    def case(self):
        self.choose_home_device(conf["MAC"]["HW"][0])

        self.set_power("power_off")

        self.delete_delay_timer()

        self.widget_click(self.page["control_device_page"]["delay_timer"],
                          self.page["delay_timer_roll_popup"]["title"])

        now = time.strftime("%H:%M")

        delay_time_1 = 2
        start_time_1, set_time_1 = self.set_timer_roll(self.page["delay_timer_roll_popup"]["roll_h"],
                                                       self.page["delay_timer_roll_popup"]["roll_m"],
                                                       now, delay_time_1)

        self.check_timer(start_time_1, set_time_1, "power_on")

        self.case_over(True)
