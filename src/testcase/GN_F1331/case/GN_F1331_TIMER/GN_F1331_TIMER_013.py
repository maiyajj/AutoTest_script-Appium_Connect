# coding=utf-8
from src.testcase.GN_F1331.WidgetOperation import *


class GNF1331Timer13(WidgetOperation):
    @case_run(False)
    def run(self):
        self.case_module = u"定时器(#9)"  # 用例所属模块
        self.case_title = u'随机各层设置9组普通定时，执行完成后删除原有定时，再次设置9组普通定时'  # 用例名称
        self.zentao_id = "101"  # 禅道ID

    # 用例动作
    def case(self):
        self.choose_home_device(conf["MAC"][self.app][self.device_mac])

        self.delete_out_date_timer()
        self.delete_normal_timer_all()

        self.set_power("main_button_off")

        self.input_serial_command("power", "set_normal_timer", "launch_normal_timer_once")

        # 第一遍执行
        # 上层
        self.widget_click(self.page["control_device_page"]["up_timer"],
                          self.page["up_timer_page"]["title"])

        now = time.strftime("%H:%M")

        time_1, time_2, time_3 = 5, 10, 15
        start_time_1, set_time_1, cycle_1 = self.create_normal_timer("up_timer_page", now, time_1, "power_on")
        start_time_2, set_time_2, cycle_2 = self.create_normal_timer("up_timer_page", now, time_2, "power_off")
        start_time_3, set_time_3, cycle_3 = self.create_normal_timer("up_timer_page", now, time_3, "power_on")

        self.widget_click(self.page["up_timer_page"]["to_return"],
                          self.page["control_device_page"]["title"])

        # 中层
        self.widget_click(self.page["control_device_page"]["mid_timer"],
                          self.page["mid_timer_page"]["title"])

        now = time.strftime("%H:%M")

        time_4, time_5, time_6 = 1, 2, 3
        start_time_4, set_time_4, cycle_4 = self.create_normal_timer("mid_timer_page", now, time_4, "power_on")
        start_time_5, set_time_5, cycle_5 = self.create_normal_timer("mid_timer_page", now, time_5, "power_off")
        start_time_6, set_time_6, cycle_6 = self.create_normal_timer("mid_timer_page", now, time_6, "power_on")

        self.widget_click(self.page["mid_timer_page"]["to_return"],
                          self.page["control_device_page"]["title"])

        # 下层
        self.widget_click(self.page["control_device_page"]["down_timer"],
                          self.page["down_timer_page"]["title"])

        now = time.strftime("%H:%M")

        time_7, time_8, time_9 = 1, 2, 3
        start_time_7, set_time_7, cycle_7 = self.create_normal_timer("down_timer_page", now, time_7, "power_on")
        start_time_8, set_time_8, cycle_8 = self.create_normal_timer("down_timer_page", now, time_8, "power_off")
        start_time_9, set_time_9, cycle_9 = self.create_normal_timer("down_timer_page", now, time_9, "power_on")

        self.widget_click(self.page["down_timer_page"]["to_return"],
                          self.page["control_device_page"]["title"])

        max_time = max(set_time_1, set_time_2, set_time_3, set_time_4, set_time_5,
                       set_time_6, set_time_7, set_time_8, set_time_9)
        while True:
            if time.time() > max_time + 10:
                break
            print(time.time())
            time.sleep(1)

        # 第二遍执行
        self.delete_normal_timer_all()
        # 上层
        self.widget_click(self.page["control_device_page"]["up_timer"],
                          self.page["up_timer_page"]["title"])

        now = time.strftime("%H:%M")

        time_10, time_11, time_12 = 1, 2, 3
        start_time_10, set_time_10, cycle_10 = self.create_normal_timer("up_timer_page", now, time_10, "power_off")
        start_time_11, set_time_11, cycle_11 = self.create_normal_timer("up_timer_page", now, time_11, "power_on")
        start_time_12, set_time_12, cycle_12 = self.create_normal_timer("up_timer_page", now, time_12, "power_off")

        self.widget_click(self.page["up_timer_page"]["to_return"],
                          self.page["control_device_page"]["title"])

        # 中层
        self.widget_click(self.page["control_device_page"]["mid_timer"],
                          self.page["mid_timer_page"]["title"])

        now = time.strftime("%H:%M")

        time_13, time_14, time_15 = 1, 2, 3
        start_time_13, set_time_13, cycle_13 = self.create_normal_timer("mid_timer_page", now, time_13, "power_off")
        start_time_14, set_time_14, cycle_14 = self.create_normal_timer("mid_timer_page", now, time_14, "power_on")
        start_time_15, set_time_15, cycle_15 = self.create_normal_timer("mid_timer_page", now, time_15, "power_off")

        self.widget_click(self.page["mid_timer_page"]["to_return"],
                          self.page["control_device_page"]["title"])

        # 下层
        self.widget_click(self.page["control_device_page"]["down_timer"],
                          self.page["down_timer_page"]["title"])

        now = time.strftime("%H:%M")

        time_16, time_17, time_18 = 1, 2, 3
        start_time_16, set_time_16, cycle_16 = self.create_normal_timer("down_timer_page", now, time_16, "power_off")
        start_time_17, set_time_17, cycle_17 = self.create_normal_timer("down_timer_page", now, time_17, "power_on")
        start_time_18, set_time_18, cycle_18 = self.create_normal_timer("down_timer_page", now, time_18, "power_off")

        max_time = max(set_time_10, set_time_11, set_time_12, set_time_13, set_time_14,
                       set_time_15, set_time_16, set_time_17, set_time_18)
        while True:
            if time.time() > max_time + 10:
                break
            print(time.time())
            time.sleep(1)

        #####
        # 开关
        btn_dict = self.check_button_state(set_time_1, set_time_2, set_time_3, set_time_4, set_time_5, set_time_6,
                                           set_time_7, set_time_8, set_time_9, set_time_10, set_time_11, set_time_12,
                                           set_time_13, set_time_14, set_time_15, set_time_16, set_time_17, set_time_18)
        # 定时设置
        set_normal_dict = self.check_set_normal_timer(start_time_1, start_time_2, start_time_3, start_time_4,
                                                      start_time_5, start_time_6, start_time_7, start_time_8,
                                                      start_time_9, start_time_10, start_time_11, start_time_12,
                                                      start_time_13, start_time_14, start_time_15, start_time_16,
                                                      start_time_17, start_time_18)
        # 定时执行
        launch_normal_once_dict = self.check_launch_normal_timer_once(set_normal_dict, set_time_1, set_time_2,
                                                                      set_time_3, set_time_4, set_time_5, set_time_6,
                                                                      set_time_7, set_time_8, set_time_9, set_time_10,
                                                                      set_time_11, set_time_12, set_time_13,
                                                                      set_time_14, set_time_15, set_time_16,
                                                                      set_time_17, set_time_18)

        # 第一遍执行
        # 上层
        # 定时1
        # 设置
        set_timer = set_normal_dict[start_time_1]
        s_time, s_id, s_week = set_timer[0], set_timer[1], set_timer[3]
        result = [s_time is not None,
                  s_week == "0000000"]
        if False in result:
            raise TimeoutException("device state error, current: %s, result: %s" % (s_time, result))
        # 执行
        launch_timer = launch_normal_once_dict[set_time_1]
        l_time, l_id = launch_timer[s_id][0], launch_timer[s_id][1]
        result = [l_time is not None]
        if False in result:
            raise TimeoutException("device state error, current: %s, result: %s" % (launch_timer, result))

        # 定时2
        # 设置
        set_timer = set_normal_dict[start_time_2]
        s_time, s_id, s_week = set_timer[0], set_timer[1], set_timer[3]
        result = [s_time is not None,
                  s_week == "0000000"]
        if False in result:
            raise TimeoutException("device state error, current: %s, result: %s" % (s_time, result))
        # 执行
        launch_timer = launch_normal_once_dict[set_time_2]
        l_time, l_id = launch_timer[s_id][0], launch_timer[s_id][1]
        result = [l_time is not None]
        if False in result:
            raise TimeoutException("device state error, current: %s, result: %s" % (launch_timer, result))

        # 定时3
        # 设置
        set_timer = set_normal_dict[start_time_3]
        s_time, s_id, s_week = set_timer[0], set_timer[1], set_timer[3]
        result = [s_time is not None,
                  s_week == "0000000"]
        if False in result:
            raise TimeoutException("device state error, current: %s, result: %s" % (s_time, result))
        # 执行
        launch_timer = launch_normal_once_dict[set_time_3]
        l_time, l_id = launch_timer[s_id][0], launch_timer[s_id][1]
        result = [l_time is not None]
        if False in result:
            raise TimeoutException("device state error, current: %s, result: %s" % (launch_timer, result))

        # 中层
        # 定时4
        # 设置
        set_timer = set_normal_dict[start_time_4]
        s_time, s_id, s_week = set_timer[0], set_timer[1], set_timer[3]
        result = [s_time is not None,
                  s_week == "0000000"]
        if False in result:
            raise TimeoutException("device state error, current: %s, result: %s" % (s_time, result))
        # 执行
        launch_timer = launch_normal_once_dict[set_time_4]
        l_time, l_id = launch_timer[s_id][0], launch_timer[s_id][1]
        result = [l_time is not None]
        if False in result:
            raise TimeoutException("device state error, current: %s, result: %s" % (launch_timer, result))

        # 定时5
        # 设置
        set_timer = set_normal_dict[start_time_5]
        s_time, s_id, s_week = set_timer[0], set_timer[1], set_timer[3]
        result = [s_time is not None,
                  s_week == "0000000"]
        if False in result:
            raise TimeoutException("device state error, current: %s, result: %s" % (s_time, result))
        # 执行
        launch_timer = launch_normal_once_dict[set_time_5]
        l_time, l_id = launch_timer[s_id][0], launch_timer[s_id][1]
        result = [l_time is not None]
        if False in result:
            raise TimeoutException("device state error, current: %s, result: %s" % (launch_timer, result))

        # 定时6
        # 设置
        set_timer = set_normal_dict[start_time_6]
        s_time, s_id, s_week = set_timer[0], set_timer[1], set_timer[3]
        result = [s_time is not None,
                  s_week == "0000000"]
        if False in result:
            raise TimeoutException("device state error, current: %s, result: %s" % (s_time, result))
        # 执行
        launch_timer = launch_normal_once_dict[set_time_6]
        l_time, l_id = launch_timer[s_id][0], launch_timer[s_id][1]
        result = [l_time is not None]
        if False in result:
            raise TimeoutException("device state error, current: %s, result: %s" % (launch_timer, result))

        # 下层
        # 定时7
        # 设置
        set_timer = set_normal_dict[start_time_7]
        s_time, s_id, s_week = set_timer[0], set_timer[1], set_timer[3]
        result = [s_time is not None,
                  s_week == "0000000"]
        if False in result:
            raise TimeoutException("device state error, current: %s, result: %s" % (s_time, result))
        # 执行
        launch_timer = launch_normal_once_dict[set_time_7]
        l_time, l_id = launch_timer[s_id][0], launch_timer[s_id][1]
        result = [l_time is not None]
        if False in result:
            raise TimeoutException("device state error, current: %s, result: %s" % (launch_timer, result))

        # 定时8
        # 设置
        set_timer = set_normal_dict[start_time_8]
        s_time, s_id, s_week = set_timer[0], set_timer[1], set_timer[3]
        result = [s_time is not None,
                  s_week == "0000000"]
        if False in result:
            raise TimeoutException("device state error, current: %s, result: %s" % (s_time, result))
        # 执行
        launch_timer = launch_normal_once_dict[set_time_8]
        l_time, l_id = launch_timer[s_id][0], launch_timer[s_id][1]
        result = [l_time is not None]
        if False in result:
            raise TimeoutException("device state error, current: %s, result: %s" % (launch_timer, result))

        # 定时9
        # 设置
        set_timer = set_normal_dict[start_time_9]
        s_time, s_id, s_week = set_timer[0], set_timer[1], set_timer[3]
        result = [s_time is not None,
                  s_week == "0000000"]
        if False in result:
            raise TimeoutException("device state error, current: %s, result: %s" % (s_time, result))
        # 执行
        launch_timer = launch_normal_once_dict[set_time_9]
        l_time, l_id = launch_timer[s_id][0], launch_timer[s_id][1]
        result = [l_time is not None]
        if False in result:
            raise TimeoutException("device state error, current: %s, result: %s" % (launch_timer, result))

        # 第二遍执行
        # 上层
        # 定时10
        # 设置
        set_timer = set_normal_dict[start_time_10]
        s_time, s_id, s_week = set_timer[0], set_timer[1], set_timer[3]
        result = [s_time is not None,
                  s_week == "0000000"]
        if False in result:
            raise TimeoutException("device state error, current: %s, result: %s" % (s_time, result))
        # 执行
        launch_timer = launch_normal_once_dict[set_time_10]
        l_time, l_id = launch_timer[s_id][0], launch_timer[s_id][1]
        result = [l_time is not None]
        if False in result:
            raise TimeoutException("device state error, current: %s, result: %s" % (launch_timer, result))

        # 定时11
        # 设置
        set_timer = set_normal_dict[start_time_11]
        s_time, s_id, s_week = set_timer[0], set_timer[1], set_timer[3]
        result = [s_time is not None,
                  s_week == "0000000"]
        if False in result:
            raise TimeoutException("device state error, current: %s, result: %s" % (s_time, result))
        # 执行
        launch_timer = launch_normal_once_dict[set_time_11]
        l_time, l_id = launch_timer[s_id][0], launch_timer[s_id][1]
        result = [l_time is not None]
        if False in result:
            raise TimeoutException("device state error, current: %s, result: %s" % (launch_timer, result))

        # 定时12
        # 设置
        set_timer = set_normal_dict[start_time_12]
        s_time, s_id, s_week = set_timer[0], set_timer[1], set_timer[3]
        result = [s_time is not None,
                  s_week == "0000000"]
        if False in result:
            raise TimeoutException("device state error, current: %s, result: %s" % (s_time, result))
        # 执行
        launch_timer = launch_normal_once_dict[set_time_12]
        l_time, l_id = launch_timer[s_id][0], launch_timer[s_id][1]
        result = [l_time is not None]
        if False in result:
            raise TimeoutException("device state error, current: %s, result: %s" % (launch_timer, result))

        # 中层
        # 定时13
        # 设置
        set_timer = set_normal_dict[start_time_13]
        s_time, s_id, s_week = set_timer[0], set_timer[1], set_timer[3]
        result = [s_time is not None,
                  s_week == "0000000"]
        if False in result:
            raise TimeoutException("device state error, current: %s, result: %s" % (s_time, result))
        # 执行
        launch_timer = launch_normal_once_dict[set_time_13]
        l_time, l_id = launch_timer[s_id][0], launch_timer[s_id][1]
        result = [l_time is not None]
        if False in result:
            raise TimeoutException("device state error, current: %s, result: %s" % (launch_timer, result))

        # 定时14
        # 设置
        set_timer = set_normal_dict[start_time_14]
        s_time, s_id, s_week = set_timer[0], set_timer[1], set_timer[3]
        result = [s_time is not None,
                  s_week == "0000000"]
        if False in result:
            raise TimeoutException("device state error, current: %s, result: %s" % (s_time, result))
        # 执行
        launch_timer = launch_normal_once_dict[set_time_14]
        l_time, l_id = launch_timer[s_id][0], launch_timer[s_id][1]
        result = [l_time is not None]
        if False in result:
            raise TimeoutException("device state error, current: %s, result: %s" % (launch_timer, result))

        # 定时15
        # 设置
        set_timer = set_normal_dict[start_time_15]
        s_time, s_id, s_week = set_timer[0], set_timer[1], set_timer[3]
        result = [s_time is not None,
                  s_week == "0000000"]
        if False in result:
            raise TimeoutException("device state error, current: %s, result: %s" % (s_time, result))
        # 执行
        launch_timer = launch_normal_once_dict[set_time_15]
        l_time, l_id = launch_timer[s_id][0], launch_timer[s_id][1]
        result = [l_time is not None]
        if False in result:
            raise TimeoutException("device state error, current: %s, result: %s" % (launch_timer, result))

        # 下层
        # 定时16
        # 设置
        set_timer = set_normal_dict[start_time_16]
        s_time, s_id, s_week = set_timer[0], set_timer[1], set_timer[3]
        result = [s_time is not None,
                  s_week == "0000000"]
        if False in result:
            raise TimeoutException("device state error, current: %s, result: %s" % (s_time, result))
        # 执行
        launch_timer = launch_normal_once_dict[set_time_16]
        l_time, l_id = launch_timer[s_id][0], launch_timer[s_id][1]
        result = [l_time is not None]
        if False in result:
            raise TimeoutException("device state error, current: %s, result: %s" % (launch_timer, result))

        # 定时17
        # 设置
        set_timer = set_normal_dict[start_time_17]
        s_time, s_id, s_week = set_timer[0], set_timer[1], set_timer[3]
        result = [s_time is not None,
                  s_week == "0000000"]
        if False in result:
            raise TimeoutException("device state error, current: %s, result: %s" % (s_time, result))
        # 执行
        launch_timer = launch_normal_once_dict[set_time_17]
        l_time, l_id = launch_timer[s_id][0], launch_timer[s_id][1]
        result = [l_time is not None]
        if False in result:
            raise TimeoutException("device state error, current: %s, result: %s" % (launch_timer, result))

        # 定时18
        # 设置
        set_timer = set_normal_dict[start_time_18]
        s_time, s_id, s_week = set_timer[0], set_timer[1], set_timer[3]
        result = [s_time is not None,
                  s_week == "0000000"]
        if False in result:
            raise TimeoutException("device state error, current: %s, result: %s" % (s_time, result))
        # 执行
        launch_timer = launch_normal_once_dict[set_time_18]
        l_time, l_id = launch_timer[s_id][0], launch_timer[s_id][1]
        result = [l_time is not None]
        if False in result:
            raise TimeoutException("device state error, current: %s, result: %s" % (launch_timer, result))

        # 开关
        # 第一遍执行
        # 上层关→开
        btn = btn_dict[set_time_1]
        btn_up = btn[1][0]
        result = [btn_up == "1"]
        if False in result:
            raise TimeoutException("device state error, current: %s, result: %s" % (btn, result))
        # 上层开→关
        btn = btn_dict[set_time_2]
        btn_up = btn[1][0]
        result = [btn_up == "0"]
        if False in result:
            raise TimeoutException("device state error, current: %s, result: %s" % (btn, result))
        # 上层关→开
        btn = btn_dict[set_time_3]
        btn_up = btn[1][0]
        result = [btn_up == "1"]
        if False in result:
            raise TimeoutException("device state error, current: %s, result: %s" % (btn, result))

        # 中层关→开
        btn = btn_dict[set_time_4]
        btn_mid = btn[1][1]
        result = [btn_mid == "1"]
        if False in result:
            raise TimeoutException("device state error, current: %s, result: %s" % (btn, result))
        # 中层开→关
        btn = btn_dict[set_time_5]
        btn_mid = btn[1][1]
        result = [btn_mid == "0"]
        if False in result:
            raise TimeoutException("device state error, current: %s, result: %s" % (btn, result))
        # 中层关→开
        btn = btn_dict[set_time_6]
        btn_mid = btn[1][1]
        result = [btn_mid == "1"]
        if False in result:
            raise TimeoutException("device state error, current: %s, result: %s" % (btn, result))

        # 下层关→开
        btn = btn_dict[set_time_7]
        btn_down = btn[1][2]
        result = [btn_down == "1"]
        if False in result:
            raise TimeoutException("device state error, current: %s, result: %s" % (btn, result))
        # 下层开→关
        btn = btn_dict[set_time_8]
        btn_down = btn[1][2]
        result = [btn_down == "0"]
        if False in result:
            raise TimeoutException("device state error, current: %s, result: %s" % (btn, result))
        # 下层关→开
        btn = btn_dict[set_time_9]
        btn_down = btn[1][2]
        result = [btn_down == "1"]
        if False in result:
            raise TimeoutException("device state error, current: %s, result: %s" % (btn, result))

        # 第二遍执行
        # 上层开→关
        btn = btn_dict[set_time_10]
        btn_up = btn[1][0]
        result = [btn_up == "0"]
        if False in result:
            raise TimeoutException("device state error, current: %s, result: %s" % (btn, result))
        # 上层关→开
        btn = btn_dict[set_time_11]
        btn_up = btn[1][0]
        result = [btn_up == "1"]
        if False in result:
            raise TimeoutException("device state error, current: %s, result: %s" % (btn, result))
        # 上层开→关
        btn = btn_dict[set_time_12]
        btn_up = btn[1][0]
        result = [btn_up == "0"]
        if False in result:
            raise TimeoutException("device state error, current: %s, result: %s" % (btn, result))

        # 中层开→关
        btn = btn_dict[set_time_13]
        btn_mid = btn[1][1]
        result = [btn_mid == "0"]
        if False in result:
            raise TimeoutException("device state error, current: %s, result: %s" % (btn, result))
        # 中层关→开
        btn = btn_dict[set_time_14]
        btn_mid = btn[1][1]
        result = [btn_mid == "1"]
        if False in result:
            raise TimeoutException("device state error, current: %s, result: %s" % (btn, result))
        # 中层开→关
        btn = btn_dict[set_time_15]
        btn_mid = btn[1][1]
        result = [btn_mid == "0"]
        if False in result:
            raise TimeoutException("device state error, current: %s, result: %s" % (btn, result))

        # 下层开→关
        btn = btn_dict[set_time_16]
        btn_down = btn[1][2]
        result = [btn_down == "0"]
        if False in result:
            raise TimeoutException("device state error, current: %s, result: %s" % (btn, result))
        # 下层关→开
        btn = btn_dict[set_time_17]
        btn_down = btn[1][2]
        result = [btn_down == "1"]
        if False in result:
            raise TimeoutException("device state error, current: %s, result: %s" % (btn, result))
        # 下层开→关
        btn = btn_dict[set_time_18]
        btn_down = btn[1][2]
        result = [btn_down == "0"]
        if False in result:
            raise TimeoutException("device state error, current: %s, result: %s" % (btn, result))
