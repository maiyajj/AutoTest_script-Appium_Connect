# coding:utf-8
'''
Created on 2015-11-19
@author: Administrator
'''
# import xlwt
# book = xlwt.Workbook(encoding='utf-8')
# sheet = book.add_sheet('sheet1')
# first_col=sheet.col(0)       #xlwt中是行和列都是从0开始计算的
# sec_col=sheet.col(1)
#
# first_col.width=256*20
#
#
# book.save('width.xls')


import xlwt

book = xlwt.Workbook(encoding='utf-8')
sheet = book.add_sheet('sheet1')
first_col = sheet.col(0)
sec_col = sheet.col(1)

first_col.width = 256 * 20
tall_style = xlwt.easyxf('font:height 720;')  # 36pt,类型小初的字号
first_row = sheet.row(0)
first_row.set_style(tall_style)
sheet.Cells(1, 1).Font.Size = 20
sheet.write(0, 0, u"固件版本\n\nStart Time", style_none)

book.save('width.xls')

style = xlwt.XFStyle()  # 初始化样式
alignment.horz = xlwt.Alignment.HORZ_CENTER  # 垂直对齐
alignment.vert = xlwt.Alignment.VERT_CENTER  # 水平对齐
alignment.wrap = xlwt.Alignment.WRAP_AT_RIGHT  # 自动换行
style.alignment = alignment
sheet1.write(0, 0, 'hello', style)
