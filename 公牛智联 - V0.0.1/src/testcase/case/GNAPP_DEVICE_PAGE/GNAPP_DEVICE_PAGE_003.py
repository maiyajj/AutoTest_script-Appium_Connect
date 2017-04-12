# coding:utf-8
from src.testcase.case.ToDevicePage import *
from src.testcase.common.WidgetCheckUnit import *


class GNAppDevicePage3(object):
    def __init__(self):
        self.case_title = u'设备配网过程中，弹出终止配网提示框，取消按钮功能检查'
        logger.info('[GN_INF] <current case> [CASE_ID="%s", CASE_TITLE="%s"]'
                    % (os.path.basename(__file__).split(".")[0], self.case_title))
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        logger.info('app start [time=%s]' % time.strftime("%Y-%m-%d %H:%M:%S"))
        widget_check_unit = WidgetCheckUnit(self.driver)
        self.widget_click = widget_check_unit.widget_click
        self.wait_widget = widget_check_unit.wait_widget
        ToDevicePage()
        self.success = 0
        self.case()

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

            data = conf_wifi_pwd.decode('hex')
            wifi_pwd.send_keys(data)
            logger.info(u'[APP_INPUT] ["WiFi密码"] input success')
            time.sleep(0.5)

            self.widget_click(set_network_page_page["title"],
                              set_network_page_page["prepare_next"],
                              scan_with_subscribe_page["title"],
                              1, 1, 1, 10, 0.5)

            self.widget_click(scan_with_subscribe_page["title"],
                              scan_with_subscribe_page["to_return"],
                              terminate_add_device_popup["title"],
                              1, 1, 1, 10, 0.5)

            self.widget_click(terminate_add_device_popup["title"],
                              terminate_add_device_popup["cancel"],
                              scan_with_subscribe_page["title"],
                              1, 1, 1, 10, 0.5)
            self.case_over(1)
        except TimeoutException:
            self.case_over(0)

    def case_over(self, success):
        self.success = success
        time.sleep(1)
        self.driver.close_app()
        self.driver.quit()
        logger.info('app closed [time=%s]' % time.strftime("%Y-%m-%d %H:%M:%S"))

    def result(self):
        if self.success == 1:
            logger.info('[GN_INF] <current case> [CASE_TITLE="%s"] success!' % self.case_title)
            return "success", self.case_title
        elif self.success == 0:
            logger.info('[GN_INF] <current case> [CASE_TITLE="%s"] failed!' % self.case_title)
            return "failed", self.case_title
