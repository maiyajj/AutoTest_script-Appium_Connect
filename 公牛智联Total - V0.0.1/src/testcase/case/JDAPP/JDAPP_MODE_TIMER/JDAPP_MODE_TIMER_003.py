# coding=utf-8
from src.testcase.case.LaunchApp_JD import *


class JDAppModeTimer3(LaunchAppJD):
    @case_run_jd(False)
    def run(self):
        self.case_module = u"模式定时"  # 用例所属模块
        self.case_title = u'充电保护模式下延时关闭1分钟'  # 用例名称
        self.zentao_id = 1086  # 禅道ID
    
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
        
        delay_time_1 = -1
        self.widget_click(self.page["water_mode_timer_page"]["start_time"],
                          self.page["water_mode_timer_page"]["start_h"])
        
        self.set_timer_roll(self.page["water_mode_timer_page"]["start_h"],
                            self.page["water_mode_timer_page"]["start_m"],
                            self.page["water_mode_timer_page"]["start_time_text"], delay_time_1)
        
        self.widget_click(self.page["water_mode_timer_page"]["start_time"],
                          self.page["water_mode_timer_page"]["title"])
        
        delay_time_2 = 3
        self.widget_click(self.page["water_mode_timer_page"]["end_time"],
                          self.page["water_mode_timer_page"]["end_h"])
        
        self.set_timer_roll(self.page["water_mode_timer_page"]["end_h"],
                            self.page["water_mode_timer_page"]["end_m"],
                            self.page["water_mode_timer_page"]["end_time_text"], delay_time_2)
        
        self.widget_click(self.page["water_mode_timer_page"]["end_time"],
                          self.page["water_mode_timer_page"]["title"])
        
        attribute = self.ac.get_attribute(self.wait_widget(self.page["water_mode_timer_page"]["repeat"]), "name")
        if u"执行一次" not in attribute:
            self.widget_click(self.page["water_mode_timer_page"]["repeat"],
                              self.page["timer_repeat_page"]["title"])
            
            self.widget_click(self.page["timer_repeat_page"]["repeat_button"],
                              self.page["timer_repeat_page"]["once"])
            
            self.widget_click(self.page["timer_repeat_page"]["to_return"],
                              self.page["water_mode_timer_page"]["title"])
            
            attribute = self.ac.get_attribute(self.wait_widget(self.page["water_mode_timer_page"]["repeat"]), "name")
            if u"执行一次" not in attribute:
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
        
        self.check_timer(3, u"设备已开启")
        
        self.case_over(True)
    
    def check_timer(self, time_delay, power_state):
        now = time.time()
        element = self.wait_widget(self.page["control_device_page"]["power_state"])
        while True:
            attribute = self.ac.get_attribute(element, "name")
            if attribute == power_state:
                self.logger.info("[APP_INFO]Timer Run:%s" % (time.time() - now))
                self.logger.info(u"[APP_INFO]Device Info:%s" % power_state)
                break
            else:
                if time.time() < now + time_delay * 60 + 30:
                    time.sleep(1)
                else:
                    raise TimeoutException("Device state Error")
