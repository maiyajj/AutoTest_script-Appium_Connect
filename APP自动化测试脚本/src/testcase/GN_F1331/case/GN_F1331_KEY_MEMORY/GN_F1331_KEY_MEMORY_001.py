# coding=utf-8
from src.testcase.GN_F1331.WidgetOperation import *


class GNF1331KeyMemory1(WidgetOperation):
    @case_run(False)
    def run(self):
        self.case_module = u"APP功能测试"  # 用例所属模块
        self.case_title = u'开关操作及记忆功能'  # 用例名称
        self.zentao_id = 1216  # 禅道ID

    # 用例动作
    def case(self):
        self.choose_home_device(conf["MAC"][self.app][self.device_mac])

        self.set_power("main_button_on")

        tmp = 10
        while tmp > 0:
            self.widget_click(self.page["control_device_page"]["main_button"])
            self.wait_widget(self.page["control_device_page"]["main_button_on"])
            self.logger.info(u"[APP_INFO]Device info: main button on")

            self.widget_click(self.page["control_device_page"]["main_button"])
            self.wait_widget(self.page["control_device_page"]["main_button_off"])
            self.logger.info(u"[APP_INFO]Device info: main button off")
            tmp -= 1
