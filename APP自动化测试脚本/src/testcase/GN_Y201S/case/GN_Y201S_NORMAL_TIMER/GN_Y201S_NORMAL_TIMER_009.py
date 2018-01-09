# coding=utf-8
from src.testcase.GN_Y201S.WidgetOperation import *


class GNY201SNormalTimer9(WidgetOperation):
    @case_run(False)
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

            self.delete_normal_timer()

            now = time.strftime("%H:%M")

            delay_time_1 = 1
            start_time_1, set_time_1, cycle1 = self.create_normal_timer(now, delay_time_1, "power_on", u"永不")

            delay_time_2 = 2
            start_time_2, set_time_2, cycle2 = self.create_normal_timer(now, delay_time_2, "power_off", u"永不")

            delay_time_3 = 3
            start_time_3, set_time_3, cycle3 = self.create_normal_timer(now, delay_time_3, "power_on", u"永不")

            delay_time_4 = 4
            start_time_4, set_time_4, cycle4 = self.create_normal_timer(now, delay_time_4, "power_off", u"永不")

            delay_time_5 = 5
            start_time_5, set_time_5, cycle5 = self.create_normal_timer(now, delay_time_5, "power_on", u"永不")

            delay_time_6 = 6
            start_time_6, set_time_6, cycle6 = self.create_normal_timer(now, delay_time_6, "power_off", u"永不")

            delay_time_7 = 7
            start_time_7, set_time_7, cycle7 = self.create_normal_timer(now, delay_time_7, "power_on", u"永不")

            delay_time_8 = 8
            start_time_8, set_time_8, cycle8 = self.create_normal_timer(now, delay_time_8, "power_off", u"永不")

            delay_time_9 = 9
            start_time_9, set_time_9, cycle9 = self.create_normal_timer(now, delay_time_9, "power_on", u"永不")

            delay_time_10 = 10
            start_time_10, set_time_10, cycle10 = self.create_normal_timer(now, delay_time_10, "power_off", u"永不")

            delay_time_11 = 11
            start_time_11, set_time_11, cycle11 = self.create_normal_timer(now, delay_time_11, "power_on", u"永不")

            delay_time_12 = 12
            start_time_12, set_time_12, cycle12 = self.create_normal_timer(now, delay_time_12, "power_off", u"永不")

            delay_time_13 = 13
            start_time_13, set_time_13, cycle13 = self.create_normal_timer(now, delay_time_13, "power_on", u"永不")

            delay_time_14 = 14
            start_time_14, set_time_14, cycle14 = self.create_normal_timer(now, delay_time_14, "power_off", u"永不")

            delay_time_15 = 15
            start_time_15, set_time_15, cycle15 = self.create_normal_timer(now, delay_time_15, "power_on", u"永不")

            delay_time_16 = 16
            start_time_16, set_time_16, cycle16 = self.create_normal_timer(now, delay_time_16, "power_off", u"永不")

            delay_time_17 = 17
            start_time_17, set_time_17, cycle17 = self.create_normal_timer(now, delay_time_17, "power_on", u"永不")

            delay_time_18 = 18
            start_time_18, set_time_18, cycle18 = self.create_normal_timer(now, delay_time_18, "power_off", u"永不")

            delay_time_19 = 19
            start_time_19, set_time_19, cycle19 = self.create_normal_timer(now, delay_time_19, "power_on", u"永不")

            delay_time_20 = 20
            start_time_20, set_time_20, cycle20 = self.create_normal_timer(now, delay_time_20, "power_off", u"永不")

            try:
                time.sleep(3)
                self.widget_click(self.page["normal_timer_page"]["add_normal_timer"],
                                  self.page["add_normal_timer_page"]["title"])
                raise KeyError()
            except TimeoutException:
                self.debug.info("[APP_INFO]add normal timer already 20")
            except KeyError:
                raise TimeoutException("[APP_INFO]add normal timer already 20,but it can add timer yet!\n%s"
                                       % self.driver.page_source)

            self.widget_click(self.page["normal_timer_page"]["to_return"],
                              self.page["control_device_page"]["title"])

            attribute = self.ac.get_attribute(self.wait_widget(self.page["control_device_page"]["launch_mode"]), "name")
            if attribute != u"定时任务开":
                raise TimeoutException("mode launch failed, current: %s" % [attribute])

            self.widget_click(self.page["control_device_page"]["to_return"],
                              self.page["app_home_page"]["title"])

            self.check_timer(device, start_time_1, set_time_1, u"开", cycle1)
            self.check_timer(device, start_time_2, set_time_2, u"关", cycle2)
            self.check_timer(device, start_time_3, set_time_3, u"开", cycle3)
            self.check_timer(device, start_time_4, set_time_4, u"关", cycle4)
            self.check_timer(device, start_time_5, set_time_5, u"开", cycle5)
            self.check_timer(device, start_time_6, set_time_6, u"关", cycle6)
            self.check_timer(device, start_time_7, set_time_7, u"开", cycle7)
            self.check_timer(device, start_time_8, set_time_8, u"关", cycle8)
            self.check_timer(device, start_time_9, set_time_9, u"开", cycle9)
            self.check_timer(device, start_time_10, set_time_10, u"关", cycle10)
            self.check_timer(device, start_time_11, set_time_11, u"开", cycle11)
            self.check_timer(device, start_time_12, set_time_12, u"关", cycle12)
            self.check_timer(device, start_time_13, set_time_13, u"开", cycle13)
            self.check_timer(device, start_time_14, set_time_14, u"关", cycle14)
            self.check_timer(device, start_time_15, set_time_15, u"开", cycle15)
            self.check_timer(device, start_time_16, set_time_16, u"关", cycle16)
            self.check_timer(device, start_time_17, set_time_17, u"开", cycle17)
            self.check_timer(device, start_time_18, set_time_18, u"关", cycle18)
            self.check_timer(device, start_time_19, set_time_19, u"开", cycle19)
            self.check_timer(device, start_time_20, set_time_20, u"关", cycle20)
