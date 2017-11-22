# coding=utf-8
from src.testcase.common.WidgetOperation_AL import *


class ALAppNormalTimer11(WidgetOperationAL):
    @case_run(False)
    def run(self):
        self.case_module = u"FUT_NTIMER_普通定时(#48)"  # 用例所属模块
        self.case_title = u'FUT_NTIMER_普通定时循环信息检查'  # 用例名称
        self.zentao_id = 417  # 禅道ID

    # 用例动作
    def case(self):
        device = conf["MAC"]["AL"][0]
        self.set_power(device, "power_off")

        self.choose_home_device(device)

        self.close_mode_timer()

        self.close_general_timer()

        self.widget_click(self.page["control_device_page"]["normal_timer"],
                          self.page["normal_timer_page"]["title"])

        self.delete_normal_timer()

        now = time.strftime("%H:%M")

        delay_time_1 = 10
        self.create_normal_timer(now, delay_time_1, "power_on", u"永不")

        delay_time_2 = 10
        self.create_normal_timer(now, delay_time_2, "power_off", [u"周一", u"周日"])

        delay_time_3 = 10
        self.create_normal_timer(now, delay_time_3, "power_on", u"工作日")

        delay_time_4 = 10
        self.create_normal_timer(now, delay_time_4, "power_off", u"每天")

        loop_list = [[u"永不"], [u"周一", u"周日"], [u"工作日"], [u"每天"]]
        for i in loop_list:
            tmp = u"、".join(i)
            new_value = copy.copy(self.page["normal_timer_page"]["timer_loop"])
            new_value[0] = new_value[0][loop_list.index(i)]
            attribute = self.ac.get_attribute(self.wait_widget(new_value), "name")
            if tmp not in attribute:
                raise TimeoutException("loop is wrong!")

        self.case_over(True)
