# coding=utf-8
from src.testcase.GN_F1331.WidgetOperation import *


class GNF1331NormalTimer3(WidgetOperation):
    @case_run(False)
    def run(self):
        self.case_module = u"APP功能测试"  # 用例所属模块
        self.case_title = u'上、中、下层循环定时'  # 用例名称
        self.zentao_id = 1216  # 禅道ID

    # 用例动作
    def case(self):
        self.choose_home_device(conf["MAC"][self.app][self.device_mac])

        self.delete_out_date_timer()

        self.set_power("main_button_off")

        self.input_serial_command("power", "set_cycle_timer", "launch_cycle_timer_on", "launch_cycle_timer_off")

        # 上层
        self.widget_click(self.page["control_device_page"]["up_timer"],
                          self.page["up_timer_page"]["title"])

        now = time.strftime("%H:%M")

        delay_time_1, delay_time_2 = ["delay", "00:01"], ["delay", "00:01"]
        tmp = self.create_cycle_timer("up_timer_page", now, delay_time_1, delay_time_2, u"永久循环")
        start_time_1, set_time_1, start_time_2, set_time_2 = tmp[0]

        self.widget_click(self.page["up_timer_page"]["to_return"],
                          self.page["control_device_page"]["title"])

        # 中层
        self.widget_click(self.page["control_device_page"]["mid_timer"],
                          self.page["mid_timer_page"]["title"])

        now = time.strftime("%H:%M")

        delay_time_3, delay_time_4 = ["delay", "00:01"], ["delay", "00:01"]
        tmp = self.create_cycle_timer("mid_timer_page", now, delay_time_3, delay_time_4, u"永久循环", delay_s=135)
        start_time_3, set_time_3, start_time_4, set_time_4 = tmp[0]

        self.widget_click(self.page["mid_timer_page"]["to_return"],
                          self.page["control_device_page"]["title"])

        # 下层
        self.widget_click(self.page["control_device_page"]["down_timer"],
                          self.page["down_timer_page"]["title"])

        now = time.strftime("%H:%M")

        delay_time_5, delay_time_6 = ["delay", "00:01"], ["delay", "00:01"]
        tmp = self.create_cycle_timer("down_timer_page", now, delay_time_5, delay_time_6, u"永久循环", delay_s=150)
        start_time_5, set_time_5, start_time_6, set_time_6 = tmp[0]

        while True:
            if time.time() > set_time_6 + 10:
                break
            print(time.time())
            time.sleep(1)

        #####
        btn_state_list = self.check_serial_button_state()  # 开关
        set_cycle_timer_list = self.check_serial_set_cycle_timer()  # 定时设置
        launch_cycle_timer_on_list = self.check_serial_launch_cycle_timer_on()  # 定时执行开
        launch_cycle_timer_off_list = self.check_serial_launch_cycle_timer_off()  # 定时执行关
        timer_list = self.get_timer_id_from_set(set_cycle_timer_list)
        result = self.get_layer_timer_from_launch(timer_list,
                                                  a=launch_cycle_timer_on_list,
                                                  b=launch_cycle_timer_off_list)

        up_cycle_id, mid_cycle_id, down_cycle_id = timer_list  # timer id
        up_launch_cycle_timer_on_list, mid_launch_cycle_timer_on_list, down_launch_cycle_timer_on_list = \
            result[up_cycle_id]["a"], result[mid_cycle_id]["a"], result[down_cycle_id]["a"]
        up_launch_cycle_timer_off_list, mid_launch_cycle_timer_off_list, down_launch_cycle_timer_off_list = \
            result[up_cycle_id]["b"], result[mid_cycle_id]["b"], result[down_cycle_id]["b"]

        # 上层
        # 设置
        set_cycle_timer = set_cycle_timer_list[0]
        set_cycle_timer_id = set_cycle_timer[1]
        set_cycle_timer_times = set_cycle_timer[2]
        result = [start_time_1 - 15 <= set_cycle_timer[0] <= start_time_1 + 15,
                  set_cycle_timer_times == "255"]
        if False in result:
            raise TimeoutException("device state error, current: %s, result: %s" % (set_cycle_timer, result))
        # 执行开→关
        launch_cycle_timer = up_launch_cycle_timer_off_list[0]
        launch_cycle_timer_id = launch_cycle_timer[1]
        launch_cycle_timer_times = launch_cycle_timer[2]
        result = [set_time_1 - 15 <= launch_cycle_timer[0] <= set_time_1 + 15,
                  launch_cycle_timer_id == set_cycle_timer_id,
                  launch_cycle_timer_times == set_cycle_timer_times]
        if False in result:
            raise TimeoutException("device state error, current: %s, result: %s" % (launch_cycle_timer, result))
        # 执行关→开
        launch_cycle_timer = up_launch_cycle_timer_on_list[0]
        launch_cycle_timer_id = launch_cycle_timer[1]
        launch_cycle_timer_times = launch_cycle_timer[2]
        result = [set_time_2 - 15 <= launch_cycle_timer[0] <= set_time_2 + 15,
                  launch_cycle_timer_id == set_cycle_timer_id,
                  launch_cycle_timer_times == set_cycle_timer_times]
        if False in result:
            raise TimeoutException("device state error, current: %s, result: %s" % (launch_cycle_timer, result))

        # 中层
        # 设置
        set_cycle_timer = set_cycle_timer_list[1]
        set_cycle_timer_id = set_cycle_timer[1]
        set_cycle_timer_times = set_cycle_timer[2]
        result = [start_time_3 - 15 <= set_cycle_timer[0] <= start_time_3 + 15,
                  set_cycle_timer_times == "255"]
        if False in result:
            raise TimeoutException("device state error, current: %s, result: %s" % (set_cycle_timer, result))
        # 执行开→关
        launch_cycle_timer = mid_launch_cycle_timer_off_list[0]
        launch_cycle_timer_id = launch_cycle_timer[1]
        launch_cycle_timer_times = launch_cycle_timer[2]
        result = [set_time_3 - 15 <= launch_cycle_timer[0] <= set_time_3 + 15,
                  launch_cycle_timer_id == set_cycle_timer_id,
                  launch_cycle_timer_times == set_cycle_timer_times]
        if False in result:
            raise TimeoutException("device state error, current: %s, result: %s" % (launch_cycle_timer, result))
        # 执行关→开
        launch_cycle_timer = mid_launch_cycle_timer_on_list[0]
        launch_cycle_timer_id = launch_cycle_timer[1]
        launch_cycle_timer_times = launch_cycle_timer[2]
        result = [set_time_4 - 15 <= launch_cycle_timer[0] <= set_time_4 + 15,
                  launch_cycle_timer_id == set_cycle_timer_id,
                  launch_cycle_timer_times == set_cycle_timer_times]
        if False in result:
            raise TimeoutException("device state error, current: %s, result: %s" % (launch_cycle_timer, result))

        # 下层
        # 设置
        set_cycle_timer = set_cycle_timer_list[2]
        set_cycle_timer_id = set_cycle_timer[1]
        set_cycle_timer_times = set_cycle_timer[2]
        result = [start_time_5 - 15 <= set_cycle_timer[0] <= start_time_5 + 15,
                  set_cycle_timer_times == "255"]
        if False in result:
            raise TimeoutException("device state error, current: %s, result: %s" % (set_cycle_timer, result))
        # 执行开→关
        launch_cycle_timer = down_launch_cycle_timer_off_list[0]
        launch_cycle_timer_id = launch_cycle_timer[1]
        launch_cycle_timer_times = launch_cycle_timer[2]
        result = [set_time_5 - 15 <= launch_cycle_timer[0] <= set_time_5 + 15,
                  launch_cycle_timer_id == set_cycle_timer_id,
                  launch_cycle_timer_times == set_cycle_timer_times]
        if False in result:
            raise TimeoutException("device state error, current: %s, result: %s" % (launch_cycle_timer, result))
        # 执行关→开
        launch_cycle_timer = down_launch_cycle_timer_on_list[0]
        launch_cycle_timer_id = launch_cycle_timer[1]
        launch_cycle_timer_times = launch_cycle_timer[2]
        result = [set_time_6 - 15 <= launch_cycle_timer[0] <= set_time_6 + 15,
                  launch_cycle_timer_id == set_cycle_timer_id,
                  launch_cycle_timer_times == set_cycle_timer_times]
        if False in result:
            raise TimeoutException("device state error, current: %s, result: %s" % (launch_cycle_timer, result))

        # 开关
        # 100, 000, 100, 110, 010, 000, 100, 110, 111, 011, 001, 000, 100, 110, 111
        # 上层初始开关,先跳开
        btn_state = btn_state_list[0]
        btn_all_layer = btn_state[1]
        result = [start_time_1 - 15 <= btn_state[0] <= start_time_1 + 15,
                  btn_all_layer == "100"]
        if False in result:
            raise TimeoutException("device state error, current: %s, result: %s" % (btn_state, result))
        # 上层开→关开关
        btn_state = btn_state_list[1]
        btn_all_layer = btn_state[1]
        result = [set_time_1 - 15 <= btn_state[0] <= set_time_1 + 15,
                  btn_all_layer == "000"]
        if False in result:
            raise TimeoutException("device state error, current: %s, result: %s" % (btn_state, result))
        # 上层关→开开关
        btn_state = btn_state_list[2]
        btn_all_layer = btn_state[1]
        result = [set_time_2 - 15 <= btn_state[0] <= set_time_2 + 15,
                  btn_all_layer == "100"]
        if False in result:
            raise TimeoutException("device state error, current: %s, result: %s" % (btn_state, result))

        # 中层初始开关,先跳开
        btn_state = btn_state_list[3]
        btn_all_layer = btn_state[1]
        result = [start_time_3 - 15 <= btn_state[0] <= start_time_3 + 15,
                  btn_all_layer == "110"]
        if False in result:
            raise TimeoutException("device state error, current: %s, result: %s" % (btn_state, result))
        # 中层开→关开关
        btn_state = btn_state_list[5]
        btn_all_layer = btn_state[1]
        result = [set_time_3 - 15 <= btn_state[0] <= set_time_3 + 15,
                  btn_all_layer == "000"]
        if False in result:
            raise TimeoutException("device state error, current: %s, result: %s" % (btn_state, result))
        # 中层关→开开关
        btn_state = btn_state_list[7]
        btn_all_layer = btn_state[1]
        result = [set_time_4 - 15 <= btn_state[0] <= set_time_4 + 15,
                  btn_all_layer == "110"]
        if False in result:
            raise TimeoutException("device state error, current: %s, result: %s" % (btn_state, result))

        # 下层初始开关,先跳开
        btn_state = btn_state_list[8]
        btn_all_layer = btn_state[1]
        result = [start_time_5 - 15 <= btn_state[0] <= start_time_5 + 15,
                  btn_all_layer == "111"]
        if False in result:
            raise TimeoutException("device state error, current: %s, result: %s" % (btn_state, result))
        # 下层开→关开关
        btn_state = btn_state_list[11]
        btn_all_layer = btn_state[1]
        result = [set_time_5 - 15 <= btn_state[0] <= set_time_5 + 15,
                  btn_all_layer == "000"]
        if False in result:
            raise TimeoutException("device state error, current: %s, result: %s" % (btn_state, result))
        # 下层关→开开关
        btn_state = btn_state_list[14]
        btn_all_layer = btn_state[1]
        result = [set_time_6 - 15 <= btn_state[0] <= set_time_6 + 15,
                  btn_all_layer == "111"]
        if False in result:
            raise TimeoutException("device state error, current: %s, result: %s" % (btn_state, result))
