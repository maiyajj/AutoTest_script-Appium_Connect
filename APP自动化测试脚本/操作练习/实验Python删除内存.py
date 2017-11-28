# coding:utf-8
import gc
import time
from time import sleep, time


def mem(way=1):
    print time.strftime("%Y-%m-%d %H:%M:%S")
    for i in range(10000000):
        if way == 1:
            pass
        else:  # way 2, 3
            del i

    print time.strftime("%Y-%m-%d %H:%M:%S")
    if way == 1 or way == 2:
        pass
    else:  # way 3
        gc.collect()
    print time.strftime("%Y-%m-%d %H:%M:%S")


if __name__ == "__main__":
    # print "Test way 1: just pass"
    # mem(way=1)
    # sleep(10)  # 占用236M，峰值312M
    # print "Test way 2: just del"
    # mem(way=2)
    sleep(5)  # 占用236M，峰值312M
    print "Test way 3: del, and then gc.collect()"
    mem(way=3)
    sleep(10)  # 占用3.6M，峰值312M
