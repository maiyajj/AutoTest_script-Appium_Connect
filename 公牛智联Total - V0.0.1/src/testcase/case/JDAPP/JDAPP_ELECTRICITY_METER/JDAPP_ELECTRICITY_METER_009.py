# coding=utf-8
from src.testcase.case.LaunchApp_JD import *


class JDAppElectricityMeter9(LaunchAppJD):
    @case_run_jd(False)
    def run(self):
        self.case_module = u"APP功能测试"  # 用例所属模块
        self.case_title = u'实时功率检查_2000W'  # 用例名称
        self.zentao_id = 1136  # 禅道ID

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
        except TimeoutException:
            self.widget_click(self.page["control_device_page"]["power_button"],
                              self.page["control_device_page"]["power_on"])

        power = []

        i = 10
        end_time = time.time() + 60
        while i > 0:
            if time.time() < end_time:
                try:
                    tmp = self.ac.get_attribute(self.wait_widget(self.page["control_device_page"]["power"]), "name")
                    if isinstance(tmp, unicode):
                        power.append(tmp)
                        if len(power) >= 60:
                            break
                except TimeoutException:
                    pass
            else:
                end_time = time.time() + 60
                i -= 1

        power = map(lambda x: float(x.replace(" W", "")), power)

        aver_power = sum(power) / len(power)

        if aver_power / 2000 > 0.01:
            raise TimeoutException()

        self.case_over(True)
