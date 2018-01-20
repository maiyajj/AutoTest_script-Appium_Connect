# coding=utf-8
try:
    import src.testcase.GN_APP.WaitCase as gn_app_wc
    import src.testcase.GN_F1331.WaitCase as gn_f1331_wc
    import src.testcase.GN_Y201H.WaitCase as gn_201h_wc
    import src.testcase.GN_Y201J.WaitCase as gn_201j_wc
    import src.testcase.GN_Y201S.WaitCase as gn_201s_wc
except ImportError, e:
    print e
from src.utils.SendMail import *

_main_version = ""
_build_version = ""


class CreateFunc(object):
    def create_ReadAPPElement(self, func1, app):
        app_list = {"GN_Y201S": "阿里智能-GN_Y201S",
                    "GN_APP": "公牛智联-GN_APP",
                    "GN_Y201J": "京东微联-GN_Y201J",
                    "GN_Y201H": "智能家居-GN_Y201H",
                    "GN_F1331": "京东微联-GN_F1331"}
        tmp_list = []
        for i in dir(func1("Andriod").mpwa):
            tmp = re.findall("__.+", i)
            if not tmp and 'wrapper' not in i:
                tmp_list.append(i)
        for i in dir(func1("Andriod").pwa):
            tmp = re.findall("__.+", i)
            if not tmp and 'wrapper' not in i:
                tmp_list.append(i)
        a = [i for i in tmp_list if "_page" in i]
        b = [i for i in tmp_list if "_popup" in i]
        with open(r"./src/testcase/%s/page/ReadAPPElement.py" % app, "w") as files:
            files.write("# coding=utf-8\n")
            files.write("# 由CreateSomeFiles.py生成\n")
            files.write("from src.testcase.%s.page.AppPageElement import *\n\n\n" % app)
            files.write("class PageElement(object):\n")
            files.write('    """\n')
            files.write('    %s all page element\n' % app_list[app])
            files.write('    """\n\n')
            files.write("    def __init__(self, phone_os):\n")
            files.write("        self.mpw = MainPageWidget(phone_os)\n\n")
            files.write("    def get_page_element(self):\n")
            files.write('''        d = {}\n''')
            for i in a:
                files.write('''        d["{0}"] = self.mpw.{0}()\n'''.format(i))
            files.write('''\n''')
            for i in b:
                files.write('''        d["{0}"] = self.mpw.{0}()\n'''.format(i))
            files.write('''\n        return d\n''')

    def create_AppPageElement(self, func1, app):
        tmp_list = []
        for i in dir(func1("Andriod").mpwa):
            tmp = re.findall("__.+", i)
            if not tmp and 'wrapper' not in i:
                tmp_list.append(i)
        for i in dir(func1("Andriod").pwa):
            tmp = re.findall("__.+", i)
            if not tmp and 'wrapper' not in i:
                tmp_list.append(i)
        a = [i for i in tmp_list if "_page" in i]
        b = [i for i in tmp_list if "_popup" in i]
        with open("./src/testcase/%s/page/AppPageElement.py" % app, "w") as files:
            files.write("# coding=utf-8\n")
            files.write("from AppPageElement_Android import *\n")
            files.write("from AppPageElement_iOS import *\n\n\n")
            files.write("class MainPageWidget(object):\n")
            files.write("    def __init__(self, phone_os):\n")
            files.write("        self.phone_os = phone_os\n")
            files.write("        self.mpwa = MainPageWidgetAndroid()\n")
            files.write("        self.mpwi = MainPageWidgetIos()\n")
            files.write("        self.pwa = PopupWidgetAndroid()\n")
            files.write("        self.pwi = PopupWidgetIos()\n\n")
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
        rootdir = r"../"
        for parents, dirnames, filenames in os.walk(rootdir):
            for filename in filenames:
                if ".DS_Store" in filename:
                    os.remove(os.path.join(parents, filename))

        tmp_dir = "./src/testcase"  # 指明被遍历的文件夹
        tmp_dir = [i for i in os.listdir(tmp_dir) if "_" in i and "__init__" not in i]
        # 写INPUT_CASE文件夹内容
        for device_name in tmp_dir:
            rootdir = "./src/testcase/%s/case" % device_name  # 指明被遍历的文件夹
            dirname_list = []
            for parents, dirnames, filenames in os.walk(rootdir):  # 三个参数：分别返回1.父目录 2.所有文件夹名字（不含路径） 3.所有文件名字
                for dirname in [i for i in dirnames if device_name in i]:
                    dirname_list.append(os.path.join(parents, dirname))
                    with open(os.path.join(rootdir, "%s/__init__.py" % dirname), "w") as tmp:
                        del tmp

            file_path = os.path.join("./src/testcase/%s" % device_name, "input_case")
            if not os.path.exists(file_path):
                os.makedirs(file_path)
            with open("%s/__init__.py" % file_path, "w") as tmp:
                del tmp

            file_list = []
            files_list = {}
            for x in dirname_list:
                files = [i for i in os.listdir(x) if "pyc" not in i and "init" not in i]
                input_name = files[0][:-7]
                tmp = device_name
                for i in [i.capitalize() for i in input_name.split("_")[2:]]:
                    tmp = tmp + "_" + i
                input_names = tmp + ".py"
                file_list.append(input_names)
                files_list[input_names] = files

            for k, v in files_list.items():
                vv = [i[:-3] for i in v]
                with open(os.path.join(file_path, k), "w") as files:
                    files.write("# coding=utf-8" + "\n")
                    # from src.testcase.GN_Y201S.case.GN_Y201S_CMP.GN_Y201S_CMP_001 import *
                    vv = ["from src.testcase.%s.case.%s.%s import *" % (device_name, i[:-4], i) for i in vv]
                    for i in vv:
                        files.write(i + "\n")
                    files.write("\n")
                    vv = ["%s%s%s" % ("".join([x for x in i[:-7].split("_")[:2]]),
                                      "".join([x.capitalize() for x in i[:-7].split("_")[2:]]),
                                      str(int(i[-6:-3]))) for i in v]
                    for i in vv:
                        files.write("{0} = {0}".format(i) + "\n")

            with open(os.path.join(file_path, "%s_Input_Case.py" % device_name), "w") as files:
                files.write("# coding=utf-8" + "\n")
                for i in [i[:-3] for i in file_list]:
                    files.write("from %s import *" % i + "\n")
                files.write("\n")
                for i in ["%s%s1" % ("".join([x for x in i[:-3].split("_")[:2]]),
                                     "".join([x.capitalize() for x in i[:-3].split("_")[2:]]),) for i in file_list]:
                    files.write("{0} = {0}".format(i) + "\n")

    def correct_func_name(self):
        result = []
        rootdir = "./src/testcase/case/"  # 指明被遍历的文件夹
        for parents, dirnamess, filenamess in os.walk(rootdir):
            for dirnames in dirnamess:
                for parent, dirnames, filenames in os.walk(os.path.join(parents, dirnames)):
                    for filename in [i for i in filenames if "APP" in i and "pyc" not in i]:
                        with open(os.path.join(parent, filename), "r") as files:
                            filename = "%s%s%s" % (filename[:2],
                                                   "".join([i.capitalize() for i in filename[2:-7].split("_")]),
                                                   str(int(filename[-6:-3])))
                            tmp = filename == re.findall("class (.+?)\(", files.read())[0]
                            result.append(tmp)
                            if not tmp:
                                print filename
        result = list(set(result))
        print result

    def create_WaitCase(self):
        CaseList = []
        tmp_dir = "./src/testcase"  # 指明被遍历的文件夹
        tmp_dir = [i for i in os.listdir(tmp_dir) if "_" in i and "__init__" not in i]
        for i in tmp_dir:
            rootdir = r"./src/testcase/%s/case" % i
            for parent, dirnames, filenames in os.walk(rootdir):
                for filename in [i for i in filenames if "GN_" in i and "pyc" not in i]:
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
app_l = {"GN_Y201S": gn_201s_wc.MainPageWidget,
         "GN_APP": gn_app_wc.MainPageWidget,
         "GN_Y201J": gn_201j_wc.MainPageWidget,
         "GN_Y201H": gn_201h_wc.MainPageWidget,
         "GN_F1331": gn_f1331_wc.MainPageWidget}
[CF.create_AppPageElement(v, k) or CF.create_ReadAPPElement(v, k) for k, v in app_l.items()]
# CF.correct_func_name()
CF.create_WaitCase()
