# coding=utf-8
from src.testcase.common.WidgetOperation_JD import *


class JDAppModeTimer6(WidgetOperationJD):
    @case_run_jd(False)
    def run(self):
        self.case_module = u"模式定时"  # 用例所属模块
        self.case_title = u'鱼缸模式开启1分钟，关闭1分钟定时是否正确执行'  # 用例名称
        self.zentao_id = 1103  # 禅道ID
    
    # 用例动作
    def case(self):
        self.choose_home_device(conf["MAC"][0])
    
        self.close_mode_timer()

        self.set_power("power_off")

        self.widget_click(self.page["control_device_page"]["mode_timer"],
                          self.page["mode_timer_page"]["title"])
        
        self.widget_click(self.page["mode_timer_page"]["fish_mode"],
                          self.page["fish_mode_timer_page"]["title"])
    
        self.now = time.strftime("%H:%M")

        delay_time_1 = ["delay", "00:01"]
        self.widget_click(self.page["fish_mode_timer_page"]["start_time"],
                          self.page["fish_mode_timer_page"]["roll_h"])
    
        start_time_1, set_time_1 = self.set_timer_roll(self.page["fish_mode_timer_page"]["roll_h"],
                                                       self.page["fish_mode_timer_page"]["roll_m"],
                                                       self.page["fish_mode_timer_page"]["start_time_text"],
                                                       delay_time_1, self.now)
        
        self.widget_click(self.page["fish_mode_timer_page"]["start_time"],
                          self.page["fish_mode_timer_page"]["title"])

        delay_time_2 = ["delay", "00:01"]
        self.widget_click(self.page["fish_mode_timer_page"]["end_time"],
                          self.page["fish_mode_timer_page"]["end_h"])
    
        start_time_2, set_time_2 = self.set_timer_roll(self.page["fish_mode_timer_page"]["end_h"],
                                                       self.page["fish_mode_timer_page"]["end_m"],
                                                       self.page["fish_mode_timer_page"]["end_time_text"],
                                                       delay_time_2, set_time_1)
        
        self.widget_click(self.page["fish_mode_timer_page"]["end_time"],
                          self.page["fish_mode_timer_page"]["title"])

        self.set_timer_loop("fish_mode_timer_page", u"永久循环")

        self.launch_mode_timer("fish_mode_timer_page", False, start_time_1)

        self.widget_click(self.page["mode_timer_page"]["to_return"],
                          self.page["control_device_page"]["title"])
        
        self.wait_widget(self.page["control_device_page"]["power_on"])
    
        self.check_timer(start_time_1, set_time_1, u"设备已关闭")
    
        self.check_timer(start_time_2, set_time_2, u"设备已开启")
        
        self.case_over(True)
    
