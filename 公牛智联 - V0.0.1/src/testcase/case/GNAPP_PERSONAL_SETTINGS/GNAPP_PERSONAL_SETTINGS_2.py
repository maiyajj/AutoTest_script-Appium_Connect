# coding:utf-8
from src.testcase.common.WidgetCheckUnit import *
from src.testcase.case.ToLoginPage import *


class GNAppPersonalSettings1(object):
    def __init__(self):
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        logger.info('app start [time=%s]' % time.strftime("%Y-%m-%d %H:%M:%S"))
        widget_check_unit = WidgetCheckUnit(self.driver)
        self.widget_click = widget_check_unit.widget_click
        self.case_title = u'账户设置-修改密码页面，"返回"按钮功能检查'
        logger.info('[GN_INF] <current case> [CASE_ID="%s", CASE_TITLE="%s"]'
                    % (os.path.basename(__file__).split(".")[0], self.case_title))
        ToDevicePage(1)
        self.case()

    # 用例动作
    def case(self):
        self.widget_click(device_page["title"],
                          device_page["user_image"],
                          personal_settings_page["title"],
                          1, 1, 1, 3, 0.5, 0)

        self.widget_click(personal_settings_page["title"],
                          personal_settings_page["account_setting"],
                          account_setting_page["title"],
                          1, 1, 1, 3, 0.5, 0)

        self.widget_click(account_setting_page["title"],
                          account_setting_page["change_pwd"],
                          change_pwd_page["title"],
                          1, 1, 1, 3, 0.5, 0)

        old_pwd = self.widget_click(change_pwd_page["title"],
                                    change_pwd_page["old_pwd"],
                                    change_pwd_page["title"],
                                    1, 1, 1, 3, 0.5, 0)
        data = App["old_pwd"].decode['hex']
        old_pwd.send_keys(data)
        logger.info(u'[APP_INPUT] ["旧密码"] input success')
        time.sleep(0.5)

        new_pwd = self.widget_click(change_pwd_page["title"],
                                    change_pwd_page["new_pwd"],
                                    change_pwd_page["title"],
                                    1, 1, 1, 3, 0.5, 0)
        data = App["new_pwd"].decode['hex']
        new_pwd.send_keys(data)
        logger.info(u'[APP_INPUT] ["新密码"] input success')
        time.sleep(0.5)

        conform_pwd = self.widget_click(change_pwd_page["title"],
                                        change_pwd_page["conform_pwd"],
                                        change_pwd_page["title"],
                                        1, 1, 1, 3, 0.5, 0)
        data = App["new_pwd"].decode['hex']
        conform_pwd.send_keys(data)
        logger.info(u'[APP_INPUT] ["确认新密码"] input success')
        time.sleep(0.5)

        self.widget_click(change_pwd_page["title"],
                          change_pwd_page["to_return"],
                          account_setting_page["title"],
                          1, 1, 1, 3, 0.5, 0)

        self.case_over()

    def case_over(self):
        logger.info('[GN_INF] <current case> [CASE_TITLE="%s"] success!' % self.case_title)
        time.sleep(1)
        self.driver.close_app()
        logger.info('app closed [time=%s]' % time.strftime("%Y-%m-%d %H:%M:%S"))
        self.driver.quit()
