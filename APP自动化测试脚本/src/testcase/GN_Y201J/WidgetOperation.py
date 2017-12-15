# coding=utf-8
from src.testcase.GN_Y201J.LaunchApp import *


class WidgetOperation(LaunchApp):
    # 获取元素索引
    def get_index(self, device, element1):
        while True:
            elements = self.wait_widget(element1)  # 返回元素字典
            for index, element in elements.items():
                if element is not None and self.ac.get_attribute(element, "name") == device:
                    return index

    # 主页面选择待测设备
    def choose_home_device(self, device, device_index=None):
        if device_index is None:
            index = self.get_index(device, self.page["app_home_page"]["device"])
        else:
            index = device_index

        new_value = copy.copy(self.page["app_home_page"]["device"])
        new_value[0] = new_value[0][index]
        while True:
            try:
                self.widget_click(new_value, self.page["control_device_page"]["title"])
                break
            except TimeoutException:
                self.ac.swipe(0.6, 0.9, 0.6, 0.6, self.driver)
                time.sleep(1)

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
        swipe_time = conf["roll_time"]["JD"]  # 京东微联APP的滚轮滑动间隔时间
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
            raise KeyError("now time must be time.strftime('%%H:%%M'), current: %s" % str(now_time))

        # 获取“时”“分”滚轮滑动的基准值
        """"""
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
        """"""

        # 从控件拿到当前控件的值
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
        if time_seg == "int" or time_seg == "minus":
            time_set = time_now + set_timer * 60 + delay_s
        elif time_seg == "point" or time_seg == "delay":
            time_set = time.strftime("%Y-%m-%d r:00").replace("r", set_timer[1])
            time_set = time.mktime(time.strptime(time_set, "%Y-%m-%d %X"))
        else:
            time_set = "error"

        # 定时开始执行和设定的时间点
        time_start = time_now + delay_s
        time_set = time_set

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
        while time_et_m_a > 0:
            swipe(start_x_m, start_y_m, start_x_m, end_y_m, self.driver, 0, False)
            print(time_et_m_a)
            time_et_m_a -= 1
            time.sleep(swipe_time)
        while time_et_h_a > 0:
            swipe(start_x_h, start_y_h, start_x_h, end_y_h, self.driver, 0, False)
            print(time_et_h_a)
            time_et_h_a -= 1
            time.sleep(swipe_time)

        # 将定时时间（时间戳，float型）格式化为时间（字符串型），仅做日志输出
        start_time = time.strftime("%Y-%m-%d %X", time.localtime(time_start))

        # 延时定时的滚轮时间和实际执行时间不一致，需转换一下
        if time_seg == "delay":
            delay_time = set_timer[1]
            add_h, add_m = delay_time.split(":")
            time_delay = int(add_h) * 3600 + int(add_m) * 60
            time_set = time_now + time_delay + delay_s
            set_time = time.strftime("%Y-%m-%d %X", time.localtime(time_set))
        else:
            delay_time = "None"
            time_delay = "None"
            set_time = time.strftime("%Y-%m-%d %X", time.localtime(time_set))
        self.logger.info("[APP_TIMER]start_time: %s, set_time: %s, delay_time: %s" % (start_time, set_time, delay_time))
        self.logger.info("[APP_TIMER]time_start: %s, time_set: %s, time_delay: %s" % (time_start, time_set, time_delay))
        time.sleep(1)

        # 判断设置后的滚轮是否与设定一致
        if self.ac.get_attribute(self.wait_widget(elem_t), "name") == set_time[11:16]:
            pass
        else:
            raise TimeoutException("timer set error")

        return int(time_start), int(time_set)

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
                                                         now_time, delay_time, delay_s=delay_s)
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

        return start_time, start_set_time, cycle

    # 创建热水器类型模式
    def create_water_mode_timer(self, now_time, set_start_time, set_end_time, loop, delay_s=120):
        """与创建普通定时相同
        return: ([start_time, start_set_time], [end_time, end_set_time])
        """
        self.widget_click(self.page["water_mode_timer_page"]["start_time"],
                          self.page["water_mode_timer_page"]["roll_h"])

        start_time, start_set_time = self.set_timer_roll(self.page["water_mode_timer_page"]["roll_h"],
                                                         self.page["water_mode_timer_page"]["roll_m"],
                                                         self.page["water_mode_timer_page"]["start_time_text"],
                                                         now_time, set_start_time, delay_s=delay_s)
        now = time.mktime(time.strptime(time.strftime("%Y-%m-%d r:00").replace("r", now_time), "%Y-%m-%d %X"))

        if start_set_time <= now:
            start_set_time = start_set_time + 3600 * 24
        self.logger.info("[APP_TIMER]Start_time: %s, Start_set_time: %s" % (
            time.strftime("%Y-%m-%d %X", time.localtime(start_time)),
            time.strftime("%Y-%m-%d %X", time.localtime(start_set_time))))

        self.widget_click(self.page["water_mode_timer_page"]["start_time"],
                          self.page["water_mode_timer_page"]["title"])

        self.widget_click(self.page["water_mode_timer_page"]["end_time"],
                          self.page["water_mode_timer_page"]["end_h"])

        end_time, end_set_time = self.set_timer_roll(self.page["water_mode_timer_page"]["end_h"],
                                                     self.page["water_mode_timer_page"]["end_m"],
                                                     self.page["water_mode_timer_page"]["end_time_text"],
                                                     now_time, set_end_time, delay_s=delay_s)
        now = time.mktime(time.strptime(time.strftime("%Y-%m-%d r:00").replace("r", now_time), "%Y-%m-%d %X"))

        if end_set_time <= now:
            end_set_time = end_set_time + 3600 * 24

        if end_set_time <= start_set_time:
            end_set_time = end_set_time + 3600 * 24
        self.logger.info("[APP_TIMER]End_time: %s, End_set_time: %s" % (
            time.strftime("%Y-%m-%d %X", time.localtime(end_time)),
            time.strftime("%Y-%m-%d %X", time.localtime(end_set_time))))

        self.widget_click(self.page["water_mode_timer_page"]["end_time"],
                          self.page["water_mode_timer_page"]["title"])

        cycle = self.set_timer_loop("water_mode_timer_page", loop)
        if cycle == ["None"]:
            cycle = [time.strftime("%A", time.localtime(start_set_time)).lower()]

        self.launch_mode_timer("water_mode_timer_page", True)

        return [[start_time, start_set_time], [end_time, end_set_time]], cycle

    # 创建鱼缸，充电保护类型模式
    def create_delay_mode_timer(self, now_time, set_timer, delay_s=120, cycle=False):
        """与创建延迟定时相同
       return: None
       """
        start_time, start_set_time = self.set_timer_roll(self.page["piocc_mode_timer_page"]["end_h"],
                                                         self.page["piocc_mode_timer_page"]["end_m"],
                                                         self.page["piocc_mode_timer_page"]["end_time_text"],
                                                         now_time, set_timer, cycle, delay_s)
        self.logger.info("[APP_TIMER]Start_time: %s, Start_set_time: %s" % (
            time.strftime("%Y-%m-%d %X", time.localtime(start_time)),
            time.strftime("%Y-%m-%d %X", time.localtime(start_set_time))))

        self.widget_click(self.page["piocc_mode_timer_page"]["end_time"],
                          self.page["piocc_mode_timer_page"]["title"])

        self.launch_mode_timer("piocc_mode_timer_page", False, start_time)

        return start_time, start_set_time

    # 创建循环定时
    def create_fish_timer(self, now_time, set_start_time, set_end_time, loop, delay_s=120, cycle=False, loops=1):
        """
        :param page: 定时模式，鱼缸模式/循环模式...etc
        :param now_time: 当前时间
        :param set_start_time: 启动时间时长
        :param set_end_time: 关闭时间时长
        :param loop: 循环模式
        :param delay_s: 定时设定与执行时间差
        :param cycle: 是否是类鱼缸模式的连续定时模式
        :param loops: 循环为永久循环时需要产出的时间对个数
        :return:
        """
        self.widget_click(self.page["fish_mode_timer_page"]["start_time"],
                          self.page["fish_mode_timer_page"]["roll_h"])

        start_time, start_set_time = self.set_timer_roll(self.page["fish_mode_timer_page"]["roll_h"],
                                                         self.page["fish_mode_timer_page"]["roll_m"],
                                                         self.page["fish_mode_timer_page"]["start_time_text"],
                                                         now_time, set_start_time)
        self.logger.info("[APP_TIMER]Start_time: %s, Start_set_time: %s" % (
            time.strftime("%Y-%m-%d %X", time.localtime(start_time)),
            time.strftime("%Y-%m-%d %X", time.localtime(start_set_time))))

        self.widget_click(self.page["fish_mode_timer_page"]["start_time"],
                          self.page["fish_mode_timer_page"]["title"])

        self.widget_click(self.page["fish_mode_timer_page"]["end_time"],
                          self.page["fish_mode_timer_page"]["end_h"])

        end_time, end_set_time = self.set_timer_roll(self.page["fish_mode_timer_page"]["end_h"],
                                                     self.page["fish_mode_timer_page"]["end_m"],
                                                     self.page["fish_mode_timer_page"]["end_time_text"],
                                                     now_time, set_end_time, True)
        self.logger.info("[APP_TIMER]End_time: %s, End_set_time: %s" % (
            time.strftime("%Y-%m-%d %X", time.localtime(end_time)),
            time.strftime("%Y-%m-%d %X", time.localtime(end_set_time))))

        self.widget_click(self.page["fish_mode_timer_page"]["end_time"],
                          self.page["fish_mode_timer_page"]["title"])

        # 设定循环次数
        set_loop = self.set_timer_loop("fish_mode_timer_page", loop)[0]
        self.logger.info("[APP_TIMER]Set loop: %s" % set_loop)
        if loop == u"永久循环":
            loop_count = loops  # 生成指定数量的时间对个数
        else:
            loop_count = int(re.findall(u"(\d+)次", set_loop)[0])  # 同时设置循环模式
        # 延迟时间段长度，30分钟为1800s，在上一段定时结束后加上1800s就是下一段定时执行时间点
        start_period = start_set_time - start_time
        end_period = end_set_time - end_time

        # [[power_on开启时间，power_on关闭时间，power_off开启时间，power_off关闭时间]...]
        # power_on关闭时间 = power_off开启时间
        loop_list = [[start_time, start_set_time, end_time, end_set_time]]
        # 第一组定时执行完毕时间
        on_start = end_set_time  # 下一组定时的power_on开启时间，等于上一组定时power_off关闭的时间
        for i in xrange(loop_count - 1):
            on_end = on_start + start_period  # power_on关闭时间
            off_start = on_end  # power_off开启时间
            off_end = off_start + end_period  # power_off关闭时间
            loop_list.append([on_start, on_end, off_start, off_end])  # 写入列表
            on_start = off_end  # 下一组power_on开启时间

        self.launch_mode_timer("fish_mode_timer_page", False, start_time)

        return loop_list

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
        cycle = ["None"]

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
                if u"每天" in loop:
                    loop_attr = [u"周一", u"周二", u"周三", u"周四", u"周五", u"周六", u"周日"]
                elif u"工作日" in loop:
                    loop_attr = [u"周一", u"周二", u"周三", u"周四", u"周五"]
                elif u"周" in loop:
                    loop_attr = [loop]
                else:
                    loop_attr = loop
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

                for i in loop_attr:
                    self.widget_click(self.page["timer_repeat_page"][loop_mode[i]],
                                      self.page["timer_repeat_page"]["title"])
                    cycle = [loop_mode[i] for i in loop]

            self.widget_click(self.page["timer_repeat_page"]["to_return"],
                              self.page[page]["title"])
            attribute = self.ac.get_attribute(self.wait_widget(self.page[page]["repeat"]), "name")
            if tmp not in attribute:
                raise TimeoutException("Cycle set error")

        if loop == u"执行一次":
            cycle = ["None"]
        elif loop == u"永久循环":
            cycle = [u"0次"]
        else:
            if u"每天" in loop:
                loop_attr = [u"周一", u"周二", u"周三", u"周四", u"周五", u"周六", u"周日"]
            elif u"工作日" in loop:
                loop_attr = [u"周一", u"周二", u"周三", u"周四", u"周五"]
            elif u"周" in loop:
                loop_attr = [loop]
            else:
                loop_attr = loop
            cycle = [loop_mode[i] for i in loop_attr]
        return cycle

    # 定时检查模板
    def check_timer(self, start_time, set_time, power_state, cycle=None):
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
                        print("[APP_CHECK_TIMER]In Time %s" % time.strftime("%Y-%m-%d %X"))
                        if time.time() > end_time:
                            raise TimeoutException("Device state Error, current: %s" % state)
                break
            else:
                time.sleep(1)
                print("[APP_CHECK_TIMER]Out Time %s" % time.strftime("%Y-%m-%d %X"))

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
