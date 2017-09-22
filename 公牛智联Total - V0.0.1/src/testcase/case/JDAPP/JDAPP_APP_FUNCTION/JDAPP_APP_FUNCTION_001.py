# coding=utf-8
from src.testcase.case.LaunchApp_JD import *


class JDAppAppFunction1(LaunchAppJD):
    @case_run_jd(False)
    def run(self):
        self.case_module = u"APP功能测试"  # 用例所属模块
        self.case_title = u'定时记录删除是否成功"'  # 用例名称
        self.zentao_id = 1170  # 禅道ID

    # 用例动作
    def case(self):
        try:
            while True:
                elements = self.wait_widget(self.page["app_home_page"]["device"])
                new_value = copy.copy(self.page["app_home_page"]["device"])
                for index, element in elements.items():
                    if self.ac.get_attribute(element, "name") == conf["MAC"][0]:
                        new_value[0] = new_value[0][index]

                        self.widget_click(new_value, self.page["control_device_page"]["title"])
                        raise ValueError()
                    else:
                        self.ac.swipe(0.6, 0.9, 0.6, 0.6, 0, self.driver)
                        time.sleep(1)
        except ValueError:
            pass

        self.widget_click(self.page["control_device_page"]["normal_timer"],
                          self.page["normal_timer_page"]["title"])

        self.widget_click(self.page["normal_timer_page"]["add_timer"],
                          self.page["add_normal_timer_page"]["title"])

        now_time = self.ac(self.wait_widget(self.page["add_normal_timer_page"]["set_timer"]), "name")
        print now_time
        self.case_over(True)
