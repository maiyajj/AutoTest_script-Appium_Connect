# coding=utf-8
# 由IncrementalUpdate.py生成
from src.testcase.page.AppPageElement import *


class PageElementJD(object):
    def __init__(self, device, phone_os, app):
        self.mpw = MainPageWidget(phone_os, app).wrapper()
        self.device = device

    def get_page_element(self):
        self.device["page"] = {}
        self.device["page"]["add_device_list_page"] = self.mpw.add_device_list_page()
        self.device["page"]["add_device_method_page"] = self.mpw.add_device_method_page()
        self.device["page"]["add_history_list_page"] = self.mpw.add_history_list_page()
        self.device["page"]["add_outlet_list_page"] = self.mpw.add_outlet_list_page()
        self.device["page"]["add_specification_page"] = self.mpw.add_specification_page()
        self.device["page"]["app_home_page"] = self.mpw.app_home_page()
        self.device["page"]["batch_add_device_page"] = self.mpw.batch_add_device_page()
        self.device["page"]["bind_device_page"] = self.mpw.bind_device_page()
        self.device["page"]["bind_device_success_page"] = self.mpw.bind_device_success_page()
        self.device["page"]["control_device_page"] = self.mpw.control_device_page()
        self.device["page"]["device_info_page"] = self.mpw.device_info_page()
        self.device["page"]["god_page"] = self.mpw.god_page()
        self.device["page"]["input_wifi_password_page"] = self.mpw.input_wifi_password_page()
        self.device["page"]["search_device_fail_page"] = self.mpw.search_device_fail_page()
        self.device["page"]["search_device_loading_page"] = self.mpw.search_device_loading_page()
        self.device["page"]["search_device_success_page"] = self.mpw.search_device_success_page()

        self.device["page"]["bind_device_fail_popup"] = self.mpw.bind_device_fail_popup()
        self.device["page"]["close_ad_popup"] = self.mpw.close_ad_popup()
        self.device["page"]["loading_popup"] = self.mpw.loading_popup()
        self.device["page"]["unbind_device_popup"] = self.mpw.unbind_device_popup()
        self.device["page"]["update_popup"] = self.mpw.update_popup()
