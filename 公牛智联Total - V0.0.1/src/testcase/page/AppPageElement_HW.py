# coding=utf-8
from AppPageElement_HW_Android import *
from AppPageElement_HW_iOS import *


class MainPageWidgetHW(object):
    def __init__(self, phone_os):
        self.phone_os = phone_os
        self.mpwa = MainPageWidgetAndroidHW()
        self.mpwi = MainPageWidgetIosHW()
        self.pwa = PopupWidgetAndroidHW()
        self.pwi = PopupWidgetIosHW()
    def wrapper(self, func1, func2):
        if self.phone_os == "Android":
            return func1
        elif self.phone_os == "iOS":
            return func2
        else:
            raise KeyError("The OS is wrong!")

    def add_device_page(self):
        return self.wrapper(self.mpwa.add_device_page(), self.mpwi.add_device_page())

    def add_normal_timer_page(self):
        return self.wrapper(self.mpwa.add_normal_timer_page(), self.mpwi.add_normal_timer_page())

    def app_home_page(self):
        return self.wrapper(self.mpwa.app_home_page(), self.mpwi.app_home_page())

    def control_device_page(self):
        return self.wrapper(self.mpwa.control_device_page(), self.mpwi.control_device_page())

    def device_info_page(self):
        return self.wrapper(self.mpwa.device_info_page(), self.mpwi.device_info_page())

    def device_setting_page(self):
        return self.wrapper(self.mpwa.device_setting_page(), self.mpwi.device_setting_page())

    def input_wifi_password_page(self):
        return self.wrapper(self.mpwa.input_wifi_password_page(), self.mpwi.input_wifi_password_page())

    def normal_timer_page(self):
        return self.wrapper(self.mpwa.normal_timer_page(), self.mpwi.normal_timer_page())

    def set_name_addr_page(self):
        return self.wrapper(self.mpwa.set_name_addr_page(), self.mpwi.set_name_addr_page())

    def change_nickname_popup(self):
        return self.wrapper(self.pwa.change_nickname_popup(), self.pwi.change_nickname_popup())

    def delay_timer_roll_popup(self):
        return self.wrapper(self.pwa.delay_timer_roll_popup(), self.pwi.delay_timer_roll_popup())

    def loading_popup(self):
        return self.wrapper(self.pwa.loading_popup(), self.pwi.loading_popup())

    def normal_timer_roll_popup(self):
        return self.wrapper(self.pwa.normal_timer_roll_popup(), self.pwi.normal_timer_roll_popup())

    def timer_repeat_popup(self):
        return self.wrapper(self.pwa.timer_repeat_popup(), self.pwi.timer_repeat_popup())

    def unbind_device_popup(self):
        return self.wrapper(self.pwa.unbind_device_popup(), self.pwi.unbind_device_popup())

    def update_popup(self):
        return self.wrapper(self.pwa.update_popup(), self.pwi.update_popup())
