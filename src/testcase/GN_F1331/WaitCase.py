# coding=utf-8
import json
import multiprocessing

from src.testcase.GN_F1331.input_case.GN_F1331_Input_Case import *
from src.testcase.GN_F1331.page.ReadAPPElement import *
from src.utils.Debug import *
from src.utils.GetSerial import *
from src.utils.OutputReport import *
from src.utils.SendMail import *
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
        self.m_queue = m_queue  # 用于主进程和子进程通讯的消息队列
        database["m_queue"] = m_queue

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
        self.receive_serial = ReceiveSerial()

        self.serial_command_queue = multiprocessing.Queue()
        self.serial_result_queue = multiprocessing.Queue()
        self.device_info["serial_command_queue"] = self.serial_command_queue
        self.device_info["serial_result_queue"] = self.serial_result_queue

        self.serial_command_queue.put_nowait((False, ""))
        # 接收设备串口log
        alive = multiprocessing.Value('b', True)
        self.serial_receive_t = multiprocessing.Process(target=self.receive_serial.start_stop_filtrate_data, args=(
            self.serial_com, self.serial_port, self.serial_command_queue, self.serial_result_queue, alive))

        try:
            self.create_debug()
            self.serial_receive_t.start()
            self.create_report()
            self.write_xls()
            self.select_page_element()
            self.check_appium()

            self.run()
            alive.value = False
            # self.serial_receive_t.terminate()
            # self.serial_receive_t.join()
        except BaseException:
            self.debug.error(traceback.format_exc())
            self.serial_receive_t.join()
            os._exit(-1)

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
        times = 1
        while times:
            self.debug.info("run times [%s]" % database["program_loop_time"])
            self.write_report(GNF1331AppInfomation1)  # 007, 设备详细界面，信息检测
            self.write_report(GNF1331DeviceInfo1)  # 1170, 设置记忆模式
            # self.write_report(GNF1331DeviceInfo2)  # 1307, 启动鱼缸模式定时，APP中开关状态检查
            self.write_report(GNF1331KeyMemory1)  # 194, 手机APP远程频繁操作总开关，设备状态检查
            self.write_report(GNF1331KeyMemory2)  # 193, 手机APP远程总开关功能检查
            self.write_report(GNF1331KeyMemory3)  # 192, 手机APP远程频繁操作分层开关，设备状态检查
            self.write_report(GNF1331KeyMemory4)  # 191, 手机APP远程分层开关功能检查
            self.write_report(GNF1331Timer1)  # 142, 设备设置多模式多定时同层，设备执行检查
            self.write_report(GNF1331Timer2)  # 141, 设备设置多模式多定时不同层，设备执行状态检查
            self.write_report(GNF1331Timer3)  # 140, 设备连接大功率设备，定时执行状态检查
            self.write_report(GNF1331Timer4)  # 139, 设备当前状态和循环定时输出状态相同，循环定时执行状态检查
            self.write_report(GNF1331Timer5)  # 134, 在线状态，多层循环定时执行状态检查
            self.write_report(GNF1331Timer6)  # 131, 在线状态，单层多次循环定时执行状态检查
            self.write_report(GNF1331Timer7)  # 130, 在线状态，单层单次循环定时执行状态检查
            self.write_report(GNF1331Timer8)  # 121, 设备当前状态和延时定时输出状态相同，延时定时执行状态检查
            self.write_report(GNF1331Timer9)  # 116, 在线状态，各层定时单关延时定时执行状态检查
            self.write_report(GNF1331Timer10)  # 114, 在线状态，单层定时单关延时定时执行状态检查
            self.write_report(GNF1331Timer11)  # 111, 设备当前状态和普通定时输出状态相同，定时执行状态检查
            self.write_report(GNF1331Timer12)  # 106, 在线状态，定时设置时选择执行均不通知，定时执行成功，检查APP是否通知
            self.write_report(GNF1331Timer13)  # 101, 随机各层设置9组普通定时，执行完成后删除原有定时，再次设置9组普通定时
            # self.write_report(GNF1331Timer14)  # 97, 在线状态，随机各层设置9组普通定时，周末执行的定时执行状态检查
            # self.write_report(GNF1331Timer15)  # 96, 在线状态，随机各层设置9组普通定时，工作日执行的定时执行状态检查
            # self.write_report(GNF1331Timer16)  # 95, 在线状态，随机各层设置9组普通定时，单次执行的定时执行状态检查
            # self.write_report(GNF1331Timer17)  # 90, 在线状态，4组开与3组关按自定义方式执行的普通定时执行状态检查
            # self.write_report(GNF1331Timer18)  # 89, 在线状态，4组开与3组关按周末方式方式执行的普通定时执行状态检查
            # self.write_report(GNF1331Timer19)  # 88, 在线状态，4组开与3组关按工作日方式执行的普通定时执行状态检查
            # self.write_report(GNF1331Timer20)  # 87, 在线状态，单层4组开与3组关单次执行的普通定时执行状态检查
            # self.write_report(GNF1331Timer21)  # 80, 在线状态，单层1组开与1组关按自定义执行的普通定时执行状态检查
            # self.write_report(GNF1331Timer22)  # 79, 在线状态，单层1组开与1组关按工作日执行的普通定时执行状态检查
            # self.write_report(GNF1331Timer23)  # 78, 在线状态，单层临界点1组开与1组关的普通定时执行状态检查
            self.write_report(GNF1331Timer24)  # 77, 在线状态，单层定时1组开与1组关普通定时执行状态检查
            self.write_report(GNF1331Timer25)  # 76, 在线状态，单层定时单关普通定时执行状态检查
            self.write_report(GNF1331Timer26)  # 75, 在线状态，单层定时单开普通定时执行状态检查
            self.write_report(GNF1331Timer27)  # 73, 设备可接受最大额外定时组数检测
            self.write_report(GNF1331Timer28)  # 72, APP默认定时数组检测

            database["program_loop_time"] += 1
            times -= 1

        Mailer(self.m_queue, conf, True, "chenghao@gongniu.cn")

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
            xls_data["row"] = database["case_row"][int(zentao_id)]
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
            try:
                # Python2
                self.debug.info("write_data: %s" % json.dumps(xls_data, encoding='UTF-8', ensure_ascii=False))
            except TypeError:
                # Python3
                self.debug.info("write_data: %s" % xls_data)
            database["case_location"] += 1
        except BaseException:
            self.debug.error(traceback.format_exc())
