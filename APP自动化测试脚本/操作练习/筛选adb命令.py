# coding=utf-8
with open(r"adb.txt", "r") as files:
    tmp = files.read().replace("8681-M02-0xa0a151df", "85GABMN9UDD2").splitlines()
    for i in tmp:
        print i
        # print os.popen(i).read()
