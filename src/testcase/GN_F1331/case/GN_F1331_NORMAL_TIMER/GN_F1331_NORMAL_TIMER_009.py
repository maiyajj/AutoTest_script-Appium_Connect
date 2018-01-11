# coding=utf-8
from src.testcase.GN_F1331.WidgetOperation import *


class GNF1331NormalTimer9(WidgetOperation):
    @case_run(False)
    def run(self):
        self.case_module = u"APP功能测试"  # 用例所属模块
        self.case_title = u'上、中、下层普通定时'  # 用例名称
        self.zentao_id = 1216  # 禅道ID

    # 用例动作
    def case(self):
        self.choose_home_device(conf["MAC"][self.app][self.device_mac])

        self.delete_out_date_timer()

        self.set_power("main_button_off")

        self.input_serial_command("power", "set_normal_timer", "launch_normal_timer_once")

        # 上层
        self.widget_click(self.page["control_device_page"]["up_timer"],
                          self.page["up_timer_page"]["title"])

        self.delete_normal_timer("up")

        now = time.strftime("%H:%M")

        delay_time_1 = 1
        delay_time_2 = 2
        start_time_1, set_time_1, cycle_1 = self.create_normal_timer("up_timer_page", now, delay_time_1, "power_on")
        start_time_2, set_time_2, cycle_2 = self.create_normal_timer("up_timer_page", now, delay_time_2, "power_off")

        self.widget_click(self.page["up_timer_page"]["to_return"],
                          self.page["control_device_page"]["title"])

        # 中层
        self.widget_click(self.page["control_device_page"]["mid_timer"],
                          self.page["mid_timer_page"]["title"])

        self.delete_normal_timer("mid")

        now = time.strftime("%H:%M")

        delay_time_3 = 1
        delay_time_4 = 2
        start_time_3, set_time_3, cycle_3 = self.create_normal_timer("mid_timer_page", now, delay_time_3, "power_on")
        start_time_4, set_time_4, cycle_4 = self.create_normal_timer("mid_timer_page", now, delay_time_4, "power_off")

        self.widget_click(self.page["mid_timer_page"]["to_return"],
                          self.page["control_device_page"]["title"])

        # 下层
        self.widget_click(self.page["control_device_page"]["down_timer"],
                          self.page["down_timer_page"]["title"])

        self.delete_normal_timer("down")

        now = time.strftime("%H:%M")

        delay_time_5 = 1
        delay_time_6 = 3
        start_time_5, set_time_5, cycle_5 = self.create_normal_timer("down_timer_page", now, delay_time_5, "power_on")
        start_time_6, set_time_6, cycle_6 = self.create_normal_timer("down_timer_page", now, delay_time_6, "power_off")

        while True:
            if time.time() > set_time_6 + 10:
                break
            print(time.time())
            time.sleep(1)

        #####
        btn_state_list = self.check_serial_button_state()  # 开关
        set_normal_timer_list = self.check_serial_set_normal_timer()  # 定时设置
        launch_normal_timer_once_list = self.check_serial_launch_normal_timer_once()  # 定时执行开
        timer_list = self.get_timer_id_from_set(set_normal_timer_list)
        result = self.get_layer_timer_from_launch(timer_list,
                                                  a=launch_normal_timer_once_list)

        up_normal_1_id, up_normal_2_id, \
        mid_normal_3_id, mid_normal_4_id, \
        down_normal_5_id, down_normal_6_id = timer_list  # timer id
        up_launch_normal_timer_1_list, up_launch_normal_timer_2_list = \
            result[up_normal_1_id]["a"], result[up_normal_2_id]["a"]
        mid_launch_normal_timer_3_list, mid_launch_normal_timer_4_list = \
            result[mid_normal_3_id]["a"], result[mid_normal_4_id]["a"]
        down_launch_normal_timer_5_list, down_launch_normal_timer_6_list = \
            result[down_normal_5_id]["a"], result[down_normal_6_id]["a"]

        # 上层
        # 定时1
        # 设置
        set_normal_timer = set_normal_timer_list[0]
        set_normal_timer_id = set_normal_timer[1]
        result = [start_time_1 - 15 <= set_normal_timer[0] <= start_time_1 + 15]
        if False in result:
            raise TimeoutException("device state error, current: %s, result: %s" % (set_normal_timer, result))
        # 执行关→开
        launch_normal_timer = up_launch_normal_timer_1_list[0]
        launch_normal_timer_id = launch_normal_timer[1]
        result = [set_time_1 - 15 <= launch_normal_timer[0] <= set_time_1 + 15,
                  launch_normal_timer_id == set_normal_timer_id]
        if False in result:
            raise TimeoutException("device state error, current: %s, result: %s" % (launch_normal_timer, result))
        # 定时2
        # 设置
        set_normal_timer = set_normal_timer_list[1]
        set_normal_timer_id = set_normal_timer[1]
        result = [start_time_2 - 15 <= set_normal_timer[0] <= start_time_2 + 15]
        if False in result:
            raise TimeoutException("device state error, current: %s, result: %s" % (set_normal_timer, result))
        # 执行开→关
        launch_normal_timer = up_launch_normal_timer_2_list[0]
        launch_normal_timer_id = launch_normal_timer[1]
        result = [set_time_2 - 15 <= launch_normal_timer[0] <= set_time_2 + 15,
                  launch_normal_timer_id == set_normal_timer_id]
        if False in result:
            raise TimeoutException("device state error, current: %s, result: %s" % (launch_normal_timer, result))

        # 中层
        # 定时3
        # 设置
        set_normal_timer = set_normal_timer_list[2]
        set_normal_timer_id = set_normal_timer[1]
        result = [start_time_3 - 15 <= set_normal_timer[0] <= start_time_3 + 15]
        if False in result:
            raise TimeoutException("device state error, current: %s, result: %s" % (set_normal_timer, result))
        # 执行关→开
        launch_normal_timer = mid_launch_normal_timer_3_list[0]
        launch_normal_timer_id = launch_normal_timer[1]
        result = [set_time_3 - 15 <= launch_normal_timer[0] <= set_time_3 + 15,
                  launch_normal_timer_id == set_normal_timer_id]
        if False in result:
            raise TimeoutException("device state error, current: %s, result: %s" % (launch_normal_timer, result))
        # 定时4
        # 设置
        set_normal_timer = set_normal_timer_list[3]
        set_normal_timer_id = set_normal_timer[1]
        result = [start_time_4 - 15 <= set_normal_timer[0] <= start_time_4 + 15]
        if False in result:
            raise TimeoutException("device state error, current: %s, result: %s" % (set_normal_timer, result))
        # 执行开→关
        launch_normal_timer = mid_launch_normal_timer_4_list[0]
        launch_normal_timer_id = launch_normal_timer[1]
        result = [set_time_4 - 15 <= launch_normal_timer[0] <= set_time_4 + 15,
                  launch_normal_timer_id == set_normal_timer_id]
        if False in result:
            raise TimeoutException("device state error, current: %s, result: %s" % (launch_normal_timer, result))

        # 下层
        # 定时5
        # 设置
        set_normal_timer = set_normal_timer_list[4]
        set_normal_timer_id = set_normal_timer[1]
        result = [start_time_5 - 15 <= set_normal_timer[0] <= start_time_5 + 15]
        if False in result:
            raise TimeoutException("device state error, current: %s, result: %s" % (set_normal_timer, result))
        # 执行关→开
        launch_normal_timer = down_launch_normal_timer_5_list[0]
        launch_normal_timer_id = launch_normal_timer[1]
        result = [set_time_5 - 15 <= launch_normal_timer[0] <= set_time_5 + 15,
                  launch_normal_timer_id == set_normal_timer_id]
        if False in result:
            raise TimeoutException("device state error, current: %s, result: %s" % (launch_normal_timer, result))
        # 定时6
        # 设置
        set_normal_timer = set_normal_timer_list[5]
        set_normal_timer_id = set_normal_timer[1]
        result = [start_time_6 - 15 <= set_normal_timer[0] <= start_time_6 + 15]
        if False in result:
            raise TimeoutException("device state error, current: %s, result: %s" % (set_normal_timer, result))
        # 执行开→关
        launch_normal_timer = down_launch_normal_timer_6_list[0]
        launch_normal_timer_id = launch_normal_timer[1]
        result = [set_time_6 - 15 <= launch_normal_timer[0] <= set_time_6 + 15,
                  launch_normal_timer_id == set_normal_timer_id]
        if False in result:
            raise TimeoutException("device state error, current: %s, result: %s" % (launch_normal_timer, result))
