# coding=utf-8
from src.testcase.GN_F1331.WidgetOperation import *


class GNF1331Timer7(WidgetOperation):
    @case_run(False)
    def run(self):
        self.case_module = u"定时器(#9)"  # 用例所属模块
        self.case_title = u'在线状态，单层单次循环定时执行状态检查'  # 用例名称
        self.zentao_id = "130"  # 禅道ID

    # 用例动作
    def case(self):
        self.choose_home_device(conf["MAC"][self.app][self.device_mac])

        self.delete_out_date_timer()
        self.delete_normal_timer_all()

        self.set_power("main_button_off")

        self.input_serial_command("power", "set_cycle_timer", "launch_cycle_timer_on", "launch_cycle_timer_off")

        # 上层
        self.widget_click(self.page["control_device_page"]["up_timer"],
                          self.page["up_timer_page"]["title"])

        now = time.strftime("%H:%M")

        time_1, time_2 = ["delay", "00:05"], ["delay", "00:05"]
        tmp = self.create_cycle_timer("up_timer_page", now, time_1, time_2, u"1次")
        start_time_1, set_time_1, set_time_2 = tmp[0]

        self.widget_click(self.page["up_timer_page"]["to_return"],
                          self.page["control_device_page"]["title"])

        while True:
            if time.time() > set_time_2 + 10:
                break
            print(time.time())
            time.sleep(1)

        #####
        # 开关
        btn_dict = self.check_button_state(start_time_1, set_time_1, set_time_2)
        # 定时设置
        set_cycle_dict = self.check_set_cycle_timer(start_time_1)
        # 定时执行开
        launch_cycle_on_dict = self.check_launch_cycle_timer_on(set_time_2)
        # 定时执行关
        launch_cycle_off_dict = self.check_launch_cycle_timer_off(set_time_1)

        # 上层
        # 设置
        set_timer = set_cycle_dict[start_time_1]
        s_time, s_id, s_times = set_timer[0], set_timer[1], set_timer[2]
        result = [s_time is not None,
                  s_times == "1"]
        if False in result:
            raise TimeoutException("device state error, current: %s, result: %s" % (set_timer, result))
        # 执行开→关
        launch_timer = launch_cycle_off_dict[set_time_1]
        l_time, l_id, l_times = launch_timer[0], launch_timer[1], launch_timer[2]
        result = [l_time is not None,
                  l_id == s_id,
                  l_times == s_times]
        if False in result:
            raise TimeoutException("device state error, current: %s, result: %s" % (launch_timer, result))
        # 执行关→开
        launch_timer = launch_cycle_on_dict[set_time_2]
        l_time, l_id, l_times = launch_timer[0], launch_timer[1], launch_timer[2]
        result = [l_time is not None,
                  l_id == s_id,
                  l_times == s_times]
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
        # 上层关→开
        btn = btn_dict[set_time_2]
        btn_up = btn[1][0]
        result = [btn_up is None]
        if False in result:
            raise TimeoutException("device state error, current: %s, result: %s" % (btn, result))
