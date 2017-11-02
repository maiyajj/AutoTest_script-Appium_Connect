import time,psutil,os
from multiprocessing import *


def ss(q, q1):
    pid = q.get()
    parent = psutil.Process(pid).parent()
    print parent
    while True:
        print 1
        try:
            psutil.Process(9999)
        except psutil.NoSuchProcess:
            psutil.Process(pid).kill()
        time.sleep(3)


if __name__ == "__main__":
    q = Queue()
    q1 = Queue()
    a = Process(target=ss, args=(q,q1))
    a.start()
    print a.pid
    q.put(a.pid)

