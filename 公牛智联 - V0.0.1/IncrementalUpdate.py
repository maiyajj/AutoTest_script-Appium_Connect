# coding=utf-8
import linecache
import os.path
import re

from src.testcase.page.AppPageElement import *


def create_ReadConf():
    head = "# coding=utf-8\n" \
           "# 由IncrementalUpdate.py生成\n" \
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
        files.write("# coding=utf-8\n")
        files.write("# 由IncrementalUpdate.py生成\n")
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

    DevicePage.write("# coding=utf-8\n")
    ForgetPassword.write("# coding=utf-8\n")
    Login.write("# coding=utf-8\n")
    MessageClassify.write("# coding=utf-8\n")
    AccountSettings.write("# coding=utf-8\n")
    Register.write("# coding=utf-8\n")
    FeedBack.write("# coding=utf-8\n")
    UsingHelp.write("# coding=utf-8\n")
    Version.write("# coding=utf-8\n")

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
                    case_name = re.findall(r"self.case_title = u(.+) +\#", file)[0][1:-2]
                    ZenTao_id = re.findall(r"self.ZenTao_id = (.+) +\#", file)[0][:-1]
                    CaseList.append([class_name, case_name, ZenTao_id])
    with open(r"./src/testcase/case/WaitCase.py", "w") as WaitCase:
        WaitCase.write('''# coding=utf-8\n''')
        WaitCase.write('''import os\n''')
        WaitCase.write('''import re\n''')
        WaitCase.write('''import time\n''')
        WaitCase.write('''\n''')
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
        WaitCase.write('''from src.utils.CollectLog import *\n''')
        WaitCase.write('''from src.utils.OutputReport import *\n\n\n''')

        WaitCase.write('''class WaitCase(object):\n''')
        WaitCase.write('''    def __init__(self, device_list, device_name):\n''')
        WaitCase.write('''        self.device_list = device_list\n''')
        WaitCase.write('''        self.device_name = device_name\n''')
        WaitCase.write('''        self.device_info = device_list[device_name]\n''')
        WaitCase.write('''        self.report = None\n''')
        WaitCase.write('''        self.logger = None\n''')
        WaitCase.write('''        self.No = 1\n''')
        WaitCase.write('''\n''')
        WaitCase.write('''        self.create_log()\n''')
        WaitCase.write('''        self.create_report()\n''')
        WaitCase.write('''        self.check_appium()\n''')
        WaitCase.write('''        self.run()\n''')
        WaitCase.write('''\n''')
        WaitCase.write('''    def create_report(self):\n''')
        WaitCase.write('''        check_report(self.device_list, self.device_name)\n''')
        WaitCase.write('''        self.report = self.device_info["report"]\n''')
        WaitCase.write('''\n''')
        WaitCase.write('''    def create_log(self):\n''')
        WaitCase.write('''        check_log(self.device_list, self.device_name)\n''')
        WaitCase.write('''        self.logger = self.device_info["logger"]\n''')
        WaitCase.write('''\n''')
        WaitCase.write('''    def check_appium(self):\n''')
        WaitCase.write('''        while True:\n''')
        WaitCase.write('''            command = "netstat -aon|findstr %s" % self.device_info["port"]\n''')
        WaitCase.write('''            server = re.findall(r".+LISTENING.+", os.popen(command).read())\n''')
        WaitCase.write('''            if server == []:\n''')
        WaitCase.write('''                time.sleep(1)\n''')
        WaitCase.write('''            else:\n''')
        WaitCase.write(
            '''                self.logger.info("Appium Sever Launch Success! %s" % time.strftime("%Y-%m-%d %H:%M:%S"))\n''')
        WaitCase.write('''                break\n''')
        WaitCase.write('''\n''')
        WaitCase.write('''    def run(self):\n''')
        WaitCase.write('''        self.logger.info("*" * 30)\n''')
        WaitCase.write(
            '''        self.logger.info(u"[APP_INF]deviceName：.....%s" % self.device_info["deviceName"])\n''')
        WaitCase.write('''        self.logger.info(u"[APP_INF]UDID：...........%s" % self.device_info["udid"])\n''')
        WaitCase.write(
            '''        self.logger.info(u"[APP_INF]platformName：...%s" % self.device_info["platformName"])\n''')
        WaitCase.write(
            '''        self.logger.info(u"[APP_INF]platformVersion：%s" % self.device_info["platformVersion"])\n''')
        WaitCase.write('''        self.logger.info(u"[APP_INF]appPackage：.....%s" % conf["App"]["GN"][0])\n''')
        WaitCase.write('''        self.logger.info(u"[APP_INF]appActivity：....%s" % conf["App"]["GN"][1])\n''')
        WaitCase.write('''        self.logger.info("*" * 30)\n''')
        WaitCase.write('''        database["case_location"] = self.No\n''')
        WaitCase.write('''        while True:\n''')
        WaitCase.write('''            self.logger.info("run times [%s]" % database["program_loop_time"])\n''')
        for i in CaseList:
            if "Version" in i[0]:
                WaitCase.write('''            self.write_report(%s)  # %s, %s\n''' % (i[0], i[2], i[1]))
        for i in CaseList:
            if "Login" in i[0]:
                WaitCase.write('''            self.write_report(%s)  # %s, %s\n''' % (i[0], i[2], i[1]))
        for i in CaseList:
            if "AccountSettings" in i[0]:
                WaitCase.write('''            self.write_report(%s)  # %s, %s\n''' % (i[0], i[2], i[1]))
        for i in CaseList:
            if "Register" in i[0]:
                WaitCase.write('''            self.write_report(%s)  # %s, %s\n''' % (i[0], i[2], i[1]))
        for i in CaseList:
            if "ForgetPassword" in i[0]:
                WaitCase.write('''            self.write_report(%s)  # %s, %s\n''' % (i[0], i[2], i[1]))
        for i in CaseList:
            if "MessageClassify" in i[0]:
                WaitCase.write('''            self.write_report(%s)  # %s, %s\n''' % (i[0], i[2], i[1]))
        for i in CaseList:
            if "DevicePage" in i[0]:
                WaitCase.write('''            self.write_report(%s)  # %s, %s\n''' % (i[0], i[2], i[1]))
        for i in CaseList:
            if "FeedBack" in i[0]:
                WaitCase.write('''            # self.write_report(%s)  # %s, %s\n''' % (i[0], i[2], i[1]))
        for i in CaseList:
            if "UsingHelp" in i[0]:
                WaitCase.write('''            self.write_report(%s)  # %s, %s\n''' % (i[0], i[2], i[1]))
        for i in CaseList:
            if "ThemeStyle" in i[0]:
                WaitCase.write('''            self.write_report(%s)  # %s, %s\n''' % (i[0], i[2], i[1]))

        WaitCase.write('''\n            database["program_loop_time"] += 1\n\n''')

        WaitCase.write('''    def write_report(self, case_name):\n''')
        WaitCase.write('''        case = case_name(self.device_list, self.device_name, self.logger).result()\n''')
        WaitCase.write(
            '''        data = u'[RUN_TIMES=%s, CASE_ID=%s, CASE_NAME="%s", RESULT=%s, START=%s, CLOSE=%s]' % \\\n''')
        WaitCase.write(
            '''               (database["program_loop_time"], self.No, case[1], case[0], case[2], time.strftime("%Y-%m-%d %H:%M:%S"))\n''')
        WaitCase.write('''        self.report.info(data)\n''')
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
                                '''        self.logger.info('[GN_INF] <current case> [CASE_ID="%s", CASE_NAME="%s", 禅道ID="%s"]'\n''')
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


# 修改文件编码方式
def modified_utf():
    rootdir = r"./"
    for parent, dirnames, filenames in os.walk(rootdir):
        for filename in filenames:
            if "py" in filename and "pyc" not in filename and "init" not in filename and "IncrementalUpdate" not in filename:
                filepath = os.path.join(parent, filename)
                lines = len(linecache.getlines(filepath))
                print filename
                with open(filepath, "w") as files:
                    for i in range(1, lines + 1):
                        if "# coding:utf-8" in linecache.getline(filepath, i):
                            print linecache.getline(filepath, i)
                            files.write(linecache.getline(filepath, i).replace("# coding:utf-8", "# coding=utf-8"))
                        else:
                            files.write(linecache.getline(filepath, i))


def check_AppPageElement():
    import sys
    file = r"./src/testcase/page/AppPageElement.py"
    MainPage = [i for i in dir(MainPageWidget()) if "__" not in i]
    Popup = [i for i in dir(PopupWidget()) if "__" not in i]
    with open(file, "r") as app:
        app = app.read()
        for i in MainPage:
            print re.findall(r".+def %s.+" % i, app)
            print sys._getframe().f_lineno

# def print_element(element ,values):
#     if element == "account_setting_page":
#         MainPageWidget().account_setting_page()
#     if element == "add_device_failed_page":
#         MainPageWidget().add_device_failed_page()
#     if element == "app_help_page":
#         MainPageWidget().app_help_page()
#         if element == "change_nickname_page":
#          = MainPageWidget().change_nickname_page()
#         if element == "app_help_page":
#          = MainPageWidget().change_pwd_page()
#         if element == "app_help_page":
#         device_add_scan_page = MainPageWidget().device_add_scan_page()
#         if element == "app_help_page":
#         device_control_page = MainPageWidget().device_control_page()
#         if element == "app_help_page":
#         device_page = MainPageWidget().device_page()
#         if element == "app_help_page":
#         feedback_page = MainPageWidget().feedback_page()
#         if element == "app_help_page":
#         find_password_page = MainPageWidget().find_password_page()
#         if element == "app_help_page":
#         gender_page = MainPageWidget().gender_page()
#         if element == "app_help_page":
#         home_message_page = MainPageWidget().home_message_page()
#         if element == "app_help_page":
#         login_page = MainPageWidget().login_page()
#         if element == "app_help_page":
#         message_classify_page = MainPageWidget().message_classify_page()
#         if element == "app_help_page":
#         message_setting_page = MainPageWidget().message_setting_page()
#         if element == "app_help_page":
#         new_password_page = MainPageWidget().new_password_page()
#         if element == "app_help_page":
#         personal_settings_page = MainPageWidget().personal_settings_page()
#         if element == "app_help_page":
#         prepare_set_network_page = MainPageWidget().prepare_set_network_page()
#         if element == "app_help_page":
#         protocol_page = MainPageWidget().protocol_page()
#         if element == "app_help_page":
#         register_page = MainPageWidget().register_page()
#         if element == "app_help_page":
#         scan_with_subscribe_page = MainPageWidget().scan_with_subscribe_page()
#         if element == "app_help_page":
#         set_network_page = MainPageWidget().set_network_page()
#         if element == "app_help_page":
#         upgrade_page = MainPageWidget().upgrade_page()
#         if element == "app_help_page":
#         view_pager_page = MainPageWidget().view_pager_page()
#
#         if element == "app_help_page":
#         clear_activity_popup = PopupWidget().clear_activity_popup()
#         if element == "app_help_page":
#         clear_device_popup = PopupWidget().clear_device_popup()
#         if element == "app_help_page":
#
#         loading_popup = PopupWidget().loading_popup()
#         if element == "app_help_page":
#         login_popup = PopupWidget().login_popup()
#
#         if element == "app_help_page":
#         logout_popup = PopupWidget().logout_popup()
#         if element == "app_help_page":
#         terminate_add_device_popup = PopupWidget().terminate_add_device_popup()
#         if element == "app_help_page":
#         update_popup = PopupWidget().update_popup()
#
#     try:
#         print MainPageWidget().element()[values]
#     except NameError:
#         print PopupWidget().element()[values]

def add_notes():
    rootdir = r"./src/testcase/case"
    for parent, dirnames, filenames in os.walk(rootdir):
        for filename in filenames:
            if "GNAPP" in filename and "pyc" not in filename and "GNAPP_LOGIN_001" not in filename:
                filepath = os.path.join(parent, filename)
                lines = len(linecache.getlines(filepath))
                # print filename[:-3]
                with open(filepath, "w") as files:
                    for i in range(1, lines + 1):
                        if ''', self.ZenTao_id, self.case_title, self.start_time''' in linecache.getline(filepath, i):
                            # files.write("\n")
                            print filename, linecache.getline(filepath, i).replace(", self.test_count", "")
                            files.write(linecache.getline(filepath, i).replace(", self.test_count", ""))
                        # files.write('''        self.test_count += 1\n''')
                        else:
                            files.write(linecache.getline(filepath, i))

# create_ReadConf()  # 创建ReadConf.py 必须
# create_ReadAPPElement()  # 创建ReadAPPElement.py 必须
# create_INPUT_CASE()  # 创建INPUT_CASE.py 必须
# create_WaitCase()  # 创建WaitCase.py 必须
# file_renames() # 将文件名后缀从1变成001 可选
# insert_code() # 将每个用例中插入from appium import webdriver 可选
# scan_path() # 扫描with open（）中路径是不是../开头要变成./开头 可选
# del_pyc()# 删除所有pyc文件 可选
# scan_backslash() # 扫描with open（）中路径是/分隔符还是\分隔符 可选
# add_ZenTao_id() # 在每个用例中插入self.ZenTao_id = 可选
# add_basename() # 在每个用例中插入self.success = 0可选
# modified_utf()  # 将每个用例的# coding=utf-8变成# coding=utf-8 可选
add_notes()
# check_AppPageElement()
