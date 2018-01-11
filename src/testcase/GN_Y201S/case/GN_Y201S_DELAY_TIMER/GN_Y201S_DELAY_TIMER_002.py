# coding=utf-8
from src.testcase.GN_Y201S.WidgetOperation import *


class GNY201SDelayTimer2(WidgetOperation):
    @case_run(False)
    def run(self):
        self.case_module = u"FUT_DELAYTIMER_延迟定时(#51)"  # 用例所属模块
        self.case_title = u'FUT_DELAYTIMER_延迟定时一小时开'  # 用例名称
        self.zentao_id = 468  # 禅道ID

    # 用例动作
    def case(self):
        device = conf["MAC"]["AL"][0]
        self.set_power(device, "power_off")

        self.choose_home_device(device)

        self.close_mode_timer()

        self.close_general_timer()

        self.widget_click(self.page["control_device_page"]["delay_timer"],
                          self.page["delay_timer_page"]["title"])

        now = time.strftime("%H:%M")

        delay_time_1 = ["delay", "01:00"]
        start_time_1, set_time_1 = self.create_delay_timer(now, delay_time_1, "power_on")

        self.widget_click(self.page["delay_timer_page"]["to_return"],
                          self.page["control_device_page"]["title"])

        attribute = self.ac.get_attribute(self.wait_widget(self.page["control_device_page"]["launch_mode"]), "name")
        if attribute != u"延时任务开":
            raise TimeoutException("mode launch failed, current: %s" % [attribute])

        self.widget_click(self.page["control_device_page"]["to_return"],
                          self.page["app_home_page"]["title"])

        self.check_timer(device, start_time_1, set_time_1, u"开")
