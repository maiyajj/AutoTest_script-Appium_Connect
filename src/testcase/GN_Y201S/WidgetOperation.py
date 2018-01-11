# coding=utf-8
from src.testcase.GN_Y201S.LaunchApp import *


class WidgetOperation(LaunchApp):
    # 主页面选择待测设备
    def choose_home_device(self, device, device_index=None):
        # 已经通过其他途径获取索引，就不再搜索索引
        if device_index is None:
            index = self.get_index(device, self.page["app_home_page"]["device"])
        else:
            index = device_index

        # 使用copy函数将列表的值赋予给另一变量，不然修改变量的值会影响到原列表的值造成问题
        new_value = copy.copy(self.page["app_home_page"]["device"])
        # 将元素定位名称字典换乘字符串，{0:"//...",1:"//..."} →对应"//..."
        new_value[0] = new_value[0][index]
        end_time = time.time() + 30
        # 通过索引控制元素
        while True:
            try:
                self.widget_click(new_value, self.page["control_device_page"]["title"], 3, 10)
                break
            except TimeoutException:
                self.ac.swipe(0.6, 0.9, 0.6, 0.6, self.driver)  # 当元素在屏幕下方未展示时滑动屏幕
                time.sleep(1)

                if time.time() > end_time:
                    raise TimeoutException("choose_home_device timeout!")

    # 获取元素索引
    def get_index(self, device, element1):
        while True:
            elements = self.wait_widget(element1)  # 返回元素字典
            for index, element in elements.items():
                if element is not None and self.ac.get_attribute(element, "name") == device:
                    return index

    # 选择元素
    def get_home_power_element(self, device, device_index=None):
        # 已经通过其他途径获取索引，就不再搜索索引
        if device_index is None:
            index = self.get_index(device, self.page["app_home_page"]["device"])
        else:
            index = device_index

        new_value = copy.copy(self.page["app_home_page"]["device_button"])
        new_value[0] = new_value[0][index]
        end_time = time.time() + 30
        while True:
            # 通过元素坐标判断元素是否显示，未展示时滑动屏幕,与set_power有关。不能通过点击来判断
            if self.wait_widget(new_value).location["y"] < self.driver.get_window_size()["height"]:
                return new_value
            else:
                self.ac.swipe(0.6, 0.9, 0.6, 0.6, self.driver)
                time.sleep(1)

                if time.time() > end_time:
                    raise TimeoutException("choose_home_power timeout!")

    # 获取电源状态
    def get_power_state(self, device, device_index=None):
        # 已经通过其他途径获取索引，就不再搜索索引
        if device_index is None:
            index = self.get_index(device, self.page["app_home_page"]["device"])
        else:
            index = device_index

        new_value = copy.copy(self.page["app_home_page"]["device_state"])
        new_value[0] = new_value[0][index]
        attribute = self.ac.get_attribute(self.wait_widget(new_value), "name")
        return attribute

    # 控制设备电源
    def control_device_button(self, device):
        index = self.get_index(device, self.page["app_home_page"]["device"])
        new_value = copy.copy(self.page["app_home_page"]["device_button"])
        new_value[0] = new_value[0][index]
        self.widget_click(new_value)

    # 设置电源状态
    def set_power(self, device, state):
        # 由于阿里智能开关按钮状态不稳定，连续控制多次来判断按钮状态
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
        int
        -int
        ["point", "09:00"]
        ["delay", "00:30"]
        :param elem_e: 滚轮控件框架，用来获取y坐标
        :param elem_h: 滚轮控件“时”框架，用来获取“时”x坐标
        :param elem_m: 滚轮控件“分”框架，用来获取“分”x坐标
        :param elem_t: 滚轮当前的时间值，“HH:MM”格式
        :param now_time: 设置定时的当前时间
        :param set_timer: 设置定时的目标时间
        :param cycle: 是否是类鱼缸模式的连续定时模式
        :param delay_s: 定时的设置时间和启动时间延迟
        :return: 定时启动时间，int(time_start)；定时执行时间，int(time_set)
        """
        # 定时的设置时间包含延迟定时和准点定时：
        # 准点定时为设置定时当前时间前/后***分钟执行，数据格式为int型及以时间格式展现的str字符串型；
        # int型包含int型正数/负数（int型/负int型），用于设置当前时间***分钟前/后执行的定时，关键字为“int”，“minus”；
        # 时间格式str字符串型（"09:00"），用于设置固定时间点执行的定时，关键字为“point”
        # 延迟定时为设置时间段区间执行的定时，多用于鱼缸模式或延迟定时模式，数据格式为以时间格式展现的str字符串型；
        # 时间格式str字符串型（"30:00"），用于设置时间段定时，关键字为“delay”
        # ps：delay_s函数关键词用于给设置定时预留时间，设置定时也需要时间，默认延迟2分钟，当前时间8:00，定时开始执行时间为8:02；
        swipe_time = conf["roll_time"]["GN_Y201S"]  # 阿里智能APP的滚轮滑动间隔时间
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

        # 获取“时”“分”滚轮滑动的基准值
        """"""
        # 滚轮
        lcx_e, lcy_e, szw_e, szh_e = self.set_roll(elem_e)
        # 时滚轮
        lcx_h, lcy_h, szw_h, szh_h = self.set_roll(elem_h)
        pxx_h, pxy_h = elem_h[3]["px"]
        aszh_h = int(szh_e / 5 * 4 / 5)  # 根据滚轮显示时间点滚条个数计算单个时间点滚条的元素宽度，个数默认为5
        start_x_h, start_y_h = int(lcx_h + pxx_h * szw_h), int(lcy_e + szh_e / 2)  # “时”滚轮的操作起始点
        # 分滚轮
        lcx_m, lcy_m, szw_m, szh_m = self.set_roll(elem_m)
        pxx_m, pxy_m = elem_m[3]["px"]
        aszh_m = int(szh_e / 5 * 4 / 5)
        start_x_m, start_y_m = int(lcx_m + pxx_m * szw_m), int(lcy_e + szh_e / 2)  # “分”滚轮的操作起始点
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
        self.debug.info("[APP_TIMER]start_time: %s, set_time: %s, delay_time: %s" % (start_time, set_time, delay_time))
        self.debug.info("[APP_TIMER]time_start: %s, time_set: %s, time_delay: %s" % (time_start, time_set, time_delay))
        time.sleep(1)

        # 判断设置后的滚轮是否与设定一致
        pass

        return int(time_start), int(time_set)

    # 设置次数滚轮
    def set_count_roll(self, elem, roll_value, set_value):
        # 滚轮
        lcx, lcy, szw, szh = self.set_roll(elem)
        pxx, pxy = elem[3]["px"]
        aszh = int(szh / 5 * 4 / 5)
        start_x, start_y = int(lcx + pxx * szw), int(lcy + pxy * szh)  # 获取滚轮滑动开始坐标值

        diff = set_value - roll_value
        diff_a = abs(diff)
        try:
            # 计算滚轮滑动目标坐标值
            end_y = start_y - diff / diff_a * aszh
        except ZeroDivisionError:
            end_y = start_y

        swipe = self.ac.swipe
        swipe_time = conf["roll_time"]["GN_Y201S"]
        while diff_a > 0:
            swipe(start_x, start_y, start_x, end_y, self.driver, percent=False)  # step=25
            print(diff_a)
            diff_a -= 1
            time.sleep(swipe_time)

        self.debug.info("roll_value: %s, set_value: %s" % (roll_value, set_value))

        time.sleep(1)

    # 创建普通定时
    def create_normal_timer(self, now_time, set_timer, power, loop, delay_s=120):
        """
        :param now_time: 当前时间
        :param set_timer: 设定时间
        :param power: 设定定时开/关
        :param loop: 定时循环模式
        :param delay_s: 定时设定与执行时间差
        :return: 定时启动时间，定时执行时间
        """
        # 根据如下操作能创建一条普通定时并返回定时列表页面
        self.widget_click(self.page["normal_timer_page"]["add_normal_timer"],
                          self.page["add_normal_timer_page"]["title"])

        start_time, start_set_time = self.set_timer_roll(self.page["add_normal_timer_page"]["roll"],
                                                         self.page["add_normal_timer_page"]["roll_h"],
                                                         self.page["add_normal_timer_page"]["roll_m"],
                                                         "14:30", now_time, set_timer, delay_s=delay_s)
        now = time.mktime(time.strptime(time.strftime("%Y-%m-%d r:00").replace("r", now_time), "%Y-%m-%d %X"))

        if start_set_time <= now:
            start_set_time = start_set_time + 3600 * 24
        self.debug.info("[APP_TIMER]Start_time: %s, Start_set_time: %s" % (
            time.strftime("%Y-%m-%d %X", time.localtime(start_time)),
            time.strftime("%Y-%m-%d %X", time.localtime(start_set_time))))

        self.widget_click(self.page["add_normal_timer_page"][power],
                          self.page["add_normal_timer_page"]["title"])

        cycle = self.set_timer_loop("add_normal_timer_page", loop)
        if cycle == ["None"]:
            cycle = [time.strftime("%A", time.localtime(start_set_time)).lower()]

        self.widget_click(self.page["add_normal_timer_page"]["saved"],
                          self.page["normal_timer_page"]["title"])
        self.debug.info(u"[APP_TIMER]Start Time: %s[%s]" % (time.strftime("%Y-%m-%d %X"), time.time()))

        return start_time, start_set_time, cycle

    # 创建延时定时
    def create_delay_timer(self, now_time, set_timer, power, delay_s=120, cycle=False):
        """
        :param now_time: 当前时间
        :param set_timer: 设定时间
        :param power: 设定定时开/关
        :param delay_s: 定时设定与执行时间差
        :param cycle: 是否是类鱼缸模式的连续定时模式
        :return: 定时启动时间，定时执行时间
        """
        # 根据如下操作能创建一条延迟定时，且定时已启动
        # 用于获取时间滚轮的时间
        self.widget_click(self.page["delay_timer_page"]["launch"],
                          self.page["delay_timer_page"]["cancel"])
        time_roll = self.ac.get_attribute(self.wait_widget(self.page["delay_timer_page"]["delay_time"]), "name")
        self.debug.info("[APP_INFO]Time roll value: %s" % time_roll)
        self.widget_click(self.page["delay_timer_page"]["cancel"],
                          self.page["delay_timer_page"]["launch"])

        try:
            time_now = time.strptime(time.strftime("%Y-%m-%d r:00").replace("r", now_time), "%Y-%m-%d %X")
        except ValueError:
            time_now = time.strptime(time.strftime("%Y-%m-%d r").replace("r", now_time), "%Y-%m-%d %X")
        time_now = time.strftime("%X", time.localtime(time.mktime(time_now)))

        self.widget_click(self.page["delay_timer_page"][power],
                          self.page["delay_timer_page"]["title"])

        start_time, start_set_time = self.set_timer_roll(self.page["delay_timer_page"]["roll"],
                                                         self.page["delay_timer_page"]["roll_h"],
                                                         self.page["delay_timer_page"]["roll_m"],
                                                         time_roll, time_now, set_timer, cycle, delay_s)
        self.debug.info("[APP_TIMER]Start_time: %s, Start_set_time: %s" % (
            time.strftime("%Y-%m-%d %X", time.localtime(start_time)),
            time.strftime("%Y-%m-%d %X", time.localtime(start_set_time))))

        # 等待启动时间点，并启动定时
        end_time = time.time() + 5 * 60 + 30
        while True:
            if int(time.time()) == start_time:
                self.widget_click(self.page["delay_timer_page"]["launch"])
                self.debug.info(u"[APP_TIMER]Start Time: %s[%s]" % (time.strftime("%Y-%m-%d %X"), time.time()))
                self.wait_widget(self.page["delay_timer_page"]["cancel"], log_record=0)
                break
            else:
                if time.time() > end_time:
                    tmp = time.strftime("%Y-%m-%d %X", time.localtime(start_time))
                    raise TimeoutException("Timer Saved Error, time: %s[%s]" % (tmp, start_time))
                time.sleep(1)

        return start_time, start_set_time

    # 创建循环定时
    def create_cycle_timer(self, page, now_time, set_start_time, set_end_time, loop, delay_s=120, cycle=False, loops=1):
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
        start_roll = self.ac.get_attribute(self.wait_widget(self.page[page]["start_time"]), "name")
        end_roll = self.ac.get_attribute(self.wait_widget(self.page[page]["end_time"]), "name")

        # 获取启动时间的时间滚轮值
        tmp = re.findall(u"(\d+)小时", start_roll)
        if not tmp:
            start_roll_h = 0
        else:
            start_roll_h = int(tmp[0])
        tmp = re.findall(u"(\d+)分钟", start_roll)
        if not tmp:
            start_roll_m = 0
        else:
            start_roll_m = int(tmp[0])
        start_roll = "%02d:%02d" % (start_roll_h, start_roll_m)
        self.debug.info("[APP_TIMER]Start roll: %s" % start_roll)

        # 获取关闭时间的时间滚轮值
        tmp = re.findall(u"(\d+)小时", end_roll)
        if not tmp:
            end_roll_h = 0
        else:
            end_roll_h = int(tmp[0])
        tmp = re.findall(u"(\d+)分钟", end_roll)
        if not tmp:
            end_roll_m = 0
        else:
            end_roll_m = int(tmp[0])
        end_roll = "%02d:%02d" % (end_roll_h, end_roll_m)
        self.debug.info("[APP_TIMER]End roll: %s" % end_roll)

        try:
            time_now = time.strptime(time.strftime("%Y-%m-%d r:00").replace("r", now_time), "%Y-%m-%d %X")
        except ValueError:
            time_now = time.strptime(time.strftime("%Y-%m-%d r").replace("r", now_time), "%Y-%m-%d %X")
        time_now = time.strftime("%X", time.localtime(time.mktime(time_now)))

        # 设定滚轮时间
        self.widget_click(self.page[page]["start_time"],
                          self.page["timer_roll_popup"]["title"])

        start_time, start_set_time = self.set_timer_roll(self.page["timer_roll_popup"]["roll"],
                                                         self.page["timer_roll_popup"]["roll_h"],
                                                         self.page["timer_roll_popup"]["roll_m"],
                                                         start_roll, time_now, set_start_time, cycle, delay_s)
        self.debug.info("[APP_TIMER]Start_time: %s, Start_set_time: %s" % (
            time.strftime("%Y-%m-%d %X", time.localtime(start_time)),
            time.strftime("%Y-%m-%d %X", time.localtime(start_set_time))))

        self.widget_click(self.page["timer_roll_popup"]["confirm"],
                          self.page[page]["launch"])

        self.widget_click(self.page[page]["end_time"],
                          self.page["timer_roll_popup"]["title"])

        time_now_end = time.strftime("%X", time.localtime(start_set_time))
        end_time, end_set_time = self.set_timer_roll(self.page["timer_roll_popup"]["roll"],
                                                     self.page["timer_roll_popup"]["roll_h"],
                                                     self.page["timer_roll_popup"]["roll_m"],
                                                     end_roll, time_now_end, set_end_time, True)
        self.debug.info("[APP_TIMER]End_time: %s, End_set_time: %s" % (
            time.strftime("%Y-%m-%d %X", time.localtime(end_time)),
            time.strftime("%Y-%m-%d %X", time.localtime(end_set_time))))

        self.widget_click(self.page["timer_roll_popup"]["confirm"],
                          self.page[page]["launch"])

        # 设定循环次数
        set_loop = self.set_timer_loop(page, loop)[0]
        self.debug.info("[APP_TIMER]Set loop: %s" % set_loop)
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

        # 定时启动时间
        end_time = time.time() + 5 * 60 + 30
        while True:
            if int(time.time()) == start_time:
                self.widget_click(self.page[page]["launch"],
                                  self.page[page]["close"])
                self.debug.info(u"[APP_TIMER]Start Time: %s; Now Time: %s[%s]" %
                                (start_time, time.strftime("%X"), time.time()))
                break
            else:
                if time.time() > end_time:
                    raise TimeoutException("Timer Saved Error, time: %s" % start_time)
                time.sleep(1)

        return loop_list

    # 创建热水器类型模式
    def create_point_mode_timer(self, page, now_time, set_start_time, set_end_time, loop, delay_s=120, exchange=False):
        """与创建普通定时相同
        return: ([start_time, start_set_time], [end_time, end_set_time])
        """
        start_roll = self.ac.get_attribute(self.wait_widget(self.page[page]["start_time"]), "name")
        end_roll = self.ac.get_attribute(self.wait_widget(self.page[page]["end_time"]), "name")
        self.debug.info("[APP_TIMER]Start roll: %s" % start_roll)
        self.debug.info("[APP_TIMER]End roll: %s" % end_roll)

        try:
            time_now = time.strptime(time.strftime("%Y-%m-%d r:00").replace("r", now_time), "%Y-%m-%d %X")
        except ValueError:
            time_now = time.strptime(time.strftime("%Y-%m-%d r").replace("r", now_time), "%Y-%m-%d %X")
        time_now = time.strftime("%X", time.localtime(time.mktime(time_now)))

        if exchange is True:
            self.widget_click(self.page[page]["time_exchange"],
                              self.page[page]["title"])

        self.widget_click(self.page[page]["start_time"],
                          self.page["timer_roll_popup"]["title"])

        start_time, start_set_time = self.set_timer_roll(self.page["timer_roll_popup"]["roll"],
                                                         self.page["timer_roll_popup"]["roll_h"],
                                                         self.page["timer_roll_popup"]["roll_m"],
                                                         start_roll, time_now, set_start_time, delay_s=delay_s)
        now = time.mktime(time.strptime(time.strftime("%Y-%m-%d r:00").replace("r", now_time), "%Y-%m-%d %X"))

        if start_set_time <= now:
            start_set_time = start_set_time + 3600 * 24
        self.debug.info("[APP_TIMER]Start_time: %s, Start_set_time: %s" % (
            time.strftime("%Y-%m-%d %X", time.localtime(start_time)),
            time.strftime("%Y-%m-%d %X", time.localtime(start_set_time))))

        self.widget_click(self.page["timer_roll_popup"]["confirm"],
                          self.page[page]["launch"])

        self.widget_click(self.page[page]["end_time"],
                          self.page["timer_roll_popup"]["title"])

        end_time, end_set_time = self.set_timer_roll(self.page["timer_roll_popup"]["roll"],
                                                     self.page["timer_roll_popup"]["roll_h"],
                                                     self.page["timer_roll_popup"]["roll_m"],
                                                     end_roll, time_now, set_end_time, delay_s=delay_s)
        now = time.mktime(time.strptime(time.strftime("%Y-%m-%d r:00").replace("r", now_time), "%Y-%m-%d %X"))

        if end_set_time <= now:
            end_set_time = end_set_time + 3600 * 24

        if end_set_time <= start_set_time:
            end_set_time = end_set_time + 3600 * 24
        self.debug.info("[APP_TIMER]End_time: %s, End_set_time: %s" % (
            time.strftime("%Y-%m-%d %X", time.localtime(end_time)),
            time.strftime("%Y-%m-%d %X", time.localtime(end_set_time))))

        self.widget_click(self.page["timer_roll_popup"]["confirm"],
                          self.page[page]["launch"])

        cycle = self.set_timer_loop(page, loop)
        if cycle == ["None"]:
            cycle = [time.strftime("%A", time.localtime(start_set_time)).lower()]

        self.widget_click(self.page[page]["launch"],
                          self.page[page]["close"])

        return [[start_time, start_set_time], [end_time, end_set_time]], cycle

    # 创建鱼缸，充电保护类型模式
    def create_delay_mode_timer(self, page, now_time, set_timer, delay_s=120, cycle=False):
        """与创建延迟定时相同
       return: None
       """
        time_roll = self.ac.get_attribute(self.wait_widget(self.page[page]["end_time"]), "name")
        tmp = re.findall(u"(\d+)小时", time_roll)
        if not tmp:
            time_roll_h = 0
        else:
            time_roll_h = int(tmp[0])
        tmp = re.findall(u"(\d+)分钟", time_roll)
        if not tmp:
            time_roll_m = 0
        else:
            time_roll_m = int(tmp[0])
        time_roll = "%02d:%02d" % (time_roll_h, time_roll_m)
        self.debug.info("[APP_TIMER]Start roll: %s" % time_roll)

        try:
            time_now = time.strptime(time.strftime("%Y-%m-%d r:00").replace("r", now_time), "%Y-%m-%d %X")
        except ValueError:
            time_now = time.strptime(time.strftime("%Y-%m-%d r").replace("r", now_time), "%Y-%m-%d %X")
        time_now = time.strftime("%X", time.localtime(time.mktime(time_now)))

        self.widget_click(self.page[page]["end_time"],
                          self.page["timer_roll_popup"]["title"])

        start_time, start_set_time = self.set_timer_roll(self.page["timer_roll_popup"]["roll"],
                                                         self.page["timer_roll_popup"]["roll_h"],
                                                         self.page["timer_roll_popup"]["roll_m"],
                                                         time_roll, time_now, set_timer, cycle, delay_s)
        self.debug.info("[APP_TIMER]Start_time: %s, Start_set_time: %s" % (
            time.strftime("%Y-%m-%d %X", time.localtime(start_time)),
            time.strftime("%Y-%m-%d %X", time.localtime(start_set_time))))

        self.widget_click(self.page["timer_roll_popup"]["confirm"],
                          self.page[page]["launch"])

        # 等待启动时间点，并启动定时
        end_time = time.time() + 5 * 60 + 30
        while True:
            now = int(time.time())
            self.debug.info("now time: %s" % now)
            if now == start_time:
                self.widget_click(self.page[page]["launch"])
                self.debug.info(u"[APP_TIMER]Start Time: %s[%s]" % (time.strftime("%Y-%m-%d %X"), time.time()))
                self.wait_widget(self.page[page]["close"], log_record=0)
                break
            else:
                if time.time() > end_time:
                    tmp = time.strftime("%Y-%m-%d %X", time.localtime(start_time))
                    raise TimeoutException("Timer Saved Error, time: %s[%s]" % (tmp, start_time))
                time.sleep(1)

        return start_time, start_set_time

    # 设置普通/模式定时循环模式
    def set_timer_loop(self, page, loop):
        loop_mode = {u"周一": "monday",
                     u"周二": "tuesday",
                     u"周三": "wednesday",
                     u"周四": "thursday",
                     u"周五": "friday",
                     u"周六": "saturday",
                     u"周日": "weekday"}
        cycle = ["None"]
        end_time = time.time() + 60
        while True:
            # 属性判断会不正常，通过以下操作验证
            """"""
            self.debug.info("""*******""")
            self.widget_click(self.page[page]["repeat"],
                              self.page["timer_repeat_page"]["title"])

            self.widget_click(self.page["timer_repeat_page"]["to_return"],
                              self.page[page]["repeat"], )
            """"""

            attr = self.ac.get_attribute(self.wait_widget(self.page[page]["repeat"]), "name")
            invalid_attr = '\ue617'
            invalid_attr = invalid_attr.decode("unicode-escape")
            if u"重复" in attr:  # 去除多余属性
                attribute = attr.replace(u"重复", "").replace(invalid_attr, "").split()[0]
            else:
                attribute = attr.replace(u"永久循环", "tmp").replace(u"循环", "").replace("tmp", u"永久循环").replace(
                    invalid_attr, "").split()[0]
            self.debug.info("[APP_INFO]Repeat attr: %s, %s" % (attribute, [attribute]))

            # 自定义模式显示为：周一、周三、周五...etc
            # loop传参为[u"周一", u"周三", u"周五"]
            if isinstance(loop, list):
                tmp = u"、".join(loop)  # list → str
            else:
                tmp = loop
            self.debug.info("[APP_INFO]Repeat set attr: %s, %s" % (tmp, [tmp]))

            # 若定时已存在循环模式与设定不同则需要重新设置，若相同则不会设置
            if tmp != attribute:
                if u"每天" in attribute:
                    attribute = [u"周一", u"周二", u"周三", u"周四", u"周五", u"周六", u"周日"]
                elif u"工作日" in attribute:
                    attribute = [u"周一", u"周二", u"周三", u"周四", u"周五"]
                elif u"永不" in attribute:
                    attribute = []
                elif u"周" in attribute:
                    attribute = attribute.split(u"、")
                else:
                    pass

                self.widget_click(self.page[page]["repeat"],
                                  self.page["timer_repeat_page"]["title"])

                if loop == u"永不":
                    self.widget_click(self.page["timer_repeat_page"]["once"],
                                      self.page["timer_repeat_page"]["title"])

                elif u"周" in loop or u"每天" in loop or u"工作日" in loop or isinstance(loop, list):
                    if u"每天" in loop:
                        loop_attr = [u"周一", u"周二", u"周三", u"周四", u"周五", u"周六", u"周日"]
                    elif u"工作日" in loop:
                        loop_attr = [u"周一", u"周二", u"周三", u"周四", u"周五"]
                    elif u"周" in loop:
                        loop_attr = [loop]
                    else:
                        loop_attr = loop
                    # 选择星期时，已存在的星期数是已经被勾选的，要取消需要再次点击；
                    # 例：已有周期为周一，周五，需要设置的周期为周三，周五
                    # 则实际操作为点击周一和周三，而周五不需要点击，因为周五已被选中，再点击周五则周五就会被取消选中
                    # 代码通过下述公式计算，输入当前循环周期和需要设定的周期，输出为需要待操作的周期
                    # 输入：当前[u"周一", u"周五"]，设定[u"周三", u"周五"]；
                    # 输出：[u"周一", u"周三"]；
                    result = list((set(attribute) | set(loop_attr)) - (set(attribute) & set(loop_attr)))
                    for i in result:  # 根据计算元素点击
                        self.widget_click(self.page["timer_repeat_page"][loop_mode[i]],
                                          self.page["timer_repeat_page"]["title"])
                else:
                    if u"永久循环" in attribute:  # 已存在模式为u"永久循环"
                        roll = 0
                    else:  # 已存在模式为u"**次"
                        roll = int(re.findall(u"(\d+)次", attribute)[0])
                    if loop == u"永久循环":
                        set_roll = [u"0次"]
                    else:
                        set_roll = [loop]
                    set_roll = int(re.findall(u"(\d+)次", set_roll[0])[0])
                    self.set_count_roll(self.page["timer_repeat_page"]["cycle_count"], roll, set_roll)  # 从“**次”到“永久循环”

                # 保存
                self.widget_click(self.page["timer_repeat_page"]["saved"],
                                  self.page[page]["title"])

                # 再次校验
                # 页面设置完成后，元素属性可能未改变，刷新页面更新元素
                self.widget_click(self.page[page]["repeat"],
                                  self.page["timer_repeat_page"]["title"])

                self.widget_click(self.page["timer_repeat_page"]["to_return"],
                                  self.page[page]["repeat"], )

                attr = self.ac.get_attribute(self.wait_widget(self.page[page]["repeat"]), "name")
                if u"重复" in attr:
                    attribute = attr.replace(u"重复", "").replace(invalid_attr, "").split()[0]
                else:
                    attribute = attr.replace(u"永久循环", "tmp").replace(u"循环", "").replace("tmp", u"永久循环").replace(
                        invalid_attr, "").split()[0]
                self.debug.info("[APP_INFO]Repeat attr: %s, %s" % (attribute, [attribute]))
                if tmp == attribute:
                    break
                else:
                    if time.time() > end_time:
                        raise TimeoutException("Cycle set error")

            if loop == u"永不":
                cycle = ["None"]
            elif u"周" in loop or u"每天" in loop or u"工作日" in loop or isinstance(loop, list):
                if u"每天" in loop:
                    loop_attr = [u"周一", u"周二", u"周三", u"周四", u"周五", u"周六", u"周日"]
                elif u"工作日" in loop:
                    loop_attr = [u"周一", u"周二", u"周三", u"周四", u"周五"]
                elif u"周" in loop:
                    loop_attr = [loop]
                else:
                    loop_attr = loop
                cycle = [loop_mode[i] for i in loop_attr]
            elif u"永久循环" in loop:
                cycle = [u"0次"]
            else:
                cycle = [loop]
            break
        self.debug.info("[APP_INFO]Cycle: %s, %s" % (",".join(cycle), cycle))

        return cycle

    # 设置峰谷电时间
    def set_peak_valley_time(self, elem, now_time, set_timer, peak):
        attribute = self.ac.get_attribute(elem, "name")
        if u"未设置" in attribute:
            if peak is True:  # 峰电/谷电
                time_roll = "08:00"
            else:
                time_roll = "22:00"
        else:
            time_roll = re.findall("(\d+:\d+)", attribute)[0]
        self.debug.info("[APP_TIMER]Start roll: %s" % time_roll)

        if peak is True:  # 峰电/谷电
            widget = "start_time"
        else:
            widget = "end_time"

        self.widget_click(self.page["peak_valley_price_page"][widget],
                          self.page["timer_roll_popup"]["title"])

        start_time, start_set_time = self.set_timer_roll(self.page["timer_roll_popup"]["roll_p"],
                                                         self.page["timer_roll_popup"]["roll_p_h"],
                                                         self.page["timer_roll_popup"]["roll_p_m"],
                                                         time_roll, now_time, set_timer, False, 0)
        self.debug.info("[APP_TIMER]Start_time: %s, Start_set_time: %s" % (
            time.strftime("%Y-%m-%d %X", time.localtime(start_time)),
            time.strftime("%Y-%m-%d %X", time.localtime(start_set_time))))

        self.widget_click(self.page["timer_roll_popup"]["confirm"],
                          self.page["peak_valley_price_page"]["title"])

        return start_time, start_set_time

    # 定时检查模板
    def check_timer(self, device, start_time, set_time, power_state, cycle=None):
        # 开始时间, 设置时间
        start_times = time.strftime("%Y-%m-%d %X", time.localtime(start_time))
        self.debug.info("[APP_CHECK_TIMER]Now time: %s. Start time: %s" % (time.strftime("%Y-%m-%d %X"), start_times))
        now_week = time.strftime("%A").lower()
        if cycle is None:
            set_week = now_week
        else:
            if len(cycle) == 1:
                set_week = cycle[0]
            else:
                set_week = ",".join(cycle)
        self.debug.info("[APP_CHECK_TIMER]Now week: %s, Set week: %s" % (now_week, set_week))
        while True:
            now_week = time.strftime("%A").lower()
            if now_week in set_week:
                tmp = time.strftime("%Y-%m-%d ")
                tmp = tmp + time.strftime("%X", time.localtime(set_time))
                set_times = int(time.mktime(time.strptime(tmp, "%Y-%m-%d %X")))
                break
            else:
                if time.strftime("%M") == "00":
                    self.debug.info("now week: %s" % now_week)
                else:
                    print("********************")
                    print("now week: %s" % now_week)
                    print("********************")
                    time.sleep(1)

        delay_times = set_times - start_time
        self.debug.info("[APP_CHECK_TIMER]Delay Time: %s" % delay_times)

        index = self.get_index(device, self.page["app_home_page"]["device"])
        element = copy.copy(self.page["app_home_page"]["device_state"])
        element[0] = element[0][index]
        element = self.wait_widget(element)
        end_time = set_times + 30
        self.debug.info("[APP_CHECK_TIMER]End Time: %s" % time.strftime("%Y-%m-%d %X", time.localtime(end_time)))
        self.debug.info("[APP_CHECK_TIMER]Set Time: %s" % time.strftime("%Y-%m-%d %X", time.localtime(set_times)))
        while True:
            current_time = int(time.time())
            if current_time >= set_times:
                while True:
                    state = self.ac.get_attribute(element, "name")
                    if state == power_state:
                        self.debug.info("[APP_CHECK_TIMER]Current Time: %s" % time.strftime("%Y-%m-%d %X"))
                        self.debug.info("[APP_CHECK_TIMER]Device Info: %s" % power_state)
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
        # 按照手动操作顺序删除定时
        end_time = time.time() + 120
        # 排除第一次进入页面加载失败造成的误判
        try:
            self.wait_widget(self.page["normal_timer_page"]["no_timer"])
        except TimeoutException:
            self.widget_click(self.page["normal_timer_page"]["to_return"],
                              self.page["control_device_page"]["title"])

            self.widget_click(self.page["control_device_page"]["normal_timer"],
                              self.page["normal_timer_page"]["title"])
        while True:
            try:
                try:
                    self.wait_widget(self.page["normal_timer_page"]["no_timer"])
                except TimeoutException:
                    raise ValueError()
                self.debug.info("It has normal timer.")
                self.widget_click(self.page["normal_timer_page"]["timer_edit"],
                                  self.page["normal_timer_page"]["delete_timer"])

                self.widget_click(self.page["normal_timer_page"]["delete_timer"],
                                  self.page["normal_timer_page"]["delete"])

                self.widget_click(self.page["normal_timer_page"]["delete"],
                                  self.page["normal_timer_page"]["saved"])

                self.widget_click(self.page["normal_timer_page"]["saved"],
                                  self.page["normal_timer_page"]["timer_edit"])
            except TimeoutException:
                time.sleep(1)
                if time.time() > end_time:
                    end_time = time.strftime("%Y-%m-%d %X", time.localtime(end_time))
                    raise TimeoutException("delete_normal_timer timeout, time limit: %s" % end_time)
            except ValueError:
                self.debug.info("It has no timer~")
                break

    # 关闭模式定时
    def close_mode_timer(self):
        timer_loop = {u"热水器模式": ["water_mode_timer", "water_mode_timer_page"],
                      u"小夜灯模式": ["night_mode_timer", "night_mode_timer_page"],
                      u"鱼缸模式": ["fish_mode_timer", "fish_mode_timer_page"],
                      u"电蚊香模式": ["mosquito_mode_timer", "mosquito_mode_timer_page"],
                      u"充电保护模式": ["piocc_mode_timer", "piocc_mode_timer_page"],
                      u"取暖器模式": ["warmer_mode_timer", "warmer_mode_timer_page"]}
        try:
            element = self.wait_widget(self.page["control_device_page"]["launch_mode"])
            while True:
                attribute = self.ac.get_attribute(element, "name")
                if u"模式" in attribute:
                    self.debug.info("[APP_INFO]Mode timer is run")
                    for timer_mode, value in timer_loop.items():
                        if timer_mode in attribute:
                            self.widget_click(self.page["control_device_page"][value[0]],
                                              self.page[value[1]]["title"])

                            self.widget_click(self.page[value[1]]["close"],
                                              self.page[value[1]]["launch"], times=2)

                            self.widget_click(self.page[value[1]]["to_return"],
                                              self.page["control_device_page"]["title"])
                else:
                    self.debug.info("[APP_INFO]Mode timer don't run")
                    break
        except TimeoutException:
            self.debug.info("[APP_INFO]Mode timer don't run")

    # 关闭定时任务
    def close_general_timer(self):
        element = self.wait_widget(self.page["control_device_page"]["launch_mode"])
        while True:
            attribute = self.ac.get_attribute(element, "name")
            if u"任务开" in attribute:
                self.debug.info("[APP_INFO]Normal timer is run")
                if u"定时任务开" in attribute:
                    self.widget_click(self.page["control_device_page"]["normal_timer"],
                                      self.page["normal_timer_page"]["title"])

                    self.delete_normal_timer()

                    self.widget_click(self.page["normal_timer_page"]["to_return"],
                                      self.page["control_device_page"]["title"])
                elif u"延时任务开" in attribute:
                    self.widget_click(self.page["control_device_page"]["delay_timer"],
                                      self.page["delay_timer_page"]["title"])

                    self.widget_click(self.page["delay_timer_page"]["cancel"],
                                      self.page["delay_timer_page"]["launch"])

                    self.widget_click(self.page["delay_timer_page"]["to_return"],
                                      self.page["control_device_page"]["title"])
                else:
                    self.ac.swipe(0.6, 0.9, 0.6, 0.4, self.driver)
                    self.widget_click(self.page["control_device_page"]["cycle_timer"],
                                      self.page["cycle_timer_page"]["title"])

                    self.widget_click(self.page["cycle_timer_page"]["close"],
                                      self.page["cycle_timer_page"]["launch"])

                    self.widget_click(self.page["cycle_timer_page"]["to_return"],
                                      self.page["control_device_page"]["title"])
                    self.ac.swipe(0.6, 0.4, 0.6, 0.9, self.driver)
            else:
                self.debug.info("[APP_INFO]Normal timer don't run")
                break

    # 启动模式定时
    def launch_mode_timer(self, page, start_time=None, start_now=False):
        if not isinstance(start_now, bool):
            raise KeyError("start_now must be bool type")
        if start_now is True:  # 立即启动，例如普通定时等
            self.widget_click(self.page[page]["launch"])
            self.debug.info(u"[APP_TIMER]Start Time: %s[%s]" % (time.strftime("%Y-%m-%d %X"), time.time()))
            self.wait_widget(self.page[page]["close"], log_record=0)
        else:  # 需要特定时间点启动，例如延时模式等
            if start_time is None:  # 若选择延迟启动，则启动时间点start_time不能为None
                raise KeyError("if start_now is False, start_time can`t be None type")

            end_time = time.time() + 5 * 60 + 30
            while True:
                now = int(time.time())
                self.debug.info("now time: %s" % now)
                if now == start_time:
                    self.widget_click(self.page[page]["launch"])
                    self.debug.info(u"[APP_TIMER]Start Time: %s[%s]" % (time.strftime("%Y-%m-%d %X"), time.time()))
                    self.wait_widget(self.page[page]["close"], log_record=0)
                    break
                else:
                    if time.time() > end_time:
                        tmp = time.strftime("%Y-%m-%d %X", time.localtime(start_time))
                        raise TimeoutException("Timer Saved Error, time: %s[%s]" % (tmp, start_time))
                    time.sleep(1)

    # 统计电量操作缩减
    def get_device_elect_unit(self, check_time):
        while True:
            if int(time.strftime("%H")) == check_time:
                time.sleep(60)
                break
            else:
                time.sleep(60)

        self.widget_click(self.page["control_device_page"]["elec"],
                          self.page["elec_page"]["title"])

        self.ac.swipe(0.5, 0.7, 0.5, 0.4, self.driver)

        self.widget_click(self.page["elec_page"]["more_elec_history"],
                          self.page["more_elec_history_page"]["title"])

        # 选择当前日期
        today = time.strftime("%m月%d日").decode("utf")  # 格式化日期
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

        # 读取指定时间点前电费数据
        elec_and_bill_e = self.wait_widget(self.page["day_elec_page"]["elec_time"])
        elec_and_bill_v = copy.copy(self.page["day_elec_page"]["elec_value"])
        for index, element in elec_and_bill_e.items():
            if element is not None:
                elec_and_bill_v[0] = self.page["day_elec_page"]["elec_value"][0][index]
                tmp = re.findall(u"(\d+.\d+|\d+)元.+?(\d+.\d+|\d+)W", self.ac.get_attribute(elec_and_bill_v, "name"))
                self.elec[index] = float(tmp[1])
                self.elec_bill[index] = float(tmp[0])
        self.debug.info("[APP_INFO]%02d:01_elec: %s" % (check_time, str(self.elec)))
        self.debug.info("[APP_INFO]%02d:01_elec_bill: %s" % (check_time, str(self.elec_bill)))

        self.widget_click(self.page["day_elec_page"]["to_return"],
                          self.page["more_elec_history_page"]["title"])

        self.widget_click(self.page["more_elec_history_page"]["to_return"],
                          self.page["elec_page"]["title"])

        self.widget_click(self.page["elec_page"]["to_return"],
                          self.page["control_device_page"]["title"])

    # 统计电量
    def get_device_elect(self, check_time, across=False):
        now_h = int(time.strftime("%H"))
        if across is False:
            if now_h + 2 <= 23:  # 电量为下一整点上传，故从当前时间2个小时后才开始统计电量。判断2个小时后是否跨天
                across_day = False
            else:
                across_day = True
        else:
            across_day = True
        self.elec = {}
        self.elec_bill = {}

        if across_day is True:
            # 晚上23点开始读取当前一天的所有电量数据
            self.get_device_elect_unit(23)

        # 到另一天指定时间点结束统计
        self.get_device_elect_unit(check_time)

        return self.elec, self.elec_bill

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
