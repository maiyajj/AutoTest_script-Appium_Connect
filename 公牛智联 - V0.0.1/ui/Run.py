# coding:utf-8
import sys

sys.path.append("..")
from src.utils.ReadConf import *
from src.utils.Launch_Appium_Services import *
from src.utils.Read_APP_Element import *
from src.testcase.common.App_init import *
from src.testcase.common.Widget_Check_Uint import *

if __name__ == '__main__':
    print device
    open_app()

    page_unit(id="com.iotbull.android.superapp:id/home_nav_btn_device")
