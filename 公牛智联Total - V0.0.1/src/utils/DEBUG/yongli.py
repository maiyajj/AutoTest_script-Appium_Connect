# coding=utf-8
from ReadAPPElement import *


class fix(a):
    # 创建延时类型定时
    def check_timer1(self, device, now_time, start_time, set_time, power_state, loop=None, same_power=False, sec=True):
        # FIXME：定时的日期检测不完善，跨多天执行会有问题
        now = time.time()
        print("[APP_TIMER]Now time: %s. Start time: %s" % (time.strftime("%Y-%m-%d %X"), now_time))
        now_week = time.strftime("%A").lower()
        if loop is None:
            set_week = now_week
        else:
            if len(loop) == 1:
                set_week = loop[0]
            else:
                set_week = ",".join(loop)
        print("[APP_TIMER]Now week: %s. Set week: %s" % (now_week, set_week))
        if now_week in set_week:





        # 开始时间, 设置时间
        start_times = start_time
        set_times = set_time
        # delay_times = set_times - start_times
        # if now_time > start_time:
        #     start_times = start_time + 3600 * 24
        #     delay_times = start_times - now
        #
        # if now_time > set_time:
        #     set_times = set_time + 3600 * 24
        if now_time < start_times:
            while True:




        if now_time < set_times:
            delay_times = (set_times - start_times) * 60
        else:
            delay_times = 24 * 60 * 60 + (set_times - start_times) * 60
        print("[APP_TIMER]Delay Time: %s" % (delay_times + 30))

        index = self.get_index(device, self.page["app_home_page"]["device"])
        element = copy.copy(self.page["app_home_page"]["power_state"])
        element[0] = element[0][index]
        element = self.wait_widget(element)
        end_time = now + delay_times + 30
        flag = False
        while True:
            if sec is True:
                if time.strftime("%X") == set_time:
                    flag = True
            else:
                if time.strftime("%H:%M") == set_time[:5]:
                    flag = True
            if flag is True:
                now = time.time()
                if same_power is True:
                    time.sleep(10)
                while True:
                    if self.ac.get_attribute(element, "name") == power_state:
                        print("[APP_TIMER]End Time: %s[%s]" % (time.strftime("%X"), now))
                        print(u"[APP_INFO]Device Info: %s" % power_state)
                        break
                break
            else:
                if time.time() > end_time:
                    raise TimeoutException("Device state Error")
                time.sleep(1)


class b(fix):
    def case(self):
        device = "C4:11:E0:00:00:00"
        now = time.strftime("%H:%M")

        delay_time_1, delay_time_2 = ["point", "08:00"], ["delay", "22:00"]
        elem = self.wait_widget(self.page["peak_valley_price_page"]["start_time"])
        tmp, tmp1 = self.set_peak_valley_time(elem, now, delay_time_1, True)
        print tmp, tmp1


b().case()
