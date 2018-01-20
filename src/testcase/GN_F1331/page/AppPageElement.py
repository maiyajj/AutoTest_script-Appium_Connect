# coding=utf-8
from AppPageElement_Android import *
from AppPageElement_iOS import *


class MainPageWidget(object):
    def __init__(self, phone_os):
        self.phone_os = phone_os
        self.mpwa = MainPageWidgetAndroid()
        self.mpwi = MainPageWidgetIos()
        self.pwa = PopupWidgetAndroid()
        self.pwi = PopupWidgetIos()

    def wrapper(self, func1, func2):
        if self.phone_os == "Android":
            return func1
        elif self.phone_os == "iOS":
            return func2
        else:
            raise KeyError("The OS is wrong!")

    def account_setting_page(self):
        return self.wrapper(self.mpwa.account_setting_page(), self.mpwi.account_setting_page())

    def add_device_list_page(self):
        return self.wrapper(self.mpwa.add_device_list_page(), self.mpwi.add_device_list_page())

    def add_device_method_page(self):
        return self.wrapper(self.mpwa.add_device_method_page(), self.mpwi.add_device_method_page())

    def add_history_list_page(self):
        return self.wrapper(self.mpwa.add_history_list_page(), self.mpwi.add_history_list_page())

    def add_normal_timer_page(self):
        return self.wrapper(self.mpwa.add_normal_timer_page(), self.mpwi.add_normal_timer_page())

    def add_outlet_list_page(self):
        return self.wrapper(self.mpwa.add_outlet_list_page(), self.mpwi.add_outlet_list_page())

    def add_specification_page(self):
        return self.wrapper(self.mpwa.add_specification_page(), self.mpwi.add_specification_page())

    def app_home_page(self):
        return self.wrapper(self.mpwa.app_home_page(), self.mpwi.app_home_page())

    def change_nickname_page(self):
        return self.wrapper(self.mpwa.change_nickname_page(), self.mpwi.change_nickname_page())

    def control_device_page(self):
        return self.wrapper(self.mpwa.control_device_page(), self.mpwi.control_device_page())

    def cycle_timer_page(self):
        return self.wrapper(self.mpwa.cycle_timer_page(), self.mpwi.cycle_timer_page())

    def delay_timer_page(self):
        return self.wrapper(self.mpwa.delay_timer_page(), self.mpwi.delay_timer_page())

    def device_info_page(self):
        return self.wrapper(self.mpwa.device_info_page(), self.mpwi.device_info_page())

    def device_setting_page(self):
        return self.wrapper(self.mpwa.device_setting_page(), self.mpwi.device_setting_page())

    def down_timer_page(self):
        return self.wrapper(self.mpwa.down_timer_page(), self.mpwi.down_timer_page())

    def elec_bill_page(self):
        return self.wrapper(self.mpwa.elec_bill_page(), self.mpwi.elec_bill_page())

    def elec_page(self):
        return self.wrapper(self.mpwa.elec_page(), self.mpwi.elec_page())

    def help_setting_page(self):
        return self.wrapper(self.mpwa.help_setting_page(), self.mpwi.help_setting_page())

    def input_wifi_password_page(self):
        return self.wrapper(self.mpwa.input_wifi_password_page(), self.mpwi.input_wifi_password_page())

    def login_page(self):
        return self.wrapper(self.mpwa.login_page(), self.mpwi.login_page())

    def mid_timer_page(self):
        return self.wrapper(self.mpwa.mid_timer_page(), self.mpwi.mid_timer_page())

    def peak_valley_price_page(self):
        return self.wrapper(self.mpwa.peak_valley_price_page(), self.mpwi.peak_valley_price_page())

    def search_device_fail_page(self):
        return self.wrapper(self.mpwa.search_device_fail_page(), self.mpwi.search_device_fail_page())

    def search_device_loading_page(self):
        return self.wrapper(self.mpwa.search_device_loading_page(), self.mpwi.search_device_loading_page())

    def search_device_success_page(self):
        return self.wrapper(self.mpwa.search_device_success_page(), self.mpwi.search_device_success_page())

    def set_elec_page(self):
        return self.wrapper(self.mpwa.set_elec_page(), self.mpwi.set_elec_page())

    def single_price_page(self):
        return self.wrapper(self.mpwa.single_price_page(), self.mpwi.single_price_page())

    def timer_log_page(self):
        return self.wrapper(self.mpwa.timer_log_page(), self.mpwi.timer_log_page())

    def timer_notes_page(self):
        return self.wrapper(self.mpwa.timer_notes_page(), self.mpwi.timer_notes_page())

    def timer_repeat_page(self):
        return self.wrapper(self.mpwa.timer_repeat_page(), self.mpwi.timer_repeat_page())

    def up_timer_page(self):
        return self.wrapper(self.mpwa.up_timer_page(), self.mpwi.up_timer_page())

    def bind_device_fail_popup(self):
        return self.wrapper(self.pwa.bind_device_fail_popup(), self.pwi.bind_device_fail_popup())

    def close_ad_popup(self):
        return self.wrapper(self.pwa.close_ad_popup(), self.pwi.close_ad_popup())

    def loading_popup(self):
        return self.wrapper(self.pwa.loading_popup(), self.pwi.loading_popup())

    def logout_popup(self):
        return self.wrapper(self.pwa.logout_popup(), self.pwi.logout_popup())

    def mode_timer_conflict_popup(self):
        return self.wrapper(self.pwa.mode_timer_conflict_popup(), self.pwi.mode_timer_conflict_popup())

    def timer_edit_popup(self):
        return self.wrapper(self.pwa.timer_edit_popup(), self.pwi.timer_edit_popup())

    def unbind_device_popup(self):
        return self.wrapper(self.pwa.unbind_device_popup(), self.pwi.unbind_device_popup())

    def update_popup(self):
        return self.wrapper(self.pwa.update_popup(), self.pwi.update_popup())
