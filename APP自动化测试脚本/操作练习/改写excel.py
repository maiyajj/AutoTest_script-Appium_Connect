# coding=utf-8
import xlrd
import xlwt
# import xlutils
from xlutils.copy import copy

# init xls file
# styleBlueBkg= xlwt.easyxf('pattern: pattern solid, fore_colour sky_blue')
# styleBold   = xlwt.easyxf('font: bold on')
styleBoldRed = xlwt.easyxf('font: color-index red, bold on')
headerStyle = styleBoldRed
wb = xlwt.Workbook()
ws = wb.add_sheet('sheet1')
ws.write(0, 0, "Header", headerStyle)
ws.write(0, 1, "CatalogNumber", headerStyle)
ws.write(0, 2, "PartNumber", headerStyle)
wb.save('width.xls')

# open existed xls file
# newWb = xlutils.copy('width.xls')
# newWb = copy('width.xls')
oldWb = xlrd.open_workbook('width.xls', formatting_info=True)
print oldWb  # <xlrd.book.Book object at 0x000000000315C940>
newWb = copy(oldWb)
print newWb  # <xlwt.Workbook.Workbook object at 0x000000000315F470>
newWs = newWb.get_sheet(0)
newWs.write(0, 0, "value1")
newWs.write(0, 1, "value2")
newWs.write(0, 2, "value3")
print"write new values ok"
newWb.save('width.xls')
print"save with same name ok"


# 不用此方法，xlwt支持改写，加内部参数即可cell_overwrite_ok=True
# self.sheet = self.book.add_sheet(self.sheet_name, cell_overwrite_ok=True)
