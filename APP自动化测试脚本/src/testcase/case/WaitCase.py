# coding=utf-8
from src.testcase.case.WaitCase_AL import *
from src.testcase.case.WaitCase_GN import *
from src.testcase.case.WaitCase_HW import *
from src.testcase.case.WaitCase_JD import *


class WaitCase(object):
    def __init__(self, device_list, device_name, m_queue):
        self.app = device_list[device_name]["app"]

        if self.app == "GN":
            WaitCaseGN(device_list, device_name, m_queue)
        elif self.app == "JD":
            WaitCaseJD(device_list, device_name, m_queue)
        elif self.app == "AL":
            WaitCaseAL(device_list, device_name, m_queue)
        elif self.app == "HW":
            WaitCaseHW(device_list, device_name, m_queue)
        else:
            raise KeyError("%s:The App not support" % self.app)
