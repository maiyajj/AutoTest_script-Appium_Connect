# coding:utf-8
from src.testcase.case.ToLoginPage import *
from src.testcase.common.WidgetCheckUnit import *


class GNAppForgetPassword1(object):
    def __init__(self):
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        logger.info('app start [time=%s]' % time.strftime("%Y-%m-%d %H:%M:%S"))
        widget_check_unit = WidgetCheckUnit(self.driver)
        self.widget_click = widget_check_unit.widget_click
        self.wait_widget = widget_check_unit.wait_widget
        self.case_title = u'忘记密码页面-点击"返回"按钮，页面检查'
        logger.info('[GN_INF] <current case> [CASE_ID="%s", CASE_TITLE="%s"]'
                    % (os.path.basename(__file__).split(".")[0], self.case_title))
        ToLoginPage()
        self.case()

    # 用例动作
    def case(self):
        try:
            self.widget_click(login_page["title"],
                              login_page["to_find_password"],
                              find_password_page["title"],
                              1, 1, 1, 10, 0.5)

            self.widget_click(find_password_page["title"],
                              find_password_page["to_return"],
                              login_page["title"],
                              1, 1, 1, 10, 0.5)

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
