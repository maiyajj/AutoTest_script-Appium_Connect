# coding:utf-8
from src.testcase.common.WidgetCheckUnit import *
from src.testcase.case.ToLoginPage import *


class GNAppLogin4(object):
    def __init__(self):
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        logger.info('app start [time=%s]' % time.strftime("%Y-%m-%d %H:%M:%S"))
        widget_check_unit = WidgetCheckUnit(self.driver)
        self.widget_click = widget_check_unit.widget_click
        self.case_title = u"登录页面—登录功能检查"
        logger.info('[GN_INF] <current case> [CASE_ID="%s", CASE_TITLE="%s"]'
                    % (os.path.basename(__file__).split(".")[0], self.case_title))
        ToLoginPage(1)
        self.case()

    # 用例动作
    def case(self):
        check_page = login_page["title"]
        operate_widget = login_page["username"]
        wait_page = login_page["title"]
        widget = self.widget_click(check_page, operate_widget, wait_page, 10, 10, 1, 60, 0.5)

        # 29 is the keycode of 'a', 28672 is the keycode of META_CTRL_MASK
        self.driver.press_keycode(29, 28672)
        # KEYCODE_FORWARD_DEL 删除键 112
        self.driver.press_keycode(112)
        # 发送数据
        data = "18042078927"
        widget.send_keys(data)
        logger.info(u'[APP_INPUT] ["用户名"] input success')
        time.sleep(0.5)

        check_page = login_page["title"]
        operate_widget = login_page["password"]
        wait_page = login_page["title"]
        widget = self.widget_click(check_page, operate_widget, wait_page, 10, 10, 1, 60, 0.5)

        self.driver.press_keycode(29, 28672)
        self.driver.press_keycode(112)
        data = "chenghao"
        widget.send_keys(data)
        logger.info(u'[APP_INPUT] ["密码"] input success')
        time.sleep(0.5)

        check_page = login_page["title"]
        operate_widget = login_page["login_button"]
        wait_page = device_page["title"]
        self.widget_click(check_page, operate_widget, wait_page, 10, 10, 1, 60, 0.5)

        self.case_over()

    def case_over(self):
        logger.info('[GN_INF] <current case> [CASE_TITLE="%s"] success!' % self.case_title)
        time.sleep(1)
        self.driver.close_app()
        logger.info('app closed [time=%s]' % time.strftime("%Y-%m-%d %H:%M:%S"))
        self.driver.quit()
