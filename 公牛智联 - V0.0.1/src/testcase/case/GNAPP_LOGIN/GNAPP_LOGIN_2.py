# coding:utf-8
from src.testcase.common.WidgetCheckUnit import *
from src.testcase.case.ToLoginPage import *

class GNAppLogin2(object):
    def __init__(self):
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        logger.info('app start [time=%s]' % time.strftime("%Y-%m-%d %H:%M:%S"))
        widget_check_unit = WidgetCheckUnit(self.driver)
        self.widget_click = widget_check_unit.widget_click
        self.case_title = u"登录页面—忘记密码页面跳转"

        logger.info('[GN_INF] <current case> [CASE_ID="%s", CASE_TITLE="%s"]'
                    % (os.path.basename(__file__).split(".")[0], self.case_title))
        ToLoginPage(1)
        self.case()

    # 用例动作
    def case(self):
        self.widget_click(login_page["title"],
                          login_page["to_find_password"],
                          find_password_page["title"],
                          10, 10, 1, 60, 0.5)

        self.case_over()

    def case_over(self):
        logger.info('[GN_INF] <current case> [CASE_TITLE="%s"] success!' % self.case_title)
        time.sleep(1)
        self.driver.close_app()
        logger.info('app closed [time=%s]' % time.strftime("%Y-%m-%d %H:%M:%S"))
        self.driver.quit()
