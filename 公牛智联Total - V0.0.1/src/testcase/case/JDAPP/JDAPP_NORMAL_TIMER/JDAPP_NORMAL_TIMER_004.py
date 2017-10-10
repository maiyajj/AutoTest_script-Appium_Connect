# coding=utf-8
from src.testcase.case.LaunchApp_JD import *


class JDAppNormalTimer4(LaunchAppJD):
    @case_run_jd(False)
    def run(self):
        self.case_module = u"模式定时"  # 用例所属模块
        self.case_title = u'普通定时_设置13组'  # 用例名称
        self.zentao_id = 1174  # 禅道ID
    
    # 用例动作
    def case(self):
        elements = self.wait_widget(self.page["app_home_page"]["device"])
        new_value = copy.copy(self.page["app_home_page"]["device"])
        for index, element in elements.items():
            if element is not None and str(self.ac.get_attribute(element, "name")) == conf["MAC"][0]:
                new_value[0] = new_value[0][index]
                while True:
                    try:
                        self.widget_click(new_value, self.page["control_device_page"]["title"])
                        break
                    except TimeoutException:
                        self.ac.swipe(0.6, 0.9, 0.6, 0.6, 0, self.driver)
                        time.sleep(1)
            break

        self.close_mode_timer()
        try:
            self.wait_widget(self.page["control_device_page"]["power_off"])
        except TimeoutException:
            self.widget_click(self.page["control_device_page"]["power_button"],
                              self.page["control_device_page"]["power_off"])

        self.widget_click(self.page["control_device_page"]["normal_timer"],
                          self.page["normal_timer_page"]["title"])
        self.delete_normal_timer()

        self.now = time.strftime("%H:%M")

        delay_time_1 = 1
        self.create_timer(delay_time_1, "power_on")

        delay_time_2 = 2
        self.create_timer(delay_time_2, "power_off")

        delay_time_3 = 3
        self.create_timer(delay_time_3, "power_on")

        delay_time_4 = 4
        self.create_timer(delay_time_4, "power_off")

        delay_time_5 = 5
        self.create_timer(delay_time_5, "power_on")

        delay_time_6 = 6
        self.create_timer(delay_time_6, "power_off")

        delay_time_7 = 7
        self.create_timer(delay_time_7, "power_on")

        delay_time_8 = 8
        self.create_timer(delay_time_8, "power_off")

        delay_time_9 = 9
        self.create_timer(delay_time_9, "power_on")

        delay_time_10 = 10
        self.create_timer(delay_time_10, "power_off")

        delay_time_11 = 11
        self.create_timer(delay_time_11, "power_on")

        delay_time_12 = 12
        self.create_timer(delay_time_12, "power_off")

        try:
            delay_time_13 = 13
            self.create_timer(delay_time_13, "power_on")
        except TimeoutException:
            self.logger.info(u"[APP_TIMER]第13个定时设置失败:%s[%s]" % (time.strftime("%H:%M:%S"), time.time()))

        self.widget_click(self.page["normal_timer_page"]["to_return"],
                          self.page["control_device_page"]["title"])

        self.wait_widget(self.page["control_device_page"]["power_off"])

        self.case_over(True)

    def create_timer(self, delay_time, power):
        self.widget_click(self.page["normal_timer_page"]["add_timer"],
                          self.page["add_normal_timer_page"]["title"])

        start_time, set_time = self.set_timer_roll(self.page["add_normal_timer_page"]["roll_h"],
                                                   self.page["add_normal_timer_page"]["roll_m"],
                                                   self.page["add_normal_timer_page"]["set_timer"],
                                                   delay_time, self.now)

        self.widget_click(self.page["add_normal_timer_page"][power],
                          self.page["add_normal_timer_page"]["title"])

        if u"执行一次" not in self.ac.get_attribute(self.wait_widget(self.page["add_normal_timer_page"]["repeat"]),
                                                "name"):
            self.widget_click(self.page["add_normal_timer_page"]["repeat"],
                              self.page["timer_repeat_page"]["title"])

            self.widget_click(self.page["timer_repeat_page"]["repeat_button"],
                              self.page["timer_repeat_page"]["once"])

            self.widget_click(self.page["timer_repeat_page"]["to_return"],
                              self.page["add_normal_timer_page"]["title"])

        self.widget_click(self.page["add_normal_timer_page"]["saved"],
                          self.page["normal_timer_page"]["title"])
        self.logger.info(u"[APP_TIMER]Start Time:%s[%s]" % (time.strftime("%H:%M:%S"), time.time()))

        return start_time, set_time
