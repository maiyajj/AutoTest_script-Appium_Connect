# coding:utf-8
from appium import webdriver
from src.testcase.case.ToDevicePage import *
from src.testcase.common.WidgetCheckUnit import *


class GNAppAccountSettings8(object):
    def __init__(self):
        self.case_module = u"账户设置"
        self.case_title = u'昵称修改成功，页面信息检查'
        self.ZenTao_id = 1949
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
        self.case()

    # 用例动作
    def case(self):
        try:
            self.widget_click(device_page["title"],
                              device_page["user_image"],
                              personal_settings_page["title"],
                              1, 1, 1, 10, 0.5)

            self.widget_click(personal_settings_page["title"],
                              personal_settings_page["account_setting"],
                              account_setting_page["title"],
                              1, 1, 1, 10, 0.5)

            self.widget_click(account_setting_page["title"],
                              account_setting_page["nickname"],
                              change_nickname_page["title"],
                              1, 1, 1, 10, 0.5)

            nickname = self.widget_click(change_nickname_page["title"],
                                         change_nickname_page["nickname"],
                                         change_nickname_page["title"],
                                         1, 1, 1, 10, 0.5)

            # 全选
            self.driver.press_keycode(29, 28672)
            # KEYCODE_FORWARD_DEL 删除键 112
            self.driver.press_keycode(112)
            nickname.send_keys(u"被修改的昵称")
            logger.info(u'[APP_INPUT] ["昵称"] input success')
            time.sleep(0.5)

            self.widget_click(change_nickname_page["title"],
                              change_nickname_page["commit"],
                              account_setting_page["title"],
                              1, 1, 1, 10, 0.5)

            self.widget_click(account_setting_page["title"],
                              account_setting_page["to_return"],
                              personal_settings_page["title"],
                              1, 1, 1, 10, 0.5)

            modified_nickname = self.wait_widget(personal_settings_page["nickname"], 3, 1)
            if modified_nickname != u"被修改的昵称":
                raise TimeoutException()

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
