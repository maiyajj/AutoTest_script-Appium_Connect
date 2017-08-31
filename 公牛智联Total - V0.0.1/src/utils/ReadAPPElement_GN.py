# coding=utf-8
# 由IncrementalUpdate.py生成
from src.testcase.page.AppPageElement import *


class PageElementGN(object):
    def __init__(self, device, phone_os, app):
        self.mpw = MainPageWidget(phone_os, app).wrapper()
        self.device = device

    def get_page_element(self):
        self.device["page"] = {}
        self.device["page"]["account_setting_page"] = self.mpw.account_setting_page()
        self.device["page"]["add_device_failed_page"] = self.mpw.add_device_failed_page()
        self.device["page"]["app_help_page"] = self.mpw.app_help_page()
        self.device["page"]["change_nickname_page"] = self.mpw.change_nickname_page()
        self.device["page"]["change_pwd_page"] = self.mpw.change_pwd_page()
        self.device["page"]["device_add_scan_page"] = self.mpw.device_add_scan_page()
        self.device["page"]["device_control_page"] = self.mpw.device_control_page()
        self.device["page"]["device_page"] = self.mpw.device_page()
        self.device["page"]["feedback_page"] = self.mpw.feedback_page()
        self.device["page"]["find_password_page"] = self.mpw.find_password_page()
        self.device["page"]["gender_page"] = self.mpw.gender_page()
        self.device["page"]["god_page"] = self.mpw.god_page()
        self.device["page"]["home_message_page"] = self.mpw.home_message_page()
        self.device["page"]["login_page"] = self.mpw.login_page()
        self.device["page"]["message_classify_page"] = self.mpw.message_classify_page()
        self.device["page"]["message_setting_page"] = self.mpw.message_setting_page()
        self.device["page"]["new_password_page"] = self.mpw.new_password_page()
        self.device["page"]["personal_settings_page"] = self.mpw.personal_settings_page()
        self.device["page"]["prepare_set_network_page"] = self.mpw.prepare_set_network_page()
        self.device["page"]["protocol_page"] = self.mpw.protocol_page()
        self.device["page"]["register_page"] = self.mpw.register_page()
        self.device["page"]["scan_with_subscribe_page"] = self.mpw.scan_with_subscribe_page()
        self.device["page"]["set_network_page"] = self.mpw.set_network_page()
        self.device["page"]["theme_style_page"] = self.mpw.theme_style_page()
        self.device["page"]["upgrade_page"] = self.mpw.upgrade_page()
        self.device["page"]["view_pager_page"] = self.mpw.view_pager_page()

        self.device["page"]["clear_activity_popup"] = self.mpw.clear_activity_popup()
        self.device["page"]["clear_device_popup"] = self.mpw.clear_device_popup()
        self.device["page"]["loading_popup"] = self.mpw.loading_popup()
        self.device["page"]["login_popup"] = self.mpw.login_popup()
        self.device["page"]["logout_popup"] = self.mpw.logout_popup()
        self.device["page"]["terminate_add_device_popup"] = self.mpw.terminate_add_device_popup()
        self.device["page"]["update_popup"] = self.mpw.update_popup()
