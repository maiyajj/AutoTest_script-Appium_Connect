# coding=utf-8
from AppPageElement_GN_Android import *
from AppPageElement_GN_iOS import *


class MainPageWidgetGN(object):
    def __init__(self, phone_os):
        self.phone_os = phone_os
        self.mpwa = MainPageWidgetAndroidGN()
        self.mpwi = MainPageWidgetIosGN()
        self.pwa = PopupWidgetAndroidGN()
        self.pwi = PopupWidgetIosGN()
    def wrapper(self, func1, func2):
        if self.phone_os == "Android":
            return func1
        elif self.phone_os == "iOS":
            return func2
        else:
            raise KeyError("The OS is wrong!")

    def account_setting_page(self):
        return self.wrapper(self.mpwa.account_setting_page(), self.mpwi.account_setting_page())

    def add_device_failed_page(self):
        return self.wrapper(self.mpwa.add_device_failed_page(), self.mpwi.add_device_failed_page())

    def app_help_page(self):
        return self.wrapper(self.mpwa.app_help_page(), self.mpwi.app_help_page())

    def change_nickname_page(self):
        return self.wrapper(self.mpwa.change_nickname_page(), self.mpwi.change_nickname_page())

    def change_pwd_page(self):
        return self.wrapper(self.mpwa.change_pwd_page(), self.mpwi.change_pwd_page())

    def device_add_scan_page(self):
        return self.wrapper(self.mpwa.device_add_scan_page(), self.mpwi.device_add_scan_page())

    def device_control_page(self):
        return self.wrapper(self.mpwa.device_control_page(), self.mpwi.device_control_page())

    def device_page(self):
        return self.wrapper(self.mpwa.device_page(), self.mpwi.device_page())

    def feedback_page(self):
        return self.wrapper(self.mpwa.feedback_page(), self.mpwi.feedback_page())

    def find_password_page(self):
        return self.wrapper(self.mpwa.find_password_page(), self.mpwi.find_password_page())

    def gender_page(self):
        return self.wrapper(self.mpwa.gender_page(), self.mpwi.gender_page())

    def home_message_page(self):
        return self.wrapper(self.mpwa.home_message_page(), self.mpwi.home_message_page())

    def login_page(self):
        return self.wrapper(self.mpwa.login_page(), self.mpwi.login_page())

    def message_classify_page(self):
        return self.wrapper(self.mpwa.message_classify_page(), self.mpwi.message_classify_page())

    def message_setting_page(self):
        return self.wrapper(self.mpwa.message_setting_page(), self.mpwi.message_setting_page())

    def new_password_page(self):
        return self.wrapper(self.mpwa.new_password_page(), self.mpwi.new_password_page())

    def personal_settings_page(self):
        return self.wrapper(self.mpwa.personal_settings_page(), self.mpwi.personal_settings_page())

    def prepare_set_network_page(self):
        return self.wrapper(self.mpwa.prepare_set_network_page(), self.mpwi.prepare_set_network_page())

    def protocol_page(self):
        return self.wrapper(self.mpwa.protocol_page(), self.mpwi.protocol_page())

    def register_page(self):
        return self.wrapper(self.mpwa.register_page(), self.mpwi.register_page())

    def scan_with_subscribe_page(self):
        return self.wrapper(self.mpwa.scan_with_subscribe_page(), self.mpwi.scan_with_subscribe_page())

    def set_network_page(self):
        return self.wrapper(self.mpwa.set_network_page(), self.mpwi.set_network_page())

    def theme_style_page(self):
        return self.wrapper(self.mpwa.theme_style_page(), self.mpwi.theme_style_page())

    def upgrade_page(self):
        return self.wrapper(self.mpwa.upgrade_page(), self.mpwi.upgrade_page())

    def view_pager_page(self):
        return self.wrapper(self.mpwa.view_pager_page(), self.mpwi.view_pager_page())

    def clear_activity_popup(self):
        return self.wrapper(self.pwa.clear_activity_popup(), self.pwi.clear_activity_popup())

    def clear_device_popup(self):
        return self.wrapper(self.pwa.clear_device_popup(), self.pwi.clear_device_popup())

    def loading_popup(self):
        return self.wrapper(self.pwa.loading_popup(), self.pwi.loading_popup())

    def login_popup(self):
        return self.wrapper(self.pwa.login_popup(), self.pwi.login_popup())

    def logout_popup(self):
        return self.wrapper(self.pwa.logout_popup(), self.pwi.logout_popup())

    def terminate_add_device_popup(self):
        return self.wrapper(self.pwa.terminate_add_device_popup(), self.pwi.terminate_add_device_popup())

    def update_popup(self):
        return self.wrapper(self.pwa.update_popup(), self.pwi.update_popup())
