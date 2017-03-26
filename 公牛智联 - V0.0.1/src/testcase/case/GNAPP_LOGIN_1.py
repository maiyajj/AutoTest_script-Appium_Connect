# coding:utf-8

from src.utils.Collect_Log import *
from src.utils.Read_APP_Element import *


def GNAPP_LOGIN_1():
    login_button = login_page["login_button"]
    print login_button
    print Widget_Check_Uint().wait_widget(login_button[1], login_button[0], 60, 1)
