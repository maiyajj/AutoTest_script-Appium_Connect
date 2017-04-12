# coding:utf-8
import os
import re

rootdir = r"..\src\testcase\case"  # 指明被遍历的文件夹
with open(u"..\\report\\自动化测试用例对照表.log", "w") as cast_title:
    cast_title.write(u"自动化测试用例对照表:\n")
    for parent, dirnames, filenames in os.walk(rootdir):  # 三个参数：分别返回1.父目录 2.所有文件夹名字（不含路径） 3.所有文件名字
        for filename in filenames:
            if "GNAPP" in filename and "pyc" not in filename:
                with open(os.path.join(parent, filename), "r") as files:
                    file = files.read()
                    name = re.findall(r"self.case_title = u(.+)", file)[0][1:-1]
                    class_name = re.findall(r"class (.+)\(", file)[0]
                    cast_title.write("[%s: u'%s']\n" % (class_name, name))  #
