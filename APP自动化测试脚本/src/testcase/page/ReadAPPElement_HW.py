# coding=utf-8
# 由CreateSomeFiles.py生成
from src.testcase.page.AppPageElement import *


class PageElementHW(object):
    """
    智能家居App all page element
    """

    def __init__(self, phone_os, app):
        self.mpw = MainPageWidget(phone_os, app).wrapper()

    def get_page_element(self):
        d = {}
        d["add_device_page"] = self.mpw.add_device_page()
        d["add_normal_timer_page"] = self.mpw.add_normal_timer_page()
        d["app_home_page"] = self.mpw.app_home_page()
        d["control_device_page"] = self.mpw.control_device_page()
        d["device_info_page"] = self.mpw.device_info_page()
        d["device_setting_page"] = self.mpw.device_setting_page()
        d["input_wifi_password_page"] = self.mpw.input_wifi_password_page()
        d["normal_timer_page"] = self.mpw.normal_timer_page()
        d["set_name_addr_page"] = self.mpw.set_name_addr_page()

        d["ad_popup"] = self.mpw.ad_popup()
        d["change_nickname_popup"] = self.mpw.change_nickname_popup()
        d["delay_timer_roll_popup"] = self.mpw.delay_timer_roll_popup()
        d["loading_popup"] = self.mpw.loading_popup()
        d["normal_timer_roll_popup"] = self.mpw.normal_timer_roll_popup()
        d["timer_repeat_popup"] = self.mpw.timer_repeat_popup()
        d["unbind_device_popup"] = self.mpw.unbind_device_popup()
        d["update_popup"] = self.mpw.update_popup()

        return d
