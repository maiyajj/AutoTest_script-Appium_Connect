# coding=utf-8
import src.testcase.GN_Y201S.WaitCase as gn_201s_wc
import src.testcase.GN_Y201J.WaitCase as gn_201j_wc
import src.testcase.GN_Y201H.WaitCase as gn_201h_wc
import src.testcase.GN_APP.WaitCase as gn_app_wc


class WaitCase(object):
    def __init__(self, device_list, device_name, m_queue):
        self.app = device_list[device_name]["app"]

        if self.app == "GN":
            gn_app_wc.WaitCase(device_list, device_name, m_queue)
        elif self.app == "JD":
            gn_201j_wc.WaitCase(device_list, device_name, m_queue)
        elif self.app == "AL":
            gn_201s_wc.WaitCase(device_list, device_name, m_queue)
        elif self.app == "HW":
            gn_201h_wc.WaitCase(device_list, device_name, m_queue)
        else:
            raise KeyError("%s:The App not support" % self.app)