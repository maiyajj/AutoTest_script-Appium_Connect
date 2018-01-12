# coding=utf-8
import linecache
import os
import re

# webview无法用uiautomatorviewer定位，使用driver.page_source可以获取
# 获取页面源码后包含中文部分都是Unicode编码，可读性差，使用此脚本进行翻译；
filepath = "page.html"
tmp_path = "tmp.html"
with open(tmp_path, "w") as files:
    for i in range(1, len(linecache.getlines(filepath))):
        tmp = linecache.getline(filepath, i)
        if "\u" in tmp:
            a = re.findall(r'(\\u.+?)"', tmp)
            print a
            if a:
                tmp = tmp.replace(a[0], a[0].decode("unicode_escape").encode("utf-8"))
                print tmp
                files.write(tmp)
            else:
                files.write(linecache.getline(filepath, i))
        else:
            files.write(linecache.getline(filepath, i))

os.remove(filepath)
os.renames(tmp_path, filepath)
