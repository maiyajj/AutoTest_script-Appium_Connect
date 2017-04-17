# coding=utf-8
from appium import webdriver
from src.testcase.case.ToDevicePage import *
from src.testcase.common.WidgetCheckUnit import *


class GNAppDevicePage5(object):
    def __init__(self):
        self.case_module = u"设备页"
        self.case_title = u'配网失败页面信息检查'
        self.ZenTao_id = 1807
        self.basename = os.path.basename(__file__).split(".")[0]
        logger.info('[GN_INF] <current case> [CASE_ID="%s", CASE_NAME="%s", 禅道ID="%s", CASE_MODULE="%s"]'
                    % (self.basename, self.case_title, self.ZenTao_id, self.case_module))
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        logger.info('app start [time=%s]' % time.strftime("%Y-%m-%d %H:%M:%S"))
        widget_check_unit = WidgetCheckUnit(self.driver)
        self.widget_click = widget_check_unit.widget_click
        self.wait_widget = widget_check_unit.wait_widget
        self.success = 0
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

            self.wait_widget(add_device_failed_page["title"], 60, 1)

            self.wait_widget(add_device_failed_page["failed_rescan"], 60, 1)

            self.wait_widget(add_device_failed_page["cancel"], 60, 1)

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
