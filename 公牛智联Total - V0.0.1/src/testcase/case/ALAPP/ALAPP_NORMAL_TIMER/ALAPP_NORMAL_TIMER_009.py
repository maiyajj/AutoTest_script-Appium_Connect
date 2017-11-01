# coding=utf-8
from src.testcase.common.WidgetOperation_AL import *


class ALAppNormalTimer9(WidgetOperationAL):
    @case_run_al(False)
    def run(self):
        self.case_module = u"FUT_NTIMER_普通定时(#48)"  # 用例所属模块
        self.case_title = u'FUT_NTIMER_普通定时最大组数设定'  # 用例名称
        self.zentao_id = 494  # 禅道ID

    # 用例动作
    def case(self):
        device = conf["MAC"]["AL"][0]
        self.set_power(device, "power_off")

        for i in xrange(2):
            self.choose_home_device(device)

            self.close_mode_timer()

            self.close_general_timer()

            self.widget_click(self.page["control_device_page"]["normal_timer"],
                              self.page["normal_timer_page"]["title"])

            now = time.strftime("%H:%M")

            delay_time_1 = 1
            start_time_1, set_time_1 = self.create_normal_timer(now, delay_time_1, "power_on", u"永不")

            delay_time_2 = 2
            start_time_2, set_time_2 = self.create_normal_timer(now, delay_time_2, "power_off", u"永不")

            delay_time_3 = 3
            start_time_3, set_time_3 = self.create_normal_timer(now, delay_time_3, "power_on", u"永不")

            delay_time_4 = 4
            start_time_4, set_time_4 = self.create_normal_timer(now, delay_time_4, "power_off", u"永不")

            delay_time_5 = 5
            start_time_5, set_time_5 = self.create_normal_timer(now, delay_time_5, "power_on", u"永不")

            delay_time_6 = 6
            start_time_6, set_time_6 = self.create_normal_timer(now, delay_time_6, "power_off", u"永不")

            delay_time_7 = 7
            start_time_7, set_time_7 = self.create_normal_timer(now, delay_time_7, "power_on", u"永不")

            delay_time_8 = 8
            start_time_8, set_time_8 = self.create_normal_timer(now, delay_time_8, "power_off", u"永不")

            delay_time_9 = 9
            start_time_9, set_time_9 = self.create_normal_timer(now, delay_time_9, "power_on", u"永不")

            delay_time_10 = 10
            start_time_10, set_time_10 = self.create_normal_timer(now, delay_time_10, "power_off", u"永不")

            delay_time_11 = 11
            start_time_11, set_time_11 = self.create_normal_timer(now, delay_time_11, "power_on", u"永不")

            delay_time_12 = 12
            start_time_12, set_time_12 = self.create_normal_timer(now, delay_time_12, "power_off", u"永不")

            delay_time_13 = 13
            start_time_13, set_time_13 = self.create_normal_timer(now, delay_time_13, "power_on", u"永不")

            delay_time_14 = 14
            start_time_14, set_time_14 = self.create_normal_timer(now, delay_time_14, "power_off", u"永不")

            delay_time_15 = 15
            start_time_15, set_time_15 = self.create_normal_timer(now, delay_time_15, "power_on", u"永不")

            delay_time_16 = 16
            start_time_16, set_time_16 = self.create_normal_timer(now, delay_time_16, "power_off", u"永不")

            delay_time_17 = 17
            start_time_17, set_time_17 = self.create_normal_timer(now, delay_time_17, "power_on", u"永不")

            delay_time_18 = 18
            start_time_18, set_time_18 = self.create_normal_timer(now, delay_time_18, "power_off", u"永不")

            delay_time_19 = 19
            start_time_19, set_time_19 = self.create_normal_timer(now, delay_time_19, "power_on", u"永不")

            delay_time_20 = 20
            start_time_20, set_time_20 = self.create_normal_timer(now, delay_time_20, "power_off", u"永不")

            try:
                self.widget_click(self.page["normal_timer_page"]["add_normal_timer"],
                                  self.page["add_normal_timer_page"]["title"])
                raise KeyError()
            except TimeoutException:
                self.logger.info("[APP_INFO]add normal timer already 20")
            except KeyError:
                raise TimeoutException("[APP_INFO]add normal timer already 20,but it can add timer yet!")

            self.widget_click(self.page["normal_timer_page"]["to_return"],
                              self.page["control_device_page"]["title"])

            attribute = self.ac.get_attribute(self.wait_widget(self.page["control_device_page"]["launch_mode"]), "name")
            if attribute != u"定时任务开":
                raise TimeoutException("mode launch failed, current:%s" % [attribute])

            self.widget_click(self.page["control_device_page"]["to_return"],
                              self.page["app_home_page"]["title"])

            self.check_timer(device, start_time_1, set_time_1, u"设备已开启")
            self.check_timer(device, start_time_2, set_time_2, u"设备已关闭")
            self.check_timer(device, start_time_3, set_time_3, u"设备已开启")
            self.check_timer(device, start_time_4, set_time_4, u"设备已关闭")
            self.check_timer(device, start_time_5, set_time_5, u"设备已开启")
            self.check_timer(device, start_time_6, set_time_6, u"设备已关闭")
            self.check_timer(device, start_time_7, set_time_7, u"设备已开启")
            self.check_timer(device, start_time_8, set_time_8, u"设备已关闭")
            self.check_timer(device, start_time_9, set_time_9, u"设备已开启")
            self.check_timer(device, start_time_10, set_time_10, u"设备已关闭")
            self.check_timer(device, start_time_11, set_time_11, u"设备已开启")
            self.check_timer(device, start_time_12, set_time_12, u"设备已关闭")
            self.check_timer(device, start_time_13, set_time_13, u"设备已开启")
            self.check_timer(device, start_time_14, set_time_14, u"设备已关闭")
            self.check_timer(device, start_time_15, set_time_15, u"设备已开启")
            self.check_timer(device, start_time_16, set_time_16, u"设备已关闭")
            self.check_timer(device, start_time_17, set_time_17, u"设备已开启")
            self.check_timer(device, start_time_18, set_time_18, u"设备已关闭")
            self.check_timer(device, start_time_19, set_time_19, u"设备已开启")
            self.check_timer(device, start_time_20, set_time_20, u"设备已关闭")

            self.close_general_timer()

        self.case_over(True)
