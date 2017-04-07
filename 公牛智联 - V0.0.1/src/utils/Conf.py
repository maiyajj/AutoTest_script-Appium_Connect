# coding=utf-8
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
