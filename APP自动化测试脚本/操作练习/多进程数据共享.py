# coding:utf-8
#
# from multiprocessing import Process
# li = []
#
# def foo(i):
#     li.append(i)
#     print 'say hi', li
# if __name__ == '__main__':
#
#     for i in range(10):
#         p = Process(target=foo, args=(i,))
#         p.start()
#
#     print 'ending', li

# 期望输出[0到10的随机排列的列表]

from multiprocessing import Process, Array


def f(a):
    # for i in range(len(a)):
    #     a[i] = -a[i]
    print a[:]


if __name__ == '__main__':
    # arr = Array('i', range(10))
    arr = Array('i', False)
    p = Process(target=f, args=(arr,))
    p.start()
    p.join()

    print(arr[:])

from multiprocessing import Process, Manager


def f(d, l):
    a = d
    a[1] = '1'
    a['2'] = 2
    a[0.25] = None
    l.reverse()


if __name__ == '__main__':
    d = Manager().dict()
    l = Manager().list(range(10))

    p = Process(target=f, args=(d, l))
    p.start()
    p.join()

    print(a)
    print(l)
