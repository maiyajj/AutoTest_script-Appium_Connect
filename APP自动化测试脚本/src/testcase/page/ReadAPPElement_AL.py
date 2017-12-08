# coding=utf-8
# 由CreateSomeFiles.py生成
from src.testcase.page.AppPageElement import *


class PageElementAL(object):
    """
    阿里智能App all page element
    """

    def __init__(self, phone_os, app):
        self.mpw = MainPageWidget(phone_os, app).wrapper()

    def get_page_element(self):
        d = {}
        d["add_device_class_page"] = self.mpw.add_device_class_page()
        d["add_device_method_page"] = self.mpw.add_device_method_page()
        d["add_normal_timer_page"] = self.mpw.add_normal_timer_page()
        d["add_outlet_list_page"] = self.mpw.add_outlet_list_page()
        d["add_specification_page"] = self.mpw.add_specification_page()
        d["app_home_page"] = self.mpw.app_home_page()
        d["change_nickname_page"] = self.mpw.change_nickname_page()
        d["control_device_page"] = self.mpw.control_device_page()
        d["cycle_timer_page"] = self.mpw.cycle_timer_page()
        d["day_elec_page"] = self.mpw.day_elec_page()
        d["delay_timer_page"] = self.mpw.delay_timer_page()
        d["device_info_page"] = self.mpw.device_info_page()
        d["elec_page"] = self.mpw.elec_page()
        d["exit_error"] = self.mpw.exit_error()
        d["fish_mode_timer_page"] = self.mpw.fish_mode_timer_page()
        d["input_wifi_password_page"] = self.mpw.input_wifi_password_page()
        d["login_page"] = self.mpw.login_page()
        d["more_elec_history_page"] = self.mpw.more_elec_history_page()
        d["mosquito_mode_timer_page"] = self.mpw.mosquito_mode_timer_page()
        d["my_page"] = self.mpw.my_page()
        d["night_mode_timer_page"] = self.mpw.night_mode_timer_page()
        d["normal_timer_page"] = self.mpw.normal_timer_page()
        d["peak_valley_price_page"] = self.mpw.peak_valley_price_page()
        d["piocc_mode_timer_page"] = self.mpw.piocc_mode_timer_page()
        d["search_device_fail_page"] = self.mpw.search_device_fail_page()
        d["search_device_loading_page"] = self.mpw.search_device_loading_page()
        d["set_elec_page"] = self.mpw.set_elec_page()
        d["set_peak_price_page"] = self.mpw.set_peak_price_page()
        d["set_valley_price_page"] = self.mpw.set_valley_price_page()
        d["setting_page"] = self.mpw.setting_page()
        d["single_price_page"] = self.mpw.single_price_page()
        d["timer_repeat_page"] = self.mpw.timer_repeat_page()
        d["warmer_mode_timer_page"] = self.mpw.warmer_mode_timer_page()
        d["water_mode_timer_page"] = self.mpw.water_mode_timer_page()
        d["welcome_page"] = self.mpw.welcome_page()

        d["add_device_popup"] = self.mpw.add_device_popup()
        d["bind_device_popup"] = self.mpw.bind_device_popup()
        d["loading_popup"] = self.mpw.loading_popup()
        d["logout_popup"] = self.mpw.logout_popup()
        d["mode_timer_conflict_popup"] = self.mpw.mode_timer_conflict_popup()
        d["timer_roll_popup"] = self.mpw.timer_roll_popup()
        d["unbind_device_popup"] = self.mpw.unbind_device_popup()
        d["update_popup"] = self.mpw.update_popup()

        return d
