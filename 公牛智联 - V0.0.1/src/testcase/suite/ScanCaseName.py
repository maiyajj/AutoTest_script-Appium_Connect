# coding:utf-8
import os
import re


def scan_case_name():
    len_case = {0: [], 1: []}
    case_attr = []
    rootdir = r"./src/testcase/case"  # 指明被遍历的文件夹
    with open(u"./report/自动化测试用例对照表.log", "w") as cast_title:
        cast_title.write(u"自动化测试用例对照表:\n")
        for parent, dirnames, filenames in os.walk(rootdir):  # 三个参数：分别返回1.父目录 2.所有文件夹名字（不含路径） 3.所有文件名字
            for filename in filenames:
                if "GNAPP" in filename and "pyc" not in filename:
                    with open(os.path.join(parent, filename), "r") as files:
                        file = files.read()
                        case_module = re.findall(r"self.case_module = u(.+)", file)[0][1:-1]
                        case_name = re.findall(r"self.case_title = u(.+)", file)[0][1:-1]
                        ZenTao_id = re.findall(r"self.ZenTao_id = (.+)", file)[0]
                        case_id = re.findall(r"class (.+)\(", file)[0]
                        case_attr.append([case_module, ZenTao_id, case_id, case_name])
                        len_case[0].append(len(case_module))
                        len_case[1].append(len(case_id))
        len_case_module = tuple(len_case[0])
        len_case_id = tuple(len_case[1])
        max_case_module = max(len_case_module)
        max_case_len = max(len_case_id)
        for i in case_attr:
            module_zen = max_case_module - len(i[0]) - 1 * (max_case_module - len(i[0])) / 3
            case_zen = max_case_len - len(i[2])
            cast_title.write("[CASE_MODULE='%s',%s  ZenTao_ID=%s,  CASE_ID=%s,%s  CASE_NAME='%s']\n"
                             % (i[0], " " * module_zen, i[1], i[2], " " * case_zen, i[3]))


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
