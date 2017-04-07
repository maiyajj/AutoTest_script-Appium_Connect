# coding:utf-8
from src.testcase.case.ToLoginPage import *
from src.testcase.common.WidgetCheckUnit import *


class GNAppLogin3(object):
    def __init__(self):
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        logger.info('app start [time=%s]' % time.strftime("%Y-%m-%d %H:%M:%S"))
        widget_check_unit = WidgetCheckUnit(self.driver)
        self.widget_click = widget_check_unit.widget_click
        self.case_title = u"登录页面—登录功能检查"
        logger.info('[GN_INF] <current case> [CASE_ID="%s", CASE_TITLE="%s"]'
                    % (os.path.basename(__file__).split(".")[0], self.case_title))
        ToLoginPage()
        self.case()

    # 用例动作
    def case(self):
        try:
            widget = self.widget_click(login_page["title"],
                                       login_page["username"],
                                       login_page["title"],
                                       10, 10, 1, 60, 0.5)

            # 29 is the keycode of 'a', 28672 is the keycode of META_CTRL_MASK
            self.driver.press_keycode(29, 28672)
            # KEYCODE_FORWARD_DEL 删除键 112
            self.driver.press_keycode(112)
            # 发送数据
            data = conf_user_name.decode('hex')
            widget.send_keys(data)
            logger.info(u'[APP_INPUT] ["用户名"] input success')
            time.sleep(0.5)

            widget = self.widget_click(login_page["title"],
                                       login_page["password"],
                                       login_page["title"],
                                       10, 10, 1, 60, 0.5)

            self.driver.press_keycode(29, 28672)
            self.driver.press_keycode(112)
            data = conf_login_pwd.decode('hex')
            widget.send_keys(data)
            logger.info(u'[APP_INPUT] ["密码"] input success')
            time.sleep(0.5)

            self.widget_click(login_page["title"],
                              login_page["login_button"],
                              device_page["title"],
                              10, 10, 1, 60, 0.5)

            self.case_over(1)
        except TimeoutException:
            self.case_over(0)

    def case_over(self, success):
        if success == 1:
            logger.info('[GN_INF] <current case> [CASE_TITLE="%s"] success!' % self.case_title)
        elif success == 0:
            logger.info('[GN_INF] <current case> [CASE_TITLE="%s"] failed!' % self.case_title)
        time.sleep(1)
        self.driver.close_app()
        logger.info('app closed [time=%s]' % time.strftime("%Y-%m-%d %H:%M:%S"))
        self.driver.quit()
