# coding=utf-8
from src.testcase.GN_F1331.WidgetOperation import *


class GNF1331Unbind2(WidgetOperation):
    @case_run(False)
    def run(self):
        self.case_module = u"解绑功能(#13)"  # 用例所属模块
        self.case_title = u'APP端解绑功能检查'  # 用例名称
        self.zentao_id = "166"  # 禅道ID

    # 用例动作
    def case(self):
        self.choose_home_device(conf["MAC"][self.app][self.device_mac])

        self.widget_click(self.page["control_device_page"]["device_setting"],
                          self.page["device_setting_page"]["title"])

        self.widget_click(self.page["device_setting_page"]["unbind"])
        try:
            self.wait_widget(self.page["unbind_device_popup"]["title1"])
        except TimeoutException:
            self.wait_widget(self.page["unbind_device_popup"]["title2"])


        self.widget_click(self.page["unbind_device_popup"]["confirm"],
                          self.page["app_home_page"]["title"])

        v = self.get_index(conf["MAC"][self.app][self.device_mac], self.page["app_home_page"]["device"])
        if v:
            raise TimeoutException()
