# coding=utf-8
import linecache
import re

filepath = "page.html"
with open("page1.html", "w") as files:
    for i in range(1, len(linecache.getlines(filepath))):
        tmp = linecache.getline(filepath, i)
        if "\u" in tmp:
            a = re.findall(r'(\\u.+?)"', tmp)
            print a
            if a != []:
                tmp = tmp.replace(a[0], a[0].decode("unicode_escape").encode("utf-8"))
                print tmp
                files.write(tmp)
            else:
                files.write(linecache.getline(filepath, i))
        else:
            files.write(linecache.getline(filepath, i))
