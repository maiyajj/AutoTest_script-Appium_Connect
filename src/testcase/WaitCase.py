# coding=utf-8
import traceback

import src.testcase.GN_APP.WaitCase as gn_app_wc
import src.testcase.GN_F1331.WaitCase as gn_f1331_wc
import src.testcase.GN_Y201H.WaitCase as gn_201h_wc
import src.testcase.GN_Y201J.WaitCase as gn_201j_wc
import src.testcase.GN_Y201S.WaitCase as gn_201s_wc


class WaitCase(object):
    def __init__(self, device_list, device_name, m_queue):
        app = device_list[device_name]["app"].upper()
        app_list = {"GN_APP": gn_app_wc.WaitCase,
                    "GN_201S": gn_201s_wc.WaitCase,
                    "GN_201J": gn_201j_wc.WaitCase,
                    "GN_201H": gn_201h_wc.WaitCase,
                    "GN_F1331": gn_f1331_wc.WaitCase}
        try:
            app_list[app](device_list, device_name, m_queue)
        except BaseException:
            print(traceback.format_exc())
            exit(-1)
