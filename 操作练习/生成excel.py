from time import strftime

import xlwt

current_date = strftime("%b %d %Y   (%H:%M)")


## Startup Code End


## Modules Begin
def _size_col(sheet, col):
    return sheet.col_width(col)


def _size_row(sheet, row):
    return sheet.row_height(row)
    ## Modules End


## Style variable Begin
tittle_style = xlwt.easyxf(
    'font: height 400, name Arial Black, colour_index blue, bold on; align: wrap on, vert centre, horiz center;'      "borders: top double, bottom double, left double, right double;")
subtittle_left_style = xlwt.easyxf(
    'font: height 240, name Arial, colour_index brown, bold on, italic on; align: wrap on, vert centre, horiz left;'      "borders: top double, bottom double, left double;")
subtittle_right_style = xlwt.easyxf(
    'font: height 240, name Arial, colour_index brown, bold on, italic on; align: wrap on, vert centre, horiz left;'      "borders: top double, bottom double, right double;")
subtittle_top_and_bottom_style = xlwt.easyxf(
    'font: height 240, name Arial, colour_index black, bold off, italic on; align: wrap on, vert centre, horiz left;'      "borders: top double, bottom double;")
blank_style = xlwt.easyxf(
    'font: height 650, name Arial, colour_index brown, bold off; align: wrap on, vert centre, horiz left;'      "borders: top double, bottom double, left double, right double;")
normal_style = xlwt.easyxf(
    'font: height 240, name Arial, colour_index black, bold off; align: wrap on, vert centre, horiz left;'      "borders: top double, bottom double, left double, right double;")


## Style variable End


## Module Add Begin
def print_blank_line(A, B, C, D):
    ws.write_merge(A, B, C, D, "", xlwt.easyxf(
        'font: height 240, name Arial, colour_index black, bold off, italic on; align: wrap on, vert centre, horiz left;'))
    ## Module Add End


## Variable Begin
Excel = xlwt.Workbook()
## Variable End


## Sheet Name Begin
ws = Excel.add_sheet('Test Sheet')
## Sheet Name End


## Column Width Determine Begin
for A in range(100):
    ws.col(A).width = 600
## Column Width Determine Begin


## Tittle Picture Begin
ws.write_merge(0, 0, 0, 42, "", xlwt.easyxf(
    'font: height 700, name Arial, colour_index brown, bold off; align: wrap on, vert centre, horiz left;'))
##ws.insert_bitmap('test.bmp', 0, 0, 60, 5, 1.75, 1)
## Tittle Picture End


## Subtittle Write Begin
# Variable Begin
job_name = "Nicolas_Parametric"
fab_name = "Nicolas_Parametric"
printed_by = "Nic"
printed_date = current_date
# Variable End

border_type = ["dashed", "double", ""]

ws.write_merge(1, 1, 0, 6, "Job Name:", xlwt.easyxf(
    'font: height 240, name Arial, colour_index black, bold on, italic on; align: wrap on, vert centre, horiz left;'      "borders: top double, bottom double, left double;"))
ws.write_merge(1, 1, 7, 21, job_name, xlwt.easyxf(
    'font: height 240, name Arial, colour_index black, bold off, italic on; align: wrap on, vert centre, horiz left;'      "borders: top double, bottom double;"))
ws.write_merge(2, 2, 0, 6, "Fab Name:", xlwt.easyxf(
    'font: height 240, name Arial, colour_index black, bold on, italic on; align: wrap on, vert centre, horiz left;'      "borders: top double, bottom double, left double;"))
ws.write_merge(2, 2, 7, 21, fab_name, xlwt.easyxf(
    'font: height 240, name Arial, colour_index black, bold off, italic on; align: wrap on, vert centre, horiz left;'      "borders: top double, bottom double;"))

ws.write_merge(1, 1, 22, 27, "Printed By:", xlwt.easyxf(
    'font: height 240, name Arial, colour_index black, bold on, italic on; align: wrap on, vert centre, horiz left;'      "borders: top double, bottom double;"))
ws.write_merge(1, 1, 28, 42, printed_by, xlwt.easyxf(
    'font: height 240, name Arial, colour_index black, bold off, italic on; align: wrap on, vert centre, horiz left;'      "borders: top double, bottom double, right double;"))
ws.write_merge(2, 2, 22, 27, "Printed Date:", xlwt.easyxf(
    'font: height 240, name Arial, colour_index black, bold on, italic on; align: wrap on, vert centre, horiz left;'      "borders: top double, bottom double;"))
ws.write_merge(2, 2, 28, 42, printed_date, xlwt.easyxf(
    'font: height 240, name Arial, colour_index black, bold off, italic on; align: wrap on, vert centre, horiz left;'      "borders: top double, bottom double, right double;"))

print_blank_line(3, 3, 0, 42)
ws.write_merge(4, 4, 0, 42, "Report Name", xlwt.easyxf(
    'font: height 400, name Arial, colour_index red, bold on, italic on, underline on; align: wrap on, vert centre, horiz center;'))
print_blank_line(5, 5, 0, 42)

ws.write_merge(6, 6, 0, 1, "#", xlwt.easyxf(
    'font: height 240, name Arial, colour_index black, bold on, italic on; align: wrap on, vert centre, horiz left;'      "borders: top double, bottom double, left double, right double;"))
ws.write_merge(6, 6, 2, 7, "Piecemark", xlwt.easyxf(
    'font: height 240, name Arial, colour_index black, bold on, italic on; align: wrap on, vert centre, horiz left;'      "borders: top double, bottom double, left dashed, right double;"))
ws.write_merge(6, 6, 8, 10, "Qty", xlwt.easyxf(
    'font: height 240, name Arial, colour_index black, bold on, italic on; align: wrap on, vert centre, horiz left;'      "borders: top double, bottom double, left dashed, right double;"))
ws.write_merge(6, 6, 11, 20, "Size", xlwt.easyxf(
    'font: height 240, name Arial, colour_index black, bold on, italic on; align: wrap on, vert centre, horiz left;'      "borders: top double, bottom double, left dashed, right double;"))
ws.write_merge(6, 6, 21, 34, "Status", xlwt.easyxf(
    'font: height 240, name Arial, colour_index black, bold on, italic on; align: wrap on, vert centre, horiz left;'      "borders: top double, bottom double, left dashed, right double;"))
ws.write_merge(6, 6, 35, 42, "Date", xlwt.easyxf(
    'font: height 240, name Arial, colour_index black, bold on, italic on; align: wrap on, vert centre, horiz left;'      "borders: top double, bottom double, left dashed, right double;"))
## Subtittle Write End


normal_font = xlwt.easyxf(
    'font: height 240, name Arial, colour_index black; align: wrap on, vert centre, horiz left;'      "borders: top dashed, bottom dashed, left double, right double;")

for A in range(98):
    ws.write_merge(7 + A, 7 + A, 0, 1, "", normal_font)
    ws.write_merge(7 + A, 7 + A, 2, 7, "", normal_font)
    ws.write_merge(7 + A, 7 + A, 8, 10, "", normal_font)
    ws.write_merge(7 + A, 7 + A, 11, 20, "", normal_font)
    ws.write_merge(7 + A, 7 + A, 21, 34, "", normal_font)
    ws.write_merge(7 + A, 7 + A, 35, 42, "", normal_font)

## File Save As Begin
Excel.save('Test.xls')
## File Save As End


#### Start File Begin
##os.startfile("C:/Documents and Settings/dev01/Desktop/Test.xls")
#### Start File End
