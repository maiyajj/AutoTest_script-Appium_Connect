# coding=utf-8

from src.testcase.GN_F1331.LaunchApp import *
from src.utils.GetSerial import *


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
        if "main" in state:
            button = "main_button"
        elif "up" in state:
            button = "up_button"
        elif "mid" in state:
            button = "mid_button"
        else:
            button = "down_button"
        if "_on" in state:
            btn = "on"
        else:
            btn = "off"
        while True:
            try:
                self.wait_widget(self.page["control_device_page"][state])
                try:
                    self.wait_widget(self.page["control_device_page"]["up_button_%s" % btn])
                except TimeoutException:
                    self.widget_click(self.page["control_device_page"]["up_button"],
                                      self.page["control_device_page"]["up_button_%s" % btn])
                try:
                    self.wait_widget(self.page["control_device_page"]["mid_button_%s" % btn])
                except TimeoutException:
                    self.widget_click(self.page["control_device_page"]["mid_button"],
                                      self.page["control_device_page"]["mid_button_%s" % btn])
                try:
                    self.wait_widget(self.page["control_device_page"]["down_button_%s" % btn])
                except TimeoutException:
                    self.widget_click(self.page["control_device_page"]["down_button"],
                                      self.page["control_device_page"]["down_button_%s" % btn])
                break
            except TimeoutException:
                self.widget_click(self.page["control_device_page"][button],
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
        :param now_time: 设置定时的当前时间
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
        swipe_time = conf["roll_time"]["GN_F1331"]  # 京东微联APP的滚轮滑动间隔时间
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
        start_x_h, start_y_h = int(lcx_h + pxx_h * szw_h), int(lcy_h + szh_h / 2)  # “时”滚轮的操作起始点
        # 分滚轮
        lcx_m, lcy_m, szw_m, szh_m = self.set_roll(elem_m)
        pxx_m, pxy_m = elem_m[3]["px"]
        start_x_m, start_y_m = int(lcx_m + pxx_m * szw_m), int(lcy_m + szh_m / 2)  # “分”滚轮的操作起始点
        """"""

        if isinstance(elem_t, str):
            attr = elem_t
        else:
            attr = self.ac.get_attribute(self.wait_widget(elem_t), "name")
            start_h, start_m = re.findall(u"(\d+)小时", attr), re.findall(u"(\d+)分钟", attr)
            if start_h:
                attr = "%02d:%02d" % (int(start_h[0]), int(start_m[0]))
            else:
                attr = "00:%02d" % int(start_m[0])

        # 从控件拿到当前控件的值
        time_roll = time.strftime("%Y-%m-%d r:00").replace("r", attr)  # 滚轮的当前时间
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
            pm_value = time_et_h / time_et_h_a
            if pm_value > 0:  # 往下滑
                aszh_h = int(szh_h * 1.9)  # 根据滚轮显示时间点滚条个数计算单个时间点滚条的元素宽度
            else:  # 往上滑
                aszh_h = int(szh_h * 1.4)
            end_y_h = start_y_h - pm_value * aszh_h
        except ZeroDivisionError:  # 若time_et相等
            end_y_h = start_y_h
        try:
            # 获取“分”滚轮滑动目的坐标值
            pm_value = time_et_m / time_et_m_a
            if pm_value > 0:  # 往下滑
                aszh_m = int(szh_m * 1.9)  # 根据滚轮显示时间点滚条个数计算单个时间点滚条的元素宽度
            else:  # 往上滑
                aszh_m = int(szh_m * 1.4)
            end_y_m = start_y_m - pm_value * aszh_m
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
        #     set_time = time.strftime("%Y-%m-%d %X", time.localtime(time_set))
        # else:
        #     delay_time = "None"
        #     time_delay = "None"
        #     set_time = time.strftime("%Y-%m-%d %X", time.localtime(time_set))
        # self.debug.info(
        #     "[APP_TIMER]Roll: start_time: %s, set_time: %s, delay_time: %s" % (start_time, set_time, delay_time))
        # self.debug.info(
        #     "[APP_TIMER]Roll: time_start: %s, time_set: %s, time_delay: %s" % (time_start, time_set, time_delay))
        time.sleep(1)

        return int(time_start), int(time_set)

    # 设置次数滚轮
    def set_count_roll(self, elem, roll_value, set_value):
        # 滚轮
        lcx, lcy, szw, szh = self.set_roll(elem)
        pxx, pxy = elem[3]["px"]
        start_x, start_y = int(lcx + pxx * szw), int(lcy + pxy * szh)  # 获取滚轮滑动开始坐标值

        diff = set_value - roll_value
        diff_a = abs(diff)
        try:
            # 计算滚轮滑动目标坐标值
            pm_value = diff / diff_a
            if pm_value > 0:  # 往下滑
                aszh = int(szh * 1.9)
            else:  # 往上滑
                aszh = int(szh * 1.4)
            end_y = start_y - pm_value * aszh
        except ZeroDivisionError:
            end_y = start_y

        swipe = self.ac.swipe
        swipe_time = conf["roll_time"]["GN_F1331"]
        while diff_a > 0:
            swipe(start_x, start_y, start_x, end_y, self.driver, percent=False)  # step=25
            print(diff_a)
            diff_a -= 1
            time.sleep(swipe_time)

        self.debug.info("roll_value: %s, set_value: %s" % (roll_value, set_value))

        time.sleep(1)

    # 创建普通定时
    def create_normal_timer(self, page, now_time, delay_time, power, delay_s=120, loop=u"执行一次"):
        """
        :param page: 设置定时层
        :param now_time: now time
        :param delay_time: delay time
        :param power: power state power on/off
        :param delay_s: 延迟多久启动
        :param loop: everyday/monday etc
        :return: start_time, set_time
        """
        try:
            self.wait_widget(self.page[page]["delay_timer_button"])
            self.widget_click(self.page[page]["delay_timer"])
        except TimeoutException:
            pass

        try:
            self.wait_widget(self.page[page]["cycle_timer_button"])
            self.widget_click(self.page[page]["cycle_timer"])
        except TimeoutException:
            pass

        while True:  # 避免设置时时间跳变
            if 1 <= int(time.strftime("%S")) <= 50:
                break
            time.sleep(1)

        self.widget_click(self.page[page]["add_normal_timer"],
                          self.page["add_normal_timer_page"]["title"])

        elem_t = time.strftime("%H:%M")

        start_time, start_set_time = self.set_timer_roll(self.page["add_normal_timer_page"]["roll_h"],
                                                         self.page["add_normal_timer_page"]["roll_m"],
                                                         elem_t, now_time, delay_time, delay_s=delay_s)
        now = time.mktime(time.strptime(time.strftime("%Y-%m-%d r:00").replace("r", now_time), "%Y-%m-%d %X"))

        if start_set_time <= now:
            start_set_time = start_set_time + 3600 * 24

        self.widget_click(self.page["add_normal_timer_page"][power])

        cycle = self.set_timer_loop("add_normal_timer_page", loop)

        if cycle == ["None"]:
            cycle = [time.strftime("%A", time.localtime(start_set_time)).lower()]

        self.widget_click(self.page["add_normal_timer_page"]["saved"],
                          self.page[page]["title"])

        start_time = int(time.time())
        self.debug.info("[APP_TIMER][%s, %s]Start_time: %s, Start_set_time: %s" % (
            start_time, start_set_time,
            time.strftime("%Y-%m-%d %X", time.localtime(start_time)),
            time.strftime("%Y-%m-%d %X", time.localtime(start_set_time))))

        self.debug.info(u"[APP_TIMER]Start Time: %s[%s]" % (time.strftime("%X"), time.time()))

        return start_time, start_set_time, cycle

    # 创建循环定时
    def create_cycle_timer(self, page, now_time, set_start_time, set_end_time, loop, delay_s=120, cycle=False, loops=1):
        """
        :param page: 设置定时层
        :param now_time: 当前时间
        :param set_start_time: 启动时间时长
        :param set_end_time: 关闭时间时长
        :param loop: 循环模式
        :param delay_s: 定时设定与执行时间差
        :param cycle: 是否是类鱼缸模式的连续定时模式
        :param loops: 循环为永久循环时需要产出的时间对个数
        :return:
        """
        try:
            self.wait_widget(self.page[page]["delay_timer_button"])
            self.widget_click(self.page[page]["delay_timer"])
        except TimeoutException:
            pass

        try:
            self.wait_widget(self.page[page]["cycle_timer_button"])
        except TimeoutException:
            self.widget_click(self.page[page]["cycle_timer"],
                              self.page[page]["cycle_timer_button"])

        self.widget_click(self.page[page]["cycle_timer_state"],
                          self.page["cycle_timer_page"]["title"])

        self.widget_click(self.page["cycle_timer_page"]["open_time"],
                          self.page["cycle_timer_page"]["roll_h"])

        start_time, start_set_time = self.set_timer_roll(self.page["cycle_timer_page"]["roll_h"],
                                                         self.page["cycle_timer_page"]["roll_m"],
                                                         self.page["cycle_timer_page"]["open_time"],
                                                         now_time, set_start_time, cycle, delay_s)
        self.debug.info("[APP_TIMER]Start_time: %s[%s], Start_set_time: %s[%s]" % (
            time.strftime("%Y-%m-%d %X", time.localtime(start_time)), start_time,
            time.strftime("%Y-%m-%d %X", time.localtime(start_set_time)), start_set_time))

        # 判断设置后的滚轮是否与设定一致
        attr = self.ac.get_attribute(self.wait_widget(self.page["cycle_timer_page"]["open_time"]), "name")
        start_h, start_m = re.findall(u"(\d+)小时", attr), re.findall(u"(\d+)分钟", attr)
        if start_h:
            attr = "%02d:%02d" % (int(start_h[0]), int(start_m[0]))
        else:
            attr = "00:%02d" % int(start_m[0])
        self.debug.info("attr: %s; set start time: %s" % (attr, set_start_time[1]))
        if attr != set_start_time[1]:
            raise TimeoutException("timer set error")

        self.widget_click(self.page["cycle_timer_page"]["open_time"])
        try:
            self.wait_widget(self.page["cycle_timer_page"]["roll_h"])
            raise AssertionError()
        except TimeoutException:
            pass
        except AssertionError:
            raise TimeoutException("open time close error!")

        self.widget_click(self.page["cycle_timer_page"]["close_time"],
                          self.page["cycle_timer_page"]["roll_h"])

        end_time, end_set_time = self.set_timer_roll(self.page["cycle_timer_page"]["roll_h"],
                                                     self.page["cycle_timer_page"]["roll_m"],
                                                     self.page["cycle_timer_page"]["close_time"],
                                                     time.strftime("%X", time.localtime(start_set_time)),
                                                     set_end_time, True)
        self.debug.info("[APP_TIMER][%s, %s]End_time: %s, End_set_time: %s" % (
            end_time, end_set_time,
            time.strftime("%Y-%m-%d %X", time.localtime(end_time)),
            time.strftime("%Y-%m-%d  %X", time.localtime(end_set_time))))

        # 判断设置后的滚轮是否与设定一致
        attr = self.ac.get_attribute(self.wait_widget(self.page["cycle_timer_page"]["open_time"]), "name")
        start_h, start_m = re.findall(u"(\d+)小时", attr), re.findall(u"(\d+)分钟", attr)
        if start_h:
            attr = "%02d:%02d" % (int(start_h[0]), int(start_m[0]))
        else:
            attr = "00:%02d" % int(start_m[0])
        self.debug.info("attr: %s; set start time: %s" % (attr, set_start_time[1]))
        if attr != set_start_time[1]:
            raise TimeoutException("timer set error")

        self.widget_click(self.page["cycle_timer_page"]["close_time"])
        try:
            self.wait_widget(self.page["cycle_timer_page"]["roll_h"])
            raise AssertionError()
        except TimeoutException:
            pass
        except AssertionError:
            raise TimeoutException("open time close error!")

        # 设定循环次数
        if loop == u"永久循环":
            self.widget_click(self.page["cycle_timer_page"]["cycle_forever"])
        else:
            elem = self.widget_click(self.page["cycle_timer_page"]["cycle_time"])
            roll_value = int(self.ac.get_attribute(elem, "name"))
            set_value = int(re.findall(u"(\d)次", loop)[0])
            self.set_count_roll(self.page["cycle_timer_page"]["roll_c"], roll_value, set_value)

        self.debug.info("[APP_TIMER]Set loop: %s" % loop)
        if loop == u"永久循环":
            loop_count = loops  # 生成指定数量的时间对个数
        else:
            loop_count = int(re.findall(u"(\d+)次", loop)[0])  # 同时设置循环模式
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
        self.debug.info("loop_list:\n %s" % loop_list)

        self.launch_mode_timer("cycle_timer_page", page, False, start_time)

        return loop_list

    # 创建延迟定时
    def create_delay_timer(self, page, now_time, set_timer, delay_s=120, cycle=False):
        """
        return: None
        """
        try:
            self.wait_widget(self.page[page]["delay_timer_button"])
        except TimeoutException:
            self.widget_click(self.page[page]["delay_timer"],
                              self.page[page]["delay_timer_button"])

        self.widget_click(self.page[page]["delay_timer_state"],
                          self.page["delay_timer_page"]["title"])

        self.widget_click(self.page["delay_timer_page"]["delay_time"],
                          self.page["delay_timer_page"]["roll_h"])

        start_time, start_set_time = self.set_timer_roll(self.page["delay_timer_page"]["roll_h"],
                                                         self.page["delay_timer_page"]["roll_m"],
                                                         self.page["delay_timer_page"]["delay_time"],
                                                         now_time, set_timer, cycle, delay_s)
        self.debug.info("[APP_TIMER][%s, %s]Start_time: %s, Start_set_time: %s" % (
            start_time, start_set_time,
            time.strftime("%Y-%m-%d %X", time.localtime(start_time)),
            time.strftime("%Y-%m-%d %X", time.localtime(start_set_time))))

        # 判断设置后的滚轮是否与设定一致
        attr = self.ac.get_attribute(self.wait_widget(self.page["delay_timer_page"]["delay_time"]), "name")
        start_h, start_m = re.findall(u"(\d+)小时", attr), re.findall(u"(\d+)分钟", attr)
        if start_h:
            attr = "%02d:%02d" % (int(start_h[0]), int(start_m[0]))
        else:
            attr = "00:%02d" % int(start_m[0])
        self.debug.info("attr: %s; set start time: %s" % (attr, set_timer[1]))
        if attr != set_timer[1]:
            raise TimeoutException("timer set error")

        self.launch_mode_timer("delay_timer_page", page, False, start_time)

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
                     u"周日": "weekday"}

        attribute = self.ac.get_attribute(self.wait_widget(self.page[page]["repeat"]), "name").replace(u"\ue909", "")

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
            elif u"执行一次" in attribute:
                attribute = []
            elif u"周" in attribute:
                attribute = attribute.split(u"、")
            else:
                pass

            self.widget_click(self.page[page]["repeat"],
                              self.page["timer_repeat_page"]["title"])
            if loop == u"执行一次":
                self.widget_click(self.page["timer_repeat_page"]["repeat_button"])
                try:
                    self.wait_widget(self.page["timer_repeat_page"]["everyday"])
                except TimeoutException:
                    pass
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

                # 选择星期时，已存在的星期数是已经被勾选的，要取消需要再次点击；
                # 例：已有周期为周一，周五，需要设置的周期为周三，周五
                # 则实际操作为点击周一和周三，而周五不需要点击，因为周五已被选中，再点击周五则周五就会被取消选中
                # 代码通过下述公式计算，输入当前循环周期和需要设定的周期，输出为需要待操作的周期
                # 输入：当前[u"周一", u"周五"]，设定[u"周三", u"周五"]；
                # 输出：[u"周一", u"周三"]；
                result = list((set(attribute) | set(loop_attr)) - (set(attribute) & set(loop_attr)))
                for i in result:  # 根据计算元素点击
                    self.widget_click(self.page["timer_repeat_page"][loop_mode[i]])

            self.widget_click(self.page["timer_repeat_page"]["to_return"],
                              self.page[page]["title"])
            attribute = self.ac.get_attribute(self.wait_widget(self.page[page]["repeat"]), "name")
            if tmp not in attribute:
                raise TimeoutException("Cycle set error")

        if loop == u"执行一次":
            cycle = ["None"]
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
        if delay_times < 0:
            raise TimeoutException("Set time is before now time, delay time is: %s" % delay_times)

        element = self.wait_widget(self.page["control_device_page"]["power_state"])
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
    def delete_normal_timer(self, layer):
        while True:
            try:
                self.wait_widget(self.page["%s_timer_page" % layer]["has_normal_timer"])
                self.debug.info("[APP_INFO]%s has normal timer" % layer)

                index = 0
                elements = self.wait_widget(self.page["%s_timer_page" % layer]["normal_timer_modify"])
                for i, element in elements.items():
                    if element is not None and self.ac.get_attribute(element, "name") == u"定时开启":
                        index = i
                        break
                    elif element is not None and self.ac.get_attribute(element, "name") == u"定时关闭":
                        index = i
                        break

                new_value = copy.copy(self.page["%s_timer_page" % layer]["normal_timer_modify"])
                new_value[0] = new_value[0][index]
                self.widget_click(new_value)
                self.widget_click(self.page["timer_edit_popup"]["delete"])
            except TimeoutException:
                self.debug.info("[APP_INFO]%s has not normal timer" % layer)
                break

    # 关闭模式定时
    def delete_out_date_timer(self):
        page_elem = ["up", "mid", "down"]
        # 上层
        for layer in page_elem:
            while True:
                element = self.wait_widget(self.page["control_device_page"]["%s_timer_state" % layer])
                attribute = self.ac.get_attribute(element, "name")
                if u"今日无定时" not in attribute:
                    self.debug.info("[APP_INFO]%s has timer" % layer)
                    self.widget_click(self.page["control_device_page"]["%s_timer" % layer],
                                      self.page["%s_timer_page" % layer]["title"])

                    # 删除已经执行的普通定时（仍会显示今日无定时）
                    self.delete_normal_timer(layer)

                    if u"循环定时" in attribute:
                        self.debug.info("[APP_INFO]%s has cycle timer" % layer)
                        self.widget_click(self.page["%s_timer_page" % layer]["cycle_timer"],
                                          self.page["%s_timer_page" % layer]["cycle_timer_button"])

                        try:
                            self.widget_click(self.page["%s_timer_page" % layer]["cycle_timer_button"])
                        except TimeoutException:
                            self.widget_click(self.page["%s_timer_page" % layer]["cycle_timer"],
                                              self.page["%s_timer_page" % layer]["cycle_timer_button"])

                            self.widget_click(self.page["%s_timer_page" % layer]["cycle_timer_button"])

                        self.widget_click(self.page["%s_timer_page" % layer]["cycle_timer"])

                        self.widget_click(self.page["%s_timer_page" % layer]["to_return"],
                                          self.page["control_device_page"]["title"])
                    elif u"延时定时" in attribute:
                        self.debug.info("[APP_INFO]%s has delay timer" % layer)
                        self.widget_click(self.page["%s_timer_page" % layer]["delay_timer"],
                                          self.page["%s_timer_page" % layer]["delay_timer_button"])

                        try:
                            self.widget_click(self.page["%s_timer_page" % layer]["delay_timer_button"])
                        except TimeoutException:
                            self.widget_click(self.page["%s_timer_page" % layer]["delay_timer"],
                                              self.page["%s_timer_page" % layer]["delay_timer_button"])

                            self.widget_click(self.page["%s_timer_page" % layer]["delay_timer_button"])

                        self.widget_click(self.page["%s_timer_page" % layer]["delay_timer"])

                        self.widget_click(self.page["%s_timer_page" % layer]["to_return"],
                                          self.page["control_device_page"]["title"])
                    else:
                        self.widget_click(self.page["%s_timer_page" % layer]["to_return"],
                                          self.page["control_device_page"]["title"])
                else:
                    self.debug.info("[APP_INFO]%s has no timer" % layer)
                    break

    # 启动模式定时
    def launch_mode_timer(self, page, to_page, start_now, start_time=None):
        if not isinstance(start_now, bool):
            raise KeyError("start_now must be bool type")
        if start_now is True:
            try:
                self.widget_click(self.page[page]["launch"],
                                  self.page[to_page]["title"])
            except KeyError:
                self.widget_click(self.page[page]["saved"],
                                  self.page[to_page]["title"])
            self.debug.info(u"[APP_TIMER]Start Time: %s[%s]" % (time.strftime("%X"), time.time()))
        else:
            if start_time is None:
                raise KeyError("if start_now is False, start_time can`t be None type")
            end_time = time.time() + 5 * 60 + 30
            while True:
                if time.time() >= start_time:
                    try:
                        self.widget_click(self.page[page]["launch"],
                                          self.page[to_page]["title"])
                    except KeyError:
                        self.widget_click(self.page[page]["saved"],
                                          self.page[to_page]["title"])
                    self.debug.info(u"[APP_TIMER]Start Time: %s[%s]" % (time.strftime("%X"), time.time()))
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
            self.debug.info("[APP_INFO]23:01_elec_bill: %s" % elec_bill)

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
            self.debug.info("[APP_INFO]23:01_elec: %s" % elec)

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
        self.debug.info("[APP_INFO]%02d:01_elec_bill: %s" % (check_time, elec_bill))

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
        self.debug.info("[APP_INFO]%02d:01_elec: %s" % (check_time, elec))

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

    # 启动按钮log检测线程启动函数
    def input_serial_command(self, *args):
        self.command_dict = {"power": [{"_f133u_uart_recv_event": 1}],
                             "set_cycle_timer": [{"bull_timer_pluse_start": 1}],
                             "launch_cycle_timer_on": [{"bull_timer_pluse_exe Pluse Timer": 0}],
                             "launch_cycle_timer_off": [{"]Pluse Timer": 0}],
                             "set_delay_timer": [{"bull_joy_countdown_timer_set countdown_timer": 0}],
                             "launch_delay_timer": [{"Count_Down_Time": 1}],
                             "set_normal_timer": [{"bull_joy_base_timer_set base_timer": 3}],
                             "launch_normal_timer_once": [{"Once Timer exe over": 0}],
                             "launch_normal_timer": [{"Repeat Timer exe over": 0}],
                             "device_info": [{"]control data send buf": 1}],
                             "device_mac": [{"<MAC": 0}]}
        tmp = {}
        command = {}
        command_list = []
        self.queue_dict = {}

        for i in args:
            tmp[i] = self.command_dict[i]

        for k, v in tmp.items():
            command_list = command_list + v

        for i in command_list:
            command = dict(command, **i)

        for i in command:
            self.queue_dict[i] = Queue.Queue()
        # command = [dict(command, **command_list[i]) for i in args][0]

        while True:
            try:
                self.serial_command_queue.get_nowait()
            except Queue.Empty:
                break

        self.serial_command_queue.put_nowait((False, "", ""))  # 待机log分析
        for k, v in self.queue_dict.items():
            while True:
                try:
                    v.get_nowait()
                except Queue.Empty:
                    break

        self.serial_command_queue.put_nowait((True, command, self.serial_result_queue))

        self.check_flag = 1

    def check_serial_result(self):
        self.serial_command_queue.put_nowait((False, "", ""))
        while True:
            if not self.serial_command_queue.qsize():
                break
            time.sleep(0.1)

        if self.check_flag:
            while True:
                try:
                    tmp = self.serial_result_queue.get_nowait()
                except Queue.Empty:
                    break

                for k, v in self.queue_dict.items():
                    if k in tmp:
                        v.put_nowait(tmp)

            self.check_flag = 0

    # 检查启动按钮状态
    def check_serial_button_state(self):
        """
        使用消息队列提取所有继电器状态并进行筛选，返回按照时间顺序排列的开关状态列表
        :return: [time, 3层开关状态"000"]
        list消息etc：[([2018-01-03 09:47:25:957]_f133u_uart_recv_event: cha_ru [2018-01-03 09:47:25:957]FF 02 00 07 09 FE cha_ru )]
        """
        key = "power"
        self.check_serial_result()
        result_queue = Queue.Queue()

        command = self.command_dict[key][0].keys()[0]

        tmp_queue = self.queue_dict[command]

        print(command, tmp_queue.qsize())

        while True:
            try:
                serial_result = tmp_queue.get_nowait()
            except Queue.Empty:
                break

            print(sys._getframe().f_code.co_name, serial_result)
            value = bin(int(re.findall("FF .+ (.+?) .+? FE", serial_result)[0], 16))[2:].zfill(4)
            now_time = time.mktime(time.strptime(serial_result[1:20], "%Y-%m-%d %X"))
            if value[0] == "0":
                result_queue.put_nowait([now_time, value[1:]])

        result = []
        while True:
            try:
                result.append(result_queue.get_nowait())
            except Queue.Empty:
                break

        self.debug.info("btn_state_list: %s" % result)
        return result

    # 检查循环定时设置状态
    def check_serial_set_cycle_timer(self):
        """
        使用消息队列提取所有循环定时设置状态并进行筛选，返回按照时间顺序排列的循环定时设置状态列表
        :return: [time, id, times]
        list消息etc：[([2018-01-03 09:47:25:957]bull_timer_pluse_start : cha_ru [2018-01-03 09:47:25:957]the 2 timer,  the timer ID 145991072,keep_ontime 0:1 set time 60s , keep_offtime  0:1 set time 60s, times 255 cha_ru )]
        """
        key = "set_cycle_timer"
        self.check_serial_result()
        result_queue = Queue.Queue()

        command = self.command_dict[key][0].keys()[0]

        tmp_queue = self.queue_dict[command]

        print(command, tmp_queue.qsize())

        while True:
            try:
                serial_result = tmp_queue.get_nowait()
            except Queue.Empty:
                break

            print(sys._getframe().f_code.co_name, serial_result)
            value = re.findall("ID (.+?),.+times (.+?) cha_ru ", serial_result)[0]
            now_time = time.mktime(time.strptime(serial_result[1:20], "%Y-%m-%d %X"))
            result_queue.put_nowait([now_time] + list(value))

        result = []
        while True:
            try:
                result.append(result_queue.get_nowait())
            except Queue.Empty:
                break

        self.debug.info("set_cycle_timer_list: %s" % result)
        return result

    # 检查循环定时执行开状态
    def check_serial_launch_cycle_timer_on(self):
        """
        使用消息队列提取所有循环定时执行开状态并进行筛选，返回按照时间顺序排列的循环定时执行开状态列表
        :return: [time, id, times]
        list消息etc：[([2018-01-03 09:47:25:957]bull_timer_pluse_exe Pluse Timer: the 2 timer, the timer ID 145991072,times 255 cha_ru )]
        """
        key = "launch_cycle_timer_on"
        self.check_serial_result()
        result_queue = Queue.Queue()

        command = self.command_dict[key][0].keys()[0]

        tmp_queue = self.queue_dict[command]

        print(command, tmp_queue.qsize())

        while True:
            try:
                serial_result = tmp_queue.get_nowait()
            except Queue.Empty:
                break

            print(sys._getframe().f_code.co_name, serial_result)
            value = re.findall("ID (.+?),times (.+?) cha_ru ", serial_result)[0]
            now_time = time.mktime(time.strptime(serial_result[1:20], "%Y-%m-%d %X"))
            result_queue.put_nowait([now_time] + list(value))

        result = []
        while True:
            try:
                result.append(result_queue.get_nowait())
            except Queue.Empty:
                break

        self.debug.info("launch_cycle_timer_on_list: %s" % result)
        return result

    # 检查循环定时执行关状态
    def check_serial_launch_cycle_timer_off(self):
        """
        使用消息队列提取所有循环定时执行关状态并进行筛选，返回按照时间顺序排列的循环定时执行关状态列表
        :return: [time, id, times]
        list消息etc：[([2018-01-03 09:47:25:957]Pluse Timer: the 2 timer, the timer ID 145991072,times 255 cha_ru )]
        """
        key = "launch_cycle_timer_off"
        self.check_serial_result()
        result_queue = Queue.Queue()

        command = self.command_dict[key][0].keys()[0]

        tmp_queue = self.queue_dict[command]

        print(command, tmp_queue.qsize())

        while True:
            try:
                serial_result = tmp_queue.get_nowait()
            except Queue.Empty:
                break

            print(sys._getframe().f_code.co_name, serial_result)
            value = re.findall("ID (.+?),times (.+?) cha_ru ", serial_result)[0]
            now_time = time.mktime(time.strptime(serial_result[1:20], "%Y-%m-%d %X"))
            result_queue.put_nowait([now_time] + list(value))

        result = []
        while True:
            try:
                result.append(result_queue.get_nowait())
            except Queue.Empty:
                break

        self.debug.info("launch_cycle_timer_off_list: %s" % result)
        return result

    # 检查延迟定时设置状态
    def check_serial_set_delay_timer(self):
        """
        使用消息队列提取所有延迟定时设置状态并进行筛选，返回按照时间顺序排列的延迟定时设置状态列表
        :return: [time, id]
        list消息etc：[([2018-01-03 09:47:25:957]bull_joy_countdown_timer_set countdown_timer: id : 177483693, state : 1, version: 18, interval : 60 cha_ru )]
        """
        key = "set_delay_timer"
        self.check_serial_result()
        result_queue = Queue.Queue()

        command = self.command_dict[key][0].keys()[0]

        tmp_queue = self.queue_dict[command]

        print(command, tmp_queue.qsize())

        while True:
            try:
                serial_result = tmp_queue.get_nowait()
            except Queue.Empty:
                break

            print(sys._getframe().f_code.co_name, serial_result)
            value = re.findall("id : (.+?),", serial_result)
            now_time = time.mktime(time.strptime(serial_result[1:20], "%Y-%m-%d %X"))
            result_queue.put_nowait([now_time] + value)

        result = []
        while True:
            try:
                result.append(result_queue.get_nowait())
            except Queue.Empty:
                break

        self.debug.info("set_delay_timer_list: %s" % result)
        return result

    # 检查延迟定时执行状态
    def check_serial_launch_delay_timer(self):
        """
        使用消息队列提取所有延迟定时执行状态并进行筛选，返回按照时间顺序排列的延迟定时执行状态列表
        :return: [time, id]
        list消息etc：[([2018-01-03 09:47:25:957]Count_Down_Time cha_ru [2018-01-03 09:47:25:957]the 3 timer ,the timer ID 177483693 cha_ru )]
        """
        key = "launch_delay_timer"
        self.check_serial_result()
        result_queue = Queue.Queue()

        command = self.command_dict[key][0].keys()[0]

        tmp_queue = self.queue_dict[command]

        print(command, tmp_queue.qsize())

        while True:
            try:
                serial_result = tmp_queue.get_nowait()
            except Queue.Empty:
                break

            print(sys._getframe().f_code.co_name, serial_result)
            value = re.findall("ID (.+?) cha_ru ", serial_result)
            now_time = time.mktime(time.strptime(serial_result[1:20], "%Y-%m-%d %X"))
            result_queue.put_nowait([now_time] + value)

        result = []
        while True:
            try:
                result.append(result_queue.get_nowait())
            except Queue.Empty:
                break

        self.debug.info("launch_delay_timer_list: %s" % result)
        return result

    # 检查普通定时设置状态
    def check_serial_set_normal_timer(self):
        """
        使用消息队列提取所有普通定时设置状态并进行筛选，返回按照时间顺序排列的普通定时设置状态列表
        :return: [time, id, set_time, week, 3层定时开关状态"0FF"]
        list消息etc：[([2018-01-03 09:47:25:957]bull_joy_base_timer_set base_timer:  id : 201033350, state : 1, version: 1 cha_ru [
        2018-01-03 09:47:25:957]2018-1-4  9:58:0  week:0 cha_ru [
        2018-01-03 09:47:25:957]BASE TIMER TRANK BUF: cha_ru [
        2018-01-03 09:47:25:957]01 FF FF 00 00 00 00 00 00 00 00 00 00 00 00 00 cha_ru )]
        """
        key = "set_normal_timer"
        self.check_serial_result()
        result_queue = Queue.Queue()

        command = self.command_dict[key][0].keys()[0]

        tmp_queue = self.queue_dict[command]

        print(command, tmp_queue.qsize())

        while True:
            try:
                serial_result = tmp_queue.get_nowait()
            except Queue.Empty:
                break

            print(sys._getframe().f_code.co_name, serial_result)
            value = list(re.findall("id : (.+?),.+](.+?) +week:(.+?) cha_ru .+](.+? .+? .+?) .+",
                                    serial_result)[0])
            value[1] = value[1].replace("  ", " ")
            value[3] = value[3].replace("FF", "").replace("00", "0").replace("01", "1").replace(" ", "")
            now_time = time.mktime(time.strptime(serial_result[1:20], "%Y-%m-%d %X"))
            result_queue.put_nowait([now_time] + value)

        result = []
        while True:
            try:
                result.append(result_queue.get_nowait())
            except Queue.Empty:
                break

        self.debug.info("set_normal_timer_list: %s" % result)
        return result

    # 检查普通定时执行状态
    def check_serial_launch_normal_timer(self):
        """
        :param once: 循环
        使用消息队列提取所有普通定时执行状态并进行筛选，返回按照时间顺序排列的普通定时执行状态列表
        :return: [time, id, launch_time, week]
        list消息etc：[([2018-01-03 09:47:25:957]Repeat Timer exe over: the 1 timer,the timer ID 110458020, start time 10:1  , week:4 cha_ru )]
        """
        key = "launch_normal_timer"
        self.check_serial_result()
        result_queue = Queue.Queue()

        command = self.command_dict[key][0].keys()[0]

        tmp_queue = self.queue_dict[command]

        print(command, tmp_queue.qsize())

        while True:
            try:
                serial_result = tmp_queue.get_nowait()
            except Queue.Empty:
                break

            print(sys._getframe().f_code.co_name, serial_result)
            value = list(re.findall("ID (.+?), start time (.+?) +, week:(.+?) cha_ru ", serial_result)[0])
            value[1] = "%s%s%s" % ("0-0-0 ", value[1][2:], ":0")
            now_time = time.mktime(time.strptime(serial_result[1:20], "%Y-%m-%d %X"))
            result_queue.put_nowait([now_time] + value)

        result = []
        while True:
            try:
                result.append(result_queue.get_nowait())
            except Queue.Empty:
                break

        self.debug.info("launch_normal_timer_list: %s" % result)
        return result

    # 检查普通定时执行状态单次
    def check_serial_launch_normal_timer_once(self):
        """
        :param once: 执行一次/循环
        使用消息队列提取所有普通定时执行状态并进行筛选，返回按照时间顺序排列的普通定时执行状态列表
        :return: [time, id, launch_time, week/None]
        list消息etc：[([2018-01-03 09:47:25:957]Once Timer exe over  the 1 timer, the timer ID 150954030, start time 18-1-4 9:58 cha_ru )]
        """
        key = "launch_normal_timer_once"
        self.check_serial_result()
        result_queue = Queue.Queue()

        command = self.command_dict[key][0].keys()[0]

        tmp_queue = self.queue_dict[command]

        print(command, tmp_queue.qsize())

        while True:
            try:
                serial_result = tmp_queue.get_nowait()
            except Queue.Empty:
                break

            print(sys._getframe().f_code.co_name, serial_result)
            value = list(re.findall("ID (.+?), start time (.+) cha_ru ", serial_result)[0])
            value[1] = "%s%s%s" % (time.strftime("%Y"), value[1][2:], ":0")
            now_time = time.mktime(time.strptime(serial_result[1:20], "%Y-%m-%d %X"))
            result_queue.put_nowait([now_time] + value)

        result = []
        while True:
            try:
                result.append(result_queue.get_nowait())
            except Queue.Empty:
                break

        self.debug.info("launch_normal_timer_once_list: %s" % result)
        return result

    # 传入定时设置信息，获取定时ID
    def get_timer_id_from_set(self, *args):
        """
        从设置定时获取定时id
        :param args:
        :return: ["id_1", "id_2", "id_3",...]
        """
        timer_list = []
        for tmp in args:
            for i in tmp:
                timer_list.append(i[1])

        self.debug.info("timer_list: %s" % timer_list)
        return timer_list

    # 传入定时ID列表和定时执行信息，获取ID对应执行信息
    def get_layer_timer_from_launch(self, timer_list, **kwargs):
        """
        根据定时id获取执行结果
        :param timer_id:
        :return: {timer_id: {"delay": [[args1],[args2],...]...}}
        """
        result = {}
        for timer_id in timer_list:
            result[timer_id] = {}
            for k in kwargs:
                result[timer_id][k] = []

        for k, v in kwargs.items():
            for i in v:
                timer_id = i[1]
                result[timer_id][k].append(i)

        self.debug.info("result: %s" % result)
        return result

    # 获取设备安全模式，记忆模式，防雷状态
    def check_device_info_state(self, wait=False):
        """

        :return:
        """
        key = "device_info"
        if wait:
            while True:
                if self.serial_result_queue.qsize():
                    break
                time.sleep(0.1)
        self.check_serial_result()
        result_queue = Queue.Queue()

        command = self.command_dict[key][0].keys()[0]

        tmp_queue = self.queue_dict[command]

        print(command, tmp_queue.qsize())

        while True:
            try:
                serial_result = tmp_queue.get_nowait()
            except Queue.Empty:
                break

            print(sys._getframe().f_code.co_name, serial_result)
            value = re.findall(".+](.+?) cha_ru ", serial_result)[0][:-15].split(" ")
            value[7], value[8] = value[7] + value[8], value[9] + value[10]
            value = value[:-2]
            for i in xrange(7):
                value[i] = value[i].replace("00", "0").replace("01", "1")
            now_time = time.mktime(time.strptime(serial_result[1:20], "%Y-%m-%d %X"))
            result_queue.put_nowait([now_time] + value)

        result = []
        while True:
            try:
                result.append(result_queue.get_nowait())
            except Queue.Empty:
                break

        self.debug.info("device_info_state_list: %s" % result)
        return result

    # 获取指定时间点的最后一个状态
    def get_last_device_info_state(self, value, end_time):
        result = []
        for i in value:
            if i[0] <= end_time:
                result = i
            else:
                break

        self.debug.info("device_info_state: %s" % result)
        return result
