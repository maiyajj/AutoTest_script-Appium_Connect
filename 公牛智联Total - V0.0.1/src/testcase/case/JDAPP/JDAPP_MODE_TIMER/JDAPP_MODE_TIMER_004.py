# coding=utf-8
from src.testcase.case.LaunchApp_JD import *


class JDAppModeTimer4(LaunchAppJD):
    @case_run_jd(False)
    def run(self):
        self.case_module = u"模式定时"  # 用例所属模块
        self.case_title = u'充电保护模式下手动改变设备为开启状态后，定时结束检查设备状态'  # 用例名称
        self.zentao_id = 1083  # 禅道ID
    
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

        self.widget_click(self.page["control_device_page"]["mode_timer"],
                          self.page["mode_timer_page"]["title"])

        self.widget_click(self.page["mode_timer_page"]["piocc_mode"],
                          self.page["piocc_mode_timer_page"]["title"])

        self.now = time.strftime("%H:%M")

        delay_time_1 = ["delay", "00:05"]
        start_time_1, set_time_1 = self.set_timer_roll(self.page["piocc_mode_timer_page"]["end_h"],
                                                       self.page["piocc_mode_timer_page"]["end_m"],
                                                       self.page["piocc_mode_timer_page"]["end_time_text"],
                                                       delay_time_1, self.now)

        self.widget_click(self.page["piocc_mode_timer_page"]["end_time"],
                          self.page["piocc_mode_timer_page"]["title"])

        now = time.time()
        while True:
            if time.strftime("%H:%M") == start_time_1:
                try:
                    self.widget_click(self.page["piocc_mode_timer_page"]["launch"],
                                      self.page["mode_timer_page"]["title"])
                    self.logger.info(u"[APP_TIMER]Start Time:%s[%s]" % (time.strftime("%H:%M:%S"), time.time()))
                except TimeoutException:
                    self.wait_widget(self.page["mode_timer_conflict_popup"]["title"])
                    self.widget_click(self.page["mode_timer_conflict_popup"]["confirm"],
                                      self.page["mode_timer_page"]["title"])
                break
            else:
                if time.time() < now + 1 * 60 + 30:
                    time.sleep(1)
                else:
                    raise TimeoutException("Timer Saved Error, time:%s" % start_time_1)

        self.widget_click(self.page["mode_timer_page"]["to_return"],
                          self.page["control_device_page"]["title"])

        self.wait_widget(self.page["control_device_page"]["power_on"])

        time.sleep(60)

        self.widget_click(self.page["control_device_page"]["power_on"],
                          self.page["control_device_page"]["power_off"])

        self.widget_click(self.page["control_device_page"]["power_off"],
                          self.page["control_device_page"]["power_on"])

        self.check_timer(start_time_1, set_time_1, u"设备已关闭")

        self.case_over(True)
