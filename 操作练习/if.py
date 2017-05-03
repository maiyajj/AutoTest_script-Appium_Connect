# coding=utf-8
import os

from xlwt import *

xfstyle = XFStyle()

align = Alignment()
align.dire = align.DIRECTION_LR

xfstyle.alignment = align

wb = Workbook()
ws = wb.add_sheet('sheet1')
ws.write(3, 3, "Header", xfstyle)
wb.save('width.xls')
os.popen("start width.xls")
