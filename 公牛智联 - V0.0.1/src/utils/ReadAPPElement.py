# coding:utf-8
from src.testcase.page.AppPageElement import *

view_pager_page = MainPageWidget().view_pager_page()
login_page = MainPageWidget().login_page()
find_password_page = MainPageWidget().find_password_page()
register_page = MainPageWidget().register_page()
protocol_page = MainPageWidget().protocol_page()
devices_page = MainPageWidget().devices_page()
personal_settings_page = MainPageWidget().personal_settings_page()
account_setting_page = MainPageWidget().account_setting_page()
change_nickname_page = MainPageWidget().change_nickname_page()
gender_page = MainPageWidget().gender_page()
change_pwd_page = MainPageWidget().change_pwd_page()
feedback_page = MainPageWidget().feedback_page()
device_page = MainPageWidget().device_page()

update_popup = PopupWidget().update_popup()
login_popup = PopupWidget().login_popup()
quit_popup = PopupWidget().quit_popup()