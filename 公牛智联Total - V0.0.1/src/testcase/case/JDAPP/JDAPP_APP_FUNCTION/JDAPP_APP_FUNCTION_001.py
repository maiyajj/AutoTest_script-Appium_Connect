# coding=utf-8
from src.testcase.case.LaunchApp_JD import *


class JDAppAppFunction1(LaunchAppJD):
    @case_run_jd(False)
    def run(self):
        self.case_module = u"APP功能测试"  # 用例所属模块
        self.case_title = u'定时记录删除是否成功'  # 用例名称
        self.zentao_id = 1170  # 禅道ID

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

        try:
            self.wait_widget(self.page["control_device_page"]["power_on"])
            power_state = "power_on"
        except TimeoutException:
            self.wait_widget(self.page["control_device_page"]["power_off"])
            power_state = "power_off"

        self.close_mode_timer()
        self.widget_click(self.page["control_device_page"]["normal_timer"],
                          self.page["normal_timer_page"]["title"])
        self.delete_normal_timer()
        
        self.widget_click(self.page["normal_timer_page"]["timer_log"],
                          self.page["timer_log_page"]["title"])
        try:
            self.wait_widget(self.page["timer_log_page"]["no_log"])
        except TimeoutException:
            self.widget_click(self.page["timer_log_page"]["clear"],
                              self.page["timer_log_clear_popup"]["title"])

            self.widget_click(self.page["timer_log_clear_popup"]["confirm"],
                              self.page["timer_log_page"]["no_log"])

        self.widget_click(self.page["timer_log_page"]["to_return"],
                          self.page["normal_timer_page"]["title"])

        self.widget_click(self.page["normal_timer_page"]["add_timer"],
                          self.page["add_normal_timer_page"]["title"])
    
        self.now = time.strftime("%H:%M")
    
        delay_time_1 = 1
        start_time_1, set_time_1 = self.set_timer_roll(self.page["add_normal_timer_page"]["roll_h"],
                                                       self.page["add_normal_timer_page"]["roll_m"],
                                                       self.page["add_normal_timer_page"]["set_timer"],
                                                       delay_time_1, self.now)

        if power_state == "power_on":
            self.widget_click(self.page["add_normal_timer_page"]["power_off"],
                              self.page["add_normal_timer_page"]["title"])
        elif power_state == "power_off":
            self.widget_click(self.page["add_normal_timer_page"]["power_on"],
                              self.page["add_normal_timer_page"]["title"])
    
        self.widget_click(self.page["add_normal_timer_page"]["saved"],
                          self.page["normal_timer_page"]["title"])
        self.logger.info(u"[APP_TIMER]Start Time:%s[%s]" % (time.strftime("%H:%M:%S"), time.time()))

        self.widget_click(self.page["normal_timer_page"]["to_return"],
                          self.page["control_device_page"]["title"])

        if power_state == "power_on":
            power_state = u"设备已关闭"
        elif power_state == "power_off":
            power_state = u"设备已开启"
    
        self.check_timer(start_time_1, set_time_1, power_state)
        
        self.widget_click(self.page["control_device_page"]["normal_timer"],
                          self.page["normal_timer_page"]["title"])
    
        time.sleep(3)
        self.widget_click(self.page["normal_timer_page"]["timer_log"],
                          self.page["timer_log_page"]["title"])

        month, day = time.strftime("%m-%d").split("-")
        set_time_date = u"%s%s月%s日" % (set_time_1, month, day)
        element = self.wait_widget(self.page["timer_log_page"]["has_log"])
        if self.ac.get_attribute(element, "name") == set_time_date:
            self.logger.info(u"[APP_INFO]存在定时记录%s" % set_time_date)
        else:
            raise TimeoutException()

        self.widget_click(self.page["timer_log_page"]["clear"],
                          self.page["timer_log_clear_popup"]["title"])

        self.widget_click(self.page["timer_log_clear_popup"]["confirm"],
                          self.page["timer_log_page"]["no_log"])

        self.case_over(True)
