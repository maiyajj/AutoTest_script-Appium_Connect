# coding=utf-8
import os
import re


def scan_case_name():
    len_case = {0: [], 1: []}
    case_attr = []
    rootdir = r"./src/testcase/case"  # 指明被遍历的文件夹
    with open(u"./report/自动化测试用例对照表.log", "w") as cast_title:
        cast_title.write(u"自动化测试用例对照表:\n".encode("utf-8"))
        for parent, dirnames, filenames in os.walk(rootdir):  # 三个参数：分别返回1.父目录 2.所有文件夹名字（不含路径） 3.所有文件名字
            for filename in filenames:
                if "GNAPP" in filename and "pyc" not in filename:
                    with open(os.path.join(parent, filename), "r") as files:
                        file = files.read()
                        case_module = re.findall(r"self.case_module = u(.+) +\#", file)[0][1:-2]
                        case_name = re.findall(r"self.case_title = u(.+) +\#", file)[0][1:-2]
                        ZenTao_id = re.findall(r"self.ZenTao_id = (.+) +\#", file)[0][:-1]
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
