# coding=utf-8
from src.testcase.common.WidgetOperation_JD import *


class JDAppOverDay5(WidgetOperationJD):
    @case_run(False)
    def run(self):
        self.case_module = u"模式定时"  # 用例所属模块
        self.case_title = u'每日循环普通定时'  # 用例名称
        self.zentao_id = 1304  # 禅道ID
    
    # 用例动作
    def case(self):
        self.choose_home_device(conf["MAC"]["JD"][0])
    
        self.close_mode_timer()

        self.set_power("power_off")

        self.widget_click(self.page["control_device_page"]["normal_timer"],
                          self.page["normal_timer_page"]["title"])
        self.delete_normal_timer()

        now = time.strftime("%H:%M")
        
        delay_time_1 = 2
        delay_time_2 = 4
        start_time_1, set_time_1, cycle1 = self.create_normal_timer(now, delay_time_1, "power_on", u"每天")
        start_time_2, set_time_2, cycle2 = self.create_normal_timer(now, delay_time_2, "power_off", u"每天")
        
        self.widget_click(self.page["normal_timer_page"]["to_return"],
                          self.page["control_device_page"]["title"])
        
        self.wait_widget(self.page["control_device_page"]["power_off"])

        self.check_timer(start_time_1, set_time_1, u"设备已开启", cycle1)
        self.check_timer(start_time_2, set_time_2, u"设备已关闭", cycle2)
