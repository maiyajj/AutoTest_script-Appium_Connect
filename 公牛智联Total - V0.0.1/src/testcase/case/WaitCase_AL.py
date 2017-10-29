# coding=utf-8
from src.testcase.case.ALAPP.INPUT_CASE.ALAppInputCase import *
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


class WaitCaseAL(object):
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
        LaunchAppAL(**self.device_info_list).init_app()

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
            self.write_report(ALAppCmp1)  # 431, FUT_CMP_不同型号手机是否能正常添加设备
            self.write_report(ALAppCrossTimer1)  # 519, FUT_CROSSTIMER_普通定时、循环定时、延时定时交叉设置后定时执行
            self.write_report(ALAppCycleTimer1)  # 470, FUT_CYCLETIMER_循环定时设置永久循环执行（1分钟开1分钟关）
            self.write_report(ALAppCycleTimer2)  # 471, FUT_CYCLETIMER_循环定时执行过程中手动切换设备状态
            self.write_report(ALAppCycleTimer3)  # 482, FUT_CYCLETIMER_循环定时5次
            self.write_report(ALAppCycleTimer4)  # 483, FUT_CYCLETIMER_循环定时1次
            self.write_report(ALAppDelayTimer1)  # 469, FUT_DELAYTIMER_延时定时一分钟开关
            self.write_report(ALAppDelayTimer2)  # 468, FUT_DELAYTIMER_延迟定时一小时开
            self.write_report(ALAppDelayTimer3)  # 466, FUT_DELAYTIMER_延迟定时5分钟开
            self.write_report(ALAppDelayTimer4)  # 465, FUT_DELAYTIMER_延时定时23小时59分钟开
            self.write_report(ALAppEem1)  # 559, FUT_EEM_峰谷电价设置
            self.write_report(ALAppEem2)  # 558, FUT_EEM_用电图表显示周期设置
            self.write_report(ALAppEem3)  # 551, FUT_EEM_电价设置验证（待定）
            self.write_report(ALAppEem4)  # 550, FUT_EEM_实时功率显示及精度检查
            self.write_report(ALAppLogin1)  # 0000, 阿里智能APP账号登录
            self.write_report(ALAppNormalTimer1)  # 517, FUT_NTIMER_冲突定时设置
            self.write_report(ALAppNormalTimer2)  # 515, FUT_NTIMER_单次定时关
            self.write_report(ALAppNormalTimer3)  # 513, FUT_NTIMER_单次定时开
            self.write_report(ALAppNormalTimer4)  # 512, FUT_NTIMER_单日循环定时
            self.write_report(ALAppNormalTimer5)  # 510, FUT_NTIMER_定时时间早于当前时间的永不循环定时设置
            self.write_report(ALAppNormalTimer6)  # 508, FUT_NTIMER_隔天普通定时
            self.write_report(ALAppNormalTimer7)  # 505, FUT_NTIMER_普通交叉定时
            self.write_report(ALAppNormalTimer8)  # 497, FUT_NTIMER_每日循环普通定时
            self.write_report(ALAppNormalTimer9)  # 494, FUT_NTIMER_普通定时最大组数设定
            self.write_report(ALAppNormalTimer10)  # 488, FUT_NTIMER_普通定时设置后手动改变设备状态
            self.write_report(ALAppNormalTimer11)  # 417, FUT_NTIMER_普通定时循环信息检查
            self.write_report(ALAppSmartLink1)  # 498, FUT_SMTLNK_app能正常添加设备_按分类查找
            self.write_report(ALAppSwitch1)  # 517, FUT_NTIMER_冲突定时设置
            self.write_report(ALAppTimerFish1)  # 442, FUT_MTIMER_FISH_鱼缸模式开启1分钟，关闭1分钟功能是否正常
            self.write_report(ALAppTimerFish2)  # 441, FUT_MTIMER_FISH_鱼缸模式开启1小时，关闭1小时功能是否正常
            self.write_report(ALAppTimerFish3)  # 440, FUT_MTIMER_FISH_鱼缸模式开启2分钟，关闭2分钟功能是否正常
            self.write_report(ALAppTimerFish4)  # 438, FUT_MTIMER_FISH_鱼缸模式开启23小时59分钟，关闭23小时59分钟功能是否正常
            self.write_report(ALAppTimerFish5)  # 436, FUT_MTIMER_FISH_鱼缸模式_循环1次
            self.write_report(ALAppTimerFish6)  # 435, FUT_MTIMER_FISH_鱼缸模式_循环2次
            self.write_report(ALAppTimerMos1)  # 461, FUT_MTIMER_MOS_电蚊香模式_延时功能（1min，2min，1h，23h59min，断电恢复）是否正常
            self.write_report(ALAppTimerOvp1)  # 459, FUT_MTIMER_OVP_充电保护模式_延时功能（1min，2min，1h，23h59min，断电恢复）是否正常
            self.write_report(ALAppTimerTime1)  # 450, FUT_MTIMER_TIME_当前时间在设定时间内模式时间执行
            self.write_report(ALAppTimerTime2)  # 446, FUT_MTIMER_TIME_模式定时每日循环
            self.write_report(ALAppTimerTime3)  # 445, FUT_MTIMER_TIME_模式定时每周日循环
            self.write_report(ALAppTimerTime4)  # 444, FUT_MTIMER_TIME_循环定时每周一循环
            self.write_report(ALAppTimerTime5)  # 443, FUT_MTIMER_TIME_模式定时状态下手动改变设备状态
            self.write_report(ALAppTimerTime6)  # 434, FUT_MTIMER_TIME_设定关闭时间早于开启时间的模式定时执行
            self.write_report(ALAppTimerTime7)  # 433, FUT_MTIMER_TIME_正常状态下模式定时

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
