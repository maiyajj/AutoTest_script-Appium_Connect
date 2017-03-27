# coding:utf-8
from data.Database import *
from src.testcase.common.Widget_Check_Unit import *
# from src.utils.Collect_Log import *
from src.utils.Read_APP_Element import *


class GN_app_login_1(object):
    def __init__(self):
        self.driver = database["driver"]
        self.widget_check_unit = Widget_Check_Unit(self.driver)
        self.case()
        # driver.find_element_by_id("com.iotbull.android.superapp:id/loginFindPasswordTextView").click()

    def case(self):
        self.widget_check_unit.widget_click(login_page["to_find_password"],
                                            login_page["to_find_password"],
                                            find_password_page["title"], 60, 60, 1, 60, 0.5)
        self.driver.close_app()
