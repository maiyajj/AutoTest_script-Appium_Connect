# coding=utf-8
from src.testcase.case.LaunchApp_JD import *


class JDAppOverDay5(LaunchAppJD):
    @case_run_jd(False)
    def run(self):
        self.case_module = u"模式定时"  # 用例所属模块
        self.case_title = u'每日循环普通定时'  # 用例名称
        self.zentao_id = 1304  # 禅道ID
    
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
        
        delay_time_1 = 2
        delay_time_2 = 4
        start_time_1, set_time_1 = self.create_normal_timer(delay_time_1, "power_on")
        start_time_2, set_time_2 = self.create_normal_timer(delay_time_2, "power_off")
        
        self.widget_click(self.page["normal_timer_page"]["to_return"],
                          self.page["control_device_page"]["title"])
        
        self.wait_widget(self.page["control_device_page"]["power_off"])
    
        self.check_timer(start_time_1, set_time_1, u"设备已开启")
        self.check_timer(start_time_2, set_time_2, u"设备已关闭")

        self.case_over(True)
    
    def create_normal_timer(self, delay_time, power):
        self.widget_click(self.page["normal_timer_page"]["add_timer"],
                          self.page["add_normal_timer_page"]["title"])

        start_time, set_time = self.set_timer_roll(self.page["add_normal_timer_page"]["roll_h"],
                                                   self.page["add_normal_timer_page"]["roll_m"],
                                                   self.page["add_normal_timer_page"]["set_timer"],
                                                   delay_time, self.now)
        
        self.widget_click(self.page["add_normal_timer_page"][power],
                          self.page["add_normal_timer_page"]["title"])
        
        attribute = self.ac.get_attribute(self.wait_widget(self.page["add_normal_timer_page"]["repeat"]), "name")
        if u"每天" not in attribute:
            self.widget_click(self.page["add_normal_timer_page"]["repeat"],
                              self.page["timer_repeat_page"]["title"])
            
            self.widget_click(self.page["timer_repeat_page"]["repeat_button"],
                              self.page["timer_repeat_page"]["everyday"])
            
            self.widget_click(self.page["timer_repeat_page"]["everyday"],
                              self.page["timer_repeat_page"]["title"])
            
            self.widget_click(self.page["timer_repeat_page"]["to_return"],
                              self.page["add_normal_timer_page"]["title"])
            
            attribute = self.ac.get_attribute(self.wait_widget(self.page["add_normal_timer_page"]["repeat"]), "name")
            if u"每天" not in attribute:
                raise TimeoutException("Cycle set error")
        
        self.widget_click(self.page["add_normal_timer_page"]["saved"],
                          self.page["normal_timer_page"]["title"])
        self.logger.info(u"[APP_TIMER]Start Time:%s[%s]" % (time.strftime("%H:%M:%S"), time.time()))
        
        return start_time, set_time
