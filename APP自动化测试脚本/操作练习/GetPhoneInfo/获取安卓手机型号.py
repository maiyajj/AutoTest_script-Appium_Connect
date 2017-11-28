# coding:utf-8
import re

with open(r"360.txt", "r") as qiku:
    qikus = qiku.read()
    # command = "adb -s 8681-M02-0xa0a151df shell getprop"
    # platformVersion = os.popen(command).read()
    tmp = re.findall(r".+product.model.+", qikus)
    print "360", tmp
with open(r"mx5.txt", "r") as qiku:
    qikus = qiku.read()
    # command = "adb -s 8681-M02-0xa0a151df shell getprop"
    # platformVersion = os.popen(command).read()
    tmp = re.findall(r".+product.model.+", qikus)
    print "mx5", tmp
with open(r"vivo.txt", "r") as qiku:
    qikus = qiku.read()
    # command = "adb -s 8681-M02-0xa0a151df shell getprop"
    # platformVersion = os.popen(command).read()
    tmp = re.findall(r".+product.model.+", qikus)
    print "vivo", tmp
