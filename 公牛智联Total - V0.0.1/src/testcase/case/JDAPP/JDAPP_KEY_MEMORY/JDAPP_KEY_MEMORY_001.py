# coding=utf-8
from src.testcase.common.WidgetOperation_JD import *


class JDAppKeyMemory1(WidgetOperationJD):
    @case_run(False)
    def run(self):
        self.case_module = u"APP功能测试"  # 用例所属模块
        self.case_title = u'开关操作及记忆功能'  # 用例名称
        self.zentao_id = 1216  # 禅道ID

    # 用例动作
    def case(self):
        self.choose_home_device(conf["MAC"]["JD"][0])

        self.set_power("power_off")

        tmp = 10
        while tmp > 0:
            self.widget_click(self.page["control_device_page"]["power_button"],
                              self.page["control_device_page"]["power_on"])
            self.logger.info(u"[APP_INFO]Device info: power on")

            self.widget_click(self.page["control_device_page"]["power_button"],
                              self.page["control_device_page"]["power_off"])
            self.logger.info(u"[APP_INFO]Device info: power off")
            tmp -= 1

