# coding=utf-8
from AppPageElement_AL_Android import *
from AppPageElement_AL_iOS import *


class MainPageWidgetAL(object):
    def __init__(self, phone_os):
        self.phone_os = phone_os
        self.mpwa = MainPageWidgetAndroidAL()
        self.mpwi = MainPageWidgetIosAL()
        self.pwa = PopupWidgetAndroidAL()
        self.pwi = PopupWidgetIosAL()
    def wrapper(self, func1, func2):
        if self.phone_os == "Android":
            return func1
        elif self.phone_os == "iOS":
            return func2
        else:
            raise KeyError("The OS is wrong!")

    def add_device_class_page(self):
        return self.wrapper(self.mpwa.add_device_class_page(), self.mpwi.add_device_class_page())

    def add_device_method_page(self):
        return self.wrapper(self.mpwa.add_device_method_page(), self.mpwi.add_device_method_page())

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

    def day_elec_page(self):
        return self.wrapper(self.mpwa.day_elec_page(), self.mpwi.day_elec_page())

    def delay_timer_page(self):
        return self.wrapper(self.mpwa.delay_timer_page(), self.mpwi.delay_timer_page())

    def device_info_page(self):
        return self.wrapper(self.mpwa.device_info_page(), self.mpwi.device_info_page())

    def elec_page(self):
        return self.wrapper(self.mpwa.elec_page(), self.mpwi.elec_page())

    def exit_error(self):
        return self.wrapper(self.mpwa.exit_error(), self.mpwi.exit_error())

    def fish_mode_timer_page(self):
        return self.wrapper(self.mpwa.fish_mode_timer_page(), self.mpwi.fish_mode_timer_page())

    def input_wifi_password_page(self):
        return self.wrapper(self.mpwa.input_wifi_password_page(), self.mpwi.input_wifi_password_page())

    def login_page(self):
        return self.wrapper(self.mpwa.login_page(), self.mpwi.login_page())

    def more_elec_history_page(self):
        return self.wrapper(self.mpwa.more_elec_history_page(), self.mpwi.more_elec_history_page())

    def mosquito_mode_timer_page(self):
        return self.wrapper(self.mpwa.mosquito_mode_timer_page(), self.mpwi.mosquito_mode_timer_page())

    def my_page(self):
        return self.wrapper(self.mpwa.my_page(), self.mpwi.my_page())

    def night_mode_timer_page(self):
        return self.wrapper(self.mpwa.night_mode_timer_page(), self.mpwi.night_mode_timer_page())

    def normal_timer_page(self):
        return self.wrapper(self.mpwa.normal_timer_page(), self.mpwi.normal_timer_page())

    def peak_valley_price_page(self):
        return self.wrapper(self.mpwa.peak_valley_price_page(), self.mpwi.peak_valley_price_page())

    def piocc_mode_timer_page(self):
        return self.wrapper(self.mpwa.piocc_mode_timer_page(), self.mpwi.piocc_mode_timer_page())

    def search_device_fail_page(self):
        return self.wrapper(self.mpwa.search_device_fail_page(), self.mpwi.search_device_fail_page())

    def search_device_loading_page(self):
        return self.wrapper(self.mpwa.search_device_loading_page(), self.mpwi.search_device_loading_page())

    def set_elec_page(self):
        return self.wrapper(self.mpwa.set_elec_page(), self.mpwi.set_elec_page())

    def set_peak_price_page(self):
        return self.wrapper(self.mpwa.set_peak_price_page(), self.mpwi.set_peak_price_page())

    def set_valley_price_page(self):
        return self.wrapper(self.mpwa.set_valley_price_page(), self.mpwi.set_valley_price_page())

    def setting_page(self):
        return self.wrapper(self.mpwa.setting_page(), self.mpwi.setting_page())

    def single_price_page(self):
        return self.wrapper(self.mpwa.single_price_page(), self.mpwi.single_price_page())

    def timer_repeat_page(self):
        return self.wrapper(self.mpwa.timer_repeat_page(), self.mpwi.timer_repeat_page())

    def warmer_mode_timer_page(self):
        return self.wrapper(self.mpwa.warmer_mode_timer_page(), self.mpwi.warmer_mode_timer_page())

    def water_mode_timer_page(self):
        return self.wrapper(self.mpwa.water_mode_timer_page(), self.mpwi.water_mode_timer_page())

    def welcome_page(self):
        return self.wrapper(self.mpwa.welcome_page(), self.mpwi.welcome_page())

    def add_device_popup(self):
        return self.wrapper(self.pwa.add_device_popup(), self.pwi.add_device_popup())

    def bind_device_popup(self):
        return self.wrapper(self.pwa.bind_device_popup(), self.pwi.bind_device_popup())

    def loading_popup(self):
        return self.wrapper(self.pwa.loading_popup(), self.pwi.loading_popup())

    def logout_popup(self):
        return self.wrapper(self.pwa.logout_popup(), self.pwi.logout_popup())

    def mode_timer_conflict_popup(self):
        return self.wrapper(self.pwa.mode_timer_conflict_popup(), self.pwi.mode_timer_conflict_popup())

    def timer_roll_popup(self):
        return self.wrapper(self.pwa.timer_roll_popup(), self.pwi.timer_roll_popup())

    def unbind_device_popup(self):
        return self.wrapper(self.pwa.unbind_device_popup(), self.pwi.unbind_device_popup())

    def update_popup(self):
        return self.wrapper(self.pwa.update_popup(), self.pwi.update_popup())
