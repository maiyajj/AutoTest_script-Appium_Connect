# coding=utf-8
from src.testcase.GN_F1331.WidgetOperation import *


class GNF1331NormalTimer4(WidgetOperation):
    @case_run(False)
    def run(self):
        self.case_module = u"APP功能测试"  # 用例所属模块
        self.case_title = u'上层延迟定时'  # 用例名称
        self.zentao_id = 1216  # 禅道ID

    # 用例动作
    def case(self):
        self.choose_home_device(conf["MAC"][self.app][self.device_mac])

        self.delete_out_date_timer()

        self.set_power("main_button_off")

        self.input_serial_command("power", "set_delay_timer", "launch_delay_timer")

        self.widget_click(self.page["control_device_page"]["up_timer"],
                          self.page["up_timer_page"]["title"])

        now = time.strftime("%H:%M")

        delay_time_1 = ["delay", "00:01"]
        start_time_1, set_time_1 = self.create_delay_timer("up_timer_page", now, delay_time_1)

        while True:
            if time.time() > set_time_1 + 10:
                break
            print(time.time())
            time.sleep(1)

        #####
        btn_state_list = self.check_serial_button_state()  # 开关
        set_delay_timer_list = self.check_serial_set_delay_timer()  # 定时设置
        launch_delay_timer_list = self.check_serial_launch_delay_timer()  # 定时执行
        self.debug.info(u"[APP_INFO]device state: \n"
                        u"btn_state_list: %s;\n"
                        u"set_timer_list: %s;\n"
                        u"launch_timer_list: %s"
                        % (btn_state_list, set_delay_timer_list, launch_delay_timer_list))

        # 设置
        set_delay_timer = set_delay_timer_list[0]
        set_delay_timer_id = set_delay_timer[1]
        result = [start_time_1 - 15 <= set_delay_timer[0] <= start_time_1 + 15]
        if False in result:
            raise TimeoutException("device state error, current: %s, result: %s" % (set_delay_timer, result))
        # 执行
        launch_delay_timer = launch_delay_timer_list[0]
        launch_delay_timer_id = launch_delay_timer[1]
        result = [set_time_1 - 15 <= launch_delay_timer[0] <= set_time_1 + 15,
                  launch_delay_timer_id == set_delay_timer_id]
        if False in result:
            raise TimeoutException("device state error, current: %s, result: %s" % (launch_delay_timer, result))

        # 开关
        # 初始开关
        btn_state = btn_state_list[0]
        btn_all_layer = btn_state[1]
        result = [start_time_1 - 15 <= btn_state[0] <= start_time_1 + 15,
                  btn_all_layer == "100"]
        if False in result:
            raise TimeoutException("device state error, current: %s, result: %s" % (btn_state, result))
        # 执行结束开关
        btn_state = btn_state_list[1]
        btn_all_layer = btn_state[1]
        result = [set_time_1 - 15 <= btn_state[0] <= set_time_1 + 15,
                  btn_all_layer == "000"]
        if False in result:
            raise TimeoutException("device state error, current: %s, result: %s" % (btn_state, result))
