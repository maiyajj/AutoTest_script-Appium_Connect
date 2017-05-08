# coding=utf-8
import multiprocessing


class Process(multiprocessing.Process):
    def __init__(self, *args, **kwargs):
        multiprocessing.Process.__init__(self, *args, **kwargs)
        self._pconn, self._cconn = multiprocessing.Pipe()
        self._exception = None

    def run(self):
        try:
            multiprocessing.Process.run(self)
            self._cconn.send(None)
        except Exception as e:
            tb = traceback.format_exc()
            self._cconn.send((e, tb))

    @property
    def exception(self):
        if self._pconn.poll():
            self._exception = self._pconn.recv()
        return self._exception


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
        # child_process = multiprocessing.Process(target=heavy_load_func, args=(10, child_conn))
        child_process = Process(target=heavy_load_func, args=(10, child_conn))
        child_process.start()
        child_process.join()
        if child_process.exception:
            error, traceback = child_process.exception
            print error
            child_process.terminate()
        else:
            child_return = parent_conn.recv()  # 如果不子进程不抛出异常就接受值，否则主进程退出，避免主进程被管道阻塞！
            print child_return
    except Exception, e:
        print e
