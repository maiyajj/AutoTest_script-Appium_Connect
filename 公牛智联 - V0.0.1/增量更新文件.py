# coding=utf-8
import linecache
import os.path
import re

from src.testcase.page.AppPageElement import *


def create_ReadConf():
    head = "# coding:utf-8\n" \
           "# 由Conf.py生成\n" \
           "import sys\n\n" \
           "import yaml\n\n" \
           "reload(sys)\n" \
           "sys.setdefaultencoding('utf-8')\n\n" \
           "conf = yaml.load(file(r'config/Conf.yaml'))\n"
    with open(r"config/Conf.yaml", "r") as files:
        with open(r"./src/utils/ReadConf.py", "w") as tmp_file:
            tmp_file.write(head)
            file = files.readlines()
            for i in file:
                tmp = re.findall(r"^\S.+", i)
                if tmp != []:
                    database = tmp[0].split(":")[0].split()
                    try:
                        database = [database[0][-1] + " " + database[1]]
                    except IndexError:
                        pass
                    database = database[0]
                    data = re.findall(r"#.+", database)
                    if data == []:
                        tmp_file.write('conf_%s = conf["%s"]\n' % (database, database))
                    else:
                        tmp_file.write("%s\n" % database)


def create_ReadAPPElement():
    a = []
    b = []
    for i in dir(MainPageWidget):
        tmp = re.findall("__.+", i)
        if tmp == []:
            a.append(i)
    for i in dir(PopupWidget):
        tmp = re.findall("__.+", i)
        if tmp == []:
            b.append(i)
    with open(r"./src/utils/ReadAPPElement.py", "w") as files:
        files.write("# coding:utf-8\n")
        files.write("# 由Conf.py生成\n")
        files.write("from src.testcase.page.AppPageElement import *\n\n")
        for i in a:
            files.write("%s = MainPageWidget().%s()\n" % (i, i))
        files.write("\n")
        for i in b:
            files.write("%s = PopupWidget().%s()\n" % (i, i))


def create_INPUT_CASE():
    # 写INPUT_CASE文件夹内容
    rootdir = r"./src/testcase/case"  # 指明被遍历的文件夹

    DevicePage = open(r"./src/testcase/case/INPUT_CASE/GNAppDevicePage.py", "w")
    ForgetPassword = open(r"./src/testcase/case/INPUT_CASE/GNAppForgetPassword.py", "w")
    Login = open(r"./src/testcase/case/INPUT_CASE/GNAppLogin.py", "w")
    MessageClassify = open(r"./src/testcase/case/INPUT_CASE/GNAppMessageClassify.py", "w")
    AccountSettings = open(r"./src/testcase/case/INPUT_CASE/GNAppAccountSettings.py", "w")
    Register = open(r"./src/testcase/case/INPUT_CASE/GNAppRegister.py", "w")
    FeedBack = open(r"./src/testcase/case/INPUT_CASE/GNAppFeedBack.py", "w")
    UsingHelp = open(r"./src/testcase/case/INPUT_CASE/GNAppUsingHelp.py", "w")
    Version = open(r"./src/testcase/case/INPUT_CASE/GNAppVersion.py", "w")

    DevicePage.write("# coding:utf-8\n")
    ForgetPassword.write("# coding:utf-8\n")
    Login.write("# coding:utf-8\n")
    MessageClassify.write("# coding:utf-8\n")
    AccountSettings.write("# coding:utf-8\n")
    Register.write("# coding:utf-8\n")
    FeedBack.write("# coding:utf-8\n")
    UsingHelp.write("# coding:utf-8\n")
    Version.write("# coding:utf-8\n")

    for parent, dirnames, filenames in os.walk(rootdir):  # 三个参数：分别返回1.父目录 2.所有文件夹名字（不含路径） 3.所有文件名字
        for filename in filenames:
            if "GNAPP" in filename and "pyc" not in filename:
                filename = filename[:-3]
                if "GNAPP_DEVICE_PAGE" in filename:
                    DevicePage.write("from src.testcase.case.GNAPP_DEVICE_PAGE.%s import *\n" % filename)
                if "GNAPP_FORGET_PASSWORD" in filename:
                    ForgetPassword.write("from src.testcase.case.GNAPP_FORGET_PASSWORD.%s import *\n" % filename)
                if "GNAPP_LOGIN" in filename:
                    Login.write("from src.testcase.case.GNAPP_LOGIN.%s import *\n" % filename)
                if "GNAPP_MESSAGE_CLASSIFY" in filename:
                    MessageClassify.write("from src.testcase.case.GNAPP_MESSAGE_CLASSIFY.%s import *\n" % filename)
                if "GNAPP_ACCOUNT_SETTINGS" in filename:
                    AccountSettings.write("from src.testcase.case.GNAPP_ACCOUNT_SETTINGS.%s import *\n" % filename)
                if "GNAPP_REGISTER" in filename:
                    Register.write("from src.testcase.case.GNAPP_REGISTER.%s import *\n" % filename)
                if "GNAPP_FEED_BACK" in filename:
                    FeedBack.write("from src.testcase.case.GNAPP_FEED_BACK.%s import *\n" % filename)
                if "GNAPP_USING_HELP" in filename:
                    UsingHelp.write("from src.testcase.case.GNAPP_USING_HELP.%s import *\n" % filename)
                if "GNAPP_VERSION" in filename:
                    Version.write("from src.testcase.case.GNAPP_VERSION.%s import *\n" % filename)
    DevicePage.close()
    ForgetPassword.close()
    Login.close()
    MessageClassify.close()
    AccountSettings.close()
    Register.close()
    FeedBack.close()
    UsingHelp.close()
    Version.close()


def create_WaitCase():
    rootdir = r"./src/testcase/case"
    CaseList = []
    for parent, dirnames, filenames in os.walk(rootdir):
        for filename in filenames:
            if "GNAPP" in filename and "pyc" not in filename:
                with open(os.path.join(parent, filename), "r") as files:
                    file = files.read()
                    class_name = re.findall(r"class (.+)\(", file)[0]
                    CaseList.append(class_name)
    with open(r"./src/testcase/case/WaitCase.py", "w") as WaitCase:
        WaitCase.write('''# coding:utf-8\n''')
        WaitCase.write('''from data.Database import *\n''')
        WaitCase.write('''from src.testcase.case.INPUT_CASE.GNAppAccountSettings import *\n''')
        WaitCase.write('''from src.testcase.case.INPUT_CASE.GNAppDevicePage import *\n''')
        WaitCase.write('''from src.testcase.case.INPUT_CASE.GNAppFeedBack import *\n''')
        WaitCase.write('''from src.testcase.case.INPUT_CASE.GNAppForgetPassword import *\n''')
        WaitCase.write('''from src.testcase.case.INPUT_CASE.GNAppLogin import *\n''')
        WaitCase.write('''from src.testcase.case.INPUT_CASE.GNAppMessageClassify import *\n''')
        WaitCase.write('''from src.testcase.case.INPUT_CASE.GNAppRegister import *\n''')
        WaitCase.write('''from src.testcase.case.INPUT_CASE.GNAppUsingHelp import *\n''')
        WaitCase.write('''from src.testcase.case.INPUT_CASE.GNAppVersion import *\n''')
        WaitCase.write('''from src.testcase.suite.ScanCaseName import *\n\n\n''')

        WaitCase.write('''class WaitCase(object):\n''')
        WaitCase.write('''    def __init__(self):\n''')
        WaitCase.write('''        os.remove(r"./log/" + database["log_name"])\n''')
        WaitCase.write('''        os.remove(r"./report/Report.log")\n''')
        WaitCase.write('''        logger.info("*" * 30)\n''')
        WaitCase.write('''        logger.info(u"[APP_INF]deviceName：.....%s" % device.values()[0]["deviceName"])\n''')
        WaitCase.write('''        logger.info(u"[APP_INF]UDID：...........%s" % device.values()[0]["udid"])\n''')
        WaitCase.write('''        logger.info(u"[APP_INF]platformName：...%s" % device.values()[0]["platformName"])\n''')
        WaitCase.write(
            '''        logger.info(u"[APP_INF]platformVersion：%s" % device.values()[0]["platformVersion"])\n''')
        WaitCase.write('''        logger.info(u"[APP_INF]appPackage：.....%s" % conf_App["GN"][0])\n''')
        WaitCase.write('''        logger.info(u"[APP_INF]appActivity：....%s" % conf_App["GN"][1])\n''')
        WaitCase.write('''        logger.info("*" * 30)\n''')
        WaitCase.write('''        self.No = 1\n''')
        WaitCase.write('''        database["case_location"] = self.No\n''')
        WaitCase.write('''        while True:\n''')
        WaitCase.write('''            logger.info("run times [%s]" % database["program_loop_time"])\n''')
        WaitCase.write('''            # CheckUI()\n''')
        for i in CaseList:
            if "Login" in i:
                WaitCase.write('''            self.write_report(%s)\n''' % i)
        for i in CaseList:
            if "AccountSettings" in i:
                WaitCase.write('''            self.write_report(%s)\n''' % i)
        for i in CaseList:
            if "Register" in i:
                WaitCase.write('''            self.write_report(%s)\n''' % i)
        for i in CaseList:
            if "ForgetPassword" in i:
                WaitCase.write('''            self.write_report(%s)\n''' % i)
        for i in CaseList:
            if "MessageClassify" in i:
                WaitCase.write('''            self.write_report(%s)\n''' % i)
        for i in CaseList:
            if "DevicePage" in i:
                WaitCase.write('''            self.write_report(%s)\n''' % i)
        for i in CaseList:
            if "FeedBack" in i:
                WaitCase.write('''            self.write_report(%s)\n''' % i)
        for i in CaseList:
            if "UsingHelp" in i:
                WaitCase.write('''            self.write_report(%s)\n''' % i)
        for i in CaseList:
            if "Version" in i:
                WaitCase.write('''            self.write_report(%s)\n''' % i)
        WaitCase.write('''\n            database["program_loop_time"] += 1\n\n''')

        WaitCase.write('''    def write_report(self, case_name):\n''')
        WaitCase.write('''        case = case_name().result()\n''')
        WaitCase.write('''        data = u'[RUN_TIMES=%s, CASE_ID=%s, CASE_NAME="%s", RESULT=%s, TIME=%s]' % \\\n''')
        WaitCase.write(
            '''               (database["program_loop_time"], self.No, case[1], case[0], time.strftime("%Y-%m-%d %H:%M:%S"))\n''')
        WaitCase.write('''        report.info(data)\n''')
        WaitCase.write('''        self.No += 1\n''')
        WaitCase.write('''        database["case_location"] = self.No\n''')


def file_renames():
    rootdir = r".src/testcase/case"
    for parent, dirnames, filenames in os.walk(rootdir):
        for filename in filenames:
            if "pyc" in filename:
                try:
                    os.remove(os.path.join(parent, filename))
                except WindowsError:
                    pass
            if "GNAPP" in filename and "pyc" not in filename:
                name = re.findall(r"(.+_)(\d+)(.py)", filename)[0]
                oldpath = os.path.join(parent, filename)
                if len(name[1]) == 1:
                    newname = "00" + name[1]
                    newpathname = name[0] + newname + name[2]
                    newpath = os.path.join(parent, newpathname)
                    os.renames(oldpath, newpath)
                elif len(name[1]) == 2:
                    newname = "0" + name[1]
                    newpathname = name[0] + newname + name[2]
                    newpath = os.path.join(parent, newpathname)
                    os.renames(oldpath, newpath)


# 向每个用例文件中写入from appium import webdriver
def insert_code():
    rootdir = r"./src/testcase/case"
    for parent, dirnames, filenames in os.walk(rootdir):
        for filename in filenames:
            if "GNAPP" in filename and "pyc" not in filename:
                with open(os.path.join(parent, filename), "r+") as files:
                    first_lines = files.readline()
                    second_lines = files.readlines()
                    files.seek(0)
                    files.write(first_lines)
                    files.write("from appium import webdriver\n")
                    for i in second_lines:
                        files.write(i, )


# 删除所有pyc文件
def del_pyc():
    rootdir = r"./"
    for parent, dirnames, filenames in os.walk(rootdir):
        for filename in filenames:
            if "pyc" in filename:
                try:
                    os.remove(os.path.join(parent, filename))
                except WindowsError:
                    pass


# 扫描路径中../
def scan_path():
    rootdir = r"./"
    for parent, dirnames, filenames in os.walk(rootdir):
        for filename in filenames:
            if "py" in filename and "pyc" not in filename and "init" not in filename:
                with open(os.path.join(parent, filename), "r") as files:
                    name = re.findall(r"\.\./.+", files.read())
                    if name != []:
                        print name
                        print os.path.join(parent, filename)


# 扫描文件中不是/分隔的
def scan_backslash():
    rootdir = r"./"
    for parent, dirnames, filenames in os.walk(rootdir):
        for filename in filenames:
            if "py" in filename and "pyc" not in filename and "init" not in filename:
                with open(os.path.join(parent, filename), "r") as files:
                    name = re.findall(r'.+\\.+', files.read())
                    if name != []:
                        for i in name:
                            if "\\n" not in i:
                                print i
                                print os.path.join(parent, filename)


# 全部添加禅道ID
def add_ZenTao_id():
    rootdir = r"./src/testcase/case"
    for parent, dirnames, filenames in os.walk(rootdir):
        for filename in filenames:
            if "GNAPP" in filename and "pyc" not in filename:
                filepath = os.path.join(parent, filename)
                lines = len(linecache.getlines(filepath))
                with open(filepath, "w") as files:
                    for i in range(1, lines + 1):
                        if "self.case_title = " in linecache.getline(filepath, i):
                            print i, linecache.getline(filepath, i),
                            files.write(linecache.getline(filepath, i))
                            files.write("        self.ZenTao_id = \n")
                        elif '[CASE_ID="%s", CASE_TITLE="%s"]' in linecache.getline(filepath, i):
                            print i, linecache.getline(filepath, i),
                            files.write(
                                '''        logger.info('[GN_INF] <current case> [CASE_ID="%s", CASE_NAME="%s", 禅道ID="%s"]'\n''')
                        elif "os.path.basename" in linecache.getline(filepath, i):
                            print i, linecache.getline(filepath, i),
                            files.write(
                                '''                    % (os.path.basename(__file__).split(".")[0], self.case_title, self.ZenTao_id, self.case_module))\n''')
                        else:
                            files.write(linecache.getline(filepath, i))


def add_basename():
    rootdir = r"./src/testcase/case"
    for parent, dirnames, filenames in os.walk(rootdir):
        for filename in filenames:
            if "GNAPP" in filename and "pyc" not in filename:
                filepath = os.path.join(parent, filename)
                lines = len(linecache.getlines(filepath))
                with open(filepath, "w") as files:
                    for i in range(1, lines + 1):
                        if "self.wait_widget = widget_check_unit.wait_widget" in linecache.getline(filepath, i):
                            files.write(linecache.getline(filepath, i))
                            files.write('        self.success = 0\n')
                        else:
                            files.write(linecache.getline(filepath, i))

create_ReadConf()
# create_ReadAPPElement()
# create_INPUT_CASE()
# create_WaitCase()
# file_renames()
# insert_code()
# scan_path()
# del_pyc()
# scan_backslash()
# add_ZenTao_id()
# add_basename()
