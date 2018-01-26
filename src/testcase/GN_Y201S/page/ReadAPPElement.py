# coding=utf-8
# 由CreateSomeFiles.py生成
from src.testcase.GN_Y201S.page.AppPageElement import *


class PageElement(object):
    """
    阿里智能-GN_Y201S all page element
    """

    def __init__(self, phone_os):
        self.mpw = MainPageWidget(phone_os)

    def get_page_element(self):
        return {
            "add_device_class_page": self.mpw.add_device_class_page(),
            "add_device_method_page": self.mpw.add_device_method_page(),
            "add_normal_timer_page": self.mpw.add_normal_timer_page(),
            "add_outlet_list_page": self.mpw.add_outlet_list_page(),
            "add_specification_page": self.mpw.add_specification_page(),
            "app_home_page": self.mpw.app_home_page(),
            "change_nickname_page": self.mpw.change_nickname_page(),
            "control_device_page": self.mpw.control_device_page(),
            "cycle_timer_page": self.mpw.cycle_timer_page(),
            "day_elec_page": self.mpw.day_elec_page(),
            "delay_timer_page": self.mpw.delay_timer_page(),
            "device_info_page": self.mpw.device_info_page(),
            "elec_page": self.mpw.elec_page(),
            "fish_mode_timer_page": self.mpw.fish_mode_timer_page(),
            "input_wifi_password_page": self.mpw.input_wifi_password_page(),
            "login_page": self.mpw.login_page(),
            "more_elec_history_page": self.mpw.more_elec_history_page(),
            "mosquito_mode_timer_page": self.mpw.mosquito_mode_timer_page(),
            "my_page": self.mpw.my_page(),
            "night_mode_timer_page": self.mpw.night_mode_timer_page(),
            "normal_timer_page": self.mpw.normal_timer_page(),
            "peak_valley_price_page": self.mpw.peak_valley_price_page(),
            "piocc_mode_timer_page": self.mpw.piocc_mode_timer_page(),
            "search_device_fail_page": self.mpw.search_device_fail_page(),
            "search_device_loading_page": self.mpw.search_device_loading_page(),
            "set_elec_page": self.mpw.set_elec_page(),
            "set_peak_price_page": self.mpw.set_peak_price_page(),
            "set_valley_price_page": self.mpw.set_valley_price_page(),
            "setting_page": self.mpw.setting_page(),
            "single_price_page": self.mpw.single_price_page(),
            "timer_repeat_page": self.mpw.timer_repeat_page(),
            "warmer_mode_timer_page": self.mpw.warmer_mode_timer_page(),
            "water_mode_timer_page": self.mpw.water_mode_timer_page(),
            "welcome_page": self.mpw.welcome_page(),

            "add_device_popup": self.mpw.add_device_popup(),
            "bind_device_popup": self.mpw.bind_device_popup(),
            "loading_popup": self.mpw.loading_popup(),
            "logout_popup": self.mpw.logout_popup(),
            "mode_timer_conflict_popup": self.mpw.mode_timer_conflict_popup(),
            "timer_roll_popup": self.mpw.timer_roll_popup(),
            "unbind_device_popup": self.mpw.unbind_device_popup(),
            "update_popup": self.mpw.update_popup()
        }
