# coding=utf-8
from src.testcase.common.WidgetOperation_HW import *


class HWAppNormalTimer2(WidgetOperationHW):
    @case_run(False)
    def run(self):
        self.case_module = u"普通定时(#246)"  # 用例所属模块
        self.case_title = u'在线状态，4组开与4组关按自定义方式执行的定时执行状态检查'  # 用例名称
        self.zentao_id = 2064  # 禅道ID

    # 用例动作
    def case(self):
        self.choose_home_device(conf["MAC"]["HW"][0])

        self.delete_normal_timer()

        self.delete_delay_timer()

        self.set_power("power_off")

        self.widget_click(self.page["control_device_page"]["normal_timer"],
                          self.page["normal_timer_page"]["title"])

        now = time.strftime("%H:%M")

        delay_time_1 = ["point", "09:00"]
        start_time_1, set_time_1, cycle1 = self.create_normal_timer(now, time_on=delay_time_1,
                                                                    loop=[u"周一", u"周三", u"周五"])

        delay_time_2 = ["point", "10:00"]
        start_time_2, set_time_2, cycle2 = self.create_normal_timer(now, time_off=delay_time_2,
                                                                    loop=[u"周一", u"周三", u"周五"])

        delay_time_3 = ["point", "11:00"]
        start_time_3, set_time_3, cycle3 = self.create_normal_timer(now, time_on=delay_time_3,
                                                                    loop=[u"周一", u"周三", u"周五"])

        delay_time_4 = ["point", "12:00"]
        start_time_4, set_time_4, cycle4 = self.create_normal_timer(now, time_off=delay_time_4,
                                                                    loop=[u"周一", u"周三", u"周五"])

        delay_time_5 = ["point", "13:00"]
        start_time_5, set_time_5, cycle5 = self.create_normal_timer(now, time_on=delay_time_5,
                                                                    loop=[u"周一", u"周三", u"周五"])

        delay_time_6 = ["point", "14:00"]
        start_time_6, set_time_6, cycle6 = self.create_normal_timer(now, time_off=delay_time_6,
                                                                    loop=[u"周一", u"周三", u"周五"])

        delay_time_7 = ["point", "15:00"]
        start_time_7, set_time_7, cycle7 = self.create_normal_timer(now, time_on=delay_time_7,
                                                                    loop=[u"周一", u"周三", u"周五"])

        delay_time_8 = ["point", "16:00"]
        start_time_8, set_time_8, cycle8 = self.create_normal_timer(now, time_off=delay_time_8,
                                                                    loop=[u"周一", u"周三", u"周五"])

        self.widget_click(self.page["normal_timer_page"]["to_return"],
                          self.page["control_device_page"]["title"])

        self.check_timer(start_time_1, set_time_1, u"电源已开启", cycle1)
        self.check_timer(start_time_2, set_time_2, u"电源已关闭", cycle2)
        self.check_timer(start_time_3, set_time_3, u"电源已开启", cycle3)
        self.check_timer(start_time_4, set_time_4, u"电源已关闭", cycle4)
        self.check_timer(start_time_5, set_time_5, u"电源已开启", cycle5)
        self.check_timer(start_time_6, set_time_6, u"电源已关闭", cycle6)
        self.check_timer(start_time_7, set_time_7, u"电源已开启", cycle7)
        self.check_timer(start_time_8, set_time_8, u"电源已关闭", cycle8)

        self.case_over(True)
