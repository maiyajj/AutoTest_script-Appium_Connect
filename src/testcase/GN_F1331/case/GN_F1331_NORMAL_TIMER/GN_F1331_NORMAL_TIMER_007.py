# coding=utf-8
from src.testcase.GN_F1331.WidgetOperation import *


class GNF1331NormalTimer7(WidgetOperation):
    @case_run(False)
    def run(self):
        self.case_module = u"APP功能测试"  # 用例所属模块
        self.case_title = u'上层普通定时'  # 用例名称
        self.zentao_id = 1216  # 禅道ID

    # 用例动作
    def case(self):
        self.choose_home_device(conf["MAC"][self.app][self.device_mac])

        self.delete_out_date_timer()

        self.set_power("main_button_off")

        self.input_serial_command("power", "set_normal_timer", "launch_normal_timer_once")

        self.widget_click(self.page["control_device_page"]["up_timer"],
                          self.page["up_timer_page"]["title"])

        self.delete_normal_timer("up")

        now = time.strftime("%H:%M")

        delay_time_1 = 1
        delay_time_2 = 2
        start_time_1, set_time_1, cycle_1 = self.create_normal_timer("up_timer_page", now, delay_time_1, "power_on")
        start_time_2, set_time_2, cycle_2 = self.create_normal_timer("up_timer_page", now, delay_time_2, "power_off")
        while True:
            if time.time() > set_time_2 + 10:
                break
            print(time.time())
            time.sleep(1)

        #####
        btn_state_list = self.check_serial_button_state()  # 开关
        set_normal_timer_list = self.check_serial_set_normal_timer()  # 定时设置
        launch_normal_timer_once_list = self.check_serial_launch_normal_timer_once()  # 定时执行

        #  第一组定时
        # 设置
        set_normal_timer = set_normal_timer_list[0]
        set_normal_timer_id = set_normal_timer[1]
        set_normal_timer_set_time = set_normal_timer[2]
        set_normal_timer_state = set_normal_timer[4]
        result = [start_time_1 - 15 <= set_normal_timer[0] <= start_time_1 + 15,
                  set_normal_timer_state == "1"]
        if False in result:
            raise TimeoutException("device state error, current: %s, result: %s" % (set_normal_timer, result))
        # 执行
        launch_normal_timer = launch_normal_timer_once_list[0]
        launch_normal_timer_id = launch_normal_timer[1]
        launch_normal_timer_launch_time = launch_normal_timer[2]
        result = [set_time_1 - 15 <= launch_normal_timer[0] <= set_time_1 + 15,
                  launch_normal_timer_id == set_normal_timer_id,
                  launch_normal_timer_launch_time == set_normal_timer_set_time]
        if False in result:
            raise TimeoutException("device state error, current: %s, result: %s" % (launch_normal_timer, result))

        # 第二组定时
        # 设置
        set_normal_timer = set_normal_timer_list[1]
        set_normal_timer_id = set_normal_timer[1]
        set_normal_timer_set_time = set_normal_timer[2]
        set_normal_timer_state = set_normal_timer[4]
        result = [start_time_2 - 15 <= set_normal_timer[0] <= start_time_2 + 15,
                  set_normal_timer_state == "0"]
        if False in result:
            raise TimeoutException("device state error, current: %s, result: %s" % (set_normal_timer, result))
        # 执行
        launch_normal_timer = launch_normal_timer_once_list[1]
        launch_normal_timer_id = launch_normal_timer[1]
        launch_normal_timer_launch_time = launch_normal_timer[2]
        result = [set_time_2 - 15 <= launch_normal_timer[0] <= set_time_2 + 15,
                  launch_normal_timer_id == set_normal_timer_id,
                  launch_normal_timer_launch_time == set_normal_timer_set_time]
        if False in result:
            raise TimeoutException("device state error, current: %s, result: %s" % (launch_normal_timer, result))

        # 开关
        # 第一定时开关
        btn_state = btn_state_list[0]
        btn_all_layer = btn_state[1]
        result = [set_time_1 - 15 <= btn_state[0] <= set_time_1 + 15,
                  btn_all_layer == "100"]
        if False in result:
            raise TimeoutException("device state error, current: %s, result: %s" % (btn_state, result))
        # 第二定时开关
        btn_state = btn_state_list[1]
        btn_all_layer = btn_state[1]
        result = [set_time_2 - 15 <= btn_state[0] <= set_time_2 + 15,
                  btn_all_layer == "000"]
        if False in result:
            raise TimeoutException("device state error, current: %s, result: %s" % (btn_state, result))
