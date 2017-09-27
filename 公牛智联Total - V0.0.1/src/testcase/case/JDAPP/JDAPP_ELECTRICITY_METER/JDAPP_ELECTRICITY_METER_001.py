# coding=utf-8
from src.testcase.case.LaunchApp_JD import *


class JDAppElectricityMeter1(LaunchAppJD):
    @case_run_jd(False)
    def run(self):
        self.case_module = u"电量计量"  # 用例所属模块
        self.case_title = u'电量统计2H功能及精度检查'  # 用例名称
        self.zentao_id = 1117  # 禅道ID

    # 用例动作
    def case(self):
        elements = self.wait_widget(self.page["app_home_page"]["device"])
        new_value = copy.copy(self.page["app_home_page"]["device"])  # 直接用等于仍会修改列表的值
        for index, element in elements.items():
            if element is not None and self.ac.get_attribute(element, "name") in conf["Elec_stat_mac"]:
                new_value[0] = new_value[0][index]

                self.widget_click(new_value, self.page["control_device_page"]["title"])

                self.widget_click(self.page["control_device_page"]["to_return"],
                                  self.page["app_home_page"]["title"])

            else:
                self.ac.swipe(0.6, 0.9, 0.6, 0.4, 0, self.driver)

        self.case_over(True)
