# coding=utf-8
# 由IncrementalUpdate.py生成
from src.testcase.page.AppPageElement import *


class PageElementAL(object):
    def __init__(self, device, phone_os, app):
        self.mpw = MainPageWidget(phone_os, app).wrapper()
        self.device = device

    def get_page_element(self):
        self.device["page"] = {}
        self.device["page"]["add_device_class_page"] = self.mpw.add_device_class_page()
        self.device["page"]["add_device_method_page"] = self.mpw.add_device_method_page()
        self.device["page"]["add_history_list_page"] = self.mpw.add_history_list_page()
        self.device["page"]["add_specification_page"] = self.mpw.add_specification_page()
        self.device["page"]["app_home_page"] = self.mpw.app_home_page()
        self.device["page"]["bind_device_page"] = self.mpw.bind_device_page()
        self.device["page"]["change_nickname_page"] = self.mpw.change_nickname_page()
        self.device["page"]["control_device_page"] = self.mpw.control_device_page()
        self.device["page"]["device_info_page"] = self.mpw.device_info_page()
        self.device["page"]["god_page"] = self.mpw.god_page()
        self.device["page"]["input_wifi_password_page"] = self.mpw.input_wifi_password_page()
        self.device["page"]["my_page"] = self.mpw.my_page()
        self.device["page"]["normal_timer_page"] = self.mpw.normal_timer_page()
        self.device["page"]["search_device_fail_page"] = self.mpw.search_device_fail_page()
        self.device["page"]["search_device_loading_page"] = self.mpw.search_device_loading_page()
        self.device["page"]["setting_page"] = self.mpw.setting_page()
        self.device["page"]["timer_log_page"] = self.mpw.timer_log_page()
        self.device["page"]["water_mode_timer_page"] = self.mpw.water_mode_timer_page()

        self.device["page"]["add_device_popup"] = self.mpw.add_device_popup()
        self.device["page"]["logout_popup"] = self.mpw.logout_popup()
