# coding=utf-8
from src.testcase.GN_F1331.WidgetOperation import *


class GNF1331NormalTimer1(WidgetOperation):
    @case_run(False)
    def run(self):
        self.case_module = u"APP功能测试"  # 用例所属模块
        self.case_title = u'上层循环定时'  # 用例名称
        self.zentao_id = 1216  # 禅道ID

    # 用例动作
    def case(self):
        self.choose_home_device(conf["MAC"][self.app][self.device_mac])

        self.set_power("main_button_off")

        self.input_serial_command("power", "set_cycle_timer", "launch_cylce_timer")

        self.widget_click(self.page["control_device_page"]["up_timer"],
                          self.page["up_timer_page"]["title"])

        self.widget_click(self.page["up_timer_page"]["cycle_timer"],
                          self.page["up_timer_page"]["cycle_timer_button"])

        now = time.strftime("%H:%M")

        delay_time_1, delay_time_2 = ["delay", "00:01"], ["delay", "00:01"]
        tmp = self.create_cycle_timer("up_timer_page", now, delay_time_1, delay_time_2, u"永久循环")
        start_time_1, set_time_1, start_time_2, set_time_2 = tmp[0]

        while True:
            if time.time() > set_time_2 + 10:
                break
            print(time.time())
            time.sleep(1)

        #
        btn_state_list = self.check_serial_button_state()

        btn_state = btn_state_list[0]
        if start_time_1 - 15 <= btn_state[0] <= start_time_1 + 15 and [1, 0, 0] == btn_state[1:]:
            self.logger.info(u"[APP_INFO]device state: %s" % btn_state)
        else:
            raise TimeoutException("device state error, current: %s" % btn_state)

        btn_state = btn_state_list[1]
        if set_time_1 - 15 <= btn_state[0] <= set_time_1 + 15 and [0, 0, 0] == btn_state[1:]:
            self.logger.info(u"[APP_INFO]device state: %s" % btn_state)
        else:
            raise TimeoutException("device state error, current: %s" % btn_state)

        btn_state = btn_state_list[2]
        if set_time_2 - 15 <= btn_state[0] <= set_time_2 + 15 and [1, 0, 0] == btn_state[1:]:
            self.logger.info(u"[APP_INFO]device state: %s" % btn_state)
        else:
            raise TimeoutException("device state error, current: %s" % btn_state)

        #
        set_cycle_timer_list = self.check_serial_set_cycle_timer()

        set_cycle_timer = set_cycle_timer_list[0]
        set_cycle_timer_name = set_cycle_timer[-2]
        if start_time_1 - 15 <= set_cycle_timer[0] <= start_time_1 + 15:
            self.logger.info(u"[APP_INFO]device state: %s" % set_cycle_timer)
        else:
            raise TimeoutException("device state error, current: %s" % set_cycle_timer)

        #
        launch_cycle_timer_list = self.check_serial_launch_cycle_timer()

        launch_cycle_timer = launch_cycle_timer_list[0]
        launch_cycle_timer_name = launch_cycle_timer[-2]
        if (set_time_1 - 15 <= launch_cycle_timer[0] <= set_time_1 + 15
                and launch_cycle_timer_name == set_cycle_timer_name):
            self.logger.info(u"[APP_INFO]device state: %s" % launch_cycle_timer)
        else:
            raise TimeoutException("device state error, current: %s" % launch_cycle_timer)

        launch_cycle_timer = launch_cycle_timer_list[1]
        launch_cycle_timer_name = launch_cycle_timer[-2]
        if (set_time_2 - 15 <= launch_cycle_timer[0] <= set_time_2 + 15
                and launch_cycle_timer_name == set_cycle_timer_name):
            self.logger.info(u"[APP_INFO]device state: %s" % launch_cycle_timer)
        else:
            raise TimeoutException("device state error, current: %s" % launch_cycle_timer)
