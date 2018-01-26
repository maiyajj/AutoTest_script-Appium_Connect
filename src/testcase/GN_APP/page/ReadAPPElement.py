# coding=utf-8
# 由CreateSomeFiles.py生成
from src.testcase.GN_APP.page.AppPageElement import *


class PageElement(object):
    """
    公牛智联-GN_APP all page element
    """

    def __init__(self, phone_os):
        self.mpw = MainPageWidget(phone_os)

    def get_page_element(self):
        return {
            "account_setting_page": self.mpw.account_setting_page(),
            "add_device_failed_page": self.mpw.add_device_failed_page(),
            "app_help_page": self.mpw.app_help_page(),
            "change_nickname_page": self.mpw.change_nickname_page(),
            "change_pwd_page": self.mpw.change_pwd_page(),
            "device_add_scan_page": self.mpw.device_add_scan_page(),
            "device_control_page": self.mpw.device_control_page(),
            "device_page": self.mpw.device_page(),
            "feedback_page": self.mpw.feedback_page(),
            "find_password_page": self.mpw.find_password_page(),
            "gender_page": self.mpw.gender_page(),
            "home_message_page": self.mpw.home_message_page(),
            "login_page": self.mpw.login_page(),
            "message_classify_page": self.mpw.message_classify_page(),
            "message_setting_page": self.mpw.message_setting_page(),
            "new_password_page": self.mpw.new_password_page(),
            "personal_settings_page": self.mpw.personal_settings_page(),
            "prepare_set_network_page": self.mpw.prepare_set_network_page(),
            "protocol_page": self.mpw.protocol_page(),
            "register_page": self.mpw.register_page(),
            "scan_with_subscribe_page": self.mpw.scan_with_subscribe_page(),
            "set_network_page": self.mpw.set_network_page(),
            "theme_style_page": self.mpw.theme_style_page(),
            "upgrade_page": self.mpw.upgrade_page(),
            "view_pager_page": self.mpw.view_pager_page(),

            "clear_activity_popup": self.mpw.clear_activity_popup(),
            "clear_device_popup": self.mpw.clear_device_popup(),
            "loading_popup": self.mpw.loading_popup(),
            "login_popup": self.mpw.login_popup(),
            "logout_popup": self.mpw.logout_popup(),
            "terminate_add_device_popup": self.mpw.terminate_add_device_popup(),
            "update_popup": self.mpw.update_popup()
        }
