# -*- coding: utf-8 -*-
import os

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

    def style(self,
              Ft_n="SimSun",
              Ft_h=11,
              Ft_b=False,
              ALIGN="AllCenter",
              Brds=("R", "L", "T", "B"),
              Pat=1):
        Style = XFStyle()
        font = Font()  # Create the Font
        font.name = Ft_n
        font.height = Ft_h * 20
        font.bold = Ft_b
        Style.font = font

        borders = Borders()  # Create Borders
        for bdr in Brds:
            if bdr == "R":
                borders.right = Borders.THIN
                borders.right_colour = 0x40
            elif bdr == "L":
                borders.left = Borders.THIN  # May be: NO_LINE, THIN, MEDIUM, DASHED, DOTTED, THICK, DOUBLE, HAIR, MEDIUM_DASHED, THIN_DASH_DOTTED, MEDIUM_DASH_DOTTED, THIN_DASH_DOT_DOTTED, MEDIUM_DASH_DOT_DOTTED, SLANTED_MEDIUM_DASH_DOTTED, or 0x00 through 0x0D.
                borders.left_colour = 0x40
            elif bdr == "T":
                borders.top = Borders.THIN
                borders.top_colour = 0x40
            elif bdr == "B":
                borders.bottom = Borders.THIN
                borders.bottom_colour = 0x40
        Style.borders = borders  # Add Borders to Style

        alignment = Alignment()
        if ALIGN == "AllCenter":
            alignment.horz = Alignment.HORZ_CENTER
            alignment.vert = Alignment.VERT_CENTER
        elif ALIGN == "HCENTER":
            alignment.horz = Alignment.HORZ_CENTER
        elif ALIGN == "HLEFT":
            alignment.horz = Alignment.HORZ_LEFT
        elif ALIGN == "HRIGHT":
            alignment.horz = Alignment.HORZ_RIGHT
        elif ALIGN == "HCENERAL":
            alignment.horz = Alignment.HORZ_GENERAL
        elif ALIGN == "VCENTER":
            alignment.vert = Alignment.VERT_CENTER
        elif ALIGN == "WARP":
            alignment.wrap = Alignment.WRAP_AT_RIGHT
        elif ALIGN == "NONE":
            pass
        Style.alignment = alignment

        pattern = Pattern()  # 创建一个模式
        pattern.pattern = Pattern.SOLID_PATTERN  # 设置其模式为实型
        pattern.pattern_fore_colour = Pat
        # 设置单元格背景颜色 0 = Black, 1 = White, 2 = Red, 3 = Green, 4 = Blue, 5 = Yellow, 6 = Magenta,  the list goes on...
        Style.pattern = pattern  # 将赋值好的模式参数导入Style
        return Style

    def run(self):
        self.sheet_name = "%s{%s}" % (self.device_info["model"], self.device_info["udid"])
        os.getenv('Temp')
        self.folder = "%s{%s}.xls" % (self.device_info["model"], self.device_info["udid"])
        with open(self.folder, "w") as files:
            del files
        self.book = Workbook(encoding='utf-8')
        self.style()
        self.style_none = self.style(ALIGN="NONE")
        self.style_allctr = self.style()
        self.style_hleft = self.style(ALIGN="HLEFT")
        self.warp = self.style(ALIGN="WARP")
        self.style_blod = self.style(Ft_b=True)

        self.sheet = self.book.add_sheet(self.sheet_name)
        self.write_title()
        self.book.save(self.folder)
        return self.book

    def write_title(self):
        self.sheet.col(0).width = 256 * 14
        self.sheet.col(1).width = 256 * 56
        for i in xrange(2, 7):
            self.sheet.col(i).width = 256 * 9

        # self.sheet.write_merge(0, 1, 0, 7, u"测试报告", self.style(ALIGN="HLEFT", Pat=22))
        # self.sheet.write_merge(0, 1, 0, 7, u"1、密码修改页面，旧密码输入错误，提示信息检查", self.style(ALIGN="HLEFT", Pat=22))
        # self.sheet.write_merge(0, 1, 0, 7, u"1、密码修改页面，旧密码输入错误，提示信息检查", self.style(ALIGN="HLEFT", Pat=22))
        print help(easyxf)
        self.sheet.write_merge(6, 6, 0, 2, "Status", easyxf(
            'font: height 240, name Arial, colour_index black, bold on, italic off; align: wrap on, vert centre, horiz left;'
            'borders: top double, bottom double, left dashed, right double;'
            'pattern: pattern solid, fore_colour 23'))
        self.sheet.write(12, 0, "ZenTao_ID", self.style(ALIGN="HLEFT", Pat=23))
        self.sheet.write(12, 1, "Test Group/Test Case", self.style(ALIGN="HLEFT", Pat=23))
        self.sheet.write(12, 2, "Count", self.style(ALIGN="HLEFT", Pat=23))
        self.sheet.write(12, 3, "Pass", self.style(ALIGN="HLEFT", Pat=23))
        self.sheet.write(12, 4, "Fail", self.style(ALIGN="HLEFT", Pat=23))
        self.sheet.write(12, 5, "Error", self.style(ALIGN="HLEFT", Pat=23))
        self.sheet.write(12, 6, "Wait", self.style(ALIGN="HLEFT", Pat=23))
        self.sheet.write(12, 7, "Result", self.style(ALIGN="HLEFT", Pat=23))

    def write_data(self, Zentao, Count=0, Pass=0, Fail=0, Error=0, Wait=0):
        self.row = 13

        self.sheet.write(self.row, 0, Zentao, self.style(ALIGN="HLEFT", Pat=22))
        self.sheet.write(self.row, 1, u"密码修改页面，旧密码输入错误，提示信息检查", self.style(ALIGN="HLEFT", Pat=22))
        self.sheet.write(self.row, 2, Count, self.style(ALIGN="HRIGHT", Pat=22))
        self.sheet.write(self.row, 3, Pass, self.style(ALIGN="HRIGHT", Pat=22))
        self.sheet.write(self.row, 4, Fail, self.style(ALIGN="HRIGHT", Pat=22))
        self.sheet.write(self.row, 5, Error, self.style(ALIGN="HRIGHT", Pat=22))
        self.sheet.write(self.row, 6, Wait, self.style(ALIGN="HRIGHT", Pat=22))

        data = 'IF({1}{0}>0,"Pass",IF({2}{0}>0,"Fail",IF({3}{0}>0,"Error",IF({4}{0}>0,"Wait",""))))'. \
            format(self.row + 1, chr(68), chr(69), chr(70), chr(71))
        self.sheet.write(self.row, 7, Formula(data), self.style(ALIGN="AllCenter", Pat=22))

        self.book.save(self.folder)


device_list = {'8681-M02-0xa0a151df': {'deviceName': '8681-M02', 'log_name': '8681-M02', 'bp_port': 4726,
                                       'udid': '8681-M02-0xa0a151df',
                                       'desired_caps': {'unicodeKeyboard': 'True', 'deviceName': '8681-M02',
                                                        'driver': '8681-M02-0xa0a151df', 'browserName': '',
                                                        'resetKeyboard': 'True', 'platformVersion': '5.1',
                                                        'appPackage': 'com.iotbull.android.superapp',
                                                        'platformName': 'Android',
                                                        'appActivity': 'com.iotbull.android.superapp.activitys.regist_login.SplashActivity'},
                                       'platformVersion': '5.1', 'model': '8681_M02', 'platformName': 'Android',
                                       'port': 4725, 'dpi': {'width': '1080', 'height': '1920'}}}
device_name = '8681-M02-0xa0a151df'

xls = WriteXls(device_list, device_name)
xls.write_data(1970, 1, 1, 0, 0, 0)
