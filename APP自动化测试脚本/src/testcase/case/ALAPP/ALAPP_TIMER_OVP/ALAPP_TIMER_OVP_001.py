# coding=utf-8
from src.testcase.common.WidgetOperation_AL import *


class ALAppTimerOvp1(WidgetOperationAL):
    @case_run(False)
    def run(self):
        self.case_module = u"FUT_MTIMER_OVP_充电保护模式(#47)"  # 用例所属模块
        self.case_title = u'FUT_MTIMER_OVP_充电保护模式_延时功能（1min，2min，1h，23h59min，断电恢复）是否正常'  # 用例名称
        self.zentao_id = 459  # 禅道ID

    # 用例动作
    def case(self):
        device = conf["MAC"]["AL"][0]
        self.set_power(device, "power_on")

        time_list = [1, 2, 60, 23 * 60 + 59]
        for i in time_list:
            self.choose_home_device(device)

            self.close_mode_timer()

            self.close_general_timer()

            self.widget_click(self.page["control_device_page"]["piocc_mode_timer"],
                              self.page["piocc_mode_timer_page"]["title"])

            now = time.strftime("%H:%M")

            delay_time_1 = i
            start_time_1, set_time_1 = self.create_delay_mode_timer("piocc_mode_timer_page", now, delay_time_1)

            self.widget_click(self.page["piocc_mode_timer_page"]["to_return"],
                              self.page["control_device_page"]["title"])

            attribute = self.ac.get_attribute(self.wait_widget(self.page["control_device_page"]["launch_mode"]), "name")
            if attribute != u"充电保护模式":
                raise TimeoutException("mode launch failed, current: %s" % [attribute])

            self.widget_click(self.page["control_device_page"]["to_return"],
                              self.page["app_home_page"]["title"])

            self.check_timer(device, start_time_1, set_time_1, u"关")

