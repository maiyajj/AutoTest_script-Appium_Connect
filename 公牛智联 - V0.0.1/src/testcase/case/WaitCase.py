# coding:utf-8
from CheckUI import *
from INPUT_CASE.GNAppForgetPassword import *
from INPUT_CASE.GNAppLogin import *
from INPUT_CASE.GNAppMessageClassify import *
from INPUT_CASE.GNAppPersonalSettings import *
from INPUT_CASE.GNAppRegister import *
from INPUT_CASE.GNAppDevicePage import *
from data.Database import *


class WaitCase(object):
    def __init__(self):
        os.remove(r"../log/" + database["log_name"])
        os.remove(r"../report/Report.log")
        logger.info("*" * 30)
        logger.info(u"[APP_INF]deviceName：.....%s" % device.values()[0]['deviceName'])
        logger.info(u"[APP_INF]UDID：...........%s" % device.values()[0]['udid'])
        logger.info(u"[APP_INF]platformName：...%s" % device.values()[0]['platformName'])
        logger.info(u"[APP_INF]platformVersion：%s" % device.values()[0]['platformVersion'])
        logger.info(u"[APP_INF]appPackage：.....%s" % conf_App["GN"][0])
        logger.info(u"[APP_INF]appActivity：....%s" % conf_App["GN"][1])
        logger.info("*" * 30)
        self.No = 1
        while True:
            logger.info("run times [%s]" % database["program_loop_time"])
            # CheckUI()
            write_report.info(self.report_data(GNAppLogin1().result()))
            self.No += 1
            GNAppLogin1()
            GNAppLogin2()
            GNAppLogin3()
            GNAppPersonalSettings1()
            GNAppPersonalSettings2()
            GNAppPersonalSettings3()
            GNAppPersonalSettings4()
            GNAppRegister1()
            GNAppForgetPassword1()
            GNAppMessageClassify1()

            database["program_loop_time"] += 1

    def report_data(self, case):
        CASE = case
        data = u'[RUN_TIMES=%s, No=%s, CASE_TITLE="%s", RESULT=%s, TIME=%s]' % \
               (database["program_loop_time"], self.No, CASE[1], CASE[0], time.strftime("%Y-%m-%d %H:%M:%S"))
        return data
