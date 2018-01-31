# coding=utf-8
from src.testcase.GN_F1331.WidgetOperation import *


class GNF1331Timer9(WidgetOperation):
    @case_run(False)
    def run(self):
        self.case_module = u"定时器(#9)"  # 用例所属模块
        self.case_title = u'在线状态，各层定时单关延时定时执行状态检查'  # 用例名称
        self.zentao_id = "116"  # 禅道ID

    # 用例动作
    def case(self):
        self.choose_home_device(conf["MAC"][self.app][self.device_mac])

        self.delete_out_date_timer()
        self.delete_normal_timer_all()

        self.set_power("main_button_off")

        self.input_serial_command("power", "set_delay_timer", "launch_delay_timer")

        # 上层
        self.widget_click(self.page["control_device_page"]["up_timer"],
                          self.page["up_timer_page"]["title"])

        now = time.strftime("%H:%M")

        time_1 = ["delay", "00:02"]
        start_time_1, set_time_1 = self.create_delay_timer("up_timer_page", now, time_1)

        self.widget_click(self.page["up_timer_page"]["to_return"],
                          self.page["control_device_page"]["title"])

        # 中层
        self.widget_click(self.page["control_device_page"]["mid_timer"],
                          self.page["mid_timer_page"]["title"])

        now = time.strftime("%H:%M")

        time_2 = ["delay", "00:02"]
        start_time_2, set_time_2 = self.create_delay_timer("mid_timer_page", now, time_2)

        self.widget_click(self.page["mid_timer_page"]["to_return"],
                          self.page["control_device_page"]["title"])

        # 下层
        self.widget_click(self.page["control_device_page"]["down_timer"],
                          self.page["down_timer_page"]["title"])

        now = time.strftime("%H:%M")

        time_3 = ["delay", "00:02"]
        start_time_3, set_time_3 = self.create_delay_timer("down_timer_page", now, time_3)

        max_time = max(set_time_1, set_time_2, set_time_3)
        while True:
            if time.time() > max_time + 10:
                break
            print(time.time())
            time.sleep(1)

        #####
        # 开关
        btn_dict = self.check_button_state(start_time_1, set_time_1, start_time_2, set_time_2, start_time_3, set_time_3)
        # 定时设置
        set_delay_dict = self.check_set_delay_timer(start_time_1, start_time_2, start_time_3)
        # 定时执行
        launch_delay_dict = self.check_launch_delay_timer(set_delay_dict, set_time_1, set_time_2, set_time_3)

        # 上层
        # 设置
        set_timer = set_delay_dict[start_time_1]
        s_time, s_id = set_timer[0], set_timer[1]
        result = [s_time is not None]
        if False in result:
            raise TimeoutException("device state error, current: %s, result: %s" % (s_time, result))
        # 执行
        launch_timer = launch_delay_dict[set_time_1]
        l_time, l_id = launch_timer[s_id][0], launch_timer[s_id][1]
        result = [l_time is not None,
                  l_id == s_id]
        if False in result:
            raise TimeoutException("device state error, current: %s, result: %s" % (launch_timer, result))

        # 中层
        # 设置
        set_timer = set_delay_dict[start_time_2]
        s_time, s_id = set_timer[0], set_timer[1]
        result = [s_time is not None]
        if False in result:
            raise TimeoutException("device state error, current: %s, result: %s" % (s_time, result))
        # 执行
        launch_timer = launch_delay_dict[set_time_2]
        l_time, l_id = launch_timer[s_id][0], launch_timer[s_id][1]
        result = [l_time is not None,
                  l_id == s_id]
        if False in result:
            raise TimeoutException("device state error, current: %s, result: %s" % (launch_timer, result))

        # 下层
        # 设置
        set_timer = set_delay_dict[start_time_3]
        s_time, s_id = set_timer[0], set_timer[1]
        result = [s_time is not None]
        if False in result:
            raise TimeoutException("device state error, current: %s, result: %s" % (s_time, result))
        # 执行
        launch_timer = launch_delay_dict[set_time_3]
        l_time, l_id = launch_timer[s_id][0], launch_timer[s_id][1]
        result = [l_time is not None,
                  l_id == s_id]
        if False in result:
            raise TimeoutException("device state error, current: %s, result: %s" % (launch_timer, result))

        # 开关
        # 上层关→开
        btn = btn_dict[start_time_1]
        btn_up = btn[1][0]
        result = [btn_up == "1"]
        if False in result:
            raise TimeoutException("device state error, current: %s, result: %s" % (btn, result))
        # 上层开→关
        btn = btn_dict[set_time_1]
        btn_up = btn[1][0]
        result = [btn_up == "0"]
        if False in result:
            raise TimeoutException("device state error, current: %s, result: %s" % (btn, result))

        # 中层关→开
        btn = btn_dict[start_time_2]
        btn_mid = btn[1][1]
        result = [btn_mid == "1"]
        if False in result:
            raise TimeoutException("device state error, current: %s, result: %s" % (btn, result))
        # 中层开→关
        btn = btn_dict[set_time_2]
        btn_mid = btn[1][1]
        result = [btn_mid == "0"]
        if False in result:
            raise TimeoutException("device state error, current: %s, result: %s" % (btn, result))

        # 下层关→开
        btn = btn_dict[start_time_3]
        btn_down = btn[1][2]
        result = [btn_down == "1"]
        if False in result:
            raise TimeoutException("device state error, current: %s, result: %s" % (btn, result))
        # 下层开→关
        btn = btn_dict[set_time_3]
        btn_down = btn[1][2]
        result = [btn_down == "0"]
        if False in result:
            raise TimeoutException("device state error, current: %s, result: %s" % (btn, result))
