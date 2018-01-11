# -*- coding: utf-8 -*-
import datetime

from xlwt import *

from data.Database import *
from src.utils.ReadConf import *
from src.utils.ShellCommand import *

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


# For write excel report.
# report format is .xls
# need some other functions, you can modified by yourself.
class WriteXls(object):
    def __init__(self, device_info):
        self.device_info = device_info
        self.app = device_info["app"]
        self.debug = device_info["debug"]
        self.udid = device_info["udid"]
        self.pn = device_info["platformName"]
        self.pv = device_info["platformVersion"]
        self.user = conf["app_device_name"][self.app]
        self.app_name = self.user["app_name"]
        self.device_name = self.user["device_name"]
        self.app_ver = self.user["app_ver"]
        self.run()

    # 单元格格式
    def easy_xf(self):
        self.easyxf1 = easyxf(u'font: height 320, name 宋体, colour_index 70, bold on;'
                              u'align: wrap on, vert top, horiz centre;'
                              u'borders: top thin, left thin, right thin;')

        self.easyxf2 = easyxf(u'font: height 220, name 宋体;'
                              u'align: wrap on, horiz left;'
                              u'borders: right thin;')

        self.easyxf3 = easyxf(u'font: height 220, name 宋体;'
                              u'align: wrap on;'
                              u'borders: left thin, right thin;')

        self.easyxf4 = easyxf(u'font: height 220, name 宋体;'
                              u'align: wrap on, horiz left;'
                              u'borders: top thin, bottom thin, left thin, right thin;'
                              u'pattern: pattern solid, fore_colour 22')

        self.easyxf5 = easyxf(u'font: height 220, name 宋体, colour_index white, bold on;'
                              u'align: wrap on, horiz left;'
                              u'borders: left thin, right thin;'
                              u'pattern: pattern solid, fore_colour 23')

        self.easyxf6 = easyxf(u'font: height 220, name 宋体;'
                              u'align: wrap on, horiz centre;'
                              u'borders: top thin, bottom thin, left thin, right thin;'
                              u'pattern: pattern solid, fore_colour 22')

        self.easyxf7 = easyxf(u'font: height 220, name 宋体;'
                              u'align: wrap on, horiz left;'
                              u'borders: left thin, right thin;')

        self.easyxf8 = easyxf(u'font: height 220, name 宋体;'
                              u'align: wrap on;'
                              u'borders: top thin, bottom thin, left thin, right thin;')

        self.easyxf9 = easyxf(u'font: height 220, name 宋体, bold on;'
                              u'align: wrap on, horiz left;'
                              u'borders: left thin;')

        self.easyxf10 = easyxf(u'font: height 220, name 宋体;'
                               u'align: wrap on, horiz right;'
                               u'borders: top thin, bottom thin, left thin, right thin;'
                               u'pattern: pattern solid, fore_colour 22')

        self.easyxf11 = easyxf(u'font: height 220, name 宋体, bold on;'
                               u'align: wrap on, horiz left;'
                               u'borders: top thin, bottom thin, left thin;')

        self.easyxf12 = easyxf(u'font: height 220, name 宋体, bold on;'
                               u'align: wrap on, horiz left;'
                               u'borders: top thin, bottom thin, right thin;')

        self.easyxf13 = easyxf(u'font: height 220, name 宋体;'
                               u'align: wrap on, horiz centre;'
                               u'borders: top thin, bottom thin, left thin, right thin;',
                               num_format_str="0%")

    # 检查设备报告路径是否存在
    def check_path(self):
        current_time = time.strftime("%Y-%m-%d_%H.%M")
        parent_path = r"./report/xls_report/%s" % current_time
        database["m_queue"].put(parent_path)
        if os.path.exists(parent_path) is False:
            try:
                os.makedirs(parent_path)
            except OSError:
                pass

        self.sheet_name = self.device_info["log_name"]  # sheet名称
        self.xls_file = r"%s/%s.xls" % (parent_path, self.sheet_name)  # 文件路径及名称

    # 启动脚本首先运行此函数，会生成报告模板待填充数据
    def run(self):
        self.easy_xf()
        self.check_path()

        self.case_row = {}
        self.total_row = []
        self.book = Workbook(encoding='utf-8')
        self.sheet = self.book.add_sheet(self.sheet_name, cell_overwrite_ok=True)
        self.row = self.write_title()
        self.scan_case_files()
        self.book.save(self.xls_file)
        database["case_row"] = self.case_row

    # 报告模板设计，根据手动设计报告模板，使用函数实现
    def write_title(self):
        row = 0
        self.sheet.col(0).width = 256 * 17
        self.sheet.col(1).width = 256 * 70
        for i in xrange(2, 9):
            self.sheet.col(i).width = 256 * 11  # 设置单元格宽度

        self.sheet.write_merge(row, row + 1, 0, 8, u"%s测试报告" % self.device_name, self.easyxf1)  # 写合并单元格(x,x,y,y)
        row += 2

        self.sheet.write_merge(row, row, 0, 8, "", self.easyxf3)  # 写单元格(x, y)
        row += 1

        self.phone_module = u"%s(%s%s)" % (conf["phone_name"][self.udid]["phone_module"], self.pn, self.pv)
        self.sheet.write(row, 0, u"手机型号：", self.easyxf9)
        self.sheet.write_merge(row, row, 1, 8, self.phone_module, self.easyxf2)
        row += 1

        self.sheet.write(row, 0, u"APP及版本号：", self.easyxf9)
        self.sheet.write_merge(row, row, 1, 8, self.app_name + self.app_ver, self.easyxf2)
        row += 1

        self.start_time = time.strftime("%Y-%m-%d %X")
        self.sheet.write(row, 0, u"开始时间：", self.easyxf9)
        self.sheet.write_merge(row, row, 1, 8, self.start_time, self.easyxf2)
        row += 1

        self.sheet.write(row, 0, u"结束时间：", self.easyxf9)
        self.sheet.write_merge(row, row, 1, 8, self.start_time, self.easyxf2)
        row += 1

        self.sheet.write(row, 0, u"持续时间：", self.easyxf9)
        self.sheet.write_merge(row, row, 1, 8, "0:00:00", self.easyxf2)
        row += 1

        self.sheet.write(row, 0, u"执行用例数：", self.easyxf9)
        self.sheet.write_merge(row, row, 1, 8, 0, self.easyxf2)
        row += 1

        self.sheet.write(row, 0, u"执行结果：", self.easyxf9)
        self.sheet.write_merge(row, row, 1, 8, u"通过 0； 失败 0； 执行错误 0； 人工检查 0；", self.easyxf2)
        row += 1

        self.sheet.write_merge(row, row, 0, 8, "", self.easyxf7)
        row += 1
        self.sheet.write_merge(row, row, 0, 8, u"用例执行情况：", self.easyxf7)
        row += 1
        self.sheet.write_merge(row, row, 0, 8, "", self.easyxf7)
        row += 1

        write_list = [u"禅道ID", u"用例名称", u"是否执行", u"执行次数", u"通过", u"失败", u"未知错误", u"人工检查", u"最终结果"]
        for i in write_list:
            self.sheet.write(row, write_list.index(i), i, self.easyxf5)
        row += 1

        return row

    # 用例执行完毕调用此函数，写入测试报告数据。
    def write_data(self, row, Zentao, Name, end_time, run, Count=0, Pass=0, Fail=0, Error=0, Wait=0):
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
        self.sheet.write(row, 0, Zentao, self.easyxf4)
        self.sheet.write(row, 1, Name, self.easyxf4)
        self.sheet.write(row, 2, run, self.easyxf10)
        self.sheet.write(row, 3, Count, self.easyxf10)
        self.sheet.write(row, 4, Pass, self.easyxf10)
        self.sheet.write(row, 5, Fail, self.easyxf10)
        self.sheet.write(row, 6, Error, self.easyxf10)
        self.sheet.write(row, 7, Wait, self.easyxf10)
        formula = ('IF({3}{0}>0,"Error",IF({2}{0}>0,"Fail",IF({4}{0}>0,"Wait",IF({1}{0}>0,"Pass",""))))'.
            format(row + 1, chr(69), chr(70), chr(71), chr(72)))  # 写excel公式，由Excel软件设计好再写入代码, chr(69)="E"
        self.sheet.write(row, 8, Formula(formula), self.easyxf6)

        self.book.save(self.xls_file)
        self.write_total(row + 1, end_time)

    # 根据用例执行结果，写入统计数据
    def write_total(self, row, end_times):
        self.total_row.append(row)
        self.total_row = list(set(self.total_row))
        total_row = max(self.total_row)
        total_row_min = min(self.total_row)
        self.sheet.write(total_row, 0, "Total", self.easyxf11)
        self.sheet.write(total_row, 1, "", self.easyxf12)

        formula = 'COUNTIF({0}{2}:{0}{1},"Y")'.format(chr(67), total_row, total_row_min)
        self.sheet.write(total_row, 2, Formula(formula), self.easyxf8)
        self.sheet.write_merge(9, 9, 1, 8, Formula(formula), self.easyxf2)

        for i in xrange(3, 8):
            formula = 'SUM({0}{2}:{0}{1})'.format(chr(i + 65), total_row, total_row_min)
            self.sheet.write(total_row, i, Formula(formula), self.easyxf8)

        formula = ('COUNTIF({0}{2}:{0}{1},"Pass")/(COUNTA({0}{2}:{0}{1})-COUNTIF({0}{2}:{0}{1},""))'.
            format(chr(73), total_row, total_row_min))
        self.sheet.write(total_row, 8, Formula(formula), self.easyxf13)

        self.sheet.write_merge(6, 6, 1, 8, end_times, self.easyxf2)

        start_time = datetime.datetime.fromtimestamp(time.mktime(time.strptime(self.start_time, "%Y-%m-%d %X")))
        end_time = datetime.datetime.fromtimestamp(time.mktime(time.strptime(end_times, "%Y-%m-%d %X")))
        continue_time = str(end_time - start_time)
        self.sheet.write_merge(7, 7, 1, 8, continue_time, self.easyxf2)

        formula = (u'"通过 "&COUNTIF({0}{2}:{0}{1},"Pass")&"； 失败 "&COUNTIF({0}{2}:{0}{1},"Fail")&"； 执行错误 "&'
                   u'COUNTIF({0}{2}:{0}{1},"Error")&"； 人工检查 "&COUNTIF({0}{2}:{0}{1},"Wait")&"；"'.
            format(chr(73), total_row, total_row_min))
        self.sheet.write_merge(8, 8, 1, 8, Formula(formula), self.easyxf2)

        self.book.save(self.xls_file)

        # 写入运行时长
        with open(r"./runTime.log", "w") as run_time:
            run_time.write(str(continue_time))

    def scan_case_files(self):
        row = self.row
        rootdir = r"./src/testcase/%s/case" % self.app  # 指明被遍历的文件夹
        for parent, dirnames, filenames in os.walk(rootdir):  # 三个参
            for filename in (i for i in filenames if "__init__" not in i and "pyc" not in i):
                with open(os.path.join(parent, filename), "r") as files:
                    file = files.read()
                    case_name = re.findall(r"self.case_title = u'(.+)'", file)[0]
                    zentao_id = re.findall(r'self.zentao_id = (\d+)', file)[0]
                    self.write_data(row, zentao_id, case_name, time.strftime("%Y-%m-%d %X"), "N", 0, 0, 0, 0, 0)
                    self.case_row[int(zentao_id)] = row
                    row += 1
