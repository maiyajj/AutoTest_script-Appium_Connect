# coding=utf-8
from src.testcase.common.WidgetOperation_AL import *


class ALAppDelayTimer3(WidgetOperationAL):
    @case_run_al(True)
    def run(self):
        self.case_module = u"FUT_DELAYTIMER_延迟定时(#51)"  # 用例所属模块
        self.case_title = u'FUT_DELAYTIMER_延迟定时5分钟开'  # 用例名称
        self.zentao_id = 466  # 禅道ID

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

        delay_time_1 = 5
        start_time_1, set_time_1 = self.create_delay_timer(now, delay_time_1, "power_on")

        self.widget_click(self.page["delay_timer_page"]["to_return"],
                          self.page["control_device_page"]["title"])

        attribute = self.ac.get_attribute(self.wait_widget(self.page["control_device_page"]["launch_mode"]), "name")
        if attribute != u"延时任务开":
            raise TimeoutException("mode launch failed, current:%s" % str([attribute]))

        self.widget_click(self.page["control_device_page"]["to_return"],
                          self.page["app_home_page"]["title"])

        self.check_timer(device, start_time_1, set_time_1, u"设备已开启")

        self.case_over(True)
