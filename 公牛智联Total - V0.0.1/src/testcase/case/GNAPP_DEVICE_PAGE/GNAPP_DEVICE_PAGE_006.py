# coding=utf-8
from src.testcase.case.LaunchApp import *


class GNAppDevicePage6(LaunchApp):
    @case_run
    def run(self):
        self.case_module = u"设备页"  # 用例所属模块
        self.case_title = u'配网失败页面，取消按钮功能检查'  # 用例名称
        self.zentao_id = 1808  # 禅道ID


    # 用例动作
    def case(self):
        try:
            self.widget_click(self.page["device_page"]["title"],
                              self.page["device_page"]["add_device"],
                              self.page["device_add_scan_page"]["title"],
                              1, 1, 1, 10, 0.5)

            self.widget_click(self.page["device_add_scan_page"]["title"],
                              self.page["device_add_scan_page"]["gateway_hw"],
                              self.page["set_network_page"]["title"],
                              1, 1, 1, 10, 0.5)

            self.widget_click(self.page["set_network_page"]["title"],
                              self.page["set_network_page"]["prepare_next"],
                              self.page["set_network_page"]["title"],
                              1, 1, 1, 10, 0.5)

            wifi_pwd = self.wait_widget(self.page["set_network_page"]["wifi_pwd"], 3, 1)

            data = str(conf["wifi_pwd"]).decode('hex').replace(" ", "")
            wifi_pwd.clear()
            self.ac.send_keys(wifi_pwd, data)
            self.logger.info(u'[APP_INPUT] ["WiFi密码"] input success')
            time.sleep(0.5)

            self.widget_click(self.page["set_network_page"]["title"],
                              self.page["set_network_page"]["prepare_next"],
                              self.page["scan_with_subscribe_page"]["title"],
                              1, 1, 1, 10, 0.5)

            self.wait_widget(self.page["add_device_failed_page"]["title"], 60, 1)

            self.widget_click(self.page["add_device_failed_page"]["title"],
                              self.page["add_device_failed_page"]["cancel"],
                              self.page["scan_with_subscribe_page"]["title"],
                              1, 1, 1, 10, 0.5)

            self.case_over(True)
        except TimeoutException:
            self.case_over(False)

