# coding=utf-8
import json

from src.testcase.GN_APP.case.INPUT_CASE.GN_APP_Input_Case import *
from src.testcase.GN_APP.page.ReadAPPElement import *
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
        self.page = PageElement(self.device_info["platformName"])
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
            self.write_report(GNAPPLogin1)  # 1889, 登录页面—新用户注册页面跳转
            self.write_report(GNAPPLogin2)  # 1890, 登录页面—忘记密码页面跳转
            self.write_report(GNAPPLogin3)  # 1891, 登录页面—登录功能检查
            self.write_report(GNAPPLogin4)  # 1903, 登录页面—成功登录后杀掉APP，再次开启APP的状态查看
            self.write_report(GNAPPLogin5)  # 1900, 登录页面—成功登录后注销账号，再次进入登录页面查看
            self.write_report(GNAPPLogin6)  # 1899, 登录页面—错误密码输入次数超过5次后，账号锁定1分钟验证
            self.write_report(GNAPPLogin7)  # 1897, 登录页面—错误密码，登录提示信息检查
            self.write_report(GNAPPLogin8)  # 1898, 登录页面—密码输入超过5次后，信息检查
            self.write_report(GNAPPLogin9)  # 1896, 登录页面—密码为空，登录提示信息检查
            self.write_report(GNAPPLogin10)  # 1895, 登录页面—位数错误的数字账号，登录提示信息检查
            self.write_report(GNAPPLogin11)  # 1894, 登录页面—未注册的手机号码，登录提示信息检查
            self.write_report(GNAPPLogin12)  # 1893, 登录页面—账号为空，登录提示信息检查
            self.write_report(GNAPPLogin13)  # 1892, 登录页面—无效账号，登录提示信息检查
            self.write_report(GNAPPAccountSettings1)  # 1965, 修改密码页面，返回"按钮功能检查"
            self.write_report(GNAPPAccountSettings2)  # 1972, 密码修改后页面跳转确认
            self.write_report(GNAPPAccountSettings3)  # 1973, 退出当前账号后，取消按钮功能检查
            self.write_report(GNAPPAccountSettings4)  # 1975, 返回按钮功能确认
            self.write_report(GNAPPAccountSettings5)  # 1970, 密码修改页面，旧密码输入错误，提示信息检查
            self.write_report(GNAPPAccountSettings6)  # 1946, 点击昵称"按钮，功能检查"
            self.write_report(GNAPPAccountSettings7)  # 1948, 昵称为空时，功能检查
            self.write_report(GNAPPAccountSettings8)  # 1949, 昵称修改成功，页面信息检查
            self.write_report(GNAPPAccountSettings9)  # 1969, 密码修改页面，新密码与确认密码不一致，提示信息检查
            self.write_report(GNAPPAccountSettings10)  # 1968, 密码修改页面，确认密码为空，提示信息检查
            self.write_report(GNAPPAccountSettings11)  # 1967, 密码修改页面，新密码与确认密码均为空，提示信息检查
            self.write_report(GNAPPAccountSettings12)  # 1966, 密码修改页面，旧密码为空，提示信息检查
            self.write_report(GNAPPAccountSettings13)  # 1947, 昵称长度16位验证，功能检查
            self.write_report(GNAPPRegister1)  # 1888, 注册页面-已有账户登录按钮，跳转页面检查
            self.write_report(GNAPPRegister2)  # 1885, 注册页面-正确的用户名和密码，空的验证码，注册验证
            self.write_report(GNAPPRegister3)  # 1884, 注册页面-正确的用户名和密码，验证码大于6位，注册验证
            self.write_report(GNAPPRegister4)  # 1883, 注册页面-正确的用户名和密码，错误的6位数字验证码，注册验证
            self.write_report(GNAPPRegister5)  # 1882, 注册页面-正确的用户名和密码，小于6位数字验证码，注册验证
            self.write_report(GNAPPRegister6)  # 1881, 注册页面-验证码为特殊字符时，提示信息检查
            self.write_report(GNAPPRegister7)  # 1880, 注册页面-验证码为中文字符时，提示信息检查
            self.write_report(GNAPPRegister8)  # 1879, 注册页面-验证码为英文字符时，提示信息检查
            self.write_report(GNAPPRegister9)  # 1866, 注册页面-密码长度大于16位，注册检查
            self.write_report(GNAPPRegister10)  # 1840, 注册页面-密码长度小于6位，注册检查
            self.write_report(GNAPPRegister11)  # 1838, 注册页面-用户名长度小于11位，提示信息检查
            self.write_report(GNAPPRegister12)  # 1826, 注册页面-用户名长度大于11位，提示信息检查
            self.write_report(GNAPPRegister13)  # 1825, 注册页面-用户名为空，注册验证
            self.write_report(GNAPPRegister14)  # 1824, 注册页面-用户名为英文字符时，提示信息检查
            self.write_report(GNAPPRegister15)  # 1772, 注册页面-用户名为特殊字符时，提示信息检查
            self.write_report(GNAPPRegister16)  # 1771, 注册页面-用户名为中文字符时，提示信息检查
            self.write_report(GNAPPRegister17)  # 1769, 注册页面-用户名为数字时(非正确的手机号码)，提示信息检查
            self.write_report(GNAPPRegister18)  # 1768, 注册页面-已经注册过的用户名，再次注册验证
            self.write_report(GNAPPForgetPassword1)  # 1904, 忘记密码页面-点击"返回"按钮，页面检查
            self.write_report(GNAPPForgetPassword2)  # 1909, 忘记密码页面-未注册账户检测
            self.write_report(GNAPPForgetPassword3)  # 1907, 忘记密码页面-点击返回登入界面"按钮，页面检查"
            self.write_report(GNAPPMessageClassify1)  # 1922, 消息分类页面信息检查
            self.write_report(GNAPPMessageClassify2)  # 1926, 消息设置页面，清空活动历时消息功能检查
            self.write_report(GNAPPMessageClassify3)  # 1927, 消息设置页面，清空设备历时消息功能检查
            self.write_report(GNAPPMessageClassify4)  # 1925, 消息设置页面信息检查
            self.write_report(GNAPPMessageClassify5)  # 1924, 消息分类页面，选择多个设备后的消息内容检查
            self.write_report(GNAPPDevicePage1)  # 1773, 默认页面信息检查
            self.write_report(GNAPPDevicePage2)  # 1798, 设备配网过程中，返回按钮功能检查
            self.write_report(GNAPPDevicePage3)  # 1799, 设备配网过程中，弹出终止配网提示框，取消按钮功能检查
            self.write_report(GNAPPDevicePage4)  # 1800, 设备配网过程中，弹出终止配网提示框，确定按钮功能检查
            self.write_report(GNAPPDevicePage5)  # 1807, 配网失败页面信息检查
            self.write_report(GNAPPDevicePage6)  # 1808, 配网失败页面，取消按钮功能检查
            self.write_report(GNAPPFeedBack1)  # 1992, 版本信息-当前版本为最新版本，页面信息检查
            self.write_report(GNAPPUsingHelp1)  # 1975, 返回按钮功能确认
            self.write_report(GNAPPThemeStyle1)  # 1986, 返回按钮功能检查
            self.write_report(GNAPPThemeStyle2)  # 1990, 切换为紫色后，查看风格
            self.write_report(GNAPPThemeStyle3)  # 1989, 切换为橙色后，查看风格
            self.write_report(GNAPPThemeStyle4)  # 1988, 切换为红色后，查看风格
            self.write_report(GNAPPThemeStyle5)  # 1987, 切换为绿色后，查看风格
            self.write_report(GNAPPThemeStyle6)  # 1985, 页面检查
            self.write_report(GNAPPVersion1)  # 1992, 当前版本为最新版本，页面信息检查

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
