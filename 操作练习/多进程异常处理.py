# coding=utf-8
import multiprocessing


def heavy_load_func(N, child_conn):
    '''function do heavy computing'''

    try:

        # do_some_heavy_computing

        child_conn.send(return_value)  # return something

    except Exception, e:
        child_conn.send(e)  # 将异常通过管道送出


if __name__ == '__main__':
    '''main function'''
    try:
        parent_conn, child_conn = multiprocessing.Pipe()
        hild_process = multiprocessing.Process(target=heavy_load_func, args=(10, child_conn))
        child_process.start()
        child_process.join()
        child_return = parent_conn.recv()
        print child_return
    except Exception, e:
        print e
