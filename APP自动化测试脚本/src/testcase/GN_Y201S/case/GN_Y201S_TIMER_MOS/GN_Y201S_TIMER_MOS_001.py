# coding=utf-8
from src.testcase.GN_Y201S.WidgetOperation import *


class GNY201STimerMos1(WidgetOperation):
    @case_run(False)
    def run(self):
        self.case_module = u"FUT_MTIMER_MOS_电蚊香模式(#62)"  # 用例所属模块
        self.case_title = u'FUT_MTIMER_MOS_电蚊香模式_延时功能（1min，2min，1h，23h59min，断电恢复）是否正常'  # 用例名称
        self.zentao_id = 461  # 禅道ID

    # 用例动作
    def case(self):
        device = conf["MAC"]["AL"][0]
        self.set_power(device, "power_on")

        time_list = [1, 2, 60, 23 * 60 + 59]
        for i in time_list:
            self.choose_home_device(device)

            self.close_mode_timer()

            self.close_general_timer()

            self.widget_click(self.page["control_device_page"]["mosquito_mode_timer"],
                              self.page["mosquito_mode_timer_page"]["title"])

            now = time.strftime("%H:%M")

            delay_time_1 = i
            start_time_1, set_time_1 = self.create_delay_mode_timer("mosquito_mode_timer_page", now, delay_time_1)

            self.widget_click(self.page["mosquito_mode_timer_page"]["to_return"],
                              self.page["control_device_page"]["title"])

            attribute = self.ac.get_attribute(self.wait_widget(self.page["control_device_page"]["launch_mode"]), "name")
            if attribute != u"电蚊香模式":
                raise TimeoutException("mode launch failed, current: %s" % [attribute])

            self.widget_click(self.page["control_device_page"]["to_return"],
                              self.page["app_home_page"]["title"])

            self.check_timer(device, start_time_1, set_time_1, u"关")
