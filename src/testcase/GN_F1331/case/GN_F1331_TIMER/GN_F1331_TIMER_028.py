# coding=utf-8
from src.testcase.GN_F1331.WidgetOperation import *


class GNF1331Timer28(WidgetOperation):
    @case_run(False)
    def run(self):
        self.case_module = u"定时器(#9)"  # 用例所属模块
        self.case_title = u'APP默认定时数组检测'  # 用例名称
        self.zentao_id = "72"  # 禅道ID

    # 用例动作
    def case(self):
        self.choose_home_device(conf["MAC"][self.app][self.device_mac])

        self.delete_out_date_timer()
        self.delete_normal_timer_all()

        self.set_power("main_button_off")

        # 上层
        self.widget_click(self.page["control_device_page"]["up_timer"],
                          self.page["up_timer_page"]["title"])

        self.wait_widget(self.page["up_timer_page"]["delay_timer"])

        self.wait_widget(self.page["up_timer_page"]["cycle_timer"])

        self.wait_widget(self.page["up_timer_page"]["add_normal_timer_button"])

        self.widget_click(self.page["up_timer_page"]["to_return"],
                          self.page["control_device_page"]["title"])

        # 中层
        self.widget_click(self.page["control_device_page"]["mid_timer"],
                          self.page["mid_timer_page"]["title"])

        self.wait_widget(self.page["mid_timer_page"]["delay_timer"])

        self.wait_widget(self.page["mid_timer_page"]["cycle_timer"])

        self.wait_widget(self.page["mid_timer_page"]["add_normal_timer_button"])

        self.widget_click(self.page["mid_timer_page"]["to_return"],
                          self.page["control_device_page"]["title"])

        # 下层
        self.widget_click(self.page["control_device_page"]["down_timer"],
                          self.page["down_timer_page"]["title"])

        self.wait_widget(self.page["down_timer_page"]["delay_timer"])

        self.wait_widget(self.page["down_timer_page"]["cycle_timer"])

        self.wait_widget(self.page["down_timer_page"]["add_normal_timer_button"])

        self.widget_click(self.page["down_timer_page"]["to_return"],
                          self.page["control_device_page"]["title"])
