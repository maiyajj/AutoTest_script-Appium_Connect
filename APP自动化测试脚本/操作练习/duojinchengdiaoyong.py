# coding=utf-8
from multiprocessing import Process


def screen_shot_used():
    print "adfasdfasdfss"


if __name__ == "__main__":
    d = Process(target=screen_shot_used)
    d.start()
