# coding=utf-8
import json

from src.testcase.GN_Y201H.case.INPUT_CASE.GN_Y201H_Input_Case import *
from src.testcase.GN_Y201H.page.ReadAPPElement import *
from src.utils.CollectLog import *
from src.utils.Debug import *
from src.utils.OutputReport import *
from src.utils.WriteXls import *


class ScriptInitError(Exception):
    def __init__(self, value=None):
        self.value = value

    def __str__(self):
        return repr(self.value)


class WaitCase(object):
    def __init__(self, device_list, device_name, m_queue):
        self.device_list = device_list  # 设备列表
        self.device_name = device_name  # 设备名称
        self.device_info = device_list[device_name]  # 设备信息表
        database["m_queue"] = m_queue  # 用于主进程和子进程通讯的消息队列

        self.report = None  # 初始化结果报告模块
        self.logger = None  # 初始化log日志模块
        self.xls = None  # 初始化执行结果Excel文件模块
        self.debug = None  # 初始化debug日志模块
        self.page = None  # 初始化元素库模块
        self.device_info_list = {}  # 初始化设备信息
        self.script_init_success = False  # 脚本初始化结果标志位
        database["case_location"] = 1  # 用例执行次数
        self.row = 0  # Excel报告写入初始位置

        self.sc = ShellCommand()  # 实例化ShellCommand
        self.device_info["sc"] = self.sc
        database[device_name] = {}  # 初始化设备数据库

        try:
            self.create_debug()
            self.create_log()
            self.create_report()
            self.write_xls()
            self.select_page_element()
            self.check_appium()
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

    # 从元素库筛选对应APP元素库
    def select_page_element(self):
        self.page = PageElement(self.device_info["app"])
        self.device_info["page"] = self.page

    # 生成log日志
    def create_log(self):
        self.logger = check_log(self.device_info)
        self.device_info["logger"] = self.logger

    # 生成log格式运行结果
    def create_report(self):
        self.report = check_report(self.device_info)
        self.device_info["report"] = self.report

    # 生成debug日志
    def create_debug(self):
        self.debug = check_debug(self.device_info)
        self.device_info["debug"] = self.debug

    # 实例化Excel文件
    def write_xls(self):
        self.xls = WriteXls(self.device_info)

    # 检查Appium服务是否启动
    def check_appium(self):
        while True:
            try:
                self.sc.find_proc_and_pid_by_port(self.device_info["port"])[0]
            except IndexError:
                time.sleep(1)
            else:
                self.logger.info("Appium Sever Launch Success! %s" % time.strftime("%Y-%m-%d %X"))
                break

    # 开始执行用例
    def run(self):
        # 填写设备信息日志
        self.logger.info("*" * 30)
        self.logger.info(u"[APP_INF]deviceName：.....%s" % self.device_info["deviceName"])
        self.logger.info(u"[APP_INF]UDID：...........%s" % self.device_info["udid"])
        self.logger.info(u"[APP_INF]platformName：...%s" % self.device_info["platformName"])
        self.logger.info(u"[APP_INF]platformVersion：%s" % self.device_info["platformVersion"])

        # self.logger.info(u"[APP_INF]appPackage：.....%s" % self.device_info["desired_caps"]["appPackage"])
        # self.logger.info(u"[APP_INF]appActivity：....%s" % self.device_info["desired_caps"]["appActivity"])
        # self.logger.info(u"[APP_INF]waitActivity：...%s" % self.device_info["desired_caps"]["waitActivity"])
        # self.logger.info(u"[APP_INF]bundleId：.......%s" % self.device_info["desired_caps"]["bundleId"])
        # self.logger.info("******************************")
        for name, blank in [["appPackage", 5], ["appActivity", 4], ["waitActivity", 3], ["bundleId", 7]]:
            try:
                self.logger.info(u"[APP_INF]%s：%s%s" % (name, "." * blank, self.device_info["desired_caps"][name]))
            except KeyError:
                pass
        self.logger.info("*" * 30)

        # 执行用例
        while True:
            self.logger.info("run times [%s]" % database["program_loop_time"])
            self.write_report(GNY201HControl1)  # 2106, 在线状态，频繁开关操作后，状态检查
            self.write_report(GNY201HControl2)  # 2105, 在线状态，开关操作后，状态检查
            self.write_report(GNY201HDelayTimer1)  # 2100, 延时定时设置后，改变设备状态后查看延时定时的执行状态
            self.write_report(GNY201HDelayTimer2)  # 2099, 在线状态，1组单关的延时定时执行状态检查
            self.write_report(GNY201HDelayTimer3)  # 2098, 在线状态，1组单开的延时定时执行状态检查
            # self.write_report(GNY201HNormalTimer1)  # 2079, 在线状态，临界点1组开与1组关的定时执行状态检查
            # self.write_report(GNY201HNormalTimer2)  # 2064, 在线状态，4组开与4组关按自定义方式执行的定时执行状态检查
            # self.write_report(GNY201HNormalTimer3)  # 2063, 在线状态，4组开与4组关按周末方式执行的定时执行状态检查
            # self.write_report(GNY201HNormalTimer4)  # 2062, 在线状态，4组开与4组关按工作日方式执行的定时执行状态检查
            self.write_report(GNY201HNormalTimer5)  # 2061, 在线状态，4组开与4组关单次执行的定时执行状态检查
            # self.write_report(GNY201HNormalTimer6)  # 2060, 在线状态，1组开与1组关按自定义方式执行的定时执行状态检查
            # self.write_report(GNY201HNormalTimer7)  # 2059, 在线状态，1组开与1组关按周末执行的定时执行状态检查
            # self.write_report(GNY201HNormalTimer8)  # 2058, 在线状态，1组开与1组关按工作日执行的定时执行状态检查
            # self.write_report(GNY201HNormalTimer9)  # 2057, 在线状态，临界点1组开与1组关的定时执行状态检查
            self.write_report(GNY201HNormalTimer10)  # 2056, 在线状态，1组开与1组关定时执行状态检查
            self.write_report(GNY201HNormalTimer11)  # 2055, 在线状态，1组单关定时执行状态检查
            self.write_report(GNY201HNormalTimer12)  # 2054, 在线状态，1组单开定时执行状态检查
            self.write_report(GNY201HOtherFunc1)  # 2088, APP查看信息功能
            # self.write_report(GNY201HSmartLink1)  # 2048, 设备首次配网操作检查
            self.write_report(GNY201HTimerFunc1)  # 2023, 延时定时的定时数量检查
            self.write_report(GNY201HTimerFunc2)  # 2022, 普通定时的定时数量检查
            self.write_report(GNY201HTimerFunc3)  # 2020, 普通定时周期格式检查

            database["program_loop_time"] += 1

    # 输出报告
    def write_report(self, case_name):
        try:
            case = case_name(self.device_info).run()

            end_time = time.strftime("%Y-%m-%d %X")
            d = (u'[ZENTAO_ID=%s, RESULT=%s CASE_TITLE="%s", RUN_TIMES=%s, CASE_ID=%s, START=%s, CLOSE=%s]' % (
                case[0], case[1], case[2], database["program_loop_time"], database["case_location"], case[3], end_time))
            self.report.info(d)

            zentao_id = case[0]
            xls_data = database[self.device_name]
            xls_data = xls_data[zentao_id]
            xls_data["end_time"] = end_time
            xls_data["row"] = database["case_row"][zentao_id]
            xls_data["run"] = "Y"
            self.debug.info("row: %s" % xls_data["row"])
            self.xls.write_data(xls_data["row"],
                                xls_data["ZenTao"],
                                xls_data["case_title"],
                                xls_data["end_time"],
                                xls_data["run"],
                                xls_data["test_count"],
                                xls_data["test_pass"],
                                xls_data["test_fail"],
                                xls_data["test_error"],
                                xls_data["test_wait"])
            # 列表中的中文能以汉字的形式写入日志中
            self.debug.info("write_data: %s" % json.dumps(xls_data, encoding='UTF-8', ensure_ascii=False))
            database["case_location"] += 1
        except BaseException:
            self.debug.error(traceback.format_exc())
