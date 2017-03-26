# coding:utf-8
import sys

sys.path.append("..")
from src.utils.Read_APP_Element import *
from src.testcase.common.App_init import *
from src.testcase.common.Widget_Check_Unit import *
from src.utils.Collect_Log import *
from src.testcase.case.wait_case import *

if __name__ == '__main__':
    print device
    open_app()
    Wait_Case()

    # logger.info("dafs")
