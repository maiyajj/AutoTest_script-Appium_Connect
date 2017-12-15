# -*- coding: utf-8 -*-
import os
import re


def local_import(rootDir):
    # 判断传入的路径下是否有“__init__.py”这个文件了，如果没有则创建，否则import会认为没有这个moudle
    if os.path.exists(rootDir):
        arr = rootDir.split("/")
        pathDir = ""
        for path in arr:
            pathDir = "%s%s/" % (pathDir, path)
            if pathDir != "./":
                if not os.path.exists("%s__init__.py" % pathDir):
                    with open("%s__init__.py" % pathDir, "w") as tmp:
                        del tmp
    # 遍历文件夹找出app_开头的py文件，导入，注意globals，否则作用域只是在这个函数下
    with open(r"./config/WaitCase.yaml", "r") as wait_case:
        for i in wait_case.readlines():
            import_module = re.findall("^ .+\[(.+?),", i)
            if import_module:
                exe_str = "from %s import * " % import_module[0]
                exec(exe_str, globals())

def global_import(rootDir):
    # 判断传入的路径下是否有“__init__.py”这个文件了，如果没有则创建，否则import会认为没有这个moudle
    if os.path.exists(rootDir):
        arr = rootDir.split("/")
        pathDir = ""
        for path in arr:
            pathDir = "%s%s/" % (pathDir, path)
            if pathDir != "./":
                if not os.path.exists("%s__init__.py" % pathDir):
                    with open("%s__init__.py" % pathDir, "w") as tmp:
                        del tmp
    # 遍历文件夹找出app_开头的py文件，导入，注意globals，否则作用域只是在这个函数下
    for dirName, subdirList, fileList in os.walk(rootDir):
        for file_name in fileList:
            if "GN_APP" in file_name and "pyc" not in file_name:
                impPath = ""
                if dirName[-1:] != "/":
                    dirName = dirName.replace("\\", "/")
                    impPath = dirName.replace("/", ".")[2:]
                else:
                    dirName = dirName.replace("\\", "/")
                    impPath = dirName.replace("/", ".")[2:-1]
                if impPath != "":
                    exe_str = "from %s.%s import * " % (impPath, file_name[:-3])
                else:
                    exe_str = "from %s import * " % file_name[:-3]
                print exe_str
                exec (exe_str, globals())

local_import(r"./src/testcase/case")