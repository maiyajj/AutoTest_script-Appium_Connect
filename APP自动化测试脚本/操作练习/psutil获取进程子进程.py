# coding=utf-8
import os
import psutil
import time
from multiprocessing import *


def producer1():
    while True:
        time.sleep(1)


def producer2():
    a = Process(target=producer1)
    b = Process(target=producer1)
    a.start()
    b.start()


def producer():
    a = Process(target=producer2)
    b = Process(target=producer2)
    a.start()
    b.start()


pid_list = []
"pid_list.append(i.pid)\naa(i.pid)"


def aa(pid):
    c_pid = psutil.Process(pid).children()
    for i in c_pid:
        # exec ("pid_list.append(i.pid)\naa(i.pid)")
        pid_list.append(i.pid)
        aa(i.pid)


a = lambda pid: [pid_list.append(i.pid) or a(i.pid) for i in psutil.Process(pid).children()]
a(16152)

if __name__ == '__main__':
    current_pid = os.getpid()
    print(current_pid)
    process_producer = Process(target=producer)
    process_consumer = Process(target=producer)
    process_producer.start()
    process_consumer.start()
