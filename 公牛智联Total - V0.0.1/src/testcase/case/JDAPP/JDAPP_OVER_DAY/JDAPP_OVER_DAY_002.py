# coding=utf-8
from src.testcase.case.LaunchApp_JD import *


class JDAppOverDay2(LaunchAppJD):
    @case_run_jd(False)
    def run(self):
        self.case_module = u"模式定时"  # 用例所属模块
        self.case_title = u'热水器模式在跨天循环下的跨天执行'  # 用例名称
        self.zentao_id = 1300  # 禅道ID
    
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
        
        self.widget_click(self.page["mode_timer_page"]["water_mode"],
                          self.page["water_mode_timer_page"]["title"])
    
        self.now = time.strftime("%H:%M")
    
        delay_time_1 = ["point", "17:00"]
        self.widget_click(self.page["water_mode_timer_page"]["start_time"],
                          self.page["water_mode_timer_page"]["roll_h"])
    
        start_time_1, set_time_1 = self.set_timer_roll(self.page["water_mode_timer_page"]["roll_h"],
                                                       self.page["water_mode_timer_page"]["roll_m"],
                                                       self.page["water_mode_timer_page"]["start_time_text"],
                                                       delay_time_1, self.now)
        
        self.widget_click(self.page["water_mode_timer_page"]["start_time"],
                          self.page["water_mode_timer_page"]["title"])
    
        delay_time_2 = ["point", "01:00"]
        self.widget_click(self.page["water_mode_timer_page"]["end_time"],
                          self.page["water_mode_timer_page"]["end_h"])
    
        start_time_2, set_time_2 = self.set_timer_roll(self.page["water_mode_timer_page"]["end_h"],
                                                       self.page["water_mode_timer_page"]["end_m"],
                                                       self.page["water_mode_timer_page"]["end_time_text"],
                                                       delay_time_2, self.now)
        
        self.widget_click(self.page["water_mode_timer_page"]["end_time"],
                          self.page["water_mode_timer_page"]["title"])
        
        attribute = self.ac.get_attribute(self.wait_widget(self.page["water_mode_timer_page"]["repeat"]), "name")
        if u"周" not in attribute:
            self.widget_click(self.page["water_mode_timer_page"]["repeat"],
                              self.page["timer_repeat_page"]["title"])
            
            try:
                self.wait_widget(self.page["timer_repeat_page"]["once"])
                self.widget_click(self.page["timer_repeat_page"]["repeat_button"],
                                  self.page["timer_repeat_page"]["everyday"])
            except TimeoutException:
                pass
            
            try:
                self.wait_widget(self.page["timer_repeat_page"]["monday"])
            except TimeoutException:
                self.widget_click(self.page["timer_repeat_page"]["define"],
                                  self.page["timer_repeat_page"]["monday"])
            
            date_1 = ["monday", "wednesday", "friday"]
            now = time.strftime("%A").lower()
            if now in date_1:
                self.widget_click(self.page["timer_repeat_page"]["monday"],
                                  self.page["timer_repeat_page"]["define"])
                
                self.widget_click(self.page["timer_repeat_page"]["wednesday"],
                                  self.page["timer_repeat_page"]["define"])
                
                self.widget_click(self.page["timer_repeat_page"]["friday"],
                                  self.page["timer_repeat_page"]["define"])
                date_2 = u"周一 周三 周五"
            
            else:
                self.widget_click(self.page["timer_repeat_page"]["tuesday"],
                                  self.page["timer_repeat_page"]["define"])
                
                self.widget_click(self.page["timer_repeat_page"]["thursday"],
                                  self.page["timer_repeat_page"]["define"])
                
                self.widget_click(self.page["timer_repeat_page"]["saturday"],
                                  self.page["timer_repeat_page"]["define"])
                date_2 = u"周二 周四 周六"
            
            self.widget_click(self.page["timer_repeat_page"]["to_return"],
                              self.page["water_mode_timer_page"]["title"])
            
            attribute = self.ac.get_attribute(self.wait_widget(self.page["water_mode_timer_page"]["repeat"]), "name")
            if date_2 not in attribute:
                raise TimeoutException("Cycle set error")
        
        try:
            self.widget_click(self.page["water_mode_timer_page"]["launch"],
                              self.page["mode_timer_page"]["title"])
            self.logger.info(u"[APP_TIMER]Start Time:%s[%s]" % (time.strftime("%H:%M:%S"), time.time()))
        except TimeoutException:
            self.wait_widget(self.page["mode_timer_conflict_popup"]["title"])
            self.widget_click(self.page["mode_timer_conflict_popup"]["confirm"],
                              self.page["mode_timer_page"]["title"])
        
        self.widget_click(self.page["mode_timer_page"]["to_return"],
                          self.page["control_device_page"]["title"])
        
        self.wait_widget(self.page["control_device_page"]["power_off"])
    
        self.check_timer(start_time_1, set_time_1, u"设备已开启")
    
        self.check_timer(start_time_2, set_time_2, u"设备已关闭")
        
        self.case_over(True)
    