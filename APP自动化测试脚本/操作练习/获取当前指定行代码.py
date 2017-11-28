# coding:utf-8
import sys,os
import linecache

def div(x, y):
    try:
        return x / y
    except:
        tb = sys.exc_info()[2]  # return (exc_type, exc_value, traceback)
        print   tb
        print tb.tb_frame,tb.tb_lineno,tb.tb_next
        print linecache.getline("Widget_Check_Unit.py",91)
div(1, 0)
 # 'tb_frame','tb_lasti', 'tb_lineno', 'tb_next']
