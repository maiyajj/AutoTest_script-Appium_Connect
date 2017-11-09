# coding=utf-8
from src.testcase.common.WidgetOperation_HW import *


class HWAppNormalTimer4(WidgetOperationHW):
    @case_run(False)
    def run(self):
        self.case_module = u"普通定时(#246)"  # 用例所属模块
        self.case_title = u'在线状态，4组开与4组关按工作日方式执行的定时执行状态检查'  # 用例名称
        self.zentao_id = 2062  # 禅道ID

    # 用例动作
    def case(self):
        self.choose_home_device(conf["MAC"]["HW"][0])

        self.set_power("power_off")

        self.widget_click(self.page["control_device_page"]["normal_timer"],
                          self.page["normal_timer_page"]["title"])

        self.delete_normal_timer()

        now = time.strftime("%H:%M")

        delay_time_1 = ["point", "09:00"]
        start_time_1, set_time_1 = self.create_normal_timer(now, time_on=delay_time_1, loop=u"工作日")

        delay_time_2 = ["point", "10:00"]
        start_time_2, set_time_2 = self.create_normal_timer(now, time_off=delay_time_2, loop=u"工作日")

        delay_time_3 = ["point", "11:00"]
        start_time_3, set_time_3 = self.create_normal_timer(now, time_on=delay_time_3, loop=u"工作日")

        delay_time_4 = ["point", "12:00"]
        start_time_4, set_time_4 = self.create_normal_timer(now, time_off=delay_time_4, loop=u"工作日")

        delay_time_5 = ["point", "13:00"]
        start_time_5, set_time_5 = self.create_normal_timer(now, time_on=delay_time_5, loop=u"工作日")

        delay_time_6 = ["point", "14:00"]
        start_time_6, set_time_6 = self.create_normal_timer(now, time_off=delay_time_6, loop=u"工作日")

        delay_time_7 = ["point", "15:00"]
        start_time_7, set_time_7 = self.create_normal_timer(now, time_on=delay_time_7, loop=u"工作日")

        delay_time_8 = ["point", "16:00"]
        start_time_8, set_time_8 = self.create_normal_timer(now, time_off=delay_time_8, loop=u"工作日")

        self.widget_click(self.page["normal_timer_page"]["to_return"],
                          self.page["control_device_page"]["title"])

        self.check_timer(start_time_1, set_time_1, "power_on")
        self.check_timer(start_time_2, set_time_2, "power_off")
        self.check_timer(start_time_3, set_time_3, "power_on")
        self.check_timer(start_time_4, set_time_4, "power_off")
        self.check_timer(start_time_5, set_time_5, "power_on")
        self.check_timer(start_time_6, set_time_6, "power_off")
        self.check_timer(start_time_7, set_time_7, "power_on")
        self.check_timer(start_time_8, set_time_8, "power_off")

        self.case_over(True)
