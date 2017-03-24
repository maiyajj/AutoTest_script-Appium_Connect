# coding:utf-8
import sys

sys.path.append("..")
from src.utils.Read_APP_Element import *
from src.testcase.common.App_init import *
from src.testcase.common.Widget_Check_Uint import *
from src.utils.Collect_Log import *

if __name__ == '__main__':
    print device
    open_app()
    login_button = login_page["login_button"]
    Widget_Check_Uint().popups_unit(locate=login_button[1], key=login_button[0])
    # logger.info("dafs")
