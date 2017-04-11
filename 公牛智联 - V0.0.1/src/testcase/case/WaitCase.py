# coding:utf-8
from CheckUI import *
from data.Database import *
from src.testcase.suite.ScanCaseTitle import *


class WaitCase(object):
    def __init__(self):
        os.remove(r"../log/" + database["log_name"])
        os.remove(r"../report/Report.log")
        logger.info("*" * 30)
        logger.info(u"[APP_INF]deviceName：.....%s" % device.values()[0]['deviceName'])
        logger.info(u"[APP_INF]UDID：...........%s" % device.values()[0]['udid'])
        logger.info(u"[APP_INF]platformName：...%s" % device.values()[0]['platformName'])
        logger.info(u"[APP_INF]platformVersion：%s" % device.values()[0]['platformVersion'])
        logger.info(u"[APP_INF]appPackage：.....%s" % conf_App["GN"][0])
        logger.info(u"[APP_INF]appActivity：....%s" % conf_App["GN"][1])
        logger.info("*" * 30)
        self.No = 1
        while True:
            logger.info("run times [%s]" % database["program_loop_time"])
            # CheckUI()
            self.write_report(CaseTitle[u'登录页面—新用户注册页面跳转'])
            self.write_report(CaseTitle[u'登录页面—忘记密码页面跳转'])
            self.write_report(CaseTitle[u'登录页面—登录功能检'])
            self.write_report(CaseTitle[u'账户设置-修改密码页面，"返回"按钮功能检查'])
            self.write_report(CaseTitle[u'账户设置-密码修改后页面跳转确认'])
            self.write_report(CaseTitle[u'账户设置-退出当前账号后，取消按钮功能检查'])
            self.write_report(CaseTitle[u'使用帮助-返回按钮功能确认'])
            self.write_report(CaseTitle[u'注册页面-已有账户登录按钮，跳转页面检查'])
            self.write_report(CaseTitle[u'忘记密码页面-点击"返回"按钮，页面检查'])
            self.write_report(CaseTitle[u'消息分类页面信息检查'])
            self.write_report(CaseTitle[u'默认页面信息检查'])
            self.write_report(CaseTitle[u'设备配网过程中，返回按钮功能检查'])
            self.write_report(CaseTitle[u'设备配网过程中，弹出终止配网提示框，取消按钮功能检查'])

            database["program_loop_time"] += 1

    def write_report(self, case_title):
        case = case_title().result()
        data = u'[RUN_TIMES=%s, No=%s, CASE_TITLE="%s", RESULT=%s, TIME=%s]' % \
               (database["program_loop_time"], self.No, case[1], case[0], time.strftime("%Y-%m-%d %H:%M:%S"))
        report.info(data)
        self.No += 1
