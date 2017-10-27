# coding=utf-8
from src.testcase.common.WidgetOperation_AL import *


class ALAppTimerTime2(WidgetOperationAL):
    @case_run_al(True)
    def run(self):
        self.case_module = u"FUT_MTIMER_TIME热水器模式_小夜灯_取暖器模式(#58)"  # 用例所属模块
        self.case_title = u'FUT_MTIMER_TIME_模式定时每日循环'  # 用例名称
        self.zentao_id = 446  # 禅道ID

    # 用例动作
    def case(self):
        device = conf["MAC"]["AL"][0]
        self.set_power(device, "power_off")

        timer_list = [["water_mode_timer", "water_mode_timer_page", u"热水器模式"],
                      ["night_mode_timer", "night_mode_timer_page", u"小夜灯模式"],
                      ["warmer_mode_timer", "warmer_mode_timer_page", u"取暖器模式"], ]

        for elem, page, mode_info in timer_list:
            self.choose_home_device(device)

            self.close_mode_timer()

            self.close_general_timer()

            self.widget_click(self.page["control_device_page"][elem],
                              self.page[page]["title"])

            now = time.strftime("%H:%M")

            delay_time_1, delay_time_2 = 1, 3
            tmp = self.create_point_mode_timer(page, now, delay_time_1, delay_time_2, u"每天")
            start_time_1, set_time_1 = tmp[0]
            start_time_2, set_time_2 = tmp[1]

            self.widget_click(self.page[page]["to_return"],
                              self.page["control_device_page"]["title"])

            attribute = self.ac.get_attribute(self.wait_widget(self.page["control_device_page"]["launch_mode"]), "name")
            if attribute != mode_info:
                raise TimeoutException("mode launch failed, current:%s" % str([attribute]))

            self.widget_click(self.page["control_device_page"]["to_return"],
                              self.page["app_home_page"]["title"])

            self.check_timer(device, start_time_1, set_time_1, u"设备已关闭")
            self.check_timer(device, start_time_2, set_time_2, u"设备已开启")

        self.case_over(True)
