# coding=utf-8
from src.testcase.GN_F1331.WidgetOperation import *


class GNF1331AppInfomation1(WidgetOperation):
    @case_run("")
    def run(self):
        self.case_module = u"APP检查(#2)"  # 用例所属模块
        self.case_title = u'设备详细界面，信息检测'  # 用例名称
        self.zentao_id = "007"  # 禅道ID

    # 用例动作
    def case(self):
        self.choose_home_device(conf["MAC"][self.app][self.device_mac])

        self.widget_click(self.page["control_device_page"]["device_setting"],
                          self.page["device_setting_page"]["title"])

        self.widget_click(self.page["device_setting_page"]["device_info"],
                          self.page["device_info_page"]["title"])

        attr = self.wait_widget(self.page["device_info_page"]["name"])
        name = self.ac.get_attribute(attr, "name")
        if not name == u"公牛智立方USB插座（WiFi版）":
            raise TimeoutException("device state error, current: %s" % name)

        attr = self.wait_widget(self.page["device_info_page"]["mac"])
        name = self.ac.get_attribute(attr, "name")
        if not name == conf["MAC"][self.app][self.device_mac].replace(":", "-"):
            raise TimeoutException("device state error, current: %s" % name)
