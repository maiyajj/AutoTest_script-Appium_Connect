# coding=utf-8
from src.testcase.case.LaunchApp import *


class GNAppDevicePage5(LaunchApp):
    def run(self):
        self.case_module = u"设备页"  # 用例所属模块
        self.case_title = u'配网失败页面信息检查'  # 用例名称
        self.zentao_id = 1807  # 禅道ID
        self.basename = os.path.basename(__file__).split(".")[0]  # 获取用例的文件名称:GNAPP_DEVICE_PAGE_005
        self.driver = self.return_driver()
        self.logger.info('[GN_INF] <current case> [CASE_ID="%s", CASE_NAME="%s", 禅道ID="%s", CASE_MODULE="%s"]'
                         % (self.basename, self.case_title, self.zentao_id, self.case_module))  # 记录log

        try:
            self.launch_app(False)  # 启动APP
            self.case()
        except WebDriverException:
            self.debug.error(traceback.format_exc())  # Message: ***

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

            self.wait_widget(self.page["add_device_failed_page"]["failed_rescan"], 60, 1)

            self.wait_widget(self.page["add_device_failed_page"]["cancel"], 60, 1)

            self.case_over(True)
        except TimeoutException:
            self.case_over(False)

    def output(self):
        self.run()
        return self.result()
