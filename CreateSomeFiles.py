# coding=utf-8
try:
    import src.testcase.GN_APP.WaitCase as gn_app_wc
    import src.testcase.GN_F1331.WaitCase as gn_f1331_wc
    import src.testcase.GN_Y201H.WaitCase as gn_201h_wc
    import src.testcase.GN_Y201J.WaitCase as gn_201j_wc
    import src.testcase.GN_Y201S.WaitCase as gn_201s_wc
except ImportError as e:
    print(e)
from src.utils.SendMail import *

_main_version = ""
_build_version = ""


class CreateFunc(object):
    def create_ReadAPPElement(self, func1, app):
        app_list = {"GN_Y201S": u"阿里智能-GN_Y201S",
                    "GN_APP": u"公牛智联-GN_APP",
                    "GN_Y201J": u"京东微联-GN_Y201J",
                    "GN_Y201H": u"智能家居-GN_Y201H",
                    "GN_F1331": u"京东微联-GN_F1331"}
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
        with open(r"./src/testcase/%s/page/ReadAPPElement.py" % app, "w", encoding="utf-8") as files:
            files.write("# coding=utf-8\n")
            files.write(u"# 由CreateSomeFiles.py生成\n")
            files.write("from src.testcase.%s.page.AppPageElement import *\n\n\n" % app)
            files.write("class PageElement(object):\n")
            files.write('    """\n')
            files.write(u'    %s all page element\n' % app_list[app])
            files.write('    """\n\n')
            files.write("    def __init__(self, phone_os):\n")
            files.write("        self.mpw = MainPageWidget(phone_os)\n\n")
            files.write("    def get_page_element(self):\n")
            files.write('''        return {\n''')
            for i in a:
                files.write('''            "{0}": self.mpw.{0}(),\n'''.format(i))
            files.write('''\n''')
            lb = len(b) - 1
            for i in b:
                if b.index(i) != lb:
                    files.write('''            "{0}": self.mpw.{0}(),\n'''.format(i))
                else:
                    files.write('''            "{0}": self.mpw.{0}()\n'''.format(i))
            files.write('''        }\n''')

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
        with open("./src/testcase/%s/page/AppPageElement.py" % app, "w", encoding="utf-8") as files:
            files.write("# coding=utf-8\n")
            files.write("from .AppPageElement_Android import *\n")
            files.write("from .AppPageElement_iOS import *\n\n\n")
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
        for device_n in tmp_dir:
            rootdir = "./src/testcase/%s/case" % device_n  # 指明被遍历的文件夹
            dirname_list = []
            for parents, dirnames, filenames in os.walk(rootdir):  # 三个参数：分别返回1.父目录 2.所有文件夹名字（不含路径） 3.所有文件名字
                for dirname in [i for i in dirnames if device_n in i]:
                    dirname_list.append(os.path.join(parents, dirname))
                    with open(os.path.join(rootdir, "%s/__init__.py" % dirname), "w", encoding="utf-8") as tmp:
                        del tmp

            file_path = os.path.join("./src/testcase/%s" % device_n, "input_case")
            if not os.path.exists(file_path):
                os.makedirs(file_path)
            with open("%s/__init__.py" % file_path, "w", encoding="utf-8") as tmp:
                del tmp

            file_list = []
            files_list = {}
            for x in dirname_list:
                files = [i for i in os.listdir(x) if "pyc" not in i and "init" not in i]
                input_name = files[0][:-7]
                tmp = device_n
                for i in [i.capitalize() for i in input_name.split("_")[2:]]:
                    tmp = tmp + "_" + i
                input_names = tmp + ".py"
                file_list.append(input_names)
                files_list[input_names] = files

            for k, v in files_list.items():
                vv = [i[:-3] for i in v]
                with open(os.path.join(file_path, k), "w", encoding="utf-8") as files:
                    files.write("# coding=utf-8\n")
                    files.write("try:\n")
                    # from src.testcase.GN_Y201S.case.GN_Y201S_CMP.GN_Y201S_CMP_001 import *
                    [files.write("    from src.testcase.%s.case.%s.%s import *\n" % (device_n, i[:-4], i)) for i in vv]
                    files.write("except ImportError as e:\n")
                    files.write("    print(e)\n")

            with open(os.path.join(file_path, "%s_Input_Case.py" % device_n), "w", encoding="utf-8") as files:
                files.write("# coding=utf-8\n")
                files.write("try:\n")
                for i in [i[:-3] for i in file_list]:
                    files.write("    from .%s import *\n" % i)
                files.write("except ImportError as e:\n")
                files.write("    print(e)\n")

    def correct_func_name(self):
        result = []
        rootdir = "./src/testcase/case/"  # 指明被遍历的文件夹
        for parents, dirnamess, filenamess in os.walk(rootdir):
            for dirnames in dirnamess:
                for parent, dirnames, filenames in os.walk(os.path.join(parents, dirnames)):
                    for filename in [i for i in filenames if "APP" in i and "pyc" not in i]:
                        with open(os.path.join(parent, filename), "r", encoding="utf-8") as files:
                            filename = "%s%s%s" % (filename[:2],
                                                   "".join([i.capitalize() for i in filename[2:-7].split("_")]),
                                                   str(int(filename[-6:-3])))
                            tmp = filename == re.findall("class (.+?)\(", files.read())[0]
                            result.append(tmp)
                            if not tmp:
                                print(filename)
        result = list(set(result))
        print(result)

    def create_WaitCase(self):
        CaseList = []
        tmp_dir = "./src/testcase"  # 指明被遍历的文件夹
        tmp_dir = [i for i in os.listdir(tmp_dir) if "_" in i and "__init__" not in i]
        for i in tmp_dir:
            rootdir = r"./src/testcase/%s/case" % i
            for parent, dirnames, filenames in os.walk(rootdir):
                for filename in [i for i in filenames if "GN_" in i and "pyc" not in i]:
                    with open(os.path.join(parent, filename), "r", encoding="utf-8") as files:
                        file = files.read()
                        class_name = re.findall(r"class (.+)\(", file)[0]
                        case_name = re.findall(r"self.case_title = u(.+) +#", file)[0][1:-2]
                        ZenTao_id = re.findall(r'self.zentao_id = "(\d+)"', file)[0]
                        CaseList.append(["self.write_report(%s)" % class_name, u" # %s," % ZenTao_id, case_name])
        for x, y, z in CaseList:
            try:
                print(x, end='')  # py3换行
            except SyntaxError:
                print(x),  # py2
            try:
                print(y, end='')
            except SyntaxError:
                print(y),
            print(z)


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
