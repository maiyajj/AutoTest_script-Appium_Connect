# coding:utf-8
from src.testcase.common.Widget_Check_Unit import *
from src.utils.Read_APP_Element import *


class GN_app_login_1(object):
    def __init__(self):
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.widget_check_unit = Widget_Check_Unit(self.driver)
        self.case()

    def case(self):
        self.widget_check_unit.widget_click(login_page["to_find_password"],
                                            login_page["to_find_password"],
                                            find_password_page["title"], 60, 60, 1, 60, 0.5)
        self.driver.close_app()
        self.driver.quit()
