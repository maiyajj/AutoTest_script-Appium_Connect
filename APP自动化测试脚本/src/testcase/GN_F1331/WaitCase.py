# coding=utf-8
import json
import threading

from src.testcase.GN_F1331.input_case.GN_F1331_Input_Case import *
from src.testcase.GN_F1331.page.ReadAPPElement import *
from src.utils.Debug import *
from src.utils.GetSerial import *
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
        self.xls = None  # 初始化执行结果Excel文件模块
        self.debug = None  # 初始化debug日志模块
        self.page = None  # 初始化元素库模块
        self.device_info_list = {}  # 初始化设备信息
        self.row = 0  # Excel报告写入初始位置
        self.device_name = self.device_info["udid"]  # 设备名称
        self.app = self.device_info["app"]  # APP型号
        self.serial_port = int(conf["phone_name"][self.device_name]["serial_port"])
        self.serial_com = conf["phone_name"][self.device_name]["serial_com"]

        self.sc = ShellCommand()  # 实例化ShellCommand
        self.device_info["sc"] = self.sc
        database[device_name] = {}  # 初始化设备数据库
        database["case_location"] = 1  # 用例执行次数
        self.receive_serial = ReceiveSerial(self.serial_com, self.serial_port)

        self.serial_receive_t = threading.Thread(target=self.launch_receive_serial)
        self.serial_command_t = threading.Thread(target=self.receive_serial_command)

        self.serial_command_queue = Queue.Queue()
        self.serial_result_queue = Queue.Queue()
        self.device_info["serial_command_queue"] = self.serial_command_queue
        self.device_info["serial_result_queue"] = self.serial_result_queue

        try:
            self.create_debug()
            self.serial_receive_t.start()
            self.serial_command_t.start()
            self.create_report()
            self.write_xls()
            self.select_page_element()
            self.check_appium()

            self.run()
        except BaseException:
            self.debug.error(traceback.format_exc())
            self.receive_serial.serial_sever.close()
            self.serial_receive_t.join()
            self.serial_command_t.join()
            raise ScriptInitError("Script Init Error!!!")

    # 从元素库筛选对应APP元素库
    def select_page_element(self):
        self.page = PageElement(self.device_info["platformName"]).get_page_element()
        self.device_info["page"] = self.page

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
                self.debug.info("Appium Sever Launch Success! %s" % time.strftime("%Y-%m-%d %X"))
                break

    # 接收设备串口log
    def launch_receive_serial(self):
        self.receive_serial.receive_log()

    def receive_serial_command(self):
        self.serial_command_queue.put_nowait((False, "", ""))
        self.receive_serial.start_stop_filtrate_data(self.serial_command_queue)

    # 开始执行用例
    def run(self):
        # 填写设备信息日志
        self.debug.info("*" * 30)
        self.debug.info(u"[APP_INF]deviceName：.....%s" % self.device_info["deviceName"])
        self.debug.info(u"[APP_INF]UDID：...........%s" % self.device_info["udid"])
        self.debug.info(u"[APP_INF]platformName：...%s" % self.device_info["platformName"])
        self.debug.info(u"[APP_INF]platformVersion：%s" % self.device_info["platformVersion"])

        # self.debug.info(u"[APP_INF]appPackage：.....%s" % self.device_info["desired_caps"]["appPackage"])
        # self.debug.info(u"[APP_INF]appActivity：....%s" % self.device_info["desired_caps"]["appActivity"])
        # self.debug.info(u"[APP_INF]waitActivity：...%s" % self.device_info["desired_caps"]["waitActivity"])
        # self.debug.info(u"[APP_INF]bundleId：.......%s" % self.device_info["desired_caps"]["bundleId"])
        # self.debug.info("******************************")
        for name, blank in [["appPackage", 5], ["appActivity", 4], ["waitActivity", 3], ["bundleId", 7]]:
            try:
                self.debug.info(u"[APP_INF]%s：%s%s" % (name, "." * blank, self.device_info["desired_caps"][name]))
            except KeyError:
                pass
        self.debug.info("*" * 30)

        # 执行用例
        while True:
            self.debug.info("run times [%s]" % database["program_loop_time"])
            # self.write_report(GNF1331NormalTimer1)  # 1216, 上层循环定时
            # self.write_report(GNF1331NormalTimer2)  # 1216, 上、中层循环定时
            # self.write_report(GNF1331NormalTimer3)  # 1216, 上、中、下层循环定时
            # self.write_report(GNF1331NormalTimer4)  # 1216, 上层延迟定时
            # self.write_report(GNF1331NormalTimer5)  # 1216, 上、中层延迟定时
            # self.write_report(GNF1331NormalTimer6)  # 1216, 上、中、下层延迟定时
            # self.write_report(GNF1331NormalTimer7)  # 1216, 上层普通定时
            self.write_report(GNF1331NormalTimer8)  # 1216, 上、中层普通定时
            # self.write_report(GNF1331NormalTimer9)  # 1216, 上、中、下层普通定时
            # self.write_report(GNF1331NormalTimer10)  # 1216, 上层延迟、中层循环定时、下层普通定时开、关

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
            xls_datas = database[self.device_name]
            xls_data = xls_datas[zentao_id]
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
