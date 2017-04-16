# coding:utf-8
from data.Database import *
from src.testcase.case.INPUT_CASE.GNAppAccountSettings import *
from src.testcase.case.INPUT_CASE.GNAppDevicePage import *
from src.testcase.case.INPUT_CASE.GNAppFeedBack import *
from src.testcase.case.INPUT_CASE.GNAppForgetPassword import *
from src.testcase.case.INPUT_CASE.GNAppLogin import *
from src.testcase.case.INPUT_CASE.GNAppMessageClassify import *
from src.testcase.case.INPUT_CASE.GNAppRegister import *
from src.testcase.case.INPUT_CASE.GNAppUsingHelp import *
from src.testcase.case.INPUT_CASE.GNAppVersion import *
from src.testcase.suite.ScanCaseName import *


class WaitCase(object):
    def __init__(self):
        os.remove(r"./log/" + database["log_name"])
        os.remove(r"./report/Report.log")
        logger.info("*" * 30)
        logger.info(u"[APP_INF]deviceName：.....%s" % device.values()[0]["deviceName"])
        logger.info(u"[APP_INF]UDID：...........%s" % device.values()[0]["udid"])
        logger.info(u"[APP_INF]platformName：...%s" % device.values()[0]["platformName"])
        logger.info(u"[APP_INF]platformVersion：%s" % device.values()[0]["platformVersion"])
        logger.info(u"[APP_INF]appPackage：.....%s" % conf_App["GN"][0])
        logger.info(u"[APP_INF]appActivity：....%s" % conf_App["GN"][1])
        logger.info("*" * 30)
        self.No = 1
        database["case_location"] = self.No
        while True:
            logger.info("run times [%s]" % database["program_loop_time"])
            # CheckUI()
            # self.write_report(GNAppLogin1)
            # self.write_report(GNAppLogin2)
            # self.write_report(GNAppLogin3)
            # self.write_report(GNAppLogin4)
            # self.write_report(GNAppLogin5)
            # self.write_report(GNAppLogin6)
            self.write_report(GNAppLogin7)
            # self.write_report(GNAppAccountSettings1)
            # self.write_report(GNAppAccountSettings2)
            # self.write_report(GNAppAccountSettings3)
            # self.write_report(GNAppAccountSettings4)
            # self.write_report(GNAppAccountSettings5)
            # self.write_report(GNAppAccountSettings6)
            # self.write_report(GNAppAccountSettings7)
            # self.write_report(GNAppAccountSettings8)
            # self.write_report(GNAppAccountSettings9)
            # self.write_report(GNAppRegister1)
            # self.write_report(GNAppForgetPassword1)
            # self.write_report(GNAppMessageClassify1)
            # self.write_report(GNAppDevicePage1)
            # self.write_report(GNAppDevicePage2)
            # self.write_report(GNAppDevicePage3)
            # self.write_report(GNAppDevicePage4)
            # self.write_report(GNAppDevicePage5)
            # self.write_report(GNAppDevicePage6)
            # self.write_report(GNAppFeedBack1)
            # self.write_report(GNAppUsingHelp1)
            # self.write_report(GNAppVersion1)

            database["program_loop_time"] += 1

    def write_report(self, case_name):
        case = case_name().result()
        data = u'[RUN_TIMES=%s, CASE_ID=%s, CASE_NAME="%s", RESULT=%s, TIME=%s]' % \
               (database["program_loop_time"], self.No, case[1], case[0], time.strftime("%Y-%m-%d %H:%M:%S"))
        report.info(data)
        self.No += 1
        database["case_location"] = self.No
