# coding=utf-8
# 由CreateSomeFiles.py生成
from src.testcase.GN_F1331.page.AppPageElement import *


class PageElement(object):
    """
    京东微联-GN_F1331 all page element
    """

    def __init__(self, phone_os):
        self.mpw = MainPageWidget(phone_os)

    def get_page_element(self):
        return {
            "account_setting_page": self.mpw.account_setting_page(),
            "add_device_list_page": self.mpw.add_device_list_page(),
            "add_device_method_page": self.mpw.add_device_method_page(),
            "add_history_list_page": self.mpw.add_history_list_page(),
            "add_normal_timer_page": self.mpw.add_normal_timer_page(),
            "add_outlet_list_page": self.mpw.add_outlet_list_page(),
            "add_specification_page": self.mpw.add_specification_page(),
            "app_home_page": self.mpw.app_home_page(),
            "change_nickname_page": self.mpw.change_nickname_page(),
            "control_device_page": self.mpw.control_device_page(),
            "cycle_timer_page": self.mpw.cycle_timer_page(),
            "delay_timer_page": self.mpw.delay_timer_page(),
            "device_info_page": self.mpw.device_info_page(),
            "device_setting_page": self.mpw.device_setting_page(),
            "down_timer_page": self.mpw.down_timer_page(),
            "elec_bill_page": self.mpw.elec_bill_page(),
            "elec_page": self.mpw.elec_page(),
            "help_setting_page": self.mpw.help_setting_page(),
            "input_wifi_password_page": self.mpw.input_wifi_password_page(),
            "login_page": self.mpw.login_page(),
            "mid_timer_page": self.mpw.mid_timer_page(),
            "peak_valley_price_page": self.mpw.peak_valley_price_page(),
            "search_device_fail_page": self.mpw.search_device_fail_page(),
            "search_device_loading_page": self.mpw.search_device_loading_page(),
            "search_device_success_page": self.mpw.search_device_success_page(),
            "set_elec_page": self.mpw.set_elec_page(),
            "single_price_page": self.mpw.single_price_page(),
            "timer_log_page": self.mpw.timer_log_page(),
            "timer_notes_page": self.mpw.timer_notes_page(),
            "timer_repeat_page": self.mpw.timer_repeat_page(),
            "up_timer_page": self.mpw.up_timer_page(),

            "bind_device_fail_popup": self.mpw.bind_device_fail_popup(),
            "close_ad_popup": self.mpw.close_ad_popup(),
            "loading_popup": self.mpw.loading_popup(),
            "logout_popup": self.mpw.logout_popup(),
            "max_normal_timer_popup": self.mpw.max_normal_timer_popup(),
            "mode_timer_conflict_popup": self.mpw.mode_timer_conflict_popup(),
            "timer_edit_popup": self.mpw.timer_edit_popup(),
            "unbind_device_popup": self.mpw.unbind_device_popup(),
            "update_popup": self.mpw.update_popup()
        }
