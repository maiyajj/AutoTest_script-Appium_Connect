# coding=utf-8
from src.testcase.case.LaunchApp_JD import *


class JDAppNormalTimer1(LaunchAppJD):
    @case_run_jd(False)
    def run(self):
        self.case_module = u"模式定时"  # 用例所属模块
        self.case_title = u'普通交叉定时_8分钟'  # 用例名称
        self.zentao_id = 1181  # 禅道ID
    
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
        
        self.widget_click(self.page["control_device_page"]["normal_timer"],
                          self.page["normal_timer_page"]["title"])
        
        delay_time_1 = 2
        delay_time_2 = 4
        delay_time_3 = 6
        delay_time_4 = 8
        start_time_1, set_time_1 = self.create_normal_timer(delay_time_1, "power_on")
        start_time_2, set_time_2 = self.create_normal_timer(delay_time_2, "power_on")
        start_time_3, set_time_3 = self.create_normal_timer(delay_time_3, "power_off")
        start_time_4, set_time_4 = self.create_normal_timer(delay_time_4, "power_off")
        
        self.widget_click(self.page["normal_timer_page"]["to_return"],
                          self.page["control_device_page"]["title"])
        
        self.wait_widget(self.page["control_device_page"]["power_off"])
        
        self.check_timer(delay_time_1, u"设备已开启", set_time_1)
        self.check_timer(delay_time_2 - delay_time_1, u"设备已开启", set_time_2)
        self.check_timer(delay_time_3 - delay_time_2, u"设备已关闭", set_time_3)
        self.check_timer(delay_time_4 - delay_time_3, u"设备已关闭", set_time_4)
    
    def create_normal_timer(self, delay_time, power):
        self.widget_click(self.page["normal_timer_page"]["add_timer"],
                          self.page["add_normal_timer_page"]["title"])
        
        start_time, set_time = self.set_timer_roll(self.page["add_normal_timer_page"]["timer_h"],
                                                   self.page["add_normal_timer_page"]["timer_m"],
                                                   self.page["add_normal_timer_page"]["set_timer"],
                                                   delay_time)
        
        self.widget_click(self.page["add_normal_timer_page"][power],
                          self.page["add_normal_timer_page"]["title"])
        
        attribute = self.ac.get_attribute(self.wait_widget(self.page["add_normal_timer_page"]["repeat"]), "name")
        if u"执行一次" not in attribute:
            self.widget_click(self.page["add_normal_timer_page"]["repeat"],
                              self.page["timer_repeat_page"]["title"])
            
            self.widget_click(self.page["timer_repeat_page"]["repeat_button"],
                              self.page["timer_repeat_page"]["once"])
            
            self.widget_click(self.page["timer_repeat_page"]["to_return"],
                              self.page["add_normal_timer_page"]["title"])
        
        self.widget_click(self.page["add_normal_timer_page"]["saved"],
                          self.page["normal_timer_page"]["title"])
        return start_time, set_time
    
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
