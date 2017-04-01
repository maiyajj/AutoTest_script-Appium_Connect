# coding:utf-8
from src.testcase.common.WidgetCheckUnit import *
from src.testcase.case.ToDevicePage import *


class GNAppPersonalSettings2(object):
    def __init__(self):
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        logger.info('app start [time=%s]' % time.strftime("%Y-%m-%d %H:%M:%S"))
        widget_check_unit = WidgetCheckUnit(self.driver)
        self.widget_click = widget_check_unit.widget_click
        self.wait_widget = widget_check_unit.wait_widget
        self.case_title = u'账户设置-密码修改后页面跳转确认'
        logger.info('[GN_INF] <current case> [CASE_ID="%s", CASE_TITLE="%s"]'
                    % (os.path.basename(__file__).split(".")[0], self.case_title))
        ToDevicePage()
        self.result = True
        self.case()

    # 用例动作
    def case(self):
        self.result = self.widget_click(device_page["title"],
                                        device_page["user_image"],
                                        personal_settings_page["title"],
                                        1, 1, 1, 10, 0.5)
        if self.result is False:
            self.case_over(0)
            return False

        self.result = self.widget_click(personal_settings_page["title"],
                                        personal_settings_page["account_setting"],
                                        account_setting_page["title"],
                                        1, 1, 1, 10, 0.5)
        if self.result is False:
            self.case_over(0)
            return False

        self.result = self.widget_click(account_setting_page["title"],
                                        account_setting_page["logout"],
                                        logout_popup["title"],
                                        1, 1, 1, 10, 0.5)
        if self.result is False:
            self.case_over(0)
            return False

        self.result = self.widget_click(logout_popup["title"],
                                        logout_popup["confirm"],
                                        login_page["title"],
                                        1, 1, 1, 10, 0.5)
        if self.result is False:
            self.case_over(0)
            return False

        self.result = self.widget_click(account_setting_page["title"],
                                        account_setting_page["logout"],
                                        logout_popup["title"],
                                        1, 1, 1, 10, 0.5)
        if self.result is False:
            self.case_over(0)
            return False

        x = self.driver.get_window_size()['width']
        y = self.driver.get_window_size()['height']
        x = int(x * 0.1)
        y = int(y * 0.1)
        self.driver.tap([(x, y)])
        self.result = self.widget_click(account_setting_page["title"],
                                        account_setting_page["title"],
                                        account_setting_page["title"],
                                        1, 1, 1, 10, 0.5)
        if self.result is False:
            self.case_over(0)
            return False

        username = self.wait_widget(login_page["username"][1],
                                    login_page["username"][0], 10, 1).get_attribute("name")
        if username != conf_user_name.decode("hex"):
            self.result = False
        if self.result is False:
            self.case_over(0)
            return False

        password = self.wait_widget(login_page["password"][1],
                                    login_page["password"][0], 10, 1).get_attribute("name")
        if password != conf_login_pwd.decode("hex"):
            self.result = False
        if self.result is False:
            self.case_over(0)
            return False

        self.case_over()

    def case_over(self, success=1):
        if success == 1:
            logger.info('[GN_INF] <current case> [CASE_TITLE="%s"] success!' % self.case_title)
        elif success == 0:
            logger.info('[GN_INF] <current case> [CASE_TITLE="%s"] failed!' % self.case_title)
        time.sleep(1)
        self.driver.close_app()
        logger.info('app closed [time=%s]' % time.strftime("%Y-%m-%d %H:%M:%S"))
        self.driver.quit()
