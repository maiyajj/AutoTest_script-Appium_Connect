# coding=utf-8
from src.testcase.GN_Y201J.WidgetOperation import *


class GNY201JElectricityMeter10(WidgetOperation):
    @case_run(False)
    def run(self):
        self.case_module = u"APP功能测试"  # 用例所属模块
        self.case_title = u'实时功率检查_1500W'  # 用例名称
        self.zentao_id = "1135"  # 禅道ID

    # 用例动作
    def case(self):
        self.choose_home_device(conf["MAC"]["JD"][0])

        self.set_power("power_on")

        power = []

        i = 10
        end_time = time.time() + 60
        while i > 0:
            try:
                tmp = self.ac.get_attribute(self.wait_widget(self.page["control_device_page"]["power"]), "name")
                if isinstance(tmp, unicode):
                    power.append(tmp)
                    if len(power) >= 60:
                        break
            except TimeoutException:
                pass

            if time.time() > end_time:
                end_time = time.time() + 60
                i -= 1

        power = list(map(lambda x: float(x.replace(" W", "")), power))

        power_error = sum(power) / len(power) / 1500
        self.debug.info("[ELEC_INFO]power_error is %s" % power_error)

        if power_error > 0.01:
            raise TimeoutException("the battery error is over 0.01, current is %s" % power_error)
