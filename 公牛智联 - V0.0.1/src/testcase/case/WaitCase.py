# coding=utf-8
import time

from data.Database import *
from src.testcase.case.INPUT_CASE.GNAppAccountSettings import *
from src.testcase.case.INPUT_CASE.GNAppDevicePage import *
from src.testcase.case.INPUT_CASE.GNAppFeedBack import *
from src.testcase.case.INPUT_CASE.GNAppForgetPassword import *
from src.testcase.case.INPUT_CASE.GNAppLogin import *
from src.testcase.case.INPUT_CASE.GNAppMessageClassify import *
from src.testcase.case.INPUT_CASE.GNAppRegister import *
from src.testcase.case.INPUT_CASE.GNAppUsingHelp import *
from src.testcase.case.INPUT_CASE.GNAppVersion import *
from src.utils.CollectLog import *
from src.utils.OutputReport import *


class WaitCase(object):
    def __init__(self, device_list, device_name):
        self.device_list = device_list
        self.device_name = device_name
        self.device_info = device_list[device_name]
        self.report = None
        self.logger = None
        self.No = 1

        self.create_log()
        self.create_report()
        self.run()

    def create_report(self):
        check_report(self.device_list, self.device_name)
        self.report = self.device_info["report"]

    def create_log(self):
        check_log(self.device_list, self.device_name)
        self.logger = self.device_info["logger"]

    def run(self):
        self.logger.info("*" * 30)
        self.logger.info(u"[APP_INF]deviceName：.....%s" % self.device_info["deviceName"])
        self.logger.info(u"[APP_INF]UDID：...........%s" % self.device_info["udid"])
        self.logger.info(u"[APP_INF]platformName：...%s" % self.device_info["platformName"])
        self.logger.info(u"[APP_INF]platformVersion：%s" % self.device_info["platformVersion"])
        self.logger.info(u"[APP_INF]appPackage：.....%s" % conf_App["GN"][0])
        self.logger.info(u"[APP_INF]appActivity：....%s" % conf_App["GN"][1])
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
            # self.write_report(GNAppAccountSettings1)  # 1965, 修改密码页面，返回"按钮功能检查"
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
            self.write_report(GNAppUsingHelp1)  # 1992, 版本信息-当前版本为最新版本，页面信息检查
            self.write_report(GNAppVersion1)  # 1992, 版本信息-当前版本为最新版本，页面信息检查

            database["program_loop_time"] += 1

    def write_report(self, case_name):
        case = case_name(self.device_list, self.device_name, self.logger).result()
        data = u'[RUN_TIMES=%s, CASE_ID=%s, CASE_NAME="%s", RESULT=%s, START=%s, CLOSE=%s]' % \
               (database["program_loop_time"], self.No, case[1], case[0], case[2], time.strftime("%Y-%m-%d %H:%M:%S"))
        self.report.info(data)
        self.No += 1
        database["case_location"] = self.No
