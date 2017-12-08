# coding=utf-8
# 由CreateSomeFiles.py生成
from src.testcase.page.AppPageElement import *


class PageElementGN(object):
    """
    公牛智联App all page element
    """

    def __init__(self, phone_os, app):
        self.mpw = MainPageWidget(phone_os, app).wrapper()

    def get_page_element(self):
        d = {}
        d["account_setting_page"] = self.mpw.account_setting_page()
        d["add_device_failed_page"] = self.mpw.add_device_failed_page()
        d["app_help_page"] = self.mpw.app_help_page()
        d["change_nickname_page"] = self.mpw.change_nickname_page()
        d["change_pwd_page"] = self.mpw.change_pwd_page()
        d["device_add_scan_page"] = self.mpw.device_add_scan_page()
        d["device_control_page"] = self.mpw.device_control_page()
        d["device_page"] = self.mpw.device_page()
        d["feedback_page"] = self.mpw.feedback_page()
        d["find_password_page"] = self.mpw.find_password_page()
        d["gender_page"] = self.mpw.gender_page()
        d["home_message_page"] = self.mpw.home_message_page()
        d["login_page"] = self.mpw.login_page()
        d["message_classify_page"] = self.mpw.message_classify_page()
        d["message_setting_page"] = self.mpw.message_setting_page()
        d["new_password_page"] = self.mpw.new_password_page()
        d["personal_settings_page"] = self.mpw.personal_settings_page()
        d["prepare_set_network_page"] = self.mpw.prepare_set_network_page()
        d["protocol_page"] = self.mpw.protocol_page()
        d["register_page"] = self.mpw.register_page()
        d["scan_with_subscribe_page"] = self.mpw.scan_with_subscribe_page()
        d["set_network_page"] = self.mpw.set_network_page()
        d["theme_style_page"] = self.mpw.theme_style_page()
        d["upgrade_page"] = self.mpw.upgrade_page()
        d["view_pager_page"] = self.mpw.view_pager_page()

        d["clear_activity_popup"] = self.mpw.clear_activity_popup()
        d["clear_device_popup"] = self.mpw.clear_device_popup()
        d["loading_popup"] = self.mpw.loading_popup()
        d["login_popup"] = self.mpw.login_popup()
        d["logout_popup"] = self.mpw.logout_popup()
        d["terminate_add_device_popup"] = self.mpw.terminate_add_device_popup()
        d["update_popup"] = self.mpw.update_popup()

        return d
