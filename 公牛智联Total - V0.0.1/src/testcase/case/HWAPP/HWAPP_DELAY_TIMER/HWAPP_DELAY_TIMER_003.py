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

        self.delete_normal_timer()

        self.delete_delay_timer()

        self.set_power("power_off")

        self.widget_click(self.page["control_device_page"]["delay_timer"],
                          self.page["delay_timer_roll_popup"]["title"])

        now = time.strftime("%H:%M")

        delay_time_1 = ["delay", "00:02"]
        start_time_1, set_time_1 = self.create_delay_timer(now, delay_time_1)

        self.check_timer(start_time_1, set_time_1, u"电源已开启")

        self.case_over(True)
