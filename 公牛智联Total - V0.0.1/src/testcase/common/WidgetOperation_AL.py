# coding=utf-8
from src.testcase.case.LaunchApp_AL import *


class WidgetOperationAL(LaunchAppAL):
    # 主页面选择待测设备
    def choose_home_device(self, device, device_index=None):
        if device_index is None:
            index = self.get_index(device, self.page["app_home_page"]["device"])
        else:
            index = device_index
        new_value = copy.copy(self.page["app_home_page"]["device"])
        new_value[0] = new_value[0][index]
        end_time = time.time() + 30
        while True:
            try:
                self.widget_click(new_value, self.page["control_device_page"]["title"], 3, 10)
                break
            except TimeoutException:
                self.ac.swipe(0.6, 0.9, 0.6, 0.6, self.driver)
                time.sleep(1)

                if time.time() > end_time:
                    raise TimeoutException("choose_home_device timeout!")

    # 获取元素索引
    def get_index(self, device, element1):
        while True:
            elements = self.wait_widget(element1)
            for index, element in elements.items():
                if element is not None and self.ac.get_attribute(element, "name") == device:
                    return index

    # 选择元素
    def get_home_power_element(self, device, device_index=None):
        if device_index is None:
            index = self.get_index(device, self.page["app_home_page"]["device"])
        else:
            index = device_index
        new_value = copy.copy(self.page["app_home_page"]["device_button"])
        new_value[0] = new_value[0][index]
        end_time = time.time() + 30
        while True:
            if self.wait_widget(new_value).location["y"] < self.driver.get_window_size()["height"]:
                return new_value
            else:
                self.ac.swipe(0.6, 0.9, 0.6, 0.6, self.driver)
                time.sleep(1)

                if time.time() > end_time:
                    raise TimeoutException("choose_home_power timeout!")

    # 获取电源状态
    def get_power_state(self, device, device_index=None):
        if device_index is None:
            index = self.get_index(device, self.page["app_home_page"]["device"])
        else:
            index = device_index
        new_value = copy.copy(self.page["app_home_page"]["device_state"])
        new_value[0] = new_value[0][index]
        attribute = self.ac.get_attribute(self.wait_widget(new_value), "name")
        return attribute

    # 设置电源状态
    def set_power(self, device, state):
        index = self.get_index(device, self.page["app_home_page"]["device"])
        device_button = self.get_home_power_element(device, index)
        power_state_start = self.get_power_state(device, index)
        if state == "power_on":
            end_time = time.time() + 30
            while True:
                self.widget_click(device_button, self.page["app_home_page"]["device"])
                power_state = self.get_power_state(device, index)
                if power_state == u"开":
                    break
                else:
                    time.sleep(1)

                    if time.time() > end_time:
                        raise TimeoutException("set_power power on timeout!")
        elif state == "power_off":
            end_time = time.time() + 30
            while True:
                self.widget_click(device_button, self.page["app_home_page"]["device"])
                power_state = self.get_power_state(device, index)
                if power_state != power_state_start:
                    break
                else:
                    time.sleep(1)

                    if time.time() > end_time:
                        raise TimeoutException("set_power power off 1 timeout!")
            end_time = time.time() + 30
            while True:
                self.widget_click(device_button, self.page["app_home_page"]["device"])
                power_state = self.get_power_state(device, index)
                if power_state == u"关":
                    break
                else:
                    time.sleep(1)

                    if time.time() > end_time:
                        raise TimeoutException("set_power power off 2 timeout!")

    # 设置滚轮
    def set_roll(self, elem):
        element = self.wait_widget(elem)
        lc, sz = element.location, element.size
        lcx, lcy, szw, szh = float(lc["x"]), float(lc["y"]), float(sz["width"]), float(sz["height"])
        return lcx, lcy, szw, szh

    # 设置定时滚轮
    def set_timer_roll(self, elem_e, elem_h, elem_m, elem_t, now_time, set_timer, cycle=False, delay_s=120):
        """
        :param elem_e:
        :param elem_h:
        :param elem_m:
        :param elem_t:
        :param now_timer:
        :param set_timer:
        :param cycle:
        :param delay_m:
        :param delay_s:
        :return:
        """
        if isinstance(set_timer, int):
            if set_timer >= 0:
                time_seg = "int"
            else:
                time_seg = "minus"
        else:
            if set_timer[0] == "point":
                time_seg = "point"
            elif set_timer[0] == "delay":
                time_seg = "delay"
            else:
                time_seg = None
        if not isinstance(now_time, str):
            raise KeyError("now time must be time.strftime, current: %s" % str(now_time))
        # 滚轮
        lcx_e, lcy_e, szw_e, szh_e = self.set_roll(elem_e)
        # 时滚轮
        lcx_h, lcy_h, szw_h, szh_h = self.set_roll(elem_h)
        pxx_h, pxy_h = elem_h[3]["px"]
        aszh_h = int(szh_e / 5)
        start_x_h, start_y_h = int(lcx_h + pxx_h * szw_h), int(lcy_e + szh_e / 2)
        # 分滚轮
        lcx_m, lcy_m, szw_m, szh_m = self.set_roll(elem_m)
        pxx_m, pxy_m = elem_m[3]["px"]
        aszh_m = int(szh_e / 5)
        start_x_m, start_y_m = int(lcx_m + pxx_m * szw_m), int(lcy_e + szh_e / 2)

        time_roll = time.strftime("%Y-%m-%d r:00").replace("r", elem_t)
        time_roll = time.mktime(time.strptime(time_roll, "%Y-%m-%d %H:%M:%S"))

        try:
            time_now = time.strptime(time.strftime("%Y-%m-%d r:00").replace("r", now_time), "%Y-%m-%d %H:%M:%S")
        except ValueError:
            time_now = time.strptime(time.strftime("%Y-%m-%d r").replace("r", now_time), "%Y-%m-%d %H:%M:%S")
        time_now = time.mktime(time_now)
        if cycle is True:
            time_now = time_now - delay_s

        if time_seg == "int":
            time_set = time_now + set_timer * 60 + delay_s
            time_true = time_set
        elif time_seg == "minus":
            time_set = time_now + set_timer * 60
            time_true = time_set
        elif time_seg == "point":
            time_set = time.strftime("%Y-%m-%d r:00").replace("r", set_timer[1])
            time_set = time.mktime(time.strptime(time_set, "%Y-%m-%d %H:%M:%S"))
            time_true = time_set
        elif time_seg == "delay":
            time_set = time.strftime("%Y-%m-%d r:00").replace("r", set_timer[1])
            time_set = time.mktime(time.strptime(time_set, "%Y-%m-%d %H:%M:%S"))
            time_true = time_set + delay_s
        else:
            time_set = "error"
            time_true = time_set

        time_start = time_now + delay_s
        start_time = time.strftime("%H:%M:%S", time.localtime(time_start))
        set_time = time.strftime("%H:%M:%S", time.localtime(time_set))
        true_time = time.strftime("%H:%M:%S", time.localtime(time_true))

        time_et = time_set - time_roll
        time_et_a = abs(time_et)
        try:
            end_y_h = start_y_h - time_et / time_et_a * aszh_h
        except ZeroDivisionError:
            end_y_h = start_y_h
        try:
            end_y_m = start_y_m - time_et / time_et_a * aszh_m
        except ZeroDivisionError:
            end_y_m = start_y_m
        time_et_h, time_et_m = time_et_a / 3600, time_et_a / 60

        # 分钟在前，时钟在后，若为00:00，滚轮会自动加一
        while time_et_m > 0:
            self.driver.swipe(start_x_m, start_y_m, start_x_m, end_y_m, 0)
            time_et_m -= 1
        while time_et_h > 0:
            self.driver.swipe(start_x_h, start_y_h, start_x_h, end_y_h, 0)
            time_et_h -= 1

        self.logger.info("start_time: %s, set_time: %s, true_time: %s" % (start_time, set_time, true_time))

        time.sleep(2)

        return start_time, true_time

    # 设置次数滚轮
    def set_count_roll(self, elem, roll_value, set_value):
        # 滚轮
        lcx, lcy, szw, szh = self.set_roll(elem)
        pxx, pxy = elem[3]["px"]
        aszh = int(szh / 5)
        start_x, start_y = int(lcx + pxx * szw), int(lcy + pxy * szh)

        diff = set_value - roll_value
        diff_a = abs(diff)
        try:
            end_y = start_y - diff / diff_a * aszh
        except ZeroDivisionError:
            end_y = start_y
        while diff_a > 0:
            self.driver.swipe(start_x, start_y, start_x, end_y, 0)
            diff_a -= 1

        self.logger.info("roll_value: %s, set_value: %s" % (roll_value, set_value))

        time.sleep(2)

    # 创建普通定时
    def create_normal_timer(self, now_time, set_timer, power, loop, delay_s=120):
        """
        :param now_time:
        :param set_timer:
        :param power:
        :param loop:
        :param delay_s:
        :return:
        """
        self.widget_click(self.page["normal_timer_page"]["add_normal_timer"],
                          self.page["add_normal_timer_page"]["title"])

        start_time, set_time = self.set_timer_roll(self.page["add_normal_timer_page"]["roll"],
                                                   self.page["add_normal_timer_page"]["roll_h"],
                                                   self.page["add_normal_timer_page"]["roll_m"],
                                                   "14:30", now_time, set_timer, delay_s=delay_s)

        self.widget_click(self.page["add_normal_timer_page"][power],
                          self.page["add_normal_timer_page"]["title"])

        self.set_timer_loop("add_normal_timer_page", loop)

        self.widget_click(self.page["add_normal_timer_page"]["saved"],
                          self.page["normal_timer_page"]["title"])
        self.logger.info(u"[APP_TIMER]Start Time:%s[%s]" % (time.strftime("%H:%M:%S"), time.time()))

        return start_time, set_time

    # 创建延时定时
    def create_delay_timer(self, now_time, set_timer, power, delay_s=120, cycle=False):
        """
        :param now_time:
        :param set_timer:
        :param power:
        :param delay_s:
        :param start_delay:
        :return:
        """
        self.widget_click(self.page["delay_timer_page"]["launch"],
                          self.page["delay_timer_page"]["close"])

        time_roll = self.ac.get_attribute(self.wait_widget(self.page["delay_timer_page"]["delay_time"]), "name")

        self.widget_click(self.page["delay_timer_page"]["close"],
                          self.page["delay_timer_page"]["launch"])

        try:
            time_now = time.strptime(time.strftime("%Y-%m-%d r:00").replace("r", now_time), "%Y-%m-%d %H:%M:%S")
        except ValueError:
            time_now = time.strptime(time.strftime("%Y-%m-%d r").replace("r", now_time), "%Y-%m-%d %H:%M:%S")
        time_now = time.strftime("%H:%M:%S", time.localtime(time_now))

        self.widget_click(self.page["delay_timer_page"][power],
                          self.page["delay_timer_page"]["title"])

        start_time, set_time = self.set_timer_roll(self.page["delay_timer_page"]["roll"],
                                                   self.page["delay_timer_page"]["roll_h"],
                                                   self.page["delay_timer_page"]["roll_m"],
                                                   time_roll, time_now, set_timer, cycle, delay_s)

        end_time = time.time() + 1 * 60 + 30
        while True:
            if time.strftime("%H:%M:%S") == start_time:
                self.widget_click(self.page["delay_timer_page"]["launch"],
                                  self.page["delay_timer_page"]["close"], times=2)
                self.logger.info(u"[APP_TIMER]Start Time:%s[%s]" % (time.strftime("%H:%M:%S"), time.time()))
                break
            else:
                if time.time() > end_time:
                    raise TimeoutException("Timer Saved Error, time:%s" % start_time)
                time.sleep(1)

    # 创建循环定时
    def create_cycle_timer(self, page, now_time, set_start_time, set_end_time, loop, delay_s=120, cycle=False, loops=0):
        """
        :param now_time:
        :param set_start_time:
        :param set_end_time:
        :param loop:
        :param delay_s:
        :param start_delay:
        :return:
        """
        start_roll = self.ac.get_attribute(self.wait_widget(self.page[page]["start_time"]), "name")
        end_roll = self.ac.get_attribute(self.wait_widget(self.page[page]["end_time"]), "name")

        tmp = re.findall(u"(\d+)小时", start_roll)
        if tmp == []:
            start_roll_h = 0
        else:
            start_roll_h = int(tmp[0])
        start_roll_m = int(re.findall(u"(\d+)分钟", start_roll)[0])
        start_roll = "%02d:%02d" % (start_roll_h, start_roll_m)

        tmp = re.findall(u"(\d+)小时", end_roll)
        if tmp == []:
            end_roll_h = 0
        else:
            end_roll_h = int(tmp[0])
        end_roll_m = int(re.findall(u"(\d+)分钟", end_roll)[0])
        end_roll = "%02d:%02d" % (end_roll_h, end_roll_m)

        try:
            time_now = time.strptime(time.strftime("%Y-%m-%d r:00").replace("r", now_time), "%Y-%m-%d %H:%M:%S")
        except ValueError:
            time_now = time.strptime(time.strftime("%Y-%m-%d r").replace("r", now_time), "%Y-%m-%d %H:%M:%S")
        time_now = time.strftime("%H:%M:%S", time.localtime(time_now))

        self.widget_click(self.page[page]["start_time"],
                          self.page["timer_roll_popup"]["title"])

        start_time, start_set_time = self.set_timer_roll(self.page["timer_roll_popup"]["roll"],
                                                         self.page["timer_roll_popup"]["roll_h"],
                                                         self.page["timer_roll_popup"]["roll_m"],
                                                         start_roll, time_now, set_start_time, cycle, delay_s)

        self.widget_click(self.page["timer_roll_popup"]["confirm"],
                          self.page[page]["launch"])

        self.widget_click(self.page[page]["end_time"],
                          self.page["timer_roll_popup"]["title"])

        end_time, end_set_time = self.set_timer_roll(self.page["timer_roll_popup"]["roll"],
                                                     self.page["timer_roll_popup"]["roll_h"],
                                                     self.page["timer_roll_popup"]["roll_m"],
                                                     end_roll, start_set_time, set_end_time, True)

        self.widget_click(self.page["timer_roll_popup"]["confirm"],
                          self.page[page]["launch"])

        sr_h, sr_m = start_roll.split(":")
        sr = int(sr_h) * 3600 + int(sr_m) * 60
        er_h, er_m = end_roll.split(":")
        er = int(er_h) * 3600 + int(er_m) * 60
        if loop == u"永久循环":
            loop_count = loops
        else:
            loop_count = int(re.findall(u"(\d+)次", self.set_timer_loop(page, loop))[0])

        loop_list = [[start_time, start_set_time, end_time, end_set_time]]
        es_time = time.strftime("%Y-%m-%d r").replace("r", end_set_time)
        tmp = time.mktime(time.strptime(es_time, "%Y-%m-%d %H:%M:%S"))
        tmp_s = time.strftime("%H:%M:%S", time.localtime(tmp))
        for i in xrange(loop_count):
            tmp = tmp + sr
            s_time = time.strftime("%H:%M:%S", time.localtime(tmp))
            tmp_e = s_time
            tmp = tmp + er
            e_time = time.strftime("%H:%M:%S", time.localtime(tmp))
            loop_list.append([tmp_s, s_time, tmp_e, e_time])
            tmp_s = e_time

        end_time = time.time() + 1 * 60 + 30
        while True:
            if time.strftime("%H:%M:%S") == start_time:
                self.widget_click(self.page[page]["launch"],
                                  self.page[page]["close"], times=2)
                self.logger.info(u"[APP_TIMER]Start Time:%s[%s]" % (time.strftime("%H:%M:%S"), time.time()))
                break
            else:
                if time.time() > end_time:
                    raise TimeoutException("Timer Saved Error, time:%s" % start_time)
                time.sleep(1)

        return loop_list

    # 创建热水器类型模式
    def create_point_mode_timer(self, page, now_time, set_start_time, set_end_time, loop, delay_s=120, exchange=False):
        """
        :param now_time:
        :param set_timer:
        :param power:
        :param loop:
        :param delay_s:
        :return:
        """
        start_roll = self.ac.get_attribute(self.wait_widget(self.page[page]["start_time"]), "name")
        end_roll = self.ac.get_attribute(self.wait_widget(self.page[page]["end_time"]), "name")

        try:
            time_now = time.strptime(time.strftime("%Y-%m-%d r:00").replace("r", now_time), "%Y-%m-%d %H:%M:%S")
        except ValueError:
            time_now = time.strptime(time.strftime("%Y-%m-%d r").replace("r", now_time), "%Y-%m-%d %H:%M:%S")
        time_now = time.strftime("%H:%M:%S", time.localtime(time_now))

        if exchange is True:
            self.widget_click(self.page[page]["time_exchange"],
                              self.page[page]["title"])

        self.widget_click(self.page[page]["start_time"],
                          self.page["timer_roll_popup"]["title"])

        start_time, start_set_time = self.set_timer_roll(self.page["timer_roll_popup"]["roll"],
                                                         self.page["timer_roll_popup"]["roll_h"],
                                                         self.page["timer_roll_popup"]["roll_m"],
                                                         start_roll, time_now, set_start_time, delay_s=delay_s)

        self.widget_click(self.page["timer_roll_popup"]["confirm"],
                          self.page[page]["launch"])

        self.widget_click(self.page[page]["end_time"],
                          self.page["timer_roll_popup"]["title"])

        end_time, end_set_time = self.set_timer_roll(self.page["timer_roll_popup"]["roll"],
                                                     self.page["timer_roll_popup"]["roll_h"],
                                                     self.page["timer_roll_popup"]["roll_m"],
                                                     end_roll, time_now, set_end_time, delay_s=delay_s)

        self.widget_click(self.page["timer_roll_popup"]["confirm"],
                          self.page[page]["launch"])

        self.set_timer_loop(page, loop)

        self.widget_click(self.page[page]["launch"],
                          self.page[page]["close"])

        return [start_time, start_set_time], [end_time, end_set_time]

    # 创建充电保护类型模式
    def create_delay_mode_timer(self, page, now_time, set_timer, delay_s=120, cycle=False):
        """
        :param now_time:
        :param set_timer:
        :param power:
        :param delay_s:
        :param start_delay:
        :return:
        """
        time_roll = self.ac.get_attribute(self.wait_widget(self.page[page]["end_time"]), "name")

        tmp = re.findall(u"(\d+)小时", time_roll)
        if tmp == []:
            time_roll_h = 0
        else:
            time_roll_h = int(tmp[0])
        time_roll_m = int(re.findall(u"(\d+)分钟", time_roll)[0])
        time_roll = "%02d:%02d" % (time_roll_h, time_roll_m)

        try:
            time_now = time.strptime(time.strftime("%Y-%m-%d r:00").replace("r", now_time), "%Y-%m-%d %H:%M:%S")
        except ValueError:
            time_now = time.strptime(time.strftime("%Y-%m-%d r").replace("r", now_time), "%Y-%m-%d %H:%M:%S")
        time_now = time.strftime("%H:%M:%S", time.localtime(time_now))

        start_time, set_time = self.set_timer_roll(self.page["timer_roll_popup"]["roll"],
                                                   self.page["timer_roll_popup"]["roll_h"],
                                                   self.page["timer_roll_popup"]["roll_m"],
                                                   time_roll, time_now, set_timer, cycle, delay_s)

        end_time = time.time() + 1 * 60 + 30
        while True:
            if time.strftime("%H:%M:%S") == start_time:
                self.widget_click(self.page[page]["launch"],
                                  self.page[page]["close"], times=2)
                self.logger.info(u"[APP_TIMER]Start Time:%s[%s]" % (time.strftime("%H:%M:%S"), time.time()))
                break
            else:
                if time.time() > end_time:
                    raise TimeoutException("Timer Saved Error, time:%s" % start_time)
                time.sleep(1)

    # 设置普通/模式定时循环模式
    def set_timer_loop(self, page, loop):
        loop_mode = {u"永不": "once",
                     u"每天": "everyday",
                     u"工作日": "workday",
                     u"周一": "monday",
                     u"周二": "tuesday",
                     u"周三": "wednesday",
                     u"周四": "thursday",
                     u"周五": "friday",
                     u"周六": "saturday",
                     u"周日": "weekday"}

        attribute = self.ac.get_attribute(self.wait_widget(self.page[page]["repeat"]), "name")
        if isinstance(loop, list):
            tmp = u"、".join(loop)
        else:
            tmp = loop
        if tmp not in attribute:
            self.widget_click(self.page[page]["repeat"],
                              self.page["timer_repeat_page"]["title"])
            if loop == u"永不":
                self.widget_click(self.page["timer_repeat_page"]["once"],
                                  self.page["timer_repeat_page"]["title"])
            elif loop == u"永久循环":
                if u"永久循环" in attribute:
                    roll = 0
                else:
                    roll = int(re.findall(u"(\d+)次", attribute)[0])
                self.set_count_roll(self.page["timer_repeat_page"]["cycle_count"], roll, 0)
            elif u"周" in loop or u"每天" in loop or u"工作日" in loop:
                if u"每天" in loop:
                    attribute = [u"周一", u"周二", u"周三", u"周四", u"周五", u"周六", u"周日"]
                elif u"工作日" in loop:
                    attribute = [u"周一", u"周二", u"周三", u"周四", u"周五"]
                if u"永不" in attribute:
                    cycle = ["once"]
                else:
                    cycle = re.findall(u"(周.+?)、", attribute)  # ["周四", "周五"] ["周三"，"周四"]  ["周三"，"周五"]

                if isinstance(loop, list):
                    loop_tmp = (set(cycle) | set(loop)) - (set(cycle) & set(loop))
                else:
                    loop_tmp = [loop]
                    loop_tmp = (set(cycle) | set(loop_tmp)) - (set(cycle) & set(loop_tmp))
                try:
                    loop_tmp.remove("once")
                except KeyError:
                    pass
                for i in loop_tmp:
                    self.widget_click(self.page["timer_repeat_page"][loop_mode[i]],
                                      self.page["timer_repeat_page"]["title"])
            else:
                if u"永久循环" in attribute:
                    roll = 0
                else:
                    roll = int(re.findall(u"(\d+)次", attribute)[0])
                loop_tmp = int(re.findall(u"(\d+)次", loop)[0])
                self.set_count_roll(self.page["timer_repeat_page"]["cycle_count"], roll, loop_tmp)

            self.widget_click(self.page["timer_repeat_page"]["saved"],
                              self.page[page]["title"])
            attribute = self.ac.get_attribute(self.wait_widget(self.page[page]["repeat"]), "name")
            if tmp not in attribute:
                raise TimeoutException("Cycle set error")

        return loop

    # 设置峰谷电时间
    def set_peak_valley_time(self, elem, now_time, set_timer, peak):
        attribute = self.ac.get_attribute(elem, "name")
        if u"未设置" in attribute:
            if peak is True:
                time_roll = "08:00"
            else:
                time_roll = "22:00"
        else:
            time_roll = re.findall("(\d+:\d+)", attribute)[0]

        start_time, set_time = self.set_timer_roll(self.page["delay_timer_page"]["roll"],
                                                   self.page["delay_timer_page"]["roll_h"],
                                                   self.page["delay_timer_page"]["roll_m"],
                                                   time_roll, now_time, set_timer, False, 120)

        return start_time, set_time

    # 定时检查模板
    def check_timer(self, device, start_time, set_time, power_state, power_same_prev=False, sec=True):
        start_h, start_m, start_s = start_time.split(":")
        start_times = int(start_h) * 60 + int(start_m)
        now = time.mktime(time.strptime(time.strftime("%Y-%m-%d r").replace("r", start_time), "%Y-%m-%d %H:%M:%S"))
        self.logger.info("[APP_TIMER]Now Time:%s. Start Time:%s" % (time.strftime("%H:%M:%S"), now))

        set_h, set_m, set_s = set_time.split(":")
        set_times = int(set_h) * 60 + int(set_m)

        if start_times < set_times:
            delay_times = (set_times - start_times) * 60
        else:
            delay_times = 24 * 60 * 60 + (set_times - start_times) * 60
        self.logger.info("[APP_TIMER]Delay Time:%s" % (delay_times + 30))

        index = self.get_index(device, self.page["app_home_page"]["device"])
        element = copy.copy(self.page["app_home_page"]["power_state"])
        element[0] = element[0][index]
        element = self.wait_widget(element)
        end_time = now + delay_times + 30
        flag = False
        while True:
            if sec is True:
                if time.strftime("%H:%M:%S") == set_time:
                    flag = True
            else:
                if time.strftime("%H:%M") == set_time[:5]:
                    flag = True
            if flag is True:
                now = time.time()
                if power_same_prev is True:
                    time.sleep(10)
                while True:
                    if self.ac.get_attribute(element, "name") == power_state:
                        self.logger.info("[APP_TIMER]End Time:%s[%s]" % (time.strftime("%H:%M:%S"), now))
                        self.logger.info(u"[APP_INFO]Device Info:%s" % power_state)
                        break
                break
            else:
                if time.time() > end_time:
                    raise TimeoutException("Device state Error")
                time.sleep(1)
                # if not isinstance(args, list):
                #     raise KeyError("args must list! Current %s" % str(args))
                # time_list = []
                # for start_time, set_time, power_state in args:
                #     start_h, start_m = start_time.split(":")
                #     start_times = int(start_h) * 60 + int(start_m)
                #     set_h, set_m = set_time.split(":")
                #     set_times = int(set_h) * 60 + int(set_m)
                #     if start_times < set_times:
                #         delay_times = (set_times - start_times) * 60
                #     else:
                #         delay_times = 24 * 60 * 60 + (set_times - start_times) * 60
                #     time_list.append([start_time, set_time, delay_times, power_state])
                # self.logger.info("[APP_TIMER]Time List:%s" % str(time_list))
                # while True:
                #     if time.strftime("%H:%M") == start_time:
                #         now = time.time()
                #         break
                #     else:
                #         time.sleep(1)
                # self.logger.info("[APP_TIMER]Now Time:%s" % time.strftime("%H:%M:%S"))
                # element = self.wait_widget(self.page["control_device_page"]["power_state"])
                # while True:
                #     if time.strftime("%H:%M") == set_time:
                #         while True:
                #             if self.ac.get_attribute(element, "name") == power_state:
                #                 self.logger.info(
                #                     "[APP_TIMER]End Time:%s[%s]" % (time.strftime("%H:%M:%S"), time.time()))
                #                 self.logger.info(u"[APP_INFO]Device Info:%s" % power_state)
                #                 break
                #             else:
                #                 time.sleep(1)
                #         break
                #     else:
                #         if time.time() < now + delay_times + 30:
                #             time.sleep(1)
                #         else:
                #             raise TimeoutException("Device state Error")

    # 删除普通定时
    def delete_normal_timer(self):
        end_time = time.time() + 120
        while True:
            try:
                self.wait_widget(self.page["normal_timer_page"]["no_timer"], 5)
                self.logger.info("It has normal timer.")
                self.widget_click(self.page["normal_timer_page"]["timer_edit"],
                                  self.page["normal_timer_page"]["delete_timer"])

                self.widget_click(self.page["normal_timer_page"]["delete"],
                                  self.page["normal_timer_page"]["title"])
                try:
                    self.wait_widget(self.page["normal_timer_page"]["no_timer"], 5)
                except TimeoutException:
                    self.logger.info("It has no timer~")
                    break
            except TimeoutException:
                time.sleep(1)
                if time.time() > end_time:
                    raise TimeoutException("delete_normal_timer timeout, time limit: 120S")

    # 关闭模式定时
    def close_mode_timer(self):
        element = self.wait_widget(self.page["control_device_page"]["launch_mode"])
        while True:
            attribute = self.ac.get_attribute(element, "name")
            if u"模式" in attribute:
                self.logger.info("[APP_INFO]Mode timer is run")
                if u"热水器模式" in attribute:
                    self.widget_click(self.page["control_device_page"]["water_mode_timer"],
                                      self.page["water_mode_timer_page"]["title"])

                    self.widget_click(self.page["water_mode_timer_page"]["close"],
                                      self.page["water_mode_timer_page"]["launch"], times=2)

                    self.widget_click(self.page["water_mode_timer_page"]["to_return"],
                                      self.page["control_device_page"]["title"])
                elif u"小夜灯模式" in attribute:
                    self.widget_click(self.page["control_device_page"]["night_mode_timer"],
                                      self.page["night_mode_timer_page"]["title"])

                    self.widget_click(self.page["night_mode_timer_page"]["close"],
                                      self.page["night_mode_timer_page"]["launch"], times=2)

                    self.widget_click(self.page["night_mode_timer_page"]["to_return"],
                                      self.page["control_device_page"]["title"])
                elif u"鱼缸模式" in attribute:
                    self.widget_click(self.page["control_device_page"]["fish_mode_timer"],
                                      self.page["fish_mode_timer_page"]["title"])

                    self.widget_click(self.page["fish_mode_timer_page"]["close"],
                                      self.page["fish_mode_timer_page"]["launch"], times=2)

                    self.widget_click(self.page["fish_mode_timer_page"]["to_return"],
                                      self.page["control_device_page"]["title"])
                elif u"电蚊香模式" in attribute:
                    self.widget_click(self.page["control_device_page"]["mosquito_mode_timer"],
                                      self.page["mosquito_mode_timer_page"]["title"])

                    self.widget_click(self.page["mosquito_mode_timer_page"]["close"],
                                      self.page["mosquito_mode_timer_page"]["launch"], times=2)

                    self.widget_click(self.page["mosquito_mode_timer_page"]["to_return"],
                                      self.page["control_device_page"]["title"])
                elif u"充电保护模式" in attribute:
                    self.widget_click(self.page["control_device_page"]["piocc_mode_timer"],
                                      self.page["piocc_mode_timer_page"]["title"])

                    self.widget_click(self.page["piocc_mode_timer_page"]["close"],
                                      self.page["piocc_mode_timer_page"]["launch"], times=2)

                    self.widget_click(self.page["piocc_mode_timer_page"]["to_return"],
                                      self.page["control_device_page"]["title"])
                else:
                    self.widget_click(self.page["control_device_page"]["warmer_mode_timer"],
                                      self.page["warmer_mode_timer_page"]["title"])

                    self.widget_click(self.page["warmer_mode_timer_page"]["close"],
                                      self.page["warmer_mode_timer_page"]["launch"], times=2)

                    self.widget_click(self.page["warmer_mode_timer_page"]["to_return"],
                                      self.page["control_device_page"]["title"])
            else:
                self.logger.info("[APP_INFO]Mode timer don't run")
                break

    # 关闭定时任务
    def close_general_timer(self):
        element = self.wait_widget(self.page["control_device_page"]["launch_mode"])
        while True:
            attribute = self.ac.get_attribute(element, "name")
            if u"任务开" not in attribute:
                self.logger.info("[APP_INFO]Normal timer is run")
                if u"定时任务开" in attribute:
                    self.widget_click(self.page["control_device_page"]["normal_timer"],
                                      self.page["normal_timer_page"]["title"])

                    self.delete_normal_timer()

                    self.widget_click(self.page["normal_timer_page"]["to_return"],
                                      self.page["control_device_page"]["title"])
                elif u"延时任务开" in attribute:
                    self.widget_click(self.page["control_device_page"]["delay_timer"],
                                      self.page["delay_timer_page"]["title"])

                    self.widget_click(self.page["delay_timer_page"]["close"],
                                      self.page["delay_timer_page"]["launch"])

                    self.widget_click(self.page["delay_timer_page"]["to_return"],
                                      self.page["control_device_page"]["title"])
                else:
                    self.ac.swipe(0.6, 0.9, 0.6, 0.6, self.driver)
                    self.widget_click(self.page["control_device_page"]["cycle_timer"],
                                      self.page["cycle_timer_page"]["title"])

                    self.widget_click(self.page["cycle_timer_page"]["close"],
                                      self.page["cycle_timer_page"]["launch"])

                    self.widget_click(self.page["cycle_timer_page"]["to_return"],
                                      self.page["control_device_page"]["title"])
            else:
                self.logger.info("[APP_INFO]Normal timer don't run")
                break
    # 启动模式定时
    def launch_mode_timer(self, page, start_now, start_time=None):
        if not isinstance(start_now, bool):
            raise KeyError("start_now must be bool type")
        if start_now is True:
            try:
                self.widget_click(self.page[page]["launch"],
                                  self.page["mode_timer_page"]["title"])
                self.logger.info(u"[APP_TIMER]Start Time:%s[%s]" % (time.strftime("%H:%M:%S"), time.time()))
            except TimeoutException:
                self.wait_widget(self.page["mode_timer_conflict_popup"]["title"])
                self.widget_click(self.page["mode_timer_conflict_popup"]["confirm"],
                                  self.page["mode_timer_page"]["title"])
        else:
            if start_time is None:
                raise KeyError("if start_now is False, start_time can`t be None type")
            end_time = time.time() + 1 * 60 + 30
            while True:
                if time.strftime("%H:%M") == start_time:
                    try:
                        self.widget_click(self.page[page]["launch"],
                                          self.page["mode_timer_page"]["title"])
                        self.logger.info(u"[APP_TIMER]Start Time:%s[%s]" % (time.strftime("%H:%M:%S"), time.time()))
                    except TimeoutException:
                        self.wait_widget(self.page["mode_timer_conflict_popup"]["title"])
                        self.widget_click(self.page["mode_timer_conflict_popup"]["confirm"],
                                          self.page["mode_timer_page"]["title"])
                    break
                else:
                    if time.time() > end_time:
                        raise TimeoutException("Timer Saved Error, time:%s" % start_time)
                    time.sleep(1)

    # 统计电量
    def get_device_elect(self, check_time, across=False):
        now_h = int(time.strftime("%H"))
        if across is False:
            if now_h + 2 <= 23:
                across_day = False
            else:
                across_day = True
        else:
            across_day = True
        elec = {}
        elec_bill = {}

        if across_day is True:
            while True:
                if int(time.strftime("%H")) == 23:
                    time.sleep(60)
                    break
                else:
                    self.driver.tap([(10, 10)])
                    time.sleep(30)

            self.widget_click(self.page["control_device_page"]["elec"],
                              self.page["elec_page"]["title"])

            self.ac.swipe(0.5, 0.7, 0.5, 0.4, self.driver)

            self.widget_click(self.page["elec_page"]["more_elec_history"],
                              self.page["more_elec_history_page"]["title"])

            today = time.strftime("%m月%d日").decode("utf")
            day_list = self.wait_widget(self.page["more_elec_history_page"]["day_elec"])
            new_value = copy.copy(self.page["more_elec_history_page"]["day_elec"])
            for index, element in day_list.items():
                if element is not None and str(self.ac.get_attribute(element, "name")) == today:
                    new_value[0] = new_value[0][index]
                    while True:
                        try:
                            self.widget_click(new_value, self.page["day_elec_page"]["title"])
                            break
                        except TimeoutException:
                            self.ac.swipe(0.6, 0.9, 0.6, 0.6, self.driver)
                            time.sleep(1)
                break

            elec_bill_elements = self.wait_widget(self.page["day_elec_page"]["elec_time"])
            elec_bill_value = copy.copy(self.page["day_elec_page"]["elec_value"])
            for index, element in elec_bill_elements.items():
                if element is not None:
                    elec_bill_value[0] = self.page["day_elec_page"]["elec_value"][0][index]
                    elec_bill[index] = int(re.findall("(\d+)W", self.ac.get_attribute(elec_bill_value, "name"))[0])
                    self.logger.info("[APP_INFO]23:01_elec_bill:%s" % str(elec_bill))

            self.widget_click(self.page["day_elec_page"]["to_return"],
                              self.page["more_elec_history_page"]["title"])

            self.widget_click(self.page["more_elec_history_page"]["to_return"],
                              self.page["elec_page"]["title"])

            self.widget_click(self.page["elec_page"]["to_return"],
                              self.page["control_device_page"]["title"])

        while True:
            if int(time.strftime("%H")) == check_time:
                time.sleep(60)
                break
            else:
                self.driver.tap([(10, 10)])
                time.sleep(60)

        self.widget_click(self.page["control_device_page"]["elec_bill"],
                          self.page["elec_bill_page"]["title"])

        elec_bill_elements = self.wait_widget(self.page["elec_bill_page"]["price_time"])
        for index, element in elec_bill_elements.items():
            if element is not None:
                elec_bill_value[0] = self.page["elec_bill_page"]["price_value"][0][index]
                # if index <= now_h + 1:
                elec_bill[index] = self.ac.get_attribute(elec_bill_value, "name")
                self.logger.info("[APP_INFO]%02d:01_elec_bill:%s" % (check_time, str(elec_bill)))

        self.widget_click(self.page["elec_bill_page"]["to_return"],
                          self.page["control_device_page"]["title"])

        self.widget_click(self.page["control_device_page"]["elec"],
                          self.page["elec_page"]["title"])

        self.widget_click(self.page["elec_page"]["to_return"],
                          self.page["control_device_page"]["title"])

        return elec, elec_bill

    # 密码框显示密码
    def show_pwd(self, element, element1=None, param="name", state="false"):
        while True:
            try:
                if self.ac.get_attribute(element, param) == state:
                    break
                else:
                    if element1 is None:
                        element.click()
                    else:
                        element1.click()
            except BaseException:
                self.debug.error(traceback.format_exc())
