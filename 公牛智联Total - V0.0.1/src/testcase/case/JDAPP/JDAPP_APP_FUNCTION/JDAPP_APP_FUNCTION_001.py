# coding=utf-8
from src.testcase.common.WidgetOperation_JD import *


class JDAppAppFunction1(WidgetOperationJD):
    @case_run_jd(False)
    def run(self):
        self.case_module = u"APP功能测试"  # 用例所属模块
        self.case_title = u'定时记录删除是否成功'  # 用例名称
        self.zentao_id = 1170  # 禅道ID

    # 用例动作
    def case(self):
        self.choose_home_device(conf["MAC"]["JD"][0])

        self.set_power("power_off")

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

        now = time.strftime("%H:%M")
    
        delay_time_1 = 1
        start_time_1, set_time_1 = self.set_timer_roll(self.page["add_normal_timer_page"]["roll_h"],
                                                       self.page["add_normal_timer_page"]["roll_m"],
                                                       self.page["add_normal_timer_page"]["set_timer"],
                                                       delay_time_1, now)

        self.widget_click(self.page["add_normal_timer_page"]["power_on"],
                          self.page["add_normal_timer_page"]["title"])
    
        self.widget_click(self.page["add_normal_timer_page"]["saved"],
                          self.page["normal_timer_page"]["title"])
        self.logger.info(u"[APP_TIMER]Start Time:%s[%s]" % (time.strftime("%H:%M:%S"), time.time()))

        self.widget_click(self.page["normal_timer_page"]["to_return"],
                          self.page["control_device_page"]["title"])

        self.check_timer(start_time_1, set_time_1, u"设备已开启")
        
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
            raise TimeoutException("don`t have timing records :%s" % set_time_date)

        self.widget_click(self.page["timer_log_page"]["clear"],
                          self.page["timer_log_clear_popup"]["title"])

        self.widget_click(self.page["timer_log_clear_popup"]["confirm"],
                          self.page["timer_log_page"]["no_log"])

        self.case_over(True)
