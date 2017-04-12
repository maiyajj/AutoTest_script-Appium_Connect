# coding:utf-8
from src.testcase.case.ToDevicePage import *
from src.testcase.common.WidgetCheckUnit import *


class GNAppPersonalSettings4(object):
    def __init__(self):
        self.case_title = u'使用帮助-返回按钮功能确认'
        logger.info('[GN_INF] <current case> [CASE_ID="%s", CASE_TITLE="%s"]'
                    % (os.path.basename(__file__).split(".")[0], self.case_title))
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        logger.info('app start [time=%s]' % time.strftime("%Y-%m-%d %H:%M:%S"))
        widget_check_unit = WidgetCheckUnit(self.driver)
        self.widget_click = widget_check_unit.widget_click
        self.wait_widget = widget_check_unit.wait_widget
        ToDevicePage()
        self.case()

    # 用例动作
    def case(self):
        try:
            self.widget_click(device_page["title"],
                              device_page["user_image"],
                              personal_settings_page["title"],
                              1, 1, 1, 10, 0.5)

            self.widget_click(personal_settings_page["title"],
                              personal_settings_page["using_help"],
                              app_help_page["title"],
                              1, 1, 1, 10, 0.5)

            self.widget_click(app_help_page["title"],
                              app_help_page["to_return"],
                              personal_settings_page["title"],
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
