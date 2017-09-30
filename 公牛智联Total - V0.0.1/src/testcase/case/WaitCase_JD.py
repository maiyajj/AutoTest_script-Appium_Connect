# coding=utf-8
from src.testcase.case.JDAPP.INPUT_CASE.JDAppInputCase import *
from src.utils.CollectLog import *
from src.utils.Debug import *
from src.utils.OutputReport import *
from src.utils.ReadAPPElement import *
from src.utils.WriteXls import *


class ScriptInitError(Exception):
    def __init__(self, value=None):
        self.value = value

    def __str__(self):
        return repr(self.value)


class WaitCaseJD(object):
    def __init__(self, device_list, device_name):
        self.device_list = device_list
        self.device_name = device_name
        self.device_info = device_list[device_name]
        self.app = self.device_info["app"]

        self.report = None
        self.logger = None
        self.xls = None
        self.debug = None
        self.script_init_success = False
        self.No = 1
        self.row = 12

        self.sc = ShellCommand()
        database[device_name] = {}

        try:
            self.create_debug()
            self.create_log()
            self.create_report()
            self.write_xls()
            self.select_page_element()
            self.check_appium()
            self.init_app()
            self.script_init_success = True
        except BaseException:
            self.debug.error(traceback.format_exc())
            raise
        if self.script_init_success is True:
            self.run()
        else:
            raise ScriptInitError("Script Init Error!!! "
                                  "contain [create_debug(), create_log(), "
                                  "create_report(), write_xls(), check_appium()]")

    def select_page_element(self):
        PageElement(self.device_list, self.device_info["platformName"], self.device_info["app"]).wrapper()
        self.page_element = self.device_list["page"]

    def create_log(self):
        check_log(self.device_list, self.device_name)
        self.logger = self.device_info["logger"]

    def create_report(self):
        check_report(self.device_list, self.device_name)
        self.report = self.device_info["report"]

    def create_debug(self):
        check_debug(self.device_list, self.device_name)
        self.debug = self.device_info["debug"]

    def write_xls(self):
        self.xls = WriteXls(self.device_list, self.device_name)

    def init_app(self):
        self.device_info_list = {"device_info": self.device_info,
                                 "page_element": self.page_element,
                                 "logger": self.logger,
                                 "app": self.app,
                                 "sc": self.sc}
        LaunchAppJD(**self.device_info_list).init_app()

    def check_appium(self):
        while True:
            try:
                self.sc.find_proc_and_pid_by_port(self.device_info["port"])[0]
            except IndexError:
                time.sleep(1)
            else:
                self.logger.info("Appium Sever Launch Success! %s" % time.strftime("%Y-%m-%d %H:%M:%S"))
                break

    def run(self):
        self.logger.info("*" * 30)
        self.logger.info(u"[APP_INF]deviceName：.....%s" % self.device_info["deviceName"])
        self.logger.info(u"[APP_INF]UDID：...........%s" % self.device_info["udid"])
        self.logger.info(u"[APP_INF]platformName：...%s" % self.device_info["platformName"])
        self.logger.info(u"[APP_INF]platformVersion：%s" % self.device_info["platformVersion"])
        for i in [["appPackage", 5], ["appActivity", 4], ["waitActivity", 3], ["bundleId", 7]]:
            try:
                self.logger.info(u"[APP_INF]%s：%s%s" % (i[0], "." * i[1], self.device_info["desired_caps"][i[0]]))
            except KeyError:
                pass
        # self.logger.info(u"[APP_INF]appPackage：.....%s" % self.device_info["desired_caps"]["appPackage"])
        # self.logger.info(u"[APP_INF]appActivity：....%s" % self.device_info["desired_caps"]["appActivity"])
        # self.logger.info(u"[APP_INF]waitActivity：...%s" % self.device_info["desired_caps"]["waitActivity"])
        # self.logger.info(u"[APP_INF]bundleId：.......%s" % self.device_info["desired_caps"]["bundleId"])
        self.logger.info("*" * 30)
        database["case_location"] = self.No
        while True:
            self.logger.info("run times [%s]" % database["program_loop_time"])
            # self.write_report(JDAppLogin1)  # 0000, 京东微联APP账号登录
            # self.write_report(JDAppCompatibility1)  # 1272, 在TP-link品牌的路由器下添加设备检查
            # self.write_report(JDAppElectricityMeter1)  # 1117, 电量统计2H功能及精度检查
            # self.write_report(JDAppElectricityMeter2)  # 1138, 单一电价验证
            # self.write_report(JDAppElectricityMeter3)  # 1307, 启动鱼缸模式定时，APP中开关状态检查
            # self.write_report(JDAppElectricityMeter4)  # 1307, 启动鱼缸模式定时，APP中开关状态检查
            # self.write_report(JDAppElectricityMeter5)  # 1307, 启动鱼缸模式定时，APP中开关状态检查
            # self.write_report(JDAppElectricityMeter6)  # 1307, 启动鱼缸模式定时，APP中开关状态检查
            # self.write_report(JDAppElectricityMeter7)  # 1307, 启动鱼缸模式定时，APP中开关状态检查
            # self.write_report(JDAppAppFunction1)  # 1170, 定时记录删除是否成功
            # self.write_report(JDAppAppFunction2)  # 1307, 启动鱼缸模式定时，APP中开关状态检查
            # self.write_report(JDAppKeyMemory1)  # 1216, 开关操作及记忆功能
            # self.write_report(JDAppModeTimer1)  # 1601, 热水器模式下设定的关闭时间早于开启时间的定时是否正确执行
            # self.write_report(JDAppModeTimer2)  # 1064, 热水器模式下当前时间在设定时间内的定时是否正确执行
            self.write_report(JDAppModeTimer3)  # 1086, 充电保护模式下延时关闭1分钟
            # self.write_report(JDAppModeTimer4)  # 1103, 鱼缸模式开启1分钟，关闭1分钟定时是否正确执行
            # self.write_report(JDAppModeTimer5)  # 1105, 鱼缸模式开启1小时，关闭1小时定时是否正确执行
            self.write_report(JDAppModeTimer6)  # 1108, 鱼缸模式开启2分钟，关闭2分钟定时是否正确执行
            self.write_report(JDAppNormalTimer1)  # 1181, 普通交叉定时_8分钟
            self.write_report(JDAppNormalTimer2)  # 1184, 单次定时开_2分钟
            self.write_report(JDAppNormalTimer3)  # 1185, 单次定时关_2分钟
            self.write_report(JDAppOverDay1)  # 1299, 热水器模式设置每日循环
            # self.write_report(JDAppOverDay2)  # 1300, 热水器模式在跨天循环下的跨天执行
            # self.write_report(JDAppOverDay3)  # 1301, 定时时间早于当前时间的永不循环定时设置
            self.write_report(JDAppOverDay4)  # 1302, 隔天普通定时
            self.write_report(JDAppOverDay5)  # 1304, 每日循环普通定时
            # self.write_report(JDAppOverDay6)  # 1305, 鱼缸模式开启23小时59分钟，关闭23小时59分钟定时是否正确执行
            # self.write_report(JDAppOverDay7)  # 1306, 充电保护模式下延迟23h59min关闭

            database["program_loop_time"] += 1
            ports = [self.device_info["port"], self.device_info["bp_port"], self.device_info["wda_port"]]
            for port in ports:
                try:
                    pid = self.sc.find_proc_and_pid_by_port(port)[1]
                    self.sc.kill_proc_by_pid(pid)
                except IndexError:
                    pass

    def write_report(self, case_name):
        try:
            case = case_name(**self.device_info_list).run()
            end_time = time.strftime("%Y-%m-%d %H:%M:%S")
            zentao_id = case[1]
            data = u'[ZENTAO_ID=%s, RESULT=%s,%s CASE_NAME="%s", RUN_TIMES=%s, CASE_ID=%s, START=%s, CLOSE=%s]' % \
                   (zentao_id, case[0], " " * (7 - len(case[0])), case[2], database["program_loop_time"],
                    self.No, case[3], end_time)
            self.report.info(data)
            xls_data = database[self.device_name]
            xls_data[zentao_id]["end_time"] = end_time
            if "row" in xls_data[zentao_id].keys():
                pass
            else:
                xls_data[zentao_id]["row"] = self.row
                self.row += 1
            self.debug.info("row:%s" % xls_data[zentao_id]["row"])
            self.xls.write_data(xls_data[zentao_id]["row"],
                                xls_data[zentao_id]["ZenTao"],
                                xls_data[zentao_id]["case_title"],
                                xls_data[zentao_id]["end_time"],
                                xls_data[zentao_id]["test_count"],
                                xls_data[zentao_id]["test_pass"],
                                xls_data[zentao_id]["test_fail"],
                                xls_data[zentao_id]["test_error"],
                                xls_data[zentao_id]["test_wait"])

            self.debug.info("write_data:%s" % case[0])
            self.No += 1
            database["case_location"] = self.No
        except BaseException:
            self.debug.error(traceback.format_exc())
