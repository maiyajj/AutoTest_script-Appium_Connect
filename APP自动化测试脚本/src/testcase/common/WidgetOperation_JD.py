# coding=utf-8
from src.testcase.case.LaunchApp_JD import *


class WidgetOperationJD(LaunchAppJD):
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

    # 选择设备
    def choose_device(self, device, element1, element2, element3):
        while True:
            try:
                elements = self.wait_widget(element1)
                new_value = copy.copy(element2)
                for index, element in elements.items():
                    if element is not None and self.ac.get_attribute(element, "name") == device:
                        new_value[0] = new_value[0][index]
                        self.widget_click(new_value, element3)
                        raise ValueError()
                    else:
                        self.ac.swipe(0.6, 0.9, 0.6, 0.4, self.driver)
                        time.sleep(1)
            except ValueError:
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
    def set_timer_roll(self, elem_h, elem_m, elem_t, now_time, set_timer, cycle=False, delay_s=120):
        """
        :param elem_h: 滚轮控件“时”框架，用来获取“时”x坐标
        :param elem_m: 滚轮控件“分”框架，用来获取“分”x坐标
        :param elem_t: 滚轮当前的时间值，“HH:MM”格式
        :param now_timer: 设置定时的当前时间
        :param set_timer: 设置定时的目标时间
        :param cycle: 是否是类鱼缸模式的连续定时模式
        :param delay_s: 定时的设置时间和启动时间延迟
        :return: 定时启动时间，格式为时间戳float型；定时执行时间，格式为时间戳float型
        """
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

        # 时滚轮
        lcx_h, lcy_h, szw_h, szh_h = self.set_roll(elem_h)
        pxx_h, pxy_h = elem_h[3]["px"]
        aszh_h = int(szh_h / 5 * 4 / 5)  # 根据滚轮显示时间点滚条个数计算单个时间点滚条的元素宽度，默认为5
        start_x_h, start_y_h = int(lcx_h + pxx_h * szw_h), int(lcy_h + szh_h / 2)  # “时”滚轮的操作起始点
        # 分滚轮
        lcx_m, lcy_m, szw_m, szh_m = self.set_roll(elem_m)
        pxx_m, pxy_m = elem_m[3]["px"]
        aszh_m = int(szh_m / 5 * 4 / 5)
        start_x_m, start_y_m = int(lcx_m + pxx_m * szw_m), int(lcy_m + szh_m / 2)  # “分”滚轮的操作起始点

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
        if cycle is True:  # 若定时为鱼缸模式，第二个定时的开始时间为第一个定时的结束时间，应将定时设置延迟去除
            time_now = time_now - delay_s

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
        swipe = self.ac.swipe
        swipe_time = conf["roll_time"]["JD"]
        while time_et_m_a > 0:
            swipe(start_x_m, start_y_m, start_x_m, end_y_m, self.driver, 0, False)
            print time_et_m_a
            time_et_m_a -= 1
            time.sleep(swipe_time)
        while time_et_h_a > 0:
            swipe(start_x_h, start_y_h, start_x_h, end_y_h, self.driver, 0, False)
            print time_et_h_a
            time_et_h_a -= 1
            time.sleep(swipe_time)

        self.logger.info("start_time: %s, set_time: %s" % (start_time, set_time))
        if self.ac.get_attribute(self.wait_widget(elem_t), "name") == set_time[11:16]:
            return time_start, time_set
        else:
            raise TimeoutException("timer set error")

    # 创建普通定时
    def create_normal_timer(self, now_time, delay_time, power, delay_s=120, loop=u"执行一次"):
        '''

        :param now_time: now time
        :param delay_time: delay time
        :param power: power state power on/off
        :param loop: everyday/monday etc
        :return: start_time, set_time
        '''
        self.widget_click(self.page["normal_timer_page"]["add_timer"],
                          self.page["add_normal_timer_page"]["title"])

        start_time, start_set_time = self.set_timer_roll(self.page["add_normal_timer_page"]["roll_h"],
                                                         self.page["add_normal_timer_page"]["roll_m"],
                                                         self.page["add_normal_timer_page"]["set_timer"],
                                                         delay_time, now_time, delay_s=delay_s)
        now = time.mktime(time.strptime(time.strftime("%Y-%m-%d r:00").replace("r", now_time), "%Y-%m-%d %X"))

        if start_set_time <= now:
            start_set_time = start_set_time + 3600 * 24
        self.logger.info("[APP_TIMER]Start_time: %s, Start_set_time: %s" % (
            time.strftime("%Y-%m-%d %X", time.localtime(start_time)),
            time.strftime("%Y-%m-%d %X", time.localtime(start_set_time))))

        self.widget_click(self.page["add_normal_timer_page"][power],
                          self.page["add_normal_timer_page"]["title"])

        cycle = self.set_timer_loop("add_normal_timer_page", loop)

        if cycle == ["None"]:
            cycle = [time.strftime("%A", time.localtime(start_set_time)).lower()]

        self.widget_click(self.page["add_normal_timer_page"]["saved"],
                          self.page["normal_timer_page"]["title"])
        self.logger.info(u"[APP_TIMER]Start Time: %s[%s]" % (time.strftime("%X"), time.time()))

        return start_time, start_set_time

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
                     u"永久循环": "forever"}

        attribute = self.ac.get_attribute(self.wait_widget(self.page[page]["repeat"]), "name")
        if isinstance(loop, list):
            tmp = " ".join(loop)
        else:
            tmp = loop
        if tmp not in attribute:
            self.widget_click(self.page[page]["repeat"],
                              self.page["timer_repeat_page"]["title"])
            if loop == u"执行一次":
                self.widget_click(self.page["timer_repeat_page"]["repeat_button"],
                                  self.page["timer_repeat_page"]["once"])
                cycle = ["None"]
            elif loop == u"永久循环":
                self.widget_click(self.page["timer_repeat_page"]["fish_repeat_button"],
                                  self.page["timer_repeat_page"]["forever"])
                cycle = [u"0次"]
            else:
                try:
                    self.wait_widget(self.page["timer_repeat_page"]["everyday"])
                except TimeoutException:
                    self.widget_click(self.page["timer_repeat_page"]["repeat_button"],
                                      self.page["timer_repeat_page"]["everyday"])

                try:
                    self.wait_widget(self.page["timer_repeat_page"]["monday"])
                except TimeoutException:
                    self.widget_click(self.page["timer_repeat_page"]["define"],
                                      self.page["timer_repeat_page"]["monday"])

                if isinstance(loop, list):
                    for i in loop:
                        self.widget_click(self.page["timer_repeat_page"][loop_mode[i]],
                                          self.page["timer_repeat_page"]["title"])
                    cycle = [loop_mode[i] for i in loop]
                else:
                    self.widget_click(self.page["timer_repeat_page"][loop_mode[loop]],
                                      self.page["timer_repeat_page"]["title"])
                    cycle = [loop_mode[loop]]

            self.widget_click(self.page["timer_repeat_page"]["to_return"],
                              self.page[page]["title"])
            attribute = self.ac.get_attribute(self.wait_widget(self.page[page]["repeat"]), "name")
            if tmp not in attribute:
                raise TimeoutException("Cycle set error")
        else:
            if loop == u"执行一次":
                cycle = ["None"]
            elif loop == u"永久循环":
                cycle = [u"0次"]
            elif isinstance(loop, list):
                cycle = [loop_mode[i] for i in loop]
            else:
                cycle = [loop_mode[loop]]
        return cycle

    # 定时检查模板
    def check_timer(self, start_time, set_time, power_state, cycle):
        # 开始时间, 设置时间
        start_times = time.strftime("%Y-%m-%d %X", time.localtime(start_time))
        self.logger.info("[APP_CHECK_TIMER]Now time: %s. Start time: %s" % (time.strftime("%Y-%m-%d %X"), start_times))
        now_week = time.strftime("%A").lower()
        if cycle is None:
            set_week = now_week
        else:
            if len(cycle) == 1:
                set_week = cycle[0]
            else:
                set_week = ",".join(cycle)
        self.logger.info("[APP_CHECK_TIMER]Now week: %s, Set week: %s" % (now_week, set_week))
        i = 0
        while True:
            now_week = time.strftime("%A").lower()
            if now_week in set_week:
                tmp = time.strftime("%Y-%m-%d ")
                tmp = tmp + time.strftime("%X", time.localtime(set_time))
                set_times = int(time.mktime(time.strptime(tmp, "%Y-%m-%d %X")))
                break
            else:
                if time.strftime("%M") == "00":
                    self.logger.info("now week: %s" % now_week)
                else:
                    print("********************")
                    print("now week: %s" % now_week)
                    print("********************")
                    try:
                        self.driver.tap([(10, 10)])
                    except BaseException:
                        i += 1
                        if i == 3:
                            raise TimeoutException("tap error!")
                    time.sleep(1)

        delay_times = set_times - start_time
        self.logger.info("[APP_CHECK_TIMER]Delay Time: %s" % delay_times)
        if delay_times < 0:
            raise TimeoutException("Set time is before now time, delay time is: %s" % delay_times)

        element = self.wait_widget(self.page["control_device_page"]["power_state"])
        end_time = set_times + 30
        self.logger.info("[APP_CHECK_TIMER]End Time: %s" % time.strftime("%Y-%m-%d %X", time.localtime(end_time)))
        self.logger.info("[APP_CHECK_TIMER]Set Time: %s" % time.strftime("%Y-%m-%d %X", time.localtime(set_times)))
        while True:
            current_time = int(time.time())
            if current_time >= set_times:
                while True:
                    state = self.ac.get_attribute(element, "name")
                    if state == power_state:
                        self.logger.info("[APP_CHECK_TIMER]Current Time: %s" % time.strftime("%Y-%m-%d %X"))
                        self.logger.info("[APP_CHECK_TIMER]Device Info: %s" % power_state)
                        break
                    else:
                        time.sleep(1)
                        print "[APP_CHECK_TIMER]In Time %s" % time.strftime("%Y-%m-%d %X")
                        if time.time() > end_time:
                            raise TimeoutException("Device state Error, current: %s" % state)
                break
            else:
                time.sleep(1)
                print "[APP_CHECK_TIMER]Out Time %s" % time.strftime("%Y-%m-%d %X")

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

    # 启动模式定时
    def launch_mode_timer(self, page, start_now, start_time=None):
        if not isinstance(start_now, bool):
            raise KeyError("start_now must be bool type")
        if start_now == True:
            try:
                self.widget_click(self.page[page]["launch"],
                                  self.page["mode_timer_page"]["title"])
                self.logger.info(u"[APP_TIMER]Start Time: %s[%s]" % (time.strftime("%X"), time.time()))
            except TimeoutException:
                self.wait_widget(self.page["mode_timer_conflict_popup"]["title"])
                self.widget_click(self.page["mode_timer_conflict_popup"]["confirm"],
                                  self.page["mode_timer_page"]["title"])
        else:
            if start_time is None:
                raise KeyError("if start_now is False, start_time can`t be None type")
            end_time = time.time() + 5 * 60 + 30
            while True:
                if time.strftime("%H:%M") == start_time:
                    try:
                        self.widget_click(self.page[page]["launch"],
                                          self.page["mode_timer_page"]["title"])
                        self.logger.info(u"[APP_TIMER]Start Time: %s[%s]" % (time.strftime("%X"), time.time()))
                    except TimeoutException:
                        self.wait_widget(self.page["mode_timer_conflict_popup"]["title"])
                        self.widget_click(self.page["mode_timer_conflict_popup"]["confirm"],
                                          self.page["mode_timer_page"]["title"])
                    break
                else:
                    if time.time() > end_time:
                        raise TimeoutException("Timer Saved Error, time: %s" % start_time)
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
                    try:
                        self.driver.tap([(10, 10)])
                    except BaseException:
                        self.debug.error("tap 10, 10 error")
                    time.sleep(30)

            self.widget_click(self.page["control_device_page"]["elec_bill"],
                              self.page["elec_bill_page"]["title"])

            elec_bill_elements = self.wait_widget(self.page["elec_bill_page"]["price_time"])
            elec_bill_value = copy.copy(self.page["elec_bill_page"]["price_value"])
            for index, element in elec_bill_elements.items():
                if element is not None:
                    elec_bill_value[0] = self.page["elec_bill_page"]["price_value"][0][index]
                    # if index >= now_h + 2:
                    elec_bill[index] = self.ac.get_attribute(elec_bill_value, "name")
            self.logger.info("[APP_INFO]23:01_elec_bill: %s" % elec_bill)

            self.widget_click(self.page["elec_bill_page"]["to_return"],
                              self.page["control_device_page"]["title"])

            self.widget_click(self.page["control_device_page"]["elec"],
                              self.page["elec_page"]["title"])

            elec_elements = self.wait_widget(self.page["elec_page"]["elec_time"])
            elec_value = copy.copy(self.page["elec_page"]["elec_value"])
            for index, element in elec_elements.items():
                if element is not None:
                    elec_value[0] = self.page["elec_page"]["elec_value"][0][index]
                    # if index >= now_h + 2:
                    elec[index] = self.ac.get_attribute(elec_value, "name")
            self.logger.info("[APP_INFO]23:01_elec: %s" % elec)

            self.widget_click(self.page["elec_page"]["to_return"],
                              self.page["control_device_page"]["title"])

        while True:
            if int(time.strftime("%H")) == check_time:
                time.sleep(60)
                break
            else:
                try:
                    self.driver.tap([(10, 10)])
                except BaseException:
                    self.debug.error("tap 10, 10 error")
                time.sleep(60)

        self.widget_click(self.page["control_device_page"]["elec_bill"],
                          self.page["elec_bill_page"]["title"])

        elec_bill_elements = self.wait_widget(self.page["elec_bill_page"]["price_time"])
        for index, element in elec_bill_elements.items():
            if element is not None:
                elec_bill_value[0] = self.page["elec_bill_page"]["price_value"][0][index]
                # if index <= now_h + 1:
                elec_bill[index] = self.ac.get_attribute(elec_bill_value, "name")
        self.logger.info("[APP_INFO]%02d:01_elec_bill: %s" % (check_time, elec_bill))

        self.widget_click(self.page["elec_bill_page"]["to_return"],
                          self.page["control_device_page"]["title"])

        self.widget_click(self.page["control_device_page"]["elec"],
                          self.page["elec_page"]["title"])

        elec_elements = self.wait_widget(self.page["elec_page"]["elec_time"])
        for index, element in elec_elements.items():
            if element is not None:
                elec_value[0] = self.page["elec_page"]["elec_value"][0][index]
                # if index <= now_h + 1:
                elec[index] = self.ac.get_attribute(elec_value, "name")
        self.logger.info("[APP_INFO]%02d:01_elec: %s" % (check_time, elec))

        self.widget_click(self.page["elec_page"]["to_return"],
                          self.page["control_device_page"]["title"])

        return elec, elec_bill

    # 密码框显示密码
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
