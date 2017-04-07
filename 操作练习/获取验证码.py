# coding:utf-8
import urllib2
import os, time

# 解析短信验证码
os.system("adb logcat -c")
cmd = "adb logcat -d |findstr E/SmsRec"
cmd1 = "adb logcat -d"
# time.sleep(30);
with open(r"log.log","w") as files:
    while (1):
        smscode1 = os.popen(cmd1).read()
        files.write(smscode1,)

print "验证码是:" + smscodeprint