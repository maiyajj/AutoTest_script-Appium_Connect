# coding=utf-8
from ReadAPPElement import *


class fix(a):
    # 创建延时类型定时
    def set_peak_valley_time(self, elem, now_time, set_timer, peak):
        attribute = self.ac.get_attribute(elem, "name")
        if u"未设置" in attribute:
            if peak is True:  # 峰电/谷电
                time_roll = "08:00"
            else:
                time_roll = "22:00"
        else:
            time_roll = re.findall("(\d+:\d+)", attribute)[0]
        print("[APP_TIMER]Start roll: %s" % time_roll)

        if peak is True:  # 峰电/谷电
            widget = "start_time"
        else:
            widget = "end_time"

        self.widget_click(self.page["peak_valley_price_page"][widget],
                          self.page["timer_roll_popup"]["title"])

        start_time, set_time = self.set_timer_roll(self.page["timer_roll_popup"]["roll_p"],
                                                   self.page["timer_roll_popup"]["roll_p_h"],
                                                   self.page["timer_roll_popup"]["roll_p_m"],
                                                   time_roll, now_time, set_timer, False, 0)

        self.widget_click(self.page["timer_roll_popup"]["confirm"],
                          self.page["peak_valley_price_page"]["title"])

        return start_time, set_time


class b(fix):
    def case(self):
        device = "C4:11:E0:00:00:00"
        now = time.strftime("%H:%M")

        delay_time_1, delay_time_2 = ["point", "08:00"], ["delay", "22:00"]
        elem = self.wait_widget(self.page["peak_valley_price_page"]["start_time"])
        tmp, tmp1 = self.set_peak_valley_time(elem, now, delay_time_1, True)
        print tmp, tmp1


b().case()
