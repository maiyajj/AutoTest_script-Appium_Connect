# coding=utf-8
from src.testcase.case.LaunchApp_JD import *


class JDAppOverDay1(LaunchAppJD):
    @case_run_jd(False)
    def run(self):
        self.case_module = u"模式定时"  # 用例所属模块
        self.case_title = u'热水器模式设置每日循环'  # 用例名称
        self.zentao_id = 1299  # 禅道ID
    
    # 用例动作
    def case(self):
        try:
            while True:
                elements = self.wait_widget(self.page["app_home_page"]["device"])
                new_value = copy.copy(self.page["app_home_page"]["device"])
                for index, element in elements.items():
                    if element is not None and str(self.ac.get_attribute(element, "name")) == conf["MAC"][0]:
                        new_value[0] = new_value[0][index]
                        while True:
                            try:
                                self.widget_click(new_value, self.page["control_device_page"]["title"])
                                raise ValueError()
                            except TimeoutException:
                                self.ac.swipe(0.6, 0.9, 0.6, 0.6, 0, self.driver)
                time.sleep(1)
        except ValueError:
            pass
        
        try:
            self.wait_widget(self.page["control_device_page"]["power_off"])
        except TimeoutException:
            self.widget_click(self.page["control_device_page"]["power_button"],
                              self.page["control_device_page"]["power_off"])
        
        self.widget_click(self.page["control_device_page"]["mode_timer"],
                          self.page["mode_timer_page"]["title"])
        
        self.widget_click(self.page["mode_timer_page"]["water_mode"],
                          self.page["water_mode_timer_page"]["title"])
        
        delay_time_1 = 1
        self.widget_click(self.page["water_mode_timer_page"]["start_time"],
                          self.page["water_mode_timer_page"]["start_h"])
        
        start_time_1, set_time_1 = self.set_timer_roll(self.page["water_mode_timer_page"]["start_h"],
                                                       self.page["water_mode_timer_page"]["start_m"],
                                                       self.page["water_mode_timer_page"]["start_time_text"],
                                                       delay_time_1)
        
        self.widget_click(self.page["water_mode_timer_page"]["start_time"],
                          self.page["water_mode_timer_page"]["title"])
        
        delay_time_2 = 5
        self.widget_click(self.page["water_mode_timer_page"]["end_time"],
                          self.page["water_mode_timer_page"]["end_h"])
        
        start_time_2, set_time_2 = self.set_timer_roll(self.page["water_mode_timer_page"]["end_h"],
                                                       self.page["water_mode_timer_page"]["end_m"],
                                                       self.page["water_mode_timer_page"]["end_time_text"],
                                                       delay_time_2)
        
        self.widget_click(self.page["water_mode_timer_page"]["end_time"],
                          self.page["water_mode_timer_page"]["title"])
        
        attribute = self.ac.get_attribute(self.wait_widget(self.page["water_mode_timer_page"]["repeat"]), "name")
        if u"每日" not in attribute:
            self.widget_click(self.page["water_mode_timer_page"]["repeat"],
                              self.page["timer_repeat_page"]["title"])
            
            try:
                self.wait_widget(self.page["timer_repeat_page"]["once"])
                self.widget_click(self.page["timer_repeat_page"]["repeat_button"],
                                  self.page["timer_repeat_page"]["everyday"])
            except TimeoutException:
                pass
            
            self.widget_click(self.page["timer_repeat_page"]["everyday"],
                              self.page["timer_repeat_page"]["title"])
            
            self.widget_click(self.page["timer_repeat_page"]["to_return"],
                              self.page["water_mode_timer_page"]["title"])
            
            attribute = self.ac.get_attribute(self.wait_widget(self.page["water_mode_timer_page"]["repeat"]), "name")
            if u"每日" not in attribute:
                raise TimeoutException("Cycle set error")
        
        try:
            self.widget_click(self.page["water_mode_timer_page"]["launch"],
                              self.page["mode_timer_page"]["title"])
        except TimeoutException:
            self.wait_widget(self.page["mode_timer_conflict_popup"]["title"])
            self.widget_click(self.page["mode_timer_conflict_popup"]["confirm"],
                              self.page["mode_timer_page"]["title"])
        
        self.widget_click(self.page["mode_timer_page"]["to_return"],
                          self.page["control_device_page"]["title"])
        
        self.wait_widget(self.page["control_device_page"]["power_off"])
        
        self.check_timer(delay_time_1, u"设备已开启", set_time_1)
        
        self.check_timer(delay_time_2, u"设备已关闭", set_time_2)
        
        self.case_over(True)
    
    def check_timer(self, time_delay, power_state, times):
        if isinstance(time_delay, int):
            if time_delay >= 0:
                delay_times = time_delay
            else:
                delay_times = 24 * 60 + time_delay
        else:
            nh, nm = time.strftime("%H:%M").split(":")
            sh, sm = time_delay.split(":")
            time_tmp_1 = int(nh) * 60 + int(nm)
            time_tmp_2 = int(sh) * 60 + int(sm)
            if time_tmp_1 < time_tmp_2:
                delay_times = time_tmp_2 - time_tmp_1
            else:
                delay_times = 24 * 60 + time_tmp_2 - time_tmp_1
        self.now = time.time()
        element = self.wait_widget(self.page["control_device_page"]["power_state"])
        while True:
            attribute = self.ac.get_attribute(element, "name")
            if time.strftime("%H:%M") == times:
                time.sleep(10)
                if attribute == power_state:
                    self.logger.info("[APP_INFO]Timer Run:%s" % (time.time() - self.now - 10))
                    self.logger.info(u"[APP_INFO]Device Info:%s" % power_state)
                    break
                else:
                    raise TimeoutException("Device state Error")
            else:
                if time.time() < self.now + delay_times * 60 + 30:
                    time.sleep(1)
                else:
                    raise TimeoutException("Device state Error, time out")
