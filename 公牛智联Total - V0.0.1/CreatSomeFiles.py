# coding=utf-8
from src.testcase.case.WaitCase import *
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
        # 写INPUT_CASE文件夹内容
        rootdir = r"./src/testcase/case/"  # 指明被遍历的文件夹
        for parent, dirnames, filenames in os.walk(rootdir):  # 三个参数：分别返回1.父目录 2.所有文件夹名字（不含路径） 3.所有文件名字
            for dirname in [i for i in dirnames if "_" not in i]:
                if "GNAPP" in dirname:
                    file_list = []
                    files_list = {}
                    file_path = os.path.join(rootdir, "GNAPP/INPUT_CASE")
                    for parent, dirnames, filenames in os.walk(os.path.join(parent, dirname)):
                        for dirname in [i for i in dirnames if "INPUT_CASE" not in i]:
                            path_tmp = os.path.join(parent, dirname)
                            files = [i for i in os.listdir(path_tmp) if "pyc" not in i and "init" not in i]
                            input_name = files[0][:-7]
                            tmp = ""
                            for i in [i.capitalize() for i in input_name.split("_")[1:]]:
                                tmp = tmp + i
                            input_names = "GNApp" + tmp + ".py"
                            file_list.append(input_names)
                            files_list[input_names] = files

                    for k, v in files_list:
                        print k
                        print v
                        # with open(os.path.join(file_path,i), "w") as files:
                        #     files.write("# coding=utf-8\n")
                        # with open()
                        #     for filename in [i for i in filenames if "pyc" not in i and "init" not in i and "App" not in i]:
                        #         file_list.append(filename)
                        # print list(set(file_list))



                else:
                    rootpath = os.path.join(parent, dirname)


CF = CreateFunc()
# CF.create_INPUT_CASE()
CF.create_AppPageElement(MainPageWidgetAndroidJD, PopupWidgetAndroidJD)
CF.create_AppPageElement(MainPageWidgetAndroidGN, PopupWidgetAndroidGN)
CF.create_ReadAPPElement(MainPageWidgetAndroidGN, PopupWidgetAndroidGN)
CF.create_ReadAPPElement(MainPageWidgetAndroidJD, PopupWidgetAndroidJD)
