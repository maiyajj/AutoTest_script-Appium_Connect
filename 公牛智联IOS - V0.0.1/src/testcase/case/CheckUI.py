# coding=utf-8
from src.testcase.common.WidgetCheckUnit import *


class CheckUI(object):
    def __init__(self, flag=0):
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        widget_check_unit = WidgetCheckUnit(self.driver)
        self.widget_click = widget_check_unit.widget_click
        self.wait_widget = widget_check_unit.wait_widget
        self.check_login_page()

    def check_login_page(self):
        while True:
            try:
                for k, v in login_page.items():
                    print k, v
                    self.wait_widget(v, 3, 1)
                logger.info(u'[APP_INF] ["登录页面"] load success !')
                return True
            except TimeoutException:
                return False
