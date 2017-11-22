# coding=utf-8
import linecache
import re

appium_path = u"/Users/Synapse/My_Engine/AutoTest_script-Appium_Connect/公牛智联Total - V0.0.1/AutoTestGNApp/2017-10-11 21-07/iPhone6sPlus-6910ec366b7e396-[2017-10-11 21-07-08].log"
debug_path = u"/Users/Synapse/My_Engine/AutoTest_script-Appium_Connect/公牛智联Total - V0.0.1/debug/2017-10-11_21.07/Debug_iPhone6sPlus-6910ec366b7e396 - [6910ec366b7e396410c2be813bff57ef1c9ccc7e].log"
# with open(r"%s" % appium_path, "r") as files:
#     print files.read()
debug_len = len(linecache.getlines(debug_path)) + 1
appium_len = len(linecache.getlines(appium_path)) + 1
flag = 0
debug_mess = []
time_point = []
for i in xrange(debug_len):
    tmp = linecache.getline(debug_path, i)
    if "ERROR:Traceback" in tmp or "ERROR:case_over:" in tmp:
        flag = 1
        time_point.append(re.findall("\[(.+?)\]", tmp)[0])
    if "Exception: " in tmp or "Error: " in tmp:
        flag = 0
        debug_mess.append(tmp)
    if flag == 1:
        debug_mess.append(tmp)
# for i in debug_mess:
#     print i

line_tmp = []
with open(r"%s" % appium_path, "r") as files:
    while appium_len > 0:
        tmp = files.readline()
        line_tmp.append(tmp)
        if (re.findall("\[(.+?)\]", tmp)
        appium_len -= 1
        appium_mess =[]
        for i in time_point:
            tmp = linecache.getlines(appium_path)





            # for i in xrange(appium_len):
            #     tmp = linecache.getline(appium_path, i)
            #     if "ERROR:Traceback" in tmp or "ERROR:case_over:" in tmp:
            #         flag = 1
            #         time_point.append(re.findall("\[(.+?)\]", tmp)[0])
            #     if "Exception: " in tmp or "Error: " in tmp:
            #         flag = 0
            #         debug_mess.append(tmp)
            #     if flag == 1:
            #         debug_mess.append(tmp)
