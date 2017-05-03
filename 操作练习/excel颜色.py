#!/usr/bin/env python
# -*- coding: utf-8 -*-”                #只对当前文件的中文编码有效
# Create by zhizaiqianli 2015-12-12  Version V1.0
# ！/usr/bin/python
# Filename : Write_excel_Format.py
import os
import time

from xlwt import *

filename = 'Test.xls'  # 检测当前目录下是否有Test.xls文件，如果有则清除以前保存文件
if os.path.exists(filename):
    os.remove(filename)

print time.strftime("%Y-%m-%d", time.localtime(time.time()))  # 打印读取到当前系统时间

wbk = Workbook(encoding='utf-8')
sheet = wbk.add_sheet('new sheet 1', cell_overwrite_ok=True)  # 第二参数用于确认同一个cell单元是否可以重设值。
style = XFStyle()  # 赋值style为XFStyle()，初始化样式

for i in range(0x00, 0xff):  # 设置单元格背景颜色
    pattern = Pattern()  # 创建一个模式
    pattern.pattern = Pattern.SOLID_PATTERN  # 设置其模式为实型
    pattern.pattern_fore_colour = i
    # 设置单元格背景颜色 0 = Black, 1 = White, 2 = Red, 3 = Green, 4 = Blue, 5 = Yellow, 6 = Magenta,  the list goes on...
    style.pattern = pattern  # 将赋值好的模式参数导入Style
    Line_data = (u'测试表')  # 创建一个Line_data列表，并将其值赋为测试表，以utf-8编码时中文前加u
    sheet.write_merge(i, i, 0, 2, Line_data, style)  # 以合并单元格形式写入数据，即将数据写入以第1/2/3列合并德单元格内

for i in range(0x00, 0xff):  # 设置单元格内字体样式
    fnt = Font()  # 创建一个文本格式，包括字体、字号和颜色样式特性
    fnt.name = u'微软雅黑'  # 设置其字体为微软雅黑
    fnt.colour_index = i  # 设置其字体颜色
    fnt.bold = True
    style.font = fnt  # 将赋值好的模式参数导入Style
    sheet.write_merge(i, i, 3, 5, Line_data, style)  # 以合并单元格形式写入数据，即将数据写入以第4/5/6列合并德单元格内

for i in range(0, 0x53):  # 设置单元格下框线样式
    borders = Borders()
    borders.left = i
    borders.right = i
    borders.top = i
    borders.bottom = i
    style.borders = borders  # 将赋值好的模式参数导入Style
    sheet.write_merge(i, i, 6, 8, Line_data, style)  # 以合并单元格形式写入数据，即将数据写入以第4/5/6列合并德单元格内

for i in range(6, 80):  # 设置单元格下列宽样式
    sheet.write(0, i, Line_data, style)
    sheet.col(i).width = 0x0d00 + i * 50

wbk.save('Test.xls')  # 保存Test.xls文件，保存到脚本或exe文件运行的目录下
raw_input("Enter enter key to exit...")  # 插入一个输入命令，方便运行exe时一闪而过不到打印信息
