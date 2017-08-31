# coding=utf-8
from AppPageElement_JD_Android import *
from AppPageElement_JD_iOS import *


class MainPageWidgetJD(object):
    def __init__(self, phone_os):
        self.phone_os = phone_os
        self.mpwa = MainPageWidgetAndroidJD()
        self.mpwi = MainPageWidgetIosJD()
        self.pwa = PopupWidgetAndroidJD()
        self.pwi = PopupWidgetIosJD()

    def wrapper(self, func1, func2):
        if self.phone_os == "Android":
            return func1
        elif self.phone_os == "iOS":
            return func2
        else:
            raise KeyError("The OS is wrong!")

    def add_device_list_page(self):
        return self.wrapper(self.mpwa.add_device_list_page(), self.mpwi.add_device_list_page())

    def add_device_method_page(self):
        return self.wrapper(self.mpwa.add_device_method_page(), self.mpwi.add_device_method_page())

    def add_history_list_page(self):
        return self.wrapper(self.mpwa.add_history_list_page(), self.mpwi.add_history_list_page())

    def add_outlet_list_page(self):
        return self.wrapper(self.mpwa.add_outlet_list_page(), self.mpwi.add_outlet_list_page())

    def add_specification_page(self):
        return self.wrapper(self.mpwa.add_specification_page(), self.mpwi.add_specification_page())

    def app_home_page(self):
        return self.wrapper(self.mpwa.app_home_page(), self.mpwi.app_home_page())

    def batch_add_device_page(self):
        return self.wrapper(self.mpwa.batch_add_device_page(), self.mpwi.batch_add_device_page())

    def bind_device_page(self):
        return self.wrapper(self.mpwa.bind_device_page(), self.mpwi.bind_device_page())

    def bind_device_success_page(self):
        return self.wrapper(self.mpwa.bind_device_success_page(), self.mpwi.bind_device_success_page())

    def control_device_page(self):
        return self.wrapper(self.mpwa.control_device_page(), self.mpwi.control_device_page())

    def device_info_page(self):
        return self.wrapper(self.mpwa.device_info_page(), self.mpwi.device_info_page())

    def god_page(self):
        return self.wrapper(self.mpwa.god_page(), self.mpwi.god_page())

    def input_wifi_password_page(self):
        return self.wrapper(self.mpwa.input_wifi_password_page(), self.mpwi.input_wifi_password_page())

    def search_device_fail_page(self):
        return self.wrapper(self.mpwa.search_device_fail_page(), self.mpwi.search_device_fail_page())

    def search_device_loading_page(self):
        return self.wrapper(self.mpwa.search_device_loading_page(), self.mpwi.search_device_loading_page())

    def search_device_success_page(self):
        return self.wrapper(self.mpwa.search_device_success_page(), self.mpwi.search_device_success_page())

    def bind_device_fail_popup(self):
        return self.wrapper(self.pwa.bind_device_fail_popup(), self.pwi.bind_device_fail_popup())

    def close_ad_popup(self):
        return self.wrapper(self.pwa.close_ad_popup(), self.pwi.close_ad_popup())

    def loading_popup(self):
        return self.wrapper(self.pwa.loading_popup(), self.pwi.loading_popup())

    def unbind_device_popup(self):
        return self.wrapper(self.pwa.unbind_device_popup(), self.pwi.unbind_device_popup())

    def update_popup(self):
        return self.wrapper(self.pwa.update_popup(), self.pwi.update_popup())
