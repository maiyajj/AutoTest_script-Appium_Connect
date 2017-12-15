# coding=utf-8
from src.testcase.GN_Y201S.WidgetOperation import *


class GNY201SEem4(WidgetOperation):
    @case_run(False)
    def run(self):
        self.case_module = u"FUT_EEM_电量计量(#61)"  # 用例所属模块
        self.case_title = u'FUT_EEM_实时功率显示及精度检查'  # 用例名称
        self.zentao_id = 550  # 禅道ID

    # 用例动作
    def case(self):
        device = conf["MAC"]["AL"][0]
        self.set_power(device, "power_off")

        self.choose_home_device(device)

        self.close_mode_timer()

        self.close_general_timer()

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

        power = map(lambda x: float(x.replace("W", "")), power)

        power_error = sum(power) / len(power) / 50
        self.logger.info("[ELEC_INFO]power_error is %s" % power_error)

        if power_error > 0.01:
            raise TimeoutException("the battery error is over 0.01, current is %s" % power_error)
