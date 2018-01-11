# coding=utf-8
from src.testcase.GN_Y201H.WidgetOperation import *


class GNY201HTimerFunc3(WidgetOperation):
    @case_run(False)
    def run(self):
        self.case_module = u"定时功能(#240)"  # 用例所属模块
        self.case_title = u'普通定时周期格式检查'  # 用例名称
        self.zentao_id = 2020  # 禅道ID

    # 用例动作
    def case(self):
        self.choose_home_device(conf["MAC"]["HW"][0])

        self.delete_normal_timer()

        self.delete_delay_timer()

        self.set_power("power_off")

        self.widget_click(self.page["control_device_page"]["normal_timer"],
                          self.page["normal_timer_page"]["title"])

        self.widget_click(self.page["normal_timer_page"]["add_timer"],
                          self.page["add_normal_timer_page"]["title"])

        self.widget_click(self.page["add_normal_timer_page"]["repeat"],
                          self.page["timer_repeat_popup"]["title"])

        self.wait_widget(self.page["timer_repeat_popup"]["once"])

        self.wait_widget(self.page["timer_repeat_popup"]["everyday"])

        self.wait_widget(self.page["timer_repeat_popup"]["weekend"])

        self.wait_widget(self.page["timer_repeat_popup"]["define"])

        self.widget_click(self.page["timer_repeat_popup"]["define"],
                          self.page["timer_repeat_popup"]["monday"])

        self.wait_widget(self.page["timer_repeat_popup"]["monday"])

        self.wait_widget(self.page["timer_repeat_popup"]["tuesday"])

        self.wait_widget(self.page["timer_repeat_popup"]["wednesday"])

        self.wait_widget(self.page["timer_repeat_popup"]["thursday"])

        self.wait_widget(self.page["timer_repeat_popup"]["friday"])

        self.wait_widget(self.page["timer_repeat_popup"]["saturday"])

        self.wait_widget(self.page["timer_repeat_popup"]["weekday"])
