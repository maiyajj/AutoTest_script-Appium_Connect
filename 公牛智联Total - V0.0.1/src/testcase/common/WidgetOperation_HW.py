# coding=utf-8
from src.testcase.case.LaunchApp_HW import *


class WidgetOperationHW(LaunchAppHW):
    # 主页面选择待测设备
    def choose_home_device(self, device):
        elements = self.wait_widget(self.page["app_home_page"]["device"])
        new_value = copy.copy(self.page["app_home_page"]["device"])
        for index, element in elements.items():
            if element is not None and str(self.ac.get_attribute(element, "name")) == device:
                new_value[0] = new_value[0][index]
                while True:
                    try:
                        self.widget_click(new_value, self.page["control_device_page"]["title"])
                        break
                    except TimeoutException:
                        self.ac.swipe(0.6, 0.9, 0.6, 0.6, self.driver)
                        time.sleep(1)
            break

    # 设置电源状态
    def set_power(self, state):
        try:
            self.wait_widget(self.page["control_device_page"][state])
        except TimeoutException:
            self.widget_click(self.page["control_device_page"]["power_button"],
                              self.page["control_device_page"][state])

    # 设置滚轮
    def set_roll(self, elem):
        element = self.wait_widget(elem)
        lc, sz = element.location, element.size
        lcx, lcy, szw, szh = float(lc["x"]), float(lc["y"]), float(sz["width"]), float(sz["height"])
        return lcx, lcy, szw, szh

    # 设置定时滚轮
    def set_timer_roll(self, elem_h, elem_m, now_time, set_timer, delay_s=120):
        """
        :param elem_h: 滚轮控件“时”框架，用来获取“时”x坐标
        :param elem_m: 滚轮控件“分”框架，用来获取“分”x坐标
        :param now_timer: 设置定时的当前时间
        :param set_timer: 设置定时的目标时间
        :param delay_s: 定时的设置时间和启动时间延迟
        :return: 定时启动时间，格式为时间戳float型；定时执行时间，格式为时间戳float型
        """
        # 华为智能家居滚轮控件简单，所需元素不多。
        # 定时的设置时间包含延迟定时和准点定时：
        # 准点定时为设置定时当前时间前/后***分钟执行，数据格式为int型及以时间格式展现的str字符串型；
        # int型包含int型正数/负数（int型/负int型），用于设置当前时间***分钟前/后执行的定时，关键字为“int”，“minus”；
        # 时间格式str字符串型（"09:00"），用于设置固定时间点执行的定时，关键字为“point”
        # 延迟定时为设置时间段区间执行的定时，多用于鱼缸模式或延迟定时模式，数据格式为以时间格式展现的str字符串型；
        # 时间格式str字符串型（"30:00"），用于设置时间段定时，关键字为“delay”
        # ps：delay_s函数关键词用于给设置定时预留时间，设置定时也需要时间，默认延迟2分钟，当前时间8:00，定时开始执行时间为8:02；
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
        # 时滚轮
        lcx_h, lcy_h, szw_h, szh_h = self.set_roll(elem_h)
        pxx_h, pxy_h = elem_h[3]["px"]
        aszh_h = int(szh_h / 5)  # 根据滚轮显示时间点滚条个数计算单个时间点滚条的元素宽度，默认为5
        start_x_h, start_y_h = int(lcx_h + pxx_h * szw_h), int(lcy_h + szh_h / 2)  # “时”滚轮的操作起始点
        # 分滚轮
        lcx_m, lcy_m, szw_m, szh_m = self.set_roll(elem_m)
        pxx_m, pxy_m = elem_m[3]["px"]
        aszh_m = int(szh_m / 5)
        start_x_m, start_y_m = int(lcx_m + pxx_m * szw_m), int(lcy_m + szh_m / 2)  # “分”滚轮的操作起始点

        # 从控件拿到当前控件的值
        value_h = int(re.findall("(\d+)", self.ac.get_attribute(self.wait_widget(elem_h), "name"))[0])
        value_m = int(re.findall("(\d+)", self.ac.get_attribute(self.wait_widget(elem_m), "name"))[0])
        elem_t = "%02d:%02d" % (value_h, value_m)
        time_roll = time.strftime("%Y-%m-%d r:00").replace("r", elem_t)  # 滚轮的当前时间
        time_roll = time.mktime(time.strptime(time_roll, "%Y-%m-%d %X"))  # 转换为时间戳

        # 将now_time添加秒数。
        # 若同时设置普通定时和延迟定时，若两定时执行时间点相同，则难以判断定时执行情况
        # 将延迟模式的启动时间从准点往后推30s则可以和普通定时错开，相应的delay_s也要再加上对应的30s，默认120s→150s
        try:
            time_now = time.strptime(time.strftime("%Y-%m-%d r:00").replace("r", now_time), "%Y-%m-%d %X")
        except ValueError:
            time_now = time.strptime(time.strftime("%Y-%m-%d r").replace("r", now_time), "%Y-%m-%d %X")
        time_now = time.mktime(time_now)

        # 获取定时的执行时间点
        if time_seg == "int":
            time_set = time_now + set_timer * 60 + delay_s
        elif time_seg == "minus":
            time_set = time_now + set_timer * 60
        elif time_seg == "point":
            time_set = time.strftime("%Y-%m-%d r:00").replace("r", set_timer[1])
            time_set = time.mktime(time.strptime(time_set, "%Y-%m-%d %X"))
        elif time_seg == "delay":
            time_set = time.strftime("%Y-%m-%d r:00").replace("r", set_timer[1])
            time_set = time.mktime(time.strptime(time_set, "%Y-%m-%d %X")) + delay_s
        else:
            time_set = "error"

        # 定时开始执行和设定的时间点
        time_start = int(time_now + delay_s)
        time_set = int(time_set)
        # 将定时时间（时间戳，float型）格式化为时间（字符串型），仅做日志输出
        start_time = time.strftime("%Y-%m-%d %X", time.localtime(time_start))
        set_time = time.strftime("%Y-%m-%d %X", time.localtime(time_set))

        # 滚轮相关操作
        roll_h, roll_m = time.strftime("%H:%M", time.localtime(time_roll)).split(":")
        set_h, set_m = time.strftime("%H:%M", time.localtime(time_set)).split(":")

        time_et_h = int(set_h) - int(roll_h)  # 时间滚轮的“时”时间和待设置时间差值
        time_et_h_a = abs(time_et_h) % 24  # “时”时间滚轮滑动次数
        time_et_m = int(set_m) - int(roll_m)  # 时间滚轮的“分”时间和待设置时间差值
        time_et_m_a = abs(time_et_m) % 60  # “分”时间滚轮滑动次数

        try:  # 若time_et不相等
            # time_et / time_et_a计算结果为1/-1，获取“时”滚轮滑动目的坐标值，用于计算时间滚轮是往上滑还是往下滑
            end_y_h = start_y_h - time_et_h / time_et_h_a * aszh_h
        except ZeroDivisionError:  # 若time_et相等
            end_y_h = start_y_h
        try:
            # 获取“分”滚轮滑动目的坐标值
            end_y_m = start_y_m - time_et_m / time_et_m_a * aszh_m
        except ZeroDivisionError:
            end_y_m = start_y_m

        # 分钟在前，时钟在后，若为00:00，滚轮会自动加一
        while time_et_m_a > 0:
            self.driver.swipe(start_x_m, start_y_m, start_x_m, end_y_m, 0)
            time_et_m_a -= 1
        while time_et_h_a > 0:
            self.driver.swipe(start_x_h, start_y_h, start_x_h, end_y_h, 0)
            time_et_h_a -= 1

        self.logger.info("start_time: %s, set_time: %s" % (start_time, set_time))

        time.sleep(2)

        value_h = int(re.findall("(\d+)", self.ac.get_attribute(self.wait_widget(elem_h), "name"))[0])
        value_m = int(re.findall("(\d+)", self.ac.get_attribute(self.wait_widget(elem_m), "name"))[0])
        elem_t = "%02d:%02d" % (value_h, value_m)
        if elem_t == set_time[11:16]:
            return time_start, time_set
        else:
            raise TimeoutException("timer set error")

    # 创建普通定时
    def create_normal_timer(self, now_time, time_on=False, time_off=False, loop=u"执行一次"):
        '''
        :param now_time: now time
        :param delay_time: delay time
        :param power: power state power on/off
        :param loop: everyday/monday etc
        :return: start_time, set_time
        '''
        self.widget_click(self.page["normal_timer_page"]["add_timer"],
                          self.page["add_normal_timer_page"]["title"])

        if time_on is not False:
            self.widget_click(self.page["add_normal_timer_page"]["time_on"],
                              self.page["normal_timer_roll_popup"]["title"])

            start_time_1, set_time_1 = self.set_timer_roll(self.page["normal_timer_roll_popup"]["roll_h"],
                                                           self.page["normal_timer_roll_popup"]["roll_m"],
                                                           now_time, time_on)

            self.widget_click(self.page["normal_timer_roll_popup"]["confirm"],
                              self.page["add_normal_timer_page"]["title"])
        else:
            start_time_1, set_time_1 = None, None
            while True:
                element = self.wait_widget(self.page["add_normal_timer_page"]["button_on"])
                if self.ac.get_attribute(element, "selected") == "false":
                    self.widget_click(self.page["add_normal_timer_page"]["button_on"],
                                      self.page["add_normal_timer_page"]["title"])
                    break

        if time_off is not False:
            self.widget_click(self.page["add_normal_timer_page"]["time_off"],
                              self.page["normal_timer_roll_popup"]["title"])

            start_time_2, set_time_2 = self.set_timer_roll(self.page["normal_timer_roll_popup"]["roll_h"],
                                                           self.page["normal_timer_roll_popup"]["roll_m"],
                                                           now_time, time_off)

            self.widget_click(self.page["normal_timer_roll_popup"]["confirm"],
                              self.page["add_normal_timer_page"]["title"])
        else:
            start_time_2, set_time_2 = None, None
            while True:
                element = self.wait_widget(self.page["add_normal_timer_page"]["button_off"])
                if self.ac.get_attribute(element, "selected") == "false":
                    self.widget_click(self.page["add_normal_timer_page"]["button_off"],
                                      self.page["add_normal_timer_page"]["title"])
                    break

        self.widget_click(self.page["add_normal_timer_page"]["repeat"],
                          self.page["timer_repeat_popup"]["title"])

        self.set_timer_loop("add_normal_timer_page", loop)

        self.widget_click(self.page["add_normal_timer_page"]["saved"],
                          self.page["normal_timer_page"]["title"])
        self.logger.info(u"[APP_TIMER]Start Time: %s[%s]" % (time.strftime("%X"), time.time()))

        if time_on is False:
            return start_time_2, set_time_2
        elif time_off is False:
            return start_time_1, set_time_1
        else:
            return start_time_1, set_time_1, start_time_2, set_time_2

    # 设置普通/模式定时循环模式
    def set_timer_loop(self, page, loop):
        loop_mode = {u"执行一次": "once",
                     u"每天": "everyday",
                     u"工作日": "workday",
                     u"周一": "monday",
                     u"周二": "tuesday",
                     u"周三": "wednesday",
                     u"周四": "thursday",
                     u"周五": "friday",
                     u"周六": "saturday",
                     u"周日": "weekday",
                     u"周末": "weekend"}

        attribute = self.ac.get_attribute(self.wait_widget(self.page[page]["repeat"]), "name")
        if isinstance(loop, list):
            tmp = u"自定义"
        elif u"周" in loop and u"末" not in loop:
            tmp = u"自定义"
        else:
            tmp = loop
        if tmp not in attribute:
            self.widget_click(self.page[page]["repeat"],
                              self.page["timer_repeat_popup"]["title"])
            if loop == u"执行一次":
                self.widget_click(self.page["timer_repeat_popup"]["once"],
                                  self.page[page]["title"])
            elif loop == u"每天":
                self.widget_click(self.page["timer_repeat_popup"]["everyday"],
                                  self.page[page]["title"])
            elif loop == u"工作日":
                self.widget_click(self.page["timer_repeat_popup"]["workday"],
                                  self.page[page]["title"])
            elif loop == u"周末":
                self.widget_click(self.page["timer_repeat_popup"]["weekend"],
                                  self.page[page]["title"])
            else:
                self.widget_click(self.page["timer_repeat_popup"]["define"],
                                  self.page["timer_repeat_popup"]["confirm"])

                if isinstance(loop, list):
                    for i in loop:
                        self.widget_click(self.page["timer_repeat_popup"][loop_mode[i]],
                                          self.page["timer_repeat_popup"]["title"])
                else:
                    self.widget_click(self.page["timer_repeat_popup"][loop_mode[loop]],
                                      self.page["timer_repeat_popup"]["title"])

                self.widget_click(self.page["timer_repeat_popup"]["confirm"],
                                  self.page[page]["title"])

            attribute = self.ac.get_attribute(self.wait_widget(self.page[page]["repeat"]), "name")
            if tmp not in attribute:
                raise TimeoutException("Cycle set error")

    # 定时检查模板
    def check_timer(self, start_time, set_time, power_state, power_same_prev=False):
        if start_time is None:
            return False
        start_h, start_m = start_time.split(":")
        start_times = int(start_h) * 60 + int(start_m)
        set_h, set_m = set_time.split(":")
        set_times = int(set_h) * 60 + int(set_m)
        if start_times < set_times:
            delay_times = (set_times - start_times) * 60
        else:
            delay_times = 24 * 60 * 60 + (set_times - start_times) * 60
        self.logger.info("[APP_TIMER]Delay Time: %s" % (delay_times + 30))
        while True:
            if time.strftime("%H:%M") == start_time:
                now = time.time()
                break
            else:
                time.sleep(1)
        self.logger.info("[APP_TIMER]Now Time: %s" % time.strftime("%X"))
        element = self.wait_widget(self.page["control_device_page"]["power_state"])
        while True:
            if time.strftime("%H:%M") == set_time:
                if power_same_prev is False:
                    while True:
                        if self.ac.get_attribute(element, "name") == power_state:
                            self.logger.info("[APP_TIMER]End Time: %s[%s]" % (time.strftime("%X"), time.time()))
                            self.logger.info(u"[APP_INFO]Device Info: %s" % power_state)
                            break
                        else:
                            time.sleep(1)
                else:
                    while True:
                        time.sleep(10)
                        if self.ac.get_attribute(element, "name") == power_state:
                            self.logger.info("[APP_TIMER]End Time: %s[%s]" %
                                             (time.strftime("%X"), (time.time() - 10)))
                            self.logger.info(u"[APP_INFO]Device Info: %s" % power_state)
                            break
                        else:
                            time.sleep(1)
                break
            else:
                if time.time() > now + delay_times + 30:
                    raise TimeoutException("Device state Error")
                time.sleep(1)

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
                                  self.page["add_normal_timer_page"]["title"])

                self.widget_click(self.page["add_normal_timer_page"]["delete"],
                                  self.page["normal_timer_page"]["title"])

    # 删除普通定时
    def delete_delay_timer(self):
        while True:
            try:
                self.widget_click(self.page["control_device_page"]["delay_timer"],
                                  self.page["delay_timer_roll_popup"]["title"])

                self.wait_widget(self.page["delay_timer_roll_popup"]["stop"])
                self.logger.info("It has delay timer.")

                self.widget_click(self.page["delay_timer_roll_popup"]["stop"],
                                  self.page["control_device_page"]["title"])
            except TimeoutException:
                self.widget_click(self.page["delay_timer_roll_popup"]["cancel"],
                                  self.page["control_device_page"]["title"])
                self.logger.info("It has no timer~")
                break

    # 显示密码
    def show_pwd(self, element, element1=None, param="name", display=True):
        if display:
            while True:
                try:
                    if param == "name":
                        if self.ac.get_attribute(element, param) != "":
                            break
                        else:
                            if element1 is None:
                                element.click()
                            else:
                                element1.click()
                    else:
                        if self.ac.get_attribute(element, param) == "true":
                            break
                        else:
                            if element1 is None:
                                element.click()
                            else:
                                element1.click()

                except BaseException:
                    self.debug.error(traceback.format_exc())
        else:
            while True:
                try:
                    if param == "name":
                        if self.ac.get_attribute(element, param) == "":
                            break
                        else:
                            if element1 is None:
                                element.click()
                            else:
                                element1.click()
                    else:
                        if self.ac.get_attribute(element, param) == "false":
                            break
                        else:
                            if element1 is None:
                                element.click()
                            else:
                                element1.click()
                except BaseException:
                    self.debug.error(traceback.format_exc())
