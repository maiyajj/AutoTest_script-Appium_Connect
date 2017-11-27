# coding=utf-8
from src.testcase.common.WidgetOperation_HW import *


class HWAppDelayTimer1(WidgetOperationHW):
    @case_run(False)
    def run(self):
        self.case_module = u"延时定时(#249)"  # 用例所属模块
        self.case_title = u'延时定时设置后，改变设备状态后查看延时定时的执行状态'  # 用例名称
        self.zentao_id = 2100  # 禅道ID

    # 用例动作
    def case(self):
        self.choose_home_device(conf["MAC"]["HW"][0])

        self.delete_normal_timer()

        self.delete_delay_timer()

        self.set_power("power_on")

        self.widget_click(self.page["control_device_page"]["delay_timer"],
                          self.page["delay_timer_roll_popup"]["title"])

        now = time.strftime("%H:%M")

        delay_time_1 = ["delay", "00:02"]
        start_time_1, set_time_1 = self.create_delay_timer(now, delay_time_1)

        time.sleep(60)

        self.widget_click(self.page["control_device_page"]["power_button"],
                          self.page["control_device_page"]["power_off"])

        self.check_timer(start_time_1, set_time_1, u"电源已关闭", same_power=True)

        self.case_over(True)
