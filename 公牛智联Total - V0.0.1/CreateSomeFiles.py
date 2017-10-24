# coding=utf-8
try:
    from src.testcase.case.WaitCase import *
except ImportError:
    pass
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
            files.write("# 由CreateSomeFiles.py生成\n")
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
            files.write("from AppPageElement_%s_iOS import *\n\n\n" % app)
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
                if i != b[-1]:
                    files.write("    def %s(self):\n" % i)
                    files.write("        return self.wrapper(self.pwa.{0}(), self.pwi.{0}())\n\n".format(i))
                else:
                    files.write("    def %s(self):\n" % i)
                    files.write("        return self.wrapper(self.pwa.{0}(), self.pwi.{0}())\n".format(i))

    def create_INPUT_CASE(self):
        rootdir = r"./"
        for parents, dirnames, filenames in os.walk(rootdir):
            for filename in filenames:
                if ".DS_Store" in filename:
                    os.remove(os.path.join(parents, filename))
        # 写INPUT_CASE文件夹内容
        rootdir = r"./src/testcase/case/"  # 指明被遍历的文件夹
        for parents, dirnames, filenames in os.walk(rootdir):  # 三个参数：分别返回1.父目录 2.所有文件夹名字（不含路径） 3.所有文件名字
            for dirname in [i for i in dirnames if "_" not in i and "APP" in i]:
                name = dirname[:2]
                app_name = name + "APP"
                file_list = []
                files_list = {}
                file_path = os.path.join(rootdir, "%s/INPUT_CASE" % app_name)
                for parent, dirnames, filenames in os.walk(os.path.join(parents, dirname)):
                    for dirname in [i for i in dirnames if "INPUT_CASE" not in i]:
                        path_tmp = os.path.join(parent, dirname)
                        files = [i for i in os.listdir(path_tmp) if "pyc" not in i and "init" not in i]
                        input_name = files[0][:-7]
                        tmp = ""
                        for i in [i.capitalize() for i in input_name.split("_")[1:]]:
                            tmp = tmp + i
                        input_names = "%sApp" % name + tmp + ".py"
                        file_list.append(input_names)
                        files_list[input_names] = files
                print file_list
                for k, v in files_list.items():
                    vv = [i[:-3] for i in v]
                    with open(os.path.join(file_path, k), "w") as files:
                        files.write("# coding=utf-8" + "\n")
                        vv = ["from src.testcase.case.%s.%s.%s import *" % (app_name, i[:-4], i) for i in vv]
                        for i in vv:
                            files.write(i + "\n")
                        files.write("\n")
                        vv = ["%s%s%s" % (i[:2], "".join([x.capitalize() for x in i[2:-7].split("_")]),
                                          str(int(i[-6:-3]))) for i in v]
                        for i in vv:
                            files.write("{0} = {0}".format(i) + "\n")

                with open(os.path.join(file_path, "%sAppInputCase.py" % name), "w") as files:
                    files.write("# coding=utf-8" + "\n")
                    for i in [i[:-3] for i in file_list]:
                        files.write("from src.testcase.case.%s.INPUT_CASE.%s import *" % (app_name, i) + "\n")
                    files.write("\n")
                    for i in [i[:-3] + "1" for i in file_list]:
                        files.write("{0} = {0}".format(i) + "\n")

    def correct_func_name(self):
        result = []
        rootdir = r"./src/testcase/case/"  # 指明被遍历的文件夹
        for parents, dirnamess, filenamess in os.walk(rootdir):
            for dirnames in dirnamess:
                for parent, dirnames, filenames in os.walk(os.path.join(parents, dirnames)):
                    for filename in [i for i in filenames if "APP" in i and "pyc" not in i]:
                        with open(os.path.join(parent, filename), "r") as files:
                            filename = "%s%s%s" % (filename[:2],
                                                   "".join([i.capitalize() for i in filename[2:-7].split("_")]),
                                                   str(int(filename[-6:-3])))
                            result.append(filename == re.findall("class (.+?)\(", files.read())[0])
        result = list(set(result))
        print result

    def create_WaitCase(self):
        rootdir = r"./src/testcase/case"
        CaseList = []
        for parent, dirnames, filenames in os.walk(rootdir):
            for filename in [i for i in filenames if "APP" in i and "pyc" not in i]:
                with open(os.path.join(parent, filename), "r") as files:
                    file = files.read()
                    class_name = re.findall(r"class (.+)\(", file)[0]
                    case_name = re.findall(r"self.case_title = u(.+) +\#", file)[0][1:-2]
                    ZenTao_id = re.findall(r"self.zentao_id = (.+) +\#", file)[0][:-1]
                    CaseList.append(["self.write_report(%s)" % class_name, " # %s," % ZenTao_id, case_name])
        for x, y, z in CaseList:
            print x, y, z

CF = CreateFunc()
CF.create_INPUT_CASE()
CF.create_AppPageElement(MainPageWidgetAndroidJD, PopupWidgetAndroidJD)
CF.create_AppPageElement(MainPageWidgetAndroidGN, PopupWidgetAndroidGN)
CF.create_AppPageElement(MainPageWidgetAndroidAL, PopupWidgetAndroidAL)
CF.create_ReadAPPElement(MainPageWidgetAndroidGN, PopupWidgetAndroidGN)
CF.create_ReadAPPElement(MainPageWidgetAndroidJD, PopupWidgetAndroidJD)
CF.create_ReadAPPElement(MainPageWidgetAndroidAL, PopupWidgetAndroidAL)
CF.correct_func_name()
CF.create_WaitCase()
