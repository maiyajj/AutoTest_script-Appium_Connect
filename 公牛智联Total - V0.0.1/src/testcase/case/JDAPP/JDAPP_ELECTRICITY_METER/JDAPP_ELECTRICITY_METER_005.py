# coding=utf-8
from src.testcase.case.LaunchApp_JD import *


class JDAppElectricityMeter5(LaunchAppJD):
    @case_run_jd(False)
    def run(self):
        self.case_module = u"电量计量"  # 用例所属模块
        self.case_title = u'用电图表显示周期设置'  # 用例名称
        self.zentao_id = 1149  # 禅道ID

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

        self.widget_click(self.page["control_device_page"]["elec"],
                          self.page["elec_page"]["title"])

        elec_elements = self.wait_widget(self.page["elec_page"]["elec_time"])[0]
        if re.findall("\d+:\d+", self.ac.get_attribute(elec_elements, "name")) == []:
            raise TimeoutException()

        self.widget_click(self.page["elec_page"]["week"],
                          self.page["elec_page"]["title"])

        elec_elements = self.wait_widget(self.page["elec_page"]["elec_time"])[0]
        if re.findall(u"\d+月\d+日", self.ac.get_attribute(elec_elements, "name")) == []:
            raise TimeoutException()

        self.widget_click(self.page["elec_page"]["month"],
                          self.page["elec_page"]["title"])

        elec_elements = self.wait_widget(self.page["elec_page"]["elec_time"])[0]
        if re.findall("\d+-\d+-\d+", self.ac.get_attribute(elec_elements, "name")) == []:
            raise TimeoutException()

        self.widget_click(self.page["elec_page"]["year"],
                          self.page["elec_page"]["title"])

        elec_elements = self.wait_widget(self.page["elec_page"]["elec_time"])[0]
        if re.findall(u".+月", self.ac.get_attribute(elec_elements, "name")) == []:
            raise TimeoutException()
        if re.findall(u"月.+", self.ac.get_attribute(elec_elements, "name")) != []:
            raise TimeoutException()

        self.case_over(True)
