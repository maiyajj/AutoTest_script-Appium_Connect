# coding=utf-8
from src.testcase.case.LaunchApp_JD import *


class JDAppElectricityMeter3(LaunchAppJD):
    @case_run_jd(False)
    def run(self):
        self.case_module = u"APP功能测试"  # 用例所属模块
        self.case_title = u'启动鱼缸模式定时，APP中开关状态检查'  # 用例名称
        self.zentao_id = 1307  # 禅道ID

    # 用例动作
    def case(self):
        try:
            while True:
                element = self.wait_widget(self.page["app_home_page"]["device"])
                for i in element:
                    if self.ac.get_attribute(i, "name") == conf["MAC"][0]:
                        self.widget_click(self.page["app_home_page"]["device"],
                                          self.page["control_device_page"]["title"],
                                          operate_driver=i.parent)
                        raise ValueError()
                    else:
                        self.ac.swipe(0.6, 0.9, 0.6, 0.4, 0, self.driver)
                        time.sleep(1)
        except ValueError:
            pass

        try:
            self.wait_widget(self.page["control_device_page"]["power_on"])
            self.widget_click(self.page["control_device_page"]["power_button"],
                              self.page["control_device_page"]["power_off"])
        except TimeoutException:
            pass

        self.widget_click(self.page["control_device_page"]["mode_timer"],
                          self.page["control_device_page"]["power_off"])

        self.case_over(True)
