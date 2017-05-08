# coding=utf-8

class sssss(object):
    def ssss(self):
        raise KeyError()


def aaa():
    try:
        i = 3
        while i > 0:
            try:
                a = sssss().ssss()
                break
            except KeyError:
                a = "ddd"
                i -= 1
                print i
        if a == "ddd":
            raise KeyError()
    except Exception:
        print "KeyError"


aaa()
