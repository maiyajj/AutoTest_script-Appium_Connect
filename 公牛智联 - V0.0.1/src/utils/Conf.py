# coding=utf-8
import os.path
import re

head = "# coding:utf-8\n" \
       "# 由Conf.py生成\n" \
       "import sys\n\n" \
       "import yaml\n\n" \
       "reload(sys)\n" \
       "sys.setdefaultencoding('utf-8')\n\n" \
       "conf = yaml.load(file(r'../config/Conf.yaml'))\n"
with open(r"../config/Conf.yaml", "r") as files:
    with open(r"../src/utils/ReadConf.py", "w") as tmp_file:
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

import re
from src.testcase.page.AppPageElement import *

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
with open(r"../src/utils/ReadAPPElement.py", "w") as files:
    files.write("# coding:utf-8")
    files.write("\n# 由Conf.py生成")
    files.write("\nfrom src.testcase.page.AppPageElement import *")
    files.write("\n")
    for i in a:
        files.write("\n%s = MainPageWidget().%s()" % (i, i))
    files.write("\n")
    for i in b:
        files.write("\n%s = PopupWidget().%s()" % (i, i))

# 写INPUT_CASE文件夹内容
rootdir = r"..\src\testcase\case"  # 指明被遍历的文件夹
with open(r"..\src\testcase\case\INPUT_CASE\GNAppDevicePage.py", "w") as DevicePage:
    DevicePage.write("# coding:utf-8\n")
    with open(r"..\src\testcase\case\INPUT_CASE\GNAppForgetPassword.py", "w") as ForgetPassword:
        ForgetPassword.write("# coding:utf-8\n")
        with open(r"..\src\testcase\case\INPUT_CASE\GNAppLogin.py", "w") as Login:
            Login.write("# coding:utf-8\n")
            with open(r"..\src\testcase\case\INPUT_CASE\GNAppMessageClassify.py", "w") as MessageClassify:
                MessageClassify.write("# coding:utf-8\n")
                with open(r"..\src\testcase\case\INPUT_CASE\GNAppPersonalSettings.py", "w") as PersonalSettings:
                    PersonalSettings.write("# coding:utf-8\n")
                    with open(r"..\src\testcase\case\INPUT_CASE\GNAppRegister.py", "w") as Register:
                        Register.write("# coding:utf-8\n")
                        for parent, dirnames, filenames in os.walk(rootdir):  # 三个参数：分别返回1.父目录 2.所有文件夹名字（不含路径） 3.所有文件名字
                            for filename in filenames:
                                if "GNAPP" in filename and "pyc" not in filename:
                                    if "GNAPP_DEVICE_PAGE" in filename:
                                        DevicePage.write(
                                            "from src.testcase.case.GNAPP_DEVICE_PAGE.%s import *\n" % filename[:-3])
                                    if "GNAPP_FORGET_PASSWORD" in filename:
                                        ForgetPassword.write(
                                            "from src.testcase.case.GNAPP_FORGET_PASSWORD.%s import *\n" % filename[
                                                                                                           :-3])
                                    if "GNAPP_LOGIN" in filename:
                                        Login.write("from src.testcase.case.GNAPP_LOGIN.%s import *\n" % filename[:-3])
                                    if "GNAPP_MESSAGE_CLASSIFY" in filename:
                                        MessageClassify.write(
                                            "from src.testcase.case.GNAPP_MESSAGE_CLASSIFY.%s import *\n" % filename[
                                                                                                            :-3])
                                    if "GNAPP_PERSONAL_SETTINGS" in filename:
                                        PersonalSettings.write(
                                            "from src.testcase.case.GNAPP_PERSONAL_SETTINGS.%s import *\n" % filename[
                                                                                                             :-3])
                                    if "GNAPP_REGISTER" in filename:
                                        Register.write(
                                            "from src.testcase.case.GNAPP_REGISTER.%s import *\n" % filename[:-3])
