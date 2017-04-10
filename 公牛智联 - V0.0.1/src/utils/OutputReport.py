# coding:utf-8
import time

from data.Database import *


def write_report():
    with open(r"../report/Report.log", "w") as report:
        while True:
            report.write("adsfasdfasdfasdfasdfasdfas")
            print "adsfasdfasdfasdfasdfasdfas"
            time.sleep(1)
            if report_data != []:
                report.write(report_data[0])
                report_data.pop()
                time.sleep(1)
            else:
                time.sleep(1)
            break
