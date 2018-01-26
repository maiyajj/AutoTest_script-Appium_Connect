# coding=utf-8
# 由CreateSomeFiles.py生成
from src.testcase.GN_Y201H.page.AppPageElement import *


class PageElement(object):
    """
    智能家居-GN_Y201H all page element
    """

    def __init__(self, phone_os):
        self.mpw = MainPageWidget(phone_os)

    def get_page_element(self):
        return {
            "add_device_page": self.mpw.add_device_page(),
            "add_normal_timer_page": self.mpw.add_normal_timer_page(),
            "app_home_page": self.mpw.app_home_page(),
            "control_device_page": self.mpw.control_device_page(),
            "device_info_page": self.mpw.device_info_page(),
            "device_setting_page": self.mpw.device_setting_page(),
            "input_wifi_password_page": self.mpw.input_wifi_password_page(),
            "normal_timer_page": self.mpw.normal_timer_page(),
            "set_name_addr_page": self.mpw.set_name_addr_page(),

            "ad_popup": self.mpw.ad_popup(),
            "change_nickname_popup": self.mpw.change_nickname_popup(),
            "delay_timer_roll_popup": self.mpw.delay_timer_roll_popup(),
            "loading_popup": self.mpw.loading_popup(),
            "normal_timer_roll_popup": self.mpw.normal_timer_roll_popup(),
            "timer_repeat_popup": self.mpw.timer_repeat_popup(),
            "unbind_device_popup": self.mpw.unbind_device_popup(),
            "update_popup": self.mpw.update_popup()
        }
