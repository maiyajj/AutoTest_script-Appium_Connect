# coding:utf-8
from data.Database import *
from GNAppLogin import *
from GNAppPersonalSettings import *
from CheckUI import *


class WaitCase(object):
    def __init__(self):
        os.remove(r"../log/"+database["log_name"])
        logger.info("*" * 30)
        logger.info(u"[APP_INF]deviceName：.....%s" % device.values()[0]['deviceName'])
        logger.info(u"[APP_INF]UDID：...........%s" % device.values()[0]['udid'])
        logger.info(u"[APP_INF]platformName：...%s" % device.values()[0]['platformName'])
        logger.info(u"[APP_INF]platformVersion：%s" % device.values()[0]['platformVersion'])
        logger.info(u"[APP_INF]appPackage：.....%s" % conf_App["GN"][0])
        logger.info(u"[APP_INF]appActivity：....%s" % conf_App["GN"][1])
        logger.info("*" * 30)
        while True:
            logger.info("run times [%s]" % database["program_loop_time"])
            # CheckUI()
            # GNAppLogin1()
            # GNAppLogin2()
            # GNAppLogin3()
            GNAppPersonalSettings1()
            database["program_loop_time"] += 1
