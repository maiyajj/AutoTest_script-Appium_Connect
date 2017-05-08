# -*- coding: utf-8 -*-

def get_flush1():
    book = Workbook()
    sheet = book.add_sheet('test')
    print 'flush_row_data' in dir(sheet)

    ##  default = easyxf('font: name Arial;')

    for i in xrange(10000):
        try:
            sheet.write(i, 1, u'测试', easyxf('font: name Arial;'))
        except:
            print i
            raise
        if (i + 1) % 1000 == 0:
            book.save('test.xls')

    book.save('test.xls')


# get_flush1()

# -*- coding: utf-8 -*-
from xlwt import Workbook, easyxf


def get_flush():
    book = Workbook()
    sheet = book.add_sheet('test')
    print 'flush_row_data' in dir(sheet)

    default = easyxf('font: name Arial;')  # define style out the loop will work

    for i in xrange(10000):
        try:
            sheet.write(i, 1, u'测试', default)
        except:
            print i
            raise
        if (i + 1) % 1000 == 0:
            book.save('test.xls')

    book.save('test.xls')


get_flush()
