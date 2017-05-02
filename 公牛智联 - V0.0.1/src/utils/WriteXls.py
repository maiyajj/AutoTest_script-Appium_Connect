# -*- coding: utf-8 -*-
import datetime
import os
import time

from xlwt import *

'''
# font.bold = True
# font.underline = True
# font.italic = True
XFStyle用于设置字体样式，有描述字符串num_format_str，字体font，
居中alignment，边界borders，模式pattern，保护protection等属性。
另外还可以不写单元格，直接设置格式

  # Create Alignment
#设置单元格对齐方式 
alignment.horz = Alignment.HORZ_CENTER
***May be: HORZ_GENERAL, HORZ_LEFT, HORZ_CENTER,
***HORZ_RIGHT, HORZ_FILLED, HORZ_JUSTIFIED,
***HORZ_CENTER_ACROSS_SEL, HORZ_DISTRIBUTED
alignment.vert = Alignment.VERT_CENTER  # May be: VERT_TOP, VERT_CENTER, VERT_BOTTOM, VERT_JUSTIFIED, VERT_DISTRIBUTED
style = XFStyle()  # Create Style
style.alignment = alignment

# font_sty = [u"微软雅黑", 11]
'''


class WriteXls(object):
    def __init__(self, device_list, device_name):
        self.device_list = device_list
        self.device_name = device_name
        self.device_info = device_list[device_name]
        self.run()

    def style(self):
        self.xfstyle = XFStyle()

        font = Font()
        font.height = 11 * 20
        font.name = u"宋体"

        borders = Borders()
        borders.top = Borders.THIN
        borders.bottom = Borders.THIN
        borders.left = Borders.THIN
        borders.right = Borders.THIN

        align = Alignment()
        align.horz = Alignment.HORZ_CENTER

        self.xfstyle.font = font
        self.xfstyle.borders = borders
        self.xfstyle.alignment = align

    def run(self):
        self.case_count = []
        self.style()
        self.sheet_name = "%s{%s}" % (self.device_info["model"], self.device_info["udid"])
        os.getenv('Temp')
        self.xls_file = "%s{%s}.xls" % (self.device_info["model"], self.device_info["udid"])
        with open(self.xls_file, "w") as files:
            del files
        self.book = Workbook(encoding='utf-8')
        self.sheet = self.book.add_sheet(self.sheet_name, cell_overwrite_ok=True)
        self.write_title()
        self.book.save(self.xls_file)
        return self.book

    def write_title(self):
        self.sheet.col(0).width = 256 * 15
        self.sheet.col(1).width = 256 * 56
        for i in xrange(2, 7):
            self.sheet.col(i).width = 256 * 9

        self.sheet.write_merge(0, 1, 0, 7, u"测试报告", easyxf(
            u'font: height 320, name 宋体, colour_index 70, bold on; align: wrap on, vert top, horiz left; borders: top thin, left thin, right thin;'))
        self.sheet.write_merge(2, 2, 0, 7, "", easyxf(
            u'font: height 220, name 宋体; align: wrap on; borders: left thin, right thin;'))

        self.sheet.write(3, 0, "Start Time:", easyxf(
            u'font: height 220, name 宋体, bold on; align: wrap on, horiz left; borders: left thin;'))

        self.start_time = time.strftime("%Y-%m-%d %H:%M:%S")
        self.sheet.write_merge(3, 3, 1, 7, self.start_time, easyxf(
            u'font: height 220, name 宋体; align: wrap on, horiz left; borders: right thin;'))

        self.sheet.write(4, 0, "Duration:", easyxf(
            u'font: height 220, name 宋体, bold on; align: wrap on, horiz left; borders: left thin;'))
        self.sheet.write_merge(4, 4, 1, 7, "0:00:00", easyxf(
            u'font: height 220, name 宋体; align: wrap on, horiz left; borders: right thin;'))

        self.sheet.write(5, 0, "Status:", easyxf(
            u'font: height 220, name 宋体, bold on; align: wrap on, horiz left; borders: left thin;'))
        self.sheet.write_merge(5, 5, 1, 7, "Pass 0", easyxf(
            u'font: height 220, name 宋体; align: wrap on, horiz left; borders: right thin;'))

        self.sheet.write(6, 0, "Total Case:", easyxf(
            u'font: height 220, name 宋体, bold on; align: wrap on, horiz left; borders: left thin;'))
        self.sheet.write_merge(6, 6, 1, 7, 0, easyxf(
            u'font: height 220, name 宋体; align: wrap on, horiz left; borders: right thin;'))

        self.sheet.write_merge(7, 7, 0, 7, "", easyxf(
            u'font: height 220, name 宋体; align: wrap on, horiz left; borders: left thin, right thin;'))
        self.sheet.write_merge(8, 8, 0, 7, u"用例执行情况：", easyxf(
            u'font: height 220, name 宋体; align: wrap on, horiz left; borders: left thin, right thin;'))
        self.sheet.write_merge(9, 9, 0, 7, "", easyxf(
            u'font: height 220, name 宋体; align: wrap on, horiz left; borders: left thin, right thin;'))

        row = 10
        write_list = ["ZenTao_ID", "Test Group/Test Case", "Count", "Pass", "Fail", "Error", "Wait", "Result"]
        for i in write_list:
            self.sheet.write(row, write_list.index(i), i, easyxf(
                u'font: height 220, name 宋体, colour_index white, bold on; align: wrap on, horiz left; borders: left thin, right thin; pattern: pattern solid, fore_colour 23'))

    def write_data(self, row, Zentao, Name, end_time, Count=0, Pass=0, Fail=0, Error=0, Wait=0):
        '''
        'font: height 240, name Arial, colour_index black, bold on, italic on;'
            'align: wrap on, vert centre, horiz left;'
            'borders: top NO_LINE, bottom THIN, left dashed, right double;'
            'pattern: pattern solid, fore_colour 23'
        :param row: 
        :param Zentao: 
        :param Name: 
        :param end_time: 
        :param Count: 
        :param Pass: 
        :param Fail: 
        :param Error: 
        :param Wait: 
        :return: 
        '''
        self.case_count.append(Zentao)
        self.sheet.write(row, 0, Zentao, easyxf(
            u'font: height 220, name 宋体; align: wrap on, horiz left; borders: top thin, bottom thin, left thin, right thin; pattern: pattern solid, fore_colour 22'))
        self.sheet.write(row, 1, Name, easyxf(
            u'font: height 220, name 宋体; align: wrap on, horiz left; borders: top thin, bottom thin, left thin, right thin; pattern: pattern solid, fore_colour 22'))
        self.sheet.write(row, 2, Count, easyxf(
            u'font: height 220, name 宋体; align: wrap on, horiz right; borders: top thin, bottom thin, left thin, right thin; pattern: pattern solid, fore_colour 22'))
        self.sheet.write(row, 3, Pass, easyxf(
            u'font: height 220, name 宋体; align: wrap on, horiz right; borders: top thin, bottom thin, left thin, right thin; pattern: pattern solid, fore_colour 22'))
        self.sheet.write(row, 4, Fail, easyxf(
            u'font: height 220, name 宋体; align: wrap on, horiz right; borders: top thin, bottom thin, left thin, right thin; pattern: pattern solid, fore_colour 22'))
        self.sheet.write(row, 5, Error, easyxf(
            u'font: height 220, name 宋体; align: wrap on, horiz right; borders: top thin, bottom thin, left thin, right thin; pattern: pattern solid, fore_colour 22'))
        self.sheet.write(row, 6, Wait, easyxf(
            u'font: height 220, name 宋体; align: wrap on, horiz right; borders: top thin, bottom thin, left thin, right thin; pattern: pattern solid, fore_colour 22'))
        formula = 'IF({1}{0}>0,"Pass",IF({2}{0}>0,"Fail",IF({3}{0}>0,"Error",IF({4}{0}>0,"Wait",""))))'. \
            format(row + 1, chr(68), chr(69), chr(70), chr(71))
        self.sheet.write(row, 7, Formula(formula), easyxf(
            u'font: height 220, name 宋体; align: wrap on, horiz centre; borders: top thin, bottom thin, left thin, right thin; pattern: pattern solid, fore_colour 22'))

        self.book.save(self.xls_file)
        self.write_total(row + 1, end_time)

    def write_total(self, row, end_times):
        self.sheet.write(row, 0, "Total", easyxf(
            u'font: height 220, name 宋体, bold on; align: wrap on, horiz left; borders: top thin, bottom thin, left thin;'))
        self.sheet.write(row, 1, "", easyxf(
            u'font: height 220, name 宋体, bold on; align: wrap on, horiz left; borders: top thin, bottom thin, right thin;'))
        for i in xrange(2, 7):
            formula = 'SUM({0}12:{0}{1})'.format(chr(i + 65), row)
            self.sheet.write(row, i, Formula(formula), easyxf(
                u'font: height 220, name 宋体; align: wrap on; borders: top thin, bottom thin, left thin, right thin;'))

        formula = 'COUNTIF(H12:H{0},"Pass")/COUNTA(H12:H{0})'.format(row)

        self.xfstyle.num_format_str = "0%"
        self.sheet.write(row, 7, Formula(formula), self.xfstyle)

        formula = '"Pass "&COUNTIF(H12:H{0},"Pass")'.format(row)
        self.sheet.write_merge(5, 5, 1, 7, Formula(formula), easyxf(
            u'font: height 220, name 宋体; align: wrap on, horiz left; borders: right thin;'))

        start_time = time.strptime(self.start_time, "%Y-%m-%d %H:%M:%S")
        end_time = time.strptime(end_times, "%Y-%m-%d %H:%M:%S")
        start_time = datetime.datetime(start_time[0], start_time[1], start_time[2],
                                       start_time[3], start_time[4], start_time[5])
        end_time = datetime.datetime(end_time[0], end_time[1], end_time[2],
                                     end_time[3], end_time[4], end_time[5])
        self.time = end_time - start_time
        self.sheet.write_merge(4, 4, 1, 7, str(self.time), easyxf(
            u'font: height 220, name 宋体; align: wrap on, horiz left; borders: right thin;'))

        self.sheet.write_merge(6, 6, 1, 7, len(set(self.case_count)), easyxf(
            u'font: height 220, name 宋体; align: wrap on, horiz left; borders: right thin;'))

        self.book.save(self.xls_file)

# device_list = {'8681-M02-0xa0a151df': {'deviceName': '8681-M02', 'log_name': '8681-M02', 'bp_port': 4726,
#                                        'udid': '8681-M02-0xa0a151df',
#                                        'desired_caps': {'unicodeKeyboard': 'True', 'deviceName': '8681-M02',
#                                                         'driver': '8681-M02-0xa0a151df', 'browserName': '',
#                                                         'resetKeyboard': 'True', 'platformVersion': '5.1',
#                                                         'appPackage': 'com.iotbull.android.superapp',
#                                                         'platformName': 'Android',
#                                                         'appActivity': 'com.iotbull.android.superapp.activitys.regist_login.SplashActivity'},
#                                        'platformVersion': '5.1', 'model': '8681_M02', 'platformName': 'Android',
#                                        'port': 4725, 'dpi': {'width': '1080', 'height': '1920'}}}
# device_name = '8681-M02-0xa0a151df'
#
# xls = WriteXls(device_list, device_name)
# xls.write_data(12, 1970, u"密码修改页面，旧密码输入错误，提示信息检查", 1, 1, 0, 0, 0)
# xls.write_data(13, 1970, u"密码修改页面，旧密码输入错误，提示信息检查", 1, 1, 0, 0, 0)
