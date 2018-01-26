# coding=utf-8
import json

from src.testcase.GN_Y201S.input_case.GN_Y201S_Input_Case import *
from src.testcase.GN_Y201S.page.ReadAPPElement import *
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
            # self.write_report(GNY201SCmp1)  # 431, FUT_CMP_不同型号手机是否能正常添加设备
            # self.write_report(GNY201SCrossTimer1)  # 519, FUT_CROSSTIMER_普通定时、循环定时、延时定时交叉设置后定时执行
            self.write_report(GNY201SCycleTimer1)  # 470, FUT_CYCLETIMER_循环定时设置永久循环执行（1分钟开1分钟关）
            self.write_report(GNY201SCycleTimer2)  # 471, FUT_CYCLETIMER_循环定时执行过程中手动切换设备状态
            self.write_report(GNY201SCycleTimer3)  # 482, FUT_CYCLETIMER_循环定时5次
            self.write_report(GNY201SCycleTimer4)  # 483, FUT_CYCLETIMER_循环定时1次
            self.write_report(GNY201SDelayTimer1)  # 469, FUT_DELAYTIMER_延时定时一分钟开关
            # self.write_report(GNY201SDelayTimer2)  # 468, FUT_DELAYTIMER_延迟定时一小时开
            self.write_report(GNY201SDelayTimer3)  # 466, FUT_DELAYTIMER_延迟定时5分钟开
            # self.write_report(GNY201SDelayTimer4)  # 465, FUT_DELAYTIMER_延时定时23小时59分钟开
            self.write_report(GNY201SEem1)  # 559, FUT_EEM_峰谷电价设置
            self.write_report(GNY201SEem2)  # 558, FUT_EEM_用电图表显示周期设置
            # self.write_report(GNY201SEem3)  # 551, FUT_EEM_电价设置验证（待定）
            # self.write_report(GNY201SEem4)  # 550, FUT_EEM_实时功率显示及精度检查
            # self.write_report(GNY201SLogin1)  # 0000, 阿里智能APP账号登录
            self.write_report(GNY201SNormalTimer1)  # 517, FUT_NTIMER_冲突定时设置
            self.write_report(GNY201SNormalTimer2)  # 515, FUT_NTIMER_单次定时关
            self.write_report(GNY201SNormalTimer3)  # 513, FUT_NTIMER_单次定时开
            self.write_report(GNY201SNormalTimer4)  # 512, FUT_NTIMER_单日循环定时
            # self.write_report(GNY201SNormalTimer5)  # 510, FUT_NTIMER_定时时间早于当前时间的永不循环定时设置
            # self.write_report(GNY201SNormalTimer6)  # 508, FUT_NTIMER_隔天普通定时
            self.write_report(GNY201SNormalTimer7)  # 505, FUT_NTIMER_普通交叉定时
            # self.write_report(GNY201SNormalTimer8)  # 497, FUT_NTIMER_每日循环普通定时
            self.write_report(GNY201SNormalTimer9)  # 494, FUT_NTIMER_普通定时最大组数设定
            self.write_report(GNY201SNormalTimer10)  # 488, FUT_NTIMER_普通定时设置后手动改变设备状态
            self.write_report(GNY201SNormalTimer11)  # 417, FUT_NTIMER_普通定时循环信息检查
            # self.write_report(GNY201SSmartLink1)  # 498, FUT_SMTLNK_app能正常添加设备_按分类查找
            self.write_report(GNY201SSwitch1)  # 517, FUT_NTIMER_冲突定时设置
            self.write_report(GNY201STimerFish1)  # 442, FUT_MTIMER_FISH_鱼缸模式开启1分钟，关闭1分钟功能是否正常
            # self.write_report(GNY201STimerFish2)  # 441, FUT_MTIMER_FISH_鱼缸模式开启1小时，关闭1小时功能是否正常
            self.write_report(GNY201STimerFish3)  # 440, FUT_MTIMER_FISH_鱼缸模式开启2分钟，关闭2分钟功能是否正常
            # self.write_report(GNY201STimerFish4)  # 438, FUT_MTIMER_FISH_鱼缸模式开启23小时59分钟，关闭23小时59分钟功能是否正常
            self.write_report(GNY201STimerFish5)  # 436, FUT_MTIMER_FISH_鱼缸模式_循环1次
            self.write_report(GNY201STimerFish6)  # 435, FUT_MTIMER_FISH_鱼缸模式_循环2次
            # self.write_report(GNY201STimerMos1)  # 461, FUT_MTIMER_MOS_电蚊香模式_延时功能（1min，2min，1h，23h59min，断电恢复）是否正常
            # self.write_report(GNY201STimerOvp1)  # 459, FUT_MTIMER_OVP_充电保护模式_延时功能（1min，2min，1h，23h59min，断电恢复）是否正常
            self.write_report(GNY201STimerTime1)  # 450, FUT_MTIMER_TIME_当前时间在设定时间内模式时间执行
            # self.write_report(GNY201STimerTime2)  # 446, FUT_MTIMER_TIME_模式定时每日循环
            # self.write_report(GNY201STimerTime3)  # 445, FUT_MTIMER_TIME_模式定时每周日循环
            # self.write_report(GNY201STimerTime4)  # 444, FUT_MTIMER_TIME_循环定时每周一循环
            self.write_report(GNY201STimerTime5)  # 443, FUT_MTIMER_TIME_模式定时状态下手动改变设备状态
            # self.write_report(GNY201STimerTime6)  # 434, FUT_MTIMER_TIME_设定关闭时间早于开启时间的模式定时执行
            self.write_report(GNY201STimerTime7)  # 433, FUT_MTIMER_TIME_正常状态下模式定时

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
