# coding=utf-8
from ReadAPPElement import *


class fix(a):
    pass

a = fix


class b(a):
    def case(self):
        device = "C4:11:E0:00:00:00"

        now = time.strftime("%H:%M")

        delay_time_1 = 10
        self.create_normal_timer(now, delay_time_1, "power_on", u"永不")

        delay_time_2 = 11
        self.create_normal_timer(now, delay_time_2, "power_off", [u"周一", u"周日"])

        delay_time_3 = 12
        self.create_normal_timer(now, delay_time_3, "power_on", u"工作日")

        delay_time_4 = 13
        self.create_normal_timer(now, delay_time_4, "power_off", u"每天")

        loop_list = [[u"永不"], [u"周一", u"周日"], [u"工作日"], [u"每天"]]
        for i in loop_list:
            tmp = u"、".join(i)
            new_value = copy.copy(self.page["normal_timer_page"]["timer_loop"])
            new_value[0] = new_value[0][loop_list.index(i)]
            attribute = self.ac.get_attribute(self.wait_widget(new_value), "name")
            if tmp not in attribute:
                raise TimeoutException("loop is wrong!")


b().case()
