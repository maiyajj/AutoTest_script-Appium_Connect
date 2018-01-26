# coding=utf-8
import json

from src.testcase.GN_Y201J.input_case.GN_Y201J_Input_Case import *
from src.testcase.GN_Y201J.page.ReadAPPElement import *
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
        while True:
            self.debug.info("run times [%s]" % database["program_loop_time"])
            # self.write_report(GNY201JLogin1)  # 0000, 京东微联APP账号登录
            # self.write_report(GNY201JCompatibility1)  # 1272, 在TP-link品牌的路由器下添加设备检查
            # self.write_report(GNY201JElectricityMeter1)  # 1117, 电量统计2H功能及精度检查
            # self.write_report(GNY201JElectricityMeter2)  # 1138, 单一电价验证
            # self.write_report(GNY201JElectricityMeter3)  # 1139, 峰谷电价验证
            # self.write_report(GNY201JElectricityMeter4)  # 1150, 电价模式转换
            # self.write_report(GNY201JElectricityMeter5)  # 1149, 用电图表显示周期设置
            # self.write_report(GNY201JElectricityMeter6)  # 1151, 单一电价设置
            # self.write_report(GNY201JElectricityMeter7)  # 1152, 设置峰谷电价
            # self.write_report(GNY201JElectricityMeter8)  # 1155, 电价设置验证
            # self.write_report(GNY201JElectricityMeter9)  # 1136, 实时功率检查_2000W
            # self.write_report(GNY201JElectricityMeter10)  # 1135, 实时功率检查_1500W
            # self.write_report(GNY201JElectricityMeter11)  # 1133, 实时功率检查_500W
            # self.write_report(GNY201JElectricityMeter12)  # 1132, 实时功率检查_200W
            # self.write_report(GNY201JElectricityMeter13)  # 1130, 实时功率检查_50W
            self.write_report(GNY201JAppFunction1)  # 1170, 定时记录删除是否成功
            self.write_report(GNY201JAppFunction2)  # 1307, 启动鱼缸模式定时，APP中开关状态检查
            self.write_report(GNY201JKeyMemory1)  # 1216, 开关操作及记忆功能
            # self.write_report(GNY201JModeTimer1)  # 1061, 热水器模式下设定的关闭时间早于开启时间的定时是否正确执行
            self.write_report(GNY201JModeTimer2)  # 1064, 热水器模式下当前时间在设定时间内的定时是否正确执行
            self.write_report(GNY201JModeTimer3)  # 1081, 充电保护模式下手动改变设备为关闭状态后，定时结束检查设备状态
            self.write_report(GNY201JModeTimer4)  # 1083, 充电保护模式下手动改变设备为开启状态后，定时结束检查设备状态
            self.write_report(GNY201JModeTimer5)  # 1086, 充电保护模式下延时关闭1分钟
            self.write_report(GNY201JModeTimer6)  # 1103, 鱼缸模式开启1分钟，关闭1分钟定时是否正确执行
            # self.write_report(GNY201JModeTimer7)  # 1105, 鱼缸模式开启1小时，关闭1小时定时是否正确执行
            self.write_report(GNY201JModeTimer8)  # 1108, 鱼缸模式开启2分钟，关闭2分钟定时是否正确执行
            self.write_report(GNY201JNormalTimer1)  # 1161, 普通定时设置后手动改变设备状态为开启
            self.write_report(GNY201JNormalTimer2)  # 1162, 普通定时设置后手动改变设备状态为关闭
            self.write_report(GNY201JNormalTimer3)  # 1164, 普通定时最大组数设定_设置12组
            self.write_report(GNY201JNormalTimer4)  # 1174, 普通定时_设置13组
            self.write_report(GNY201JNormalTimer5)  # 1181, 普通交叉定时_8分钟
            self.write_report(GNY201JNormalTimer6)  # 1184, 单次定时开_2分钟
            self.write_report(GNY201JNormalTimer7)  # 1185, 单次定时关_2分钟
            # self.write_report(GNY201JOverDay1)  # 1299, 热水器模式设置每日循环
            # self.write_report(GNY201JOverDay2)  # 1300, 热水器模式在跨天循环下的跨天执行
            # self.write_report(GNY201JOverDay3)  # 1301, 定时时间早于当前时间的永不循环定时设置
            # self.write_report(GNY201JOverDay4)  # 1302, 隔天普通定时
            # self.write_report(GNY201JOverDay5)  # 1304, 每日循环普通定时
            # self.write_report(GNY201JOverDay6)  # 1305, 鱼缸模式开启23小时59分钟，关闭23小时59分钟定时是否正确执行
            # self.write_report(GNY201JOverDay7)  # 1306, 充电保护模式下延迟23h59min关闭

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
            self.debug.info("write_data: %s" % json.dumps(xls_data, encoding='UTF-8', ensure_ascii=False))
            database["case_location"] += 1
        except BaseException:
            self.debug.error(traceback.format_exc())
