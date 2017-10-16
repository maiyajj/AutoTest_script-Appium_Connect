# coding=utf-8
from src.testcase.case.LaunchApp_AL import *


class WidgetOperationAL(LaunchAppAL):
    # 设置定时滚轮
    def set_timer_roll(self, elem_h, elem_m, elem_t, et, now_time, same_fish_mode=False, leave_time=2):
        if isinstance(et, int):
            if et >= 0:
                time_seg = "int"
            else:
                time_seg = "minus"
        else:
            if et[0] == "point":
                time_seg = "point"
            elif et[0] == "delay":
                time_seg = "delay"
            else:
                time_seg = None
        # 时滚轮
        element_h = self.wait_widget(elem_h)
        pxx_h, pxy_h = elem_h[3]["px"]
        lc_h, sz_h = element_h.location, element_h.size
        lcx_h, lcy_h, szw_h, szh_h = float(lc_h["x"]), float(lc_h["y"]), float(sz_h["width"]), float(sz_h["height"])
        aszh_h = int(szh_h / 5)
        start_x_h, start_y_h = int(lcx_h + pxx_h * szw_h), int(lcy_h + pxy_h * szh_h)
        # 分滚轮
        element_m = self.wait_widget(elem_m)
        pxx_m, pxy_m = elem_m[3]["px"]
        lc_m, sz_m = element_m.location, element_m.size
        lcx_m, lcy_m, szw_m, szh_m = float(lc_m["x"]), float(lc_m["y"]), float(sz_m["width"]), float(sz_m["height"])
        aszh_m = int(szh_m / 5)
        start_x_m, start_y_m = int(lcx_m + pxx_m * szw_m), int(lcy_m + pxy_m * szh_m)

        roll_now_h, roll_now_m = self.ac.get_attribute(self.wait_widget(elem_t), "name").split(":")
        roll_now_h, roll_now_m = int(roll_now_h), int(roll_now_m)
        if roll_now_h == 0 and roll_now_m == 1:
            self.driver.swipe(start_x_h, start_y_h, start_x_h, start_y_h - aszh_h, 0)
            roll_now_h, roll_now_m = self.ac.get_attribute(self.wait_widget(elem_t), "name").split(":")
            roll_now_h, roll_now_m = int(roll_now_h), int(roll_now_m)

        now_h, now_m = now_time.split(":")
        if same_fish_mode is False:
            now_h, now_m = int(now_h), int(now_m)
        else:
            now_h, now_m = int(now_h), int(now_m) - leave_time
            now_h, now_m = (now_h + now_m / 60) % 24, now_m % 60

        if time_seg == "int":
            aet = abs(et)
            sign_aet = et / aet
            set_h, set_m = now_h + sign_aet * (aet / 60), now_m + leave_time + sign_aet * (aet % 60)
            set_h, set_m = (set_h + set_m / 60) % 24, set_m % 60
            true_h, true_m = set_h, set_m
        elif time_seg == "minus":
            aet = abs(et)
            sign_aet = et / aet
            set_h, set_m = now_h + sign_aet * (aet / 60), now_m + sign_aet * (aet % 60)
            set_h, set_m = (set_h + set_m / 60) % 24, set_m % 60
            true_h, true_m = set_h, set_m
        elif time_seg == "point":
            set_h, set_m = et[1].split(":")
            set_h, set_m = int(set_h), int(set_m)
            true_h, true_m = set_h, set_m
        elif time_seg == "delay":
            set_h, set_m = et[1].split(":")
            set_h, set_m = int(set_h), int(set_m)
            true_h, true_m = int(set_h) + now_h, int(set_m) + leave_time + now_m
            true_h, true_m = (true_h + true_m / 60) % 24, true_m % 60
        else:
            set_h, set_m = "error", "error"
            true_h, true_m = set_h, set_m

        start_h, start_m = (now_h + (now_m + leave_time) / 60) % 24, (now_m + leave_time) % 60
        start_time = "%02d:%02d" % (start_h, start_m)
        set_time = "%02d:%02d" % (set_h, set_m)
        true_time = "%02d:%02d" % (true_h, true_m)

        et_h = abs(set_h - roll_now_h)
        et_m = abs(set_m - roll_now_m)
        try:
            end_y_h = start_y_h - (set_h - roll_now_h) / et_h * aszh_h
        except ZeroDivisionError:
            end_y_h = start_y_h
        try:
            end_y_m = start_y_m - (set_m - roll_now_m) / et_m * aszh_m
        except ZeroDivisionError:
            end_y_m = start_y_m
        # 分钟在前，时钟在后，若为00:00，滚轮会自动加一
        while et_m > 0:
            self.driver.swipe(start_x_m, start_y_m, start_x_m, end_y_m, 0)
            et_m -= 1
        while et_h > 0:
            self.driver.swipe(start_x_h, start_y_h, start_x_h, end_y_h, 0)
            et_h -= 1

        self.logger.info("start_time: %s, set_time: %s, true_time: %s" % (start_time, set_time, true_time))
        if self.ac.get_attribute(self.wait_widget(elem_t), "name") == set_time:
            return start_time, true_time
        else:
            raise TimeoutException("timer set error")

    # 定时检查模板，用时删减
    def check_timer(self, start_time, set_time, power_state, power_same_prev=False):
        start_h, start_m = start_time.split(":")
        start_times = int(start_h) * 60 + int(start_m)
        set_h, set_m = set_time.split(":")
        set_times = int(set_h) * 60 + int(set_m)
        if start_times < set_times:
            delay_times = (set_times - start_times) * 60
        else:
            delay_times = 24 * 60 * 60 + (set_times - start_times) * 60
        self.logger.info("[APP_TIMER]Delay Time:%s" % (delay_times + 30))
        while True:
            if time.strftime("%H:%M") == start_time:
                now = time.time()
                break
            else:
                time.sleep(1)
        self.logger.info("[APP_TIMER]Now Time:%s" % time.strftime("%H:%M:%S"))
        element = self.wait_widget(self.page["control_device_page"]["power_state"])
        while True:
            if time.strftime("%H:%M") == set_time:
                if power_same_prev is False:
                    while True:
                        if self.ac.get_attribute(element, "name") == power_state:
                            self.logger.info("[APP_TIMER]End Time:%s[%s]" % (time.strftime("%H:%M:%S"), time.time()))
                            self.logger.info(u"[APP_INFO]Device Info:%s" % power_state)
                            break
                        else:
                            time.sleep(1)
                else:
                    while True:
                        time.sleep(10)
                        if self.ac.get_attribute(element, "name") == power_state:
                            self.logger.info(
                                "[APP_TIMER]End Time:%s[%s]" % (time.strftime("%H:%M:%S"), (time.time() - 10)))
                            self.logger.info(u"[APP_INFO]Device Info:%s" % power_state)
                            break
                        else:
                            time.sleep(1)
                break
            else:
                if time.time() < now + delay_times + 30:
                    time.sleep(1)
                else:
                    raise TimeoutException("Device state Error")

    # 删除普通定时
    def delete_normal_timer(self):
        while True:
            try:
                self.wait_widget(self.page["normal_timer_page"]["no_timer"])
                self.logger.info("It has no timer~")
                break
            except TimeoutException:
                self.logger.info("It has normal timer.")
                self.widget_click(self.page["normal_timer_page"]["timer_edit"],
                                  self.page["timer_edit_popup"]["title"])

                self.widget_click(self.page["timer_edit_popup"]["delete"],
                                  self.page["normal_timer_page"]["title"])

    # 关闭模式定时
    def close_mode_timer(self):
        element = self.wait_widget(self.page["control_device_page"]["mode_timer"])
        while True:
            attribute = self.ac.get_attribute(element, "name")
            if u"未启用" not in attribute:
                self.logger.info("[APP_INFO]Mode timer is run")
                self.widget_click(self.page["control_device_page"]["mode_timer"],
                                  self.page["mode_timer_page"]["title"])

                if u"热水器模式" in attribute:
                    self.widget_click(self.page["mode_timer_page"]["water_button"],
                                      self.page["mode_timer_page"]["title"])
                elif u"鱼缸模式" in attribute:
                    self.widget_click(self.page["mode_timer_page"]["fish_button"],
                                      self.page["mode_timer_page"]["title"])
                else:
                    self.widget_click(self.page["mode_timer_page"]["piocc_button"],
                                      self.page["mode_timer_page"]["title"])

                time.sleep(5)

                self.widget_click(self.page["mode_timer_page"]["to_return"],
                                  self.page["control_device_page"]["title"])
            else:
                self.logger.info("[APP_INFO]Mode timer don't run")
                break
