# coding=utf-8
from multiprocessing import Process


def screen_shot_used():
    print "screen_shot_used"


def ddd(ss):
    print ss


if __name__ == "__main__":
    a = Process(target=ddd, args=(screen_shot_used,))
    a.start()
