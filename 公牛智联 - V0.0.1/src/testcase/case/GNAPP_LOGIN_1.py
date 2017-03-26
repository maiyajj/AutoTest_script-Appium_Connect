# coding:utf-8
from data.Database import *
from src.testcase.common.Widget_Check_Unit import *
# from src.utils.Collect_Log import *
from src.utils.Read_APP_Element import *


class GN_app_login_1(object):
    def __init__(self):
        driver = database["driver"]
        self.widget_check_unit = Widget_Check_Unit(driver)
        self.case()
        # driver.find_element_by_id("com.iotbull.android.superapp:id/loginFindPasswordTextView").click()

    def case(self):
        to_find_password = login_page["to_find_password"]
        login_button = login_page["login_button"]
        tmp = login_page["tmp"]
        self.widget_check_unit.widget_click(tmp, to_find_password, login_button, 60, 60, 1, 60, 1)
        print help(self.widget_check_unit.widget_click)
        # while True:
        #     self.widget_check_unit.wait_widget(login_button[1], login_button[0], 60, 1).click()
