# coding=utf-8
from src.testcase.common.WidgetOperation_JD import *


class JDAppNormalTimer7(WidgetOperationJD):
    @case_run_jd(False)
    def run(self):
        self.case_module = u"模式定时"  # 用例所属模块
        self.case_title = u'单次定时关_2分钟'  # 用例名称
        self.zentao_id = 1185  # 禅道ID

    # 用例动作
    def case(self):
        self.choose_home_device(conf["MAC"][0])

        self.close_mode_timer()

        self.set_power("power_on")

        self.widget_click(self.page["control_device_page"]["normal_timer"],
                          self.page["normal_timer_page"]["title"])
        self.delete_normal_timer()

        now = time.strftime("%H:%M")

        delay_time_1 = 2
        start_time_1, set_time_1 = self.create_normal_timer(now, delay_time_1, "power_off", u"执行一次")

        self.widget_click(self.page["normal_timer_page"]["to_return"],
                          self.page["control_device_page"]["title"])

        self.wait_widget(self.page["control_device_page"]["power_on"])

        self.check_timer(start_time_1, set_time_1, u"设备已关闭")

        self.case_over(True)
