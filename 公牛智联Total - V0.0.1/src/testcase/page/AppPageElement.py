# coding=utf-8
from AppPageElement_Android import *
from AppPageElement_iOS import *


class MainPageWidget(object):
    def __init__(self, phone_os):
        self.phone_os = phone_os

    def account_setting_page(self):
        if self.phone_os == "Android":
            account_setting_page = MainPageWidgetAndroid().account_setting_page()
        elif self.phone_os == "iOS":
            account_setting_page = MainPageWidgetIos().account_setting_page()
        else:
            raise KeyError("The OS is wrong!")

        return account_setting_page

    def add_device_failed_page(self):
        if self.phone_os == "Android":
            add_device_failed_page = MainPageWidgetAndroid().add_device_failed_page()
        elif self.phone_os == "iOS":
            add_device_failed_page = MainPageWidgetIos().add_device_failed_page()
        else:
            raise KeyError("The OS is wrong!")

        return add_device_failed_page

    def app_help_page(self):
        if self.phone_os == "Android":
            app_help_page = MainPageWidgetAndroid().app_help_page()
        elif self.phone_os == "iOS":
            app_help_page = MainPageWidgetIos().app_help_page()
        else:
            raise KeyError("The OS is wrong!")

        return app_help_page

    def change_nickname_page(self):
        if self.phone_os == "Android":
            change_nickname_page = MainPageWidgetAndroid().change_nickname_page()
        elif self.phone_os == "iOS":
            change_nickname_page = MainPageWidgetIos().change_nickname_page()
        else:
            raise KeyError("The OS is wrong!")

        return change_nickname_page

    def change_pwd_page(self):
        if self.phone_os == "Android":
            change_pwd_page = MainPageWidgetAndroid().change_pwd_page()
        elif self.phone_os == "iOS":
            change_pwd_page = MainPageWidgetIos().change_pwd_page()
        else:
            raise KeyError("The OS is wrong!")

        return change_pwd_page

    def device_add_scan_page(self):
        if self.phone_os == "Android":
            device_add_scan_page = MainPageWidgetAndroid().device_add_scan_page()
        elif self.phone_os == "iOS":
            device_add_scan_page = MainPageWidgetIos().device_add_scan_page()
        else:
            raise KeyError("The OS is wrong!")

        return device_add_scan_page

    def device_control_page(self):
        if self.phone_os == "Android":
            device_control_page = MainPageWidgetAndroid().device_control_page()
        elif self.phone_os == "iOS":
            device_control_page = MainPageWidgetIos().device_control_page()
        else:
            raise KeyError("The OS is wrong!")

        return device_control_page

    def device_page(self):
        if self.phone_os == "Android":
            device_page = MainPageWidgetAndroid().device_page()
        elif self.phone_os == "iOS":
            device_page = MainPageWidgetIos().device_page()
        else:
            raise KeyError("The OS is wrong!")

        return device_page

    def feedback_page(self):
        if self.phone_os == "Android":
            feedback_page = MainPageWidgetAndroid().feedback_page()
        elif self.phone_os == "iOS":
            feedback_page = MainPageWidgetIos().feedback_page()
        else:
            raise KeyError("The OS is wrong!")

        return feedback_page

    def find_password_page(self):
        if self.phone_os == "Android":
            find_password_page = MainPageWidgetAndroid().find_password_page()
        elif self.phone_os == "iOS":
            find_password_page = MainPageWidgetIos().find_password_page()
        else:
            raise KeyError("The OS is wrong!")

        return find_password_page

    def gender_page(self):
        if self.phone_os == "Android":
            gender_page = MainPageWidgetAndroid().gender_page()
        elif self.phone_os == "iOS":
            gender_page = MainPageWidgetIos().gender_page()
        else:
            raise KeyError("The OS is wrong!")

        return gender_page

    def god_page(self):
        if self.phone_os == "Android":
            god_page = MainPageWidgetAndroid().god_page()
        elif self.phone_os == "iOS":
            god_page = MainPageWidgetIos().god_page()
        else:
            raise KeyError("The OS is wrong!")

        return god_page

    def home_message_page(self):
        if self.phone_os == "Android":
            home_message_page = MainPageWidgetAndroid().home_message_page()
        elif self.phone_os == "iOS":
            home_message_page = MainPageWidgetIos().home_message_page()
        else:
            raise KeyError("The OS is wrong!")

        return home_message_page

    def login_page(self):
        if self.phone_os == "Android":
            login_page = MainPageWidgetAndroid().login_page()
        elif self.phone_os == "iOS":
            login_page = MainPageWidgetIos().login_page()
        else:
            raise KeyError("The OS is wrong!")

        return login_page

    def message_classify_page(self):
        if self.phone_os == "Android":
            message_classify_page = MainPageWidgetAndroid().message_classify_page()
        elif self.phone_os == "iOS":
            message_classify_page = MainPageWidgetIos().message_classify_page()
        else:
            raise KeyError("The OS is wrong!")

        return message_classify_page

    def message_setting_page(self):
        if self.phone_os == "Android":
            message_setting_page = MainPageWidgetAndroid().message_setting_page()
        elif self.phone_os == "iOS":
            message_setting_page = MainPageWidgetIos().message_setting_page()
        else:
            raise KeyError("The OS is wrong!")

        return message_setting_page

    def new_password_page(self):
        if self.phone_os == "Android":
            new_password_page = MainPageWidgetAndroid().new_password_page()
        elif self.phone_os == "iOS":
            new_password_page = MainPageWidgetIos().new_password_page()
        else:
            raise KeyError("The OS is wrong!")

        return new_password_page

    def personal_settings_page(self):
        if self.phone_os == "Android":
            personal_settings_page = MainPageWidgetAndroid().personal_settings_page()
        elif self.phone_os == "iOS":
            personal_settings_page = MainPageWidgetIos().personal_settings_page()
        else:
            raise KeyError("The OS is wrong!")

        return personal_settings_page

    def prepare_set_network_page(self):
        if self.phone_os == "Android":
            prepare_set_network_page = MainPageWidgetAndroid().prepare_set_network_page()
        elif self.phone_os == "iOS":
            prepare_set_network_page = MainPageWidgetIos().prepare_set_network_page()
        else:
            raise KeyError("The OS is wrong!")

        return prepare_set_network_page

    def protocol_page(self):
        if self.phone_os == "Android":
            protocol_page = MainPageWidgetAndroid().protocol_page()
        elif self.phone_os == "iOS":
            protocol_page = MainPageWidgetIos().protocol_page()
        else:
            raise KeyError("The OS is wrong!")

        return protocol_page

    def register_page(self):
        if self.phone_os == "Android":
            register_page = MainPageWidgetAndroid().register_page()
        elif self.phone_os == "iOS":
            register_page = MainPageWidgetIos().register_page()
        else:
            raise KeyError("The OS is wrong!")

        return register_page

    def scan_with_subscribe_page(self):
        if self.phone_os == "Android":
            scan_with_subscribe_page = MainPageWidgetAndroid().scan_with_subscribe_page()
        elif self.phone_os == "iOS":
            scan_with_subscribe_page = MainPageWidgetIos().scan_with_subscribe_page()
        else:
            raise KeyError("The OS is wrong!")

        return scan_with_subscribe_page

    def set_network_page(self):
        if self.phone_os == "Android":
            set_network_page = MainPageWidgetAndroid().set_network_page()
        elif self.phone_os == "iOS":
            set_network_page = MainPageWidgetIos().set_network_page()
        else:
            raise KeyError("The OS is wrong!")

        return set_network_page

    def theme_style_page(self):
        if self.phone_os == "Android":
            theme_style_page = MainPageWidgetAndroid().theme_style_page()
        elif self.phone_os == "iOS":
            theme_style_page = MainPageWidgetIos().theme_style_page()
        else:
            raise KeyError("The OS is wrong!")

        return theme_style_page

    def upgrade_page(self):
        if self.phone_os == "Android":
            upgrade_page = MainPageWidgetAndroid().upgrade_page()
        elif self.phone_os == "iOS":
            upgrade_page = MainPageWidgetIos().upgrade_page()
        else:
            raise KeyError("The OS is wrong!")

        return upgrade_page

    def view_pager_page(self):
        if self.phone_os == "Android":
            view_pager_page = MainPageWidgetAndroid().view_pager_page()
        elif self.phone_os == "iOS":
            view_pager_page = MainPageWidgetIos().view_pager_page()
        else:
            raise KeyError("The OS is wrong!")

        return view_pager_page

    def clear_activity_popup(self):
        if self.phone_os == "Android":
            clear_activity_popup = PopupWidgetAndroid().clear_activity_popup()
        elif self.phone_os == "iOS":
            clear_activity_popup = PopupWidgetIos().clear_activity_popup()
        else:
            raise KeyError("The OS is wrong!")

        return clear_activity_popup

    def clear_device_popup(self):
        if self.phone_os == "Android":
            clear_device_popup = PopupWidgetAndroid().clear_device_popup()
        elif self.phone_os == "iOS":
            clear_device_popup = PopupWidgetIos().clear_device_popup()
        else:
            raise KeyError("The OS is wrong!")

        return clear_device_popup

    def loading_popup(self):
        if self.phone_os == "Android":
            loading_popup = PopupWidgetAndroid().loading_popup()
        elif self.phone_os == "iOS":
            loading_popup = PopupWidgetIos().loading_popup()
        else:
            raise KeyError("The OS is wrong!")

        return loading_popup

    def login_popup(self):
        if self.phone_os == "Android":
            login_popup = PopupWidgetAndroid().login_popup()
        elif self.phone_os == "iOS":
            login_popup = PopupWidgetIos().login_popup()
        else:
            raise KeyError("The OS is wrong!")

        return login_popup

    def logout_popup(self):
        if self.phone_os == "Android":
            logout_popup = PopupWidgetAndroid().logout_popup()
        elif self.phone_os == "iOS":
            logout_popup = PopupWidgetIos().logout_popup()
        else:
            raise KeyError("The OS is wrong!")

        return logout_popup

    def terminate_add_device_popup(self):
        if self.phone_os == "Android":
            terminate_add_device_popup = PopupWidgetAndroid().terminate_add_device_popup()
        elif self.phone_os == "iOS":
            terminate_add_device_popup = PopupWidgetIos().terminate_add_device_popup()
        else:
            raise KeyError("The OS is wrong!")

        return terminate_add_device_popup

    def update_popup(self):
        if self.phone_os == "Android":
            update_popup = PopupWidgetAndroid().update_popup()
        elif self.phone_os == "iOS":
            update_popup = PopupWidgetIos().update_popup()
        else:
            raise KeyError("The OS is wrong!")

        return update_popup
