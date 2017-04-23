from multiprocessing import Process, Value, Array

a = {1: 4, 2: 5}


def f(n):
    print n.get_obj()


if __name__ == '__main__':
    num = Value('d')
    arr = Array('i', a)
    p = Process(target=f, args=(arr,))
    p.start()
    p.join()
    a = []
    # for i in xrange(1,122):
    #     try:
    #         num = arr(chr(i))
    #         a.append(chr(i))
    #     except TypeError:
    #         pass
    # print a
    # print
