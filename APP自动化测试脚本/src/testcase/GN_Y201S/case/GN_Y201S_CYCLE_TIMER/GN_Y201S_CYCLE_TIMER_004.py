# coding=utf-8
from src.testcase.GN_Y201S.WidgetOperation import *


class GNY201SCycleTimer4(WidgetOperation):
    @case_run(False)
    def run(self):
        self.case_module = u"FUT_CYCLETIMER_循环定时(#50)"  # 用例所属模块
        self.case_title = u'FUT_CYCLETIMER_循环定时1次'  # 用例名称
        self.zentao_id = 483  # 禅道ID

    # 用例动作
    def case(self):
        device = conf["MAC"]["AL"][0]
        self.set_power(device, "power_off")

        self.choose_home_device(device)

        self.close_mode_timer()

        self.close_general_timer()

        self.ac.swipe(0.5, 0.6, 0.5, 0.4, self.driver)
        self.widget_click(self.page["control_device_page"]["cycle_timer"],
                          self.page["cycle_timer_page"]["title"])

        now = time.strftime("%H:%M")

        delay_time_1, delay_time_2 = ["delay", "00:01"], ["delay", "00:01"]
        tmp = self.create_cycle_timer("cycle_timer_page", now, delay_time_1, delay_time_2, u"1次")
        start_time_1, set_time_1, start_time_2, set_time_2 = tmp[0]
        start_time_3, set_time_3, start_time_4, set_time_4 = tmp[1]

        self.widget_click(self.page["cycle_timer_page"]["to_return"],
                          self.page["control_device_page"]["title"])

        self.ac.swipe(0.5, 0.4, 0.5, 0.6, self.driver)
        attribute = self.ac.get_attribute(self.wait_widget(self.page["control_device_page"]["launch_mode"]), "name")
        if attribute != u"循环任务开":
            raise TimeoutException("mode launch failed, current: %s" % [attribute])

        self.widget_click(self.page["control_device_page"]["to_return"],
                          self.page["app_home_page"]["title"])

        self.check_timer(device, start_time_1, set_time_1, u"关")
        self.check_timer(device, start_time_2, set_time_2, u"开")
        self.check_timer(device, start_time_3, set_time_3, u"关")
        self.check_timer(device, start_time_4, set_time_4, u"关")
