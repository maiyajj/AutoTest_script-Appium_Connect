# coding=utf-8
from multiprocessing import *

import psutil
from src.testcase.case.WaitCase import *
from src.testcase.suite.ScanCaseName import *
from src.utils.LaunchAppiumServices import *
from src.utils.SendMail import *

_main_version = ""
_build_version = ""


class CreateFunc(object):
    def create_ReadAPPElement(self, func1, func2):
        app = str(func1.__name__)[-2:].upper()
        a = []
        b = []
        for i in dir(func1):
            tmp = re.findall("__.+", i)
            if tmp == []:
                a.append(i)
        for i in dir(func2):
            tmp = re.findall("__.+", i)
            if tmp == []:
                b.append(i)
        with open(r"./src/utils/ReadAPPElement_%s.py" % app, "w") as files:
            files.write("# coding=utf-8\n")
            files.write("# 由IncrementalUpdate.py生成\n")
            files.write("from src.testcase.page.AppPageElement import *\n\n\n")
            files.write("class PageElement%s(object):\n" % app)
            files.write("    def __init__(self, device, phone_os, app):\n")
            files.write("        self.mpw = MainPageWidget(phone_os, app).wrapper()\n")
            files.write("        self.device = device\n\n")
            files.write("    def get_page_element(self):\n")
            files.write('''        self.device["page"] = {}\n''')
            for i in a:
                files.write('''        self.device["page"]["{0}"] = self.mpw.{0}()\n'''.format(i))
            files.write('''\n''')
            for i in b:
                files.write('''        self.device["page"]["{0}"] = self.mpw.{0}()\n'''.format(i))

    def create_AppPageElement(self, func1, func2):
            app = str(func1.__name__)[-2:].upper()
            a = []
            b = []
            for i in dir(func1):
                tmp = re.findall("__.+", i)
                if tmp == []:
                    a.append(i)
            for i in dir(func2):
                tmp = re.findall("__.+", i)
                if tmp == []:
                    b.append(i)
            with open(r"./src/testcase/page/AppPageElement_%s.py" % app, "w") as files:
                files.write("# coding=utf-8\n")
                files.write("from AppPageElement_%s_Android import *\n" % app)
                files.write("from AppPageElement_%s_iOS import *\n\n" % app)
                files.write("class MainPageWidget%s(object):\n" % app)
                files.write("    def __init__(self, phone_os):\n")
                files.write("        self.phone_os = phone_os\n")
                files.write("        self.mpwa = MainPageWidgetAndroid%s()\n" % app)
                files.write("        self.mpwi = MainPageWidgetIos%s()\n" % app)
                files.write("        self.pwa = PopupWidgetAndroid%s()\n" % app)
                files.write("        self.pwi = PopupWidgetIos%s()\n" % app)
                files.write("    def wrapper(self, func1, func2):\n")
                files.write('''        if self.phone_os == "Android":\n''')
                files.write('''            return func1\n''')
                files.write('''        elif self.phone_os == "iOS":\n''')
                files.write('''            return func2\n''')
                files.write('''        else:\n''')
                files.write('''            raise KeyError("The OS is wrong!")\n\n''')
                for i in a:
                    files.write("    def %s(self):\n" % i)
                    files.write("        return self.wrapper(self.mpwa.{0}(), self.mpwi.{0}())\n\n".format(i))
                for i in b:
                    files.write("    def %s(self):\n" % i)
                    files.write("        return self.wrapper(self.pwa.{0}(), self.pwi.{0}())\n\n".format(i))

CreateFunc().create_AppPageElement(MainPageWidgetAndroidJD, PopupWidgetAndroidJD)
CreateFunc().create_AppPageElement(MainPageWidgetAndroidGN, PopupWidgetAndroidGN)
CreateFunc().create_ReadAPPElement(MainPageWidgetAndroidGN, PopupWidgetAndroidGN)
CreateFunc().create_ReadAPPElement(MainPageWidgetAndroidJD, PopupWidgetAndroidJD)
