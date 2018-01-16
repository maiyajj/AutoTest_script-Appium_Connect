# coding=utf-8
from src.testcase.GN_F1331.WidgetOperation import *


class GNF1331NormalTimer6(WidgetOperation):
    @case_run(False)
    def run(self):
        self.case_module = u"APP功能测试"  # 用例所属模块
        self.case_title = u'上、中、下层延迟定时'  # 用例名称
        self.zentao_id = 1216  # 禅道ID

    # 用例动作
    def case(self):
        self.choose_home_device(conf["MAC"][self.app][self.device_mac])

        self.delete_out_date_timer()

        self.set_power("main_button_off")

        self.input_serial_command("power", "set_delay_timer", "launch_delay_timer")

        # 上层
        self.widget_click(self.page["control_device_page"]["up_timer"],
                          self.page["up_timer_page"]["title"])

        now = time.strftime("%H:%M")

        delay_time_1 = ["delay", "00:01"]
        start_time_1, set_time_1 = self.create_delay_timer("up_timer_page", now, delay_time_1)

        self.widget_click(self.page["up_timer_page"]["to_return"],
                          self.page["control_device_page"]["title"])

        # 中层
        self.widget_click(self.page["control_device_page"]["mid_timer"],
                          self.page["mid_timer_page"]["title"])

        now = time.strftime("%H:%M")

        delay_time_2 = ["delay", "00:01"]
        start_time_2, set_time_2 = self.create_delay_timer("mid_timer_page", now, delay_time_2, delay_s=135)

        self.widget_click(self.page["mid_timer_page"]["to_return"],
                          self.page["control_device_page"]["title"])

        # 下层
        self.widget_click(self.page["control_device_page"]["down_timer"],
                          self.page["down_timer_page"]["title"])

        now = time.strftime("%H:%M")

        delay_time_3 = ["delay", "00:01"]
        start_time_3, set_time_3 = self.create_delay_timer("down_timer_page", now, delay_time_3, delay_s=150)

        while True:
            if time.time() > set_time_3 + 10:
                break
            print(time.time())
            time.sleep(1)

        #####
        btn_state_list = self.check_serial_button_state()  # 开关
        set_delay_timer_list = self.check_serial_set_delay_timer()  # 定时设置
        launch_delay_timer_list = self.check_serial_launch_delay_timer()  # 定时执行开
        timer_list = self.get_timer_id_from_set(set_delay_timer_list)
        result = self.get_layer_timer_from_launch(timer_list,
                                                  a=launch_delay_timer_list)

        up_delay_id, mid_delay_id, down_delay_id = timer_list  # timer id
        up_launch_delay_timer_list, mid_launch_delay_timer_list, down_launch_delay_timer_list = \
            result[up_delay_id]["a"], result[mid_delay_id]["a"], result[down_delay_id]["a"]

        # 上层
        # 设置
        set_delay_timer = set_delay_timer_list[0]
        set_delay_timer_id = set_delay_timer[1]
        result = [start_time_1 - 15 <= set_delay_timer[0] <= start_time_1 + 15]
        if False in result:
            raise TimeoutException("device state error, current: %s, result: %s" % (set_delay_timer, result))
        # 执行开→关
        launch_delay_timer = up_launch_delay_timer_list[0]
        launch_delay_timer_id = launch_delay_timer[1]
        result = [set_time_1 - 15 <= launch_delay_timer[0] <= set_time_1 + 15,
                  launch_delay_timer_id == set_delay_timer_id]
        if False in result:
            raise TimeoutException("device state error, current: %s, result: %s" % (launch_delay_timer, result))

        # 中层
        # 设置
        set_delay_timer = set_delay_timer_list[1]
        set_delay_timer_id = set_delay_timer[1]
        result = [start_time_2 - 15 <= set_delay_timer[0] <= start_time_2 + 15]
        if False in result:
            raise TimeoutException("device state error, current: %s, result: %s" % (set_delay_timer, result))
        # 执行开→关
        launch_delay_timer = mid_launch_delay_timer_list[0]
        launch_delay_timer_id = launch_delay_timer[1]
        result = [set_time_2 - 15 <= launch_delay_timer[0] <= set_time_2 + 15,
                  launch_delay_timer_id == set_delay_timer_id]
        if False in result:
            raise TimeoutException("device state error, current: %s, result: %s" % (launch_delay_timer, result))

        # 下层
        # 设置
        set_delay_timer = set_delay_timer_list[2]
        set_delay_timer_id = set_delay_timer[1]
        result = [start_time_3 - 15 <= set_delay_timer[0] <= start_time_3 + 15]
        if False in result:
            raise TimeoutException("device state error, current: %s, result: %s" % (set_delay_timer, result))
        # 执行开→关
        launch_delay_timer = down_launch_delay_timer_list[0]
        launch_delay_timer_id = launch_delay_timer[1]
        result = [set_time_3 - 15 <= launch_delay_timer[0] <= set_time_3 + 15,
                  launch_delay_timer_id == set_delay_timer_id]
        if False in result:
            raise TimeoutException("device state error, current: %s, result: %s" % (launch_delay_timer, result))

        # 开关
        # 100, 000, 010, 000, 001, 000
        # 上层初始开关,先跳开
        btn_state = btn_state_list[0]
        result = [start_time_1 - 15 <= btn_state[0] <= start_time_1 + 15,
                  btn_state[1] == "100"]
        if False in result:
            raise TimeoutException("device state error, current: %s, result: %s" % (btn_state, result))
        # 上层开→关开关
        btn_state = btn_state_list[1]
        result = [set_time_1 - 15 <= btn_state[0] <= set_time_1 + 15,
                  btn_state[1] == "000"]
        if False in result:
            raise TimeoutException("device state error, current: %s, result: %s" % (btn_state, result))

        # 中层初始开关,先跳开
        btn_state = btn_state_list[2]
        result = [start_time_2 - 15 <= btn_state[0] <= start_time_2 + 15,
                  btn_state[1] == "010"]
        if False in result:
            raise TimeoutException("device state error, current: %s, result: %s" % (btn_state, result))
        # 中层开→关开关
        btn_state = btn_state_list[3]
        result = [set_time_2 - 15 <= btn_state[0] <= set_time_2 + 15,
                  btn_state[1] == "000"]
        if False in result:
            raise TimeoutException("device state error, current: %s, result: %s" % (btn_state, result))

        # 下层初始开关,先跳开
        btn_state = btn_state_list[4]
        result = [start_time_3 - 15 <= btn_state[0] <= start_time_3 + 15,
                  btn_state[1] == "001"]
        if False in result:
            raise TimeoutException("device state error, current: %s, result: %s" % (btn_state, result))
        # 下层开→关开关
        btn_state = btn_state_list[5]
        result = [set_time_3 - 15 <= btn_state[0] <= set_time_3 + 15,
                  btn_state[1] == "000"]
        if False in result:
            raise TimeoutException("device state error, current: %s, result: %s" % (btn_state, result))
