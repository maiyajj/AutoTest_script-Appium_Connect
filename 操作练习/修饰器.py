# coding=utf-8


def my_decorator(func):
    def wrapper():
        print "Before the function runs"
        func()
        print "After the function runs"

    return wrapper


def my_func():
    print "I am a stand alone function"

my_func()