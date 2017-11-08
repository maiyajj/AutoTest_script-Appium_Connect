# coding=utf-8
# 由CreateSomeFiles.py生成
from src.testcase.page.AppPageElement import *


class PageElementHW(object):
    """
    智能家居App all page element
    """

    def __init__(self, device, phone_os, app):
        self.mpw = MainPageWidget(phone_os, app).wrapper()
        self.device = device

    def get_page_element(self):
        self.device["page"] = {}
        self.device["page"]["add_device_page"] = self.mpw.add_device_page()
        self.device["page"]["add_normal_timer_page"] = self.mpw.add_normal_timer_page()
        self.device["page"]["app_home_page"] = self.mpw.app_home_page()
        self.device["page"]["control_device_page"] = self.mpw.control_device_page()
        self.device["page"]["device_info_page"] = self.mpw.device_info_page()
        self.device["page"]["device_setting_page"] = self.mpw.device_setting_page()
        self.device["page"]["input_wifi_password_page"] = self.mpw.input_wifi_password_page()
        self.device["page"]["normal_timer_page"] = self.mpw.normal_timer_page()
        self.device["page"]["set_name_addr_page"] = self.mpw.set_name_addr_page()

        self.device["page"]["change_nickname_popup"] = self.mpw.change_nickname_popup()
        self.device["page"]["delay_timer_roll_popup"] = self.mpw.delay_timer_roll_popup()
        self.device["page"]["loading_popup"] = self.mpw.loading_popup()
        self.device["page"]["normal_timer_roll_popup"] = self.mpw.normal_timer_roll_popup()
        self.device["page"]["timer_repeat_popup"] = self.mpw.timer_repeat_popup()
        self.device["page"]["unbind_device_popup"] = self.mpw.unbind_device_popup()
        self.device["page"]["update_popup"] = self.mpw.update_popup()
