# coding=utf-8
import linecache
import os.path
import re
import sys
from codecs import open

if sys.version_info[:1] > (2,):
    xrange = range


def create_WaitCase():
    rootdir = r"./src/testcase/case"
    CaseList = []
    for parent, dirnames, filenames in os.walk(rootdir):
        for filename in filenames:
            if "GN_APP" in filename and "pyc" not in filename:
                with open(os.path.join(parent, filename), "r", encoding="utf-8") as files:
                    file = files.read()
                    class_name = re.findall(r"class (.+)\(", file)[0]
                    case_name = re.findall(r"self.case_title = u(.+) +#", file)[0][1:-2]
                    ZenTao_id = re.findall(r'self.ZenTao_id = "(.+)" +#', file)[0][:-1]
                    CaseList.append([class_name, case_name, ZenTao_id])
    with open(r"./src/testcase/case/WaitCase.py", "w", encoding="utf-8") as WaitCase:
        WaitCase.write('''# coding=utf-8\n''')
        WaitCase.write('''import os\n''')
        WaitCase.write('''import re\n''')
        WaitCase.write('''import time\n''')
        WaitCase.write('''\n''')
        WaitCase.write('''from data.Database import *\n''')
        WaitCase.write('''from src.testcase.case.input_case.GNAppAccountSettings import *\n''')
        WaitCase.write('''from src.testcase.case.input_case.GNAppDevicePage import *\n''')
        WaitCase.write('''from src.testcase.case.input_case.GNAppFeedBack import *\n''')
        WaitCase.write('''from src.testcase.case.input_case.GNAppForgetPassword import *\n''')
        WaitCase.write('''from src.testcase.case.input_case.GNAppLogin import *\n''')
        WaitCase.write('''from src.testcase.case.input_case.GNAppMessageClassify import *\n''')
        WaitCase.write('''from src.testcase.case.input_case.GNAppRegister import *\n''')
        WaitCase.write('''from src.testcase.case.input_case.GNAppUsingHelp import *\n''')
        WaitCase.write('''from src.testcase.case.input_case.GNAppVersion import *\n''')
        WaitCase.write('''from src.utils.OutputReport import *\n\n\n''')

        WaitCase.write('''class WaitCase(object):\n''')
        WaitCase.write('''    def __init__(self, device_list, device_name):\n''')
        WaitCase.write('''        self.device_list = device_list\n''')
        WaitCase.write('''        self.device_name = device_name\n''')
        WaitCase.write('''        self.device_info = device_list[device_name]\n''')
        WaitCase.write('''        self.report = None\n''')
        WaitCase.write('''        self.debug = None\n''')
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
        WaitCase.write('''        self.debug = self.device_info["debug"]\n''')
        WaitCase.write('''\n''')
        WaitCase.write('''    def check_appium(self):\n''')
        WaitCase.write('''        while True:\n''')
        WaitCase.write('''            command = "netstat -aon|findstr %s" % self.device_info["port"]\n''')
        WaitCase.write('''            server = re.findall(r".+LISTENING.+", os.popen(command).read())\n''')
        WaitCase.write('''            if not server :\n''')
        WaitCase.write('''                time.sleep(1)\n''')
        WaitCase.write('''            else:\n''')
        WaitCase.write(
            '''                self.debug.info("Appium Sever Launch Success! %s" % time.strftime("%Y-%m-%d %X"))\n''')
        WaitCase.write('''                break\n''')
        WaitCase.write('''\n''')
        WaitCase.write('''    def run(self):\n''')
        WaitCase.write('''        self.debug.info("*" * 30)\n''')
        WaitCase.write(
            '''        self.debug.info(u"[APP_INF]deviceName：.....%s" % self.device_info["deviceName"])\n''')
        WaitCase.write('''        self.debug.info(u"[APP_INF]UDID：...........%s" % self.device_info["udid"])\n''')
        WaitCase.write(
            '''        self.debug.info(u"[APP_INF]platformName：...%s" % self.device_info["platformName"])\n''')
        WaitCase.write(
            '''        self.debug.info(u"[APP_INF]platformVersion：%s" % self.device_info["platformVersion"])\n''')
        WaitCase.write('''        self.debug.info(u"[APP_INF]appPackage：.....%s" % conf["App"]["GN"][0])\n''')
        WaitCase.write('''        self.debug.info(u"[APP_INF]appActivity：....%s" % conf["App"]["GN"][1])\n''')
        WaitCase.write('''        self.debug.info("*" * 30)\n''')
        WaitCase.write('''        database["case_location"] = self.No\n''')
        WaitCase.write('''        while True:\n''')
        WaitCase.write('''            self.debug.info("run times [%s]" % database["program_loop_time"])\n''')
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
        WaitCase.write('''        case = case_name(self.device_list, self.device_name, self.debug).result()\n''')
        WaitCase.write(
            '''        data = u'[RUN_TIMES=%s, CASE_ID=%s, CASE_NAME="%s", RESULT=%s, START=%s, CLOSE=%s]' % \\\n''')
        WaitCase.write(
            '''               (database["program_loop_time"], self.No, case[1], case[0], case[2], time.strftime("%Y-%m-%d %X"))\n''')
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
            if "GN_APP" in filename and "pyc" not in filename:
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
            if "GN_APP" in filename and "pyc" not in filename:
                with open(os.path.join(parent, filename), "r+", encoding="utf-8") as files:
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
                with open(os.path.join(parent, filename), "r", encoding="utf-8") as files:
                    name = re.findall(r"\.\./.+", files.read())
                    if name:
                        print(name)
                        print(os.path.join(parent, filename))


# 扫描文件中不是/分隔的
def scan_backslash():
    rootdir = r"./"
    for parent, dirnames, filenames in os.walk(rootdir):
        for filename in filenames:
            if "py" in filename and "pyc" not in filename and "init" not in filename:
                with open(os.path.join(parent, filename), "r", encoding="utf-8") as files:
                    name = re.findall(r'.+\\.+', files.read())
                    if name:
                        for i in name:
                            if "\\n" not in i:
                                print(i)
                                print(os.path.join(parent, filename))


# 全部添加禅道ID
def add_ZenTao_id():
    rootdir = r"./src/testcase/case"
    for parent, dirnames, filenames in os.walk(rootdir):
        for filename in filenames:
            if "GN_APP" in filename and "pyc" not in filename:
                filepath = os.path.join(parent, filename)
                lines = len(linecache.getlines(filepath))
                with open(filepath, "w", encoding="utf-8") as files:
                    for i in xrange(1, lines + 1):
                        if "self.case_title = " in linecache.getline(filepath, i):
                            print(i, linecache.getline(filepath, i),)
                            files.write(linecache.getline(filepath, i))
                            files.write("        self.ZenTao_id = \n")
                        elif '[CASE_ID="%s", CASE_TITLE="%s"]' in linecache.getline(filepath, i):
                            print(i, linecache.getline(filepath, i),)
                            files.write(
                                '''        self.debug.info(u'[GN_INF] <current case> [CASE_ID="%s", CASE_NAME="%s", 禅道ID="%s"]'\n''')
                        elif "os.path.basename" in linecache.getline(filepath, i):
                            print(i, linecache.getline(filepath, i),)
                            files.write(
                                '''                    % (os.path.basename(__file__).split(".")[0], self.case_title, self.ZenTao_id, self.case_module))\n''')
                        else:
                            files.write(linecache.getline(filepath, i))


def add_basename():
    rootdir = r"./src/testcase/case"
    for parent, dirnames, filenames in os.walk(rootdir):
        for filename in filenames:
            if "GN_APP" in filename and "pyc" not in filename:
                filepath = os.path.join(parent, filename)
                lines = len(linecache.getlines(filepath))
                with open(filepath, "w", encoding="utf-8") as files:
                    for i in xrange(1, lines + 1):
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
                print(filename)
                with open(filepath, "w", encoding="utf-8") as files:
                    for i in xrange(1, lines + 1):
                        if "# coding:utf-8" in linecache.getline(filepath, i):
                            print(linecache.getline(filepath, i))
                            files.write(linecache.getline(filepath, i).replace("# coding:utf-8", "# coding=utf-8"))
                        else:
                            files.write(linecache.getline(filepath, i))


def add_notes():
    rootdir = r"../testcase/"
    for parent, dirnames, filenames in os.walk(rootdir):
        for filename in filenames:
            if "GN_" in filename and "pyc" not in filename:
                filepath = os.path.join(parent, filename)
                lines = len(linecache.getlines(filepath))
                print(filename[:-3])
                # a = -100
                # with open(filepath, "r") as files:
                #     print linecache.getline(filepath, lines + 1 - 2)
                #     for i in xrange(1, lines + 1 - 2):
                #         if i == a:
                #             pass
                #         else:
                #             if '''def case(self):''' in linecache.getline(filepath, i):
                #                 a = i + 1
                #                 print "*" * 40
                #                 print filename, i
                #                 print linecache.getline(filepath, i)
                #                 files.write(linecache.getline(filepath, i))
                #             else:
                #                 files.write(linecache.getline(filepath, i))
                with open(filepath, "r", encoding="utf-8") as files:
                    for i in xrange(1, lines + 1):
                        if '''self.zentao_id =''' in linecache.getline(filepath, i):
                            value = linecache.getline(filepath, i)
                            if not re.findall('= "(.+?)" ', value):
                                tmp = re.findall('= (.+?) ', value)[0]
                                value = value.replace(tmp, '"%s"' % tmp)
                            # print(value)
                            files.write(value)
                        else:
                            files.write(linecache.getline(filepath, i))


def scan_repet():
    rootdir = r"./"
    tmp = []
    for parent, dirnames, filenames in os.walk(rootdir):
        for filename in filenames:
            if "pyc" not in filename:
                filepath = os.path.join(parent, filename)
                lines = len(linecache.getlines(filepath))
                tmp.append(lines)
    print(len(tmp))
    # print(lines)


def src_line():
    rootdir = r"./"
    line = 0
    for parent, dirnames, filenames in os.walk(rootdir):
        for filename in [i for i in filenames if "IncrementalUpdate" not in i and ".py" in i and "pyc" not in i]:
            lines = len(linecache.getlines(os.path.join(parent, filename)))
            line = lines + line
    print(line)


# src_line()

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
# scan_repet()
# check_AppPageElement()
# a = []
# b = []
# for i in dir(MainPageWidgetAndroid):
#     tmp = re.findall("__.+", i)
#     if not tmp:
#         a.append(i)
# for i in dir(PopupWidgetAndroid):
#     tmp = re.findall("__.+", i)
#     if not tmp:
#         b.append(i)
# script = r"src/testcase/case/ToLoginPage.py"
# with open(script, "r") as files:
#     page = files.read()
#     for i in a:
#         page = page.replace("%s" % i,'self.page["%s"]' % i)
#     for i in b:
#         page = page.replace("%s" % i, 'self.page["%s"]' % i)
# with open(script, "w") as files:
#     files.write(page)
# rootdir = r"./src/testcase/case"
# for parent, dirnames, filenames in os.walk(rootdir):
#     for filename in filenames:
#         if "GN_APP" in filename and "pyc" not in filename:
#             script = os.path.join(parent, filename)
#             with open(script, "r") as files:
#                 page = files.read()
#                 a = re.findall(r".+?(self.page\[.+])\[", page)
#                 # print a
#                 b = re.findall(r".+(self.page\[.+?])", page)
#                 # print b
#                 for i in xrange(len(a)):
#                     page = page.replace(a[i], b[i])
# for i in a:
#     page = page.replace("%s" % i,'self.page["%s"]' % i)
# for i in b:
#         page = page.replace("%s" % i, 'self.page["%s"]' % i)
#     with open(script, "w") as files:
#         files.write(page)
