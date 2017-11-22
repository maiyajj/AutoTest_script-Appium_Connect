from multiprocessing import Process, Queue
import os,time
def run_proc(q, name):
    time.sleep(3)
    print('Run child process %s (%s)...' % (name, os.getpid()))
    q.put("wwwwwwwwwww")


if __name__=='__main__':
    q = Queue()

    print('Parent process %s.' % os.getpid())
    p = Process(target=run_proc, args=(q, 'test',))

    print('Child process will start.')
    p.start()

    print('Child process end.')
    print("wwww"+q.get())