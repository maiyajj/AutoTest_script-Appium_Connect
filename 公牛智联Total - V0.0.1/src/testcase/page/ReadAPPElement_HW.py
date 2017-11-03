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
        self.device["page"]["add_device_list_page"] = self.mpw.add_device_list_page()
        self.device["page"]["add_device_method_page"] = self.mpw.add_device_method_page()
        self.device["page"]["add_history_list_page"] = self.mpw.add_history_list_page()
        self.device["page"]["add_normal_timer_page"] = self.mpw.add_normal_timer_page()
        self.device["page"]["add_outlet_list_page"] = self.mpw.add_outlet_list_page()
        self.device["page"]["add_specification_page"] = self.mpw.add_specification_page()
        self.device["page"]["app_home_page"] = self.mpw.app_home_page()
        self.device["page"]["change_nickname_page"] = self.mpw.change_nickname_page()
        self.device["page"]["control_device_page"] = self.mpw.control_device_page()
        self.device["page"]["device_info_page"] = self.mpw.device_info_page()
        self.device["page"]["elec_bill_page"] = self.mpw.elec_bill_page()
        self.device["page"]["elec_page"] = self.mpw.elec_page()
        self.device["page"]["fish_mode_timer_page"] = self.mpw.fish_mode_timer_page()
        self.device["page"]["god_page"] = self.mpw.god_page()
        self.device["page"]["input_wifi_password_page"] = self.mpw.input_wifi_password_page()
        self.device["page"]["mode_timer_page"] = self.mpw.mode_timer_page()
        self.device["page"]["normal_timer_page"] = self.mpw.normal_timer_page()
        self.device["page"]["peak_valley_price_page"] = self.mpw.peak_valley_price_page()
        self.device["page"]["piocc_mode_timer_page"] = self.mpw.piocc_mode_timer_page()
        self.device["page"]["search_device_fail_page"] = self.mpw.search_device_fail_page()
        self.device["page"]["search_device_loading_page"] = self.mpw.search_device_loading_page()
        self.device["page"]["search_device_success_page"] = self.mpw.search_device_success_page()
        self.device["page"]["set_elec_page"] = self.mpw.set_elec_page()
        self.device["page"]["single_price_page"] = self.mpw.single_price_page()
        self.device["page"]["timer_log_page"] = self.mpw.timer_log_page()
        self.device["page"]["timer_repeat_page"] = self.mpw.timer_repeat_page()
        self.device["page"]["water_mode_timer_page"] = self.mpw.water_mode_timer_page()

        self.device["page"]["add_device_popup"] = self.mpw.add_device_popup()
        self.device["page"]["loading_popup"] = self.mpw.loading_popup()
        self.device["page"]["logout_popup"] = self.mpw.logout_popup()
        self.device["page"]["mode_timer_conflict_popup"] = self.mpw.mode_timer_conflict_popup()
        self.device["page"]["timer_roll_popup"] = self.mpw.timer_roll_popup()
        self.device["page"]["unbind_device_popup"] = self.mpw.unbind_device_popup()
