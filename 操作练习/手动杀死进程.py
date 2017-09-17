# # coding=utf-8
from multiprocessing import *
import os
import time, sys
import subprocess as sp
import psutil

#
# def aa():
#     sp.Popen("ping www.baidu.com -t")
#     # time.sleep(2)
# 
# if __name__ == "__main__":
#     # env = os.environ.copy()
#     # env["appium"] = "C:\\Software\\Developers\\Appium\\node_modules\\.bin\\appium.cmd"
#     # print env
#     while True:
#         # a = sp.Popen("ping www.baidu.com")
#         a = sp.Popen("appium",shell=True)
#         print a.pid
#         print psutil.Process(a.pid).cmdline()
#         print psutil.Process(a.pid).name()
#         time.sleep(1)
#         i= 0
#         while True:
#             if i == 300000:
#                 a.kill()
#                 break
#             else:
#                 time.sleep(1)
#                 i += 1
# 
# # a.join()
#         # print a.terminate()
# #
# # a = sp.Popen("ping www.baidu.com -t", shell=True)
# # print a.pid
# # print a.returncode
# # print "sss"


a = [20488]
b = a
result = a
import psutil
for i in a:
    child_proc = psutil.Process(i).children()
    if child_proc != []:
        for x in child_proc:
            b.append(x.pid)
            print x.pid, x.name(), x.parent()

print b
