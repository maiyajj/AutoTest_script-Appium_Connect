# coding=utf-8
from src.testcase.case.LaunchApp import *


class GNAppDevicePage6(LaunchApp):
    def run(self):
        self.case_module = u"设备页"  # 用例所属模块
        self.case_title = u'配网失败页面，取消按钮功能检查'  # 用例名称
        self.zentao_id = 1808  # 禅道ID
        self.basename = os.path.basename(__file__).split(".")[0]  # 获取用例的文件名称:GNAPP_DEVICE_PAGE_006
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
            self.widget_click(device_page["title"],
                              device_page["add_device"],
                              device_add_scan_page["title"],
                              1, 1, 1, 10, 0.5)

            self.widget_click(device_add_scan_page["title"],
                              device_add_scan_page["gateway_hw"],
                              prepare_set_network_page["title"],
                              1, 1, 1, 10, 0.5)

            self.widget_click(prepare_set_network_page["title"],
                              prepare_set_network_page["prepare_next"],
                              set_network_page["title"],
                              1, 1, 1, 10, 0.5)

            wifi_pwd = self.wait_widget(set_network_page["wifi_pwd"], 3, 1)

            data = str(conf["wifi_pwd"]).decode('hex')
            wifi_pwd.send_keys(data)
            self.logger.info(u'[APP_INPUT] ["WiFi密码"] input success')
            time.sleep(0.5)

            self.widget_click(set_network_page["title"],
                              set_network_page["prepare_next"],
                              scan_with_subscribe_page["title"],
                              1, 1, 1, 10, 0.5)

            self.wait_widget(add_device_failed_page["title"], 60, 1)

            self.widget_click(add_device_failed_page["title"],
                              add_device_failed_page["cancel"],
                              scan_with_subscribe_page["title"],
                              1, 1, 1, 10, 0.5)

            self.case_over(True)
        except TimeoutException:
            self.case_over(False)

    def output(self):
        self.run()
        return self.result()
