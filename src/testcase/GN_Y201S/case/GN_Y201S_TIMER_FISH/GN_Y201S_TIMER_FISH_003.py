# coding=utf-8
from src.testcase.GN_Y201S.WidgetOperation import *


class GNY201STimerFish3(WidgetOperation):
    @case_run(False)
    def run(self):
        self.case_module = u"FUT_MTIMER_FISH_鱼缸模式(#59)"  # 用例所属模块
        self.case_title = u'FUT_MTIMER_FISH_鱼缸模式开启2分钟，关闭2分钟功能是否正常'  # 用例名称
        self.zentao_id = "440"  # 禅道ID

    # 用例动作
    def case(self):
        device = conf["MAC"]["AL"][0]
        self.set_power(device, "power_off")

        self.choose_home_device(device)

        self.close_mode_timer()

        self.close_general_timer()

        self.widget_click(self.page["control_device_page"]["fish_mode_timer"],
                          self.page["fish_mode_timer_page"]["title"])

        now = time.strftime("%H:%M")

        time_1, time_2 = ["delay", "00:02"], ["delay", "00:02"]
        tmp = self.create_cycle_timer("fish_mode_timer_page", now, time_1, time_2, u"永久循环")
        start_time_1, set_time_1, start_time_2, set_time_2 = tmp[0]

        self.widget_click(self.page["fish_mode_timer_page"]["to_return"],
                          self.page["control_device_page"]["title"])

        attribute = self.ac.get_attribute(self.wait_widget(self.page["control_device_page"]["launch_mode"]), "name")
        if attribute != u"鱼缸模式":
            raise TimeoutException("mode launch failed, current: %s" % [attribute])

        self.widget_click(self.page["control_device_page"]["to_return"],
                          self.page["app_home_page"]["title"])

        self.check_timer(device, start_time_1, set_time_1, u"关")
        self.check_timer(device, start_time_2, set_time_2, u"开")
