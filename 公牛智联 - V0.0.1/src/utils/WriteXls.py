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
        elif ALIGN == "HGENERAL":
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

        self.book.save(self.folder)
        return self.book

    def write_data(self, Count=0, Pass=0, Fail=0, Error=0, Wait=0):
        self.sheet.col(0).width = 256 * 14
        self.sheet.col(1).width = 256 * 49
        self.sheet.col(2).width = 256 * 9
        self.sheet.col(3).width = 256 * 9
        self.sheet.write_merge(11, 11, 0, 1, u"1、密码修改页面，旧密码输入错误，提示信息检查", self.style(ALIGN="HLEFT", Pat=22))
        self.sheet.write_merge(12, 12, 0, 1, u"    禅道ID:1970", self.style_hleft)
        self.sheet.write(11, 2, Count, self.style(Pat=22))
        self.sheet.write(11, 3, Pass, self.style(Pat=22))
        self.sheet.write(11, 4, Fail, self.style(Pat=22))
        self.sheet.write(11, 5, Error, self.style(Pat=22))
        self.sheet.write(11, 6, Wait, self.style(Pat=22))

        if Fail <= 1:
            self.sheet.write_merge(12, 12, 2, 6, u"Pass", self.style_allctr)
        else:
            self.sheet.write_merge(12, 12, 2, 6, u"Fail", self.style_allctr)
        self.book.save(self.folder)
