# coding=utf-8
from src.testcase.case.GNAPP.INPUT_CASE.GNAppInputCase import *
from src.testcase.common.AppInit import *
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


class WaitCaseGN(object):
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
        LaunchAppGN(**self.device_info_list).init_app()

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
            # self.write_report(GNAppLogin1)  # 1889, 登录页面—新用户注册页面跳转
            # self.write_report(GNAppLogin2)  # 1890, 登录页面—忘记密码页面跳转
            # self.write_report(GNAppLogin3)  # 1891, 登录页面—登录功能检查
            # self.write_report(GNAppLogin4)  # 1903, 登录页面—成功登录后杀掉APP，再次开启APP的状态查看
            # self.write_report(GNAppLogin5)  # 1900, 登录页面—成功登录后注销账号，再次进入登录页面查看
            # self.write_report(GNAppLogin6)  # 1899, 登录页面—错误密码输入次数超过5次后，账号锁定1分钟验证
            # self.write_report(GNAppLogin7)  # 1897, 登录页面—错误密码，登录提示信息检查
            # self.write_report(GNAppLogin8)  # 1898, 登录页面—密码输入超过5次后，信息检查
            # self.write_report(GNAppLogin9)  # 1896, 登录页面—密码为空，登录提示信息检查
            # self.write_report(GNAppLogin10)  # 1895, 登录页面—位数错误的数字账号，登录提示信息检查
            # self.write_report(GNAppLogin11)  # 1894, 登录页面—未注册的手机号码，登录提示信息检查
            # self.write_report(GNAppLogin12)  # 1893, 登录页面—账号为空，登录提示信息检查
            # self.write_report(GNAppLogin13)  # 1892, 登录页面—无效账号，登录提示信息检查
            self.write_report(GNAppAccountSettings1)  # 1965, 修改密码页面，返回"按钮功能检查"
            self.write_report(GNAppAccountSettings2)  # 1972, 密码修改后页面跳转确认
            self.write_report(GNAppAccountSettings3)  # 1973, 退出当前账号后，取消按钮功能检查
            self.write_report(GNAppAccountSettings4)  # 1975, 返回按钮功能确认
            self.write_report(GNAppAccountSettings5)  # 1970, 密码修改页面，旧密码输入错误，提示信息检查
            self.write_report(GNAppAccountSettings6)  # 1946, 点击昵称"按钮，功能检查"
            self.write_report(GNAppAccountSettings7)  # 1948, 昵称为空时，功能检查
            self.write_report(GNAppAccountSettings8)  # 1949, 昵称修改成功，页面信息检查
            self.write_report(GNAppAccountSettings9)  # 1969, 密码修改页面，新密码与确认密码不一致，提示信息检查
            self.write_report(GNAppAccountSettings10)  # 1968, 密码修改页面，确认密码为空，提示信息检查
            self.write_report(GNAppAccountSettings11)  # 1967, 密码修改页面，新密码与确认密码均为空，提示信息检查
            self.write_report(GNAppAccountSettings12)  # 1966, 密码修改页面，旧密码为空，提示信息检查
            self.write_report(GNAppAccountSettings13)  # 1947, 昵称长度16位验证，功能检查
            self.write_report(GNAppRegister1)  # 1888, 注册页面-已有账户登录按钮，跳转页面检查
            self.write_report(GNAppRegister2)  # 1885, 注册页面-正确的用户名和密码，空的验证码，注册验证
            self.write_report(GNAppRegister3)  # 1884, 注册页面-正确的用户名和密码，验证码大于6位，注册验证
            self.write_report(GNAppRegister4)  # 1883, 注册页面-正确的用户名和密码，错误的6位数字验证码，注册验证
            self.write_report(GNAppRegister5)  # 1882, 注册页面-正确的用户名和密码，小于6位数字验证码，注册验证
            self.write_report(GNAppRegister6)  # 1881, 注册页面-验证码为特殊字符时，提示信息检查
            self.write_report(GNAppRegister7)  # 1880, 注册页面-验证码为中文字符时，提示信息检查
            self.write_report(GNAppRegister8)  # 1879, 注册页面-验证码为英文字符时，提示信息检查
            self.write_report(GNAppRegister9)  # 1866, 注册页面-密码长度大于16位，注册检查
            self.write_report(GNAppRegister10)  # 1840, 注册页面-密码长度小于6位，注册检查
            self.write_report(GNAppRegister11)  # 1838, 注册页面-用户名长度小于11位，提示信息检查
            self.write_report(GNAppRegister12)  # 1826, 注册页面-用户名长度大于11位，提示信息检查
            self.write_report(GNAppRegister13)  # 1825, 注册页面-用户名为空，注册验证
            self.write_report(GNAppRegister14)  # 1824, 注册页面-用户名为英文字符时，提示信息检查
            self.write_report(GNAppRegister15)  # 1772, 注册页面-用户名为特殊字符时，提示信息检查
            self.write_report(GNAppRegister16)  # 1771, 注册页面-用户名为中文字符时，提示信息检查
            self.write_report(GNAppRegister17)  # 1769, 注册页面-用户名为数字时(非正确的手机号码)，提示信息检查
            self.write_report(GNAppRegister18)  # 1768, 注册页面-已经注册过的用户名，再次注册验证
            self.write_report(GNAppForgetPassword1)  # 1904, 忘记密码页面-点击"返回"按钮，页面检查
            self.write_report(GNAppForgetPassword2)  # 1909, 忘记密码页面-未注册账户检测
            self.write_report(GNAppForgetPassword3)  # 1907, 忘记密码页面-点击返回登入界面"按钮，页面检查"
            self.write_report(GNAppMessageClassify1)  # 1922, 消息分类页面信息检查
            self.write_report(GNAppMessageClassify2)  # 1926, 消息设置页面，清空活动历时消息功能检查
            self.write_report(GNAppMessageClassify3)  # 1927, 消息设置页面，清空设备历时消息功能检查
            self.write_report(GNAppMessageClassify4)  # 1925, 消息设置页面信息检查
            self.write_report(GNAppMessageClassify5)  # 1924, 消息分类页面，选择多个设备后的消息内容检查
            self.write_report(GNAppDevicePage1)  # 1773, 默认页面信息检查
            self.write_report(GNAppDevicePage2)  # 1798, 设备配网过程中，返回按钮功能检查
            self.write_report(GNAppDevicePage3)  # 1799, 设备配网过程中，弹出终止配网提示框，取消按钮功能检查
            self.write_report(GNAppDevicePage4)  # 1800, 设备配网过程中，弹出终止配网提示框，确定按钮功能检查
            self.write_report(GNAppDevicePage5)  # 1807, 配网失败页面信息检查
            self.write_report(GNAppDevicePage6)  # 1808, 配网失败页面，取消按钮功能检查
            self.write_report(GNAppFeedBack1)  # 1992, 版本信息-当前版本为最新版本，页面信息检查
            self.write_report(GNAppUsingHelp1)  # 1975, 返回按钮功能确认
            self.write_report(GNAppThemeStyle1)  # 1986, 返回按钮功能检查
            self.write_report(GNAppThemeStyle2)  # 1990, 切换为紫色后，查看风格
            self.write_report(GNAppThemeStyle3)  # 1989, 切换为橙色后，查看风格
            self.write_report(GNAppThemeStyle4)  # 1988, 切换为红色后，查看风格
            self.write_report(GNAppThemeStyle5)  # 1987, 切换为绿色后，查看风格
            self.write_report(GNAppThemeStyle6)  # 1985, 页面检查
            self.write_report(GNAppVersion1)  # 1992, 当前版本为最新版本，页面信息检查

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
