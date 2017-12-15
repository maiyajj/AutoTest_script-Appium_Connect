# from pw import *
import pw


class PortBindError(pw.PortBindError):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return repr(self.value)


def pp():
    pw.pww()
