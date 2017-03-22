import re,os
# command = "adb devices -l > UDID.txt"
# os.system(command)
# with open(r"UDID.txt","r") as files:
#     file = files.read()
#     a = re.findall(r"(.+)device product.+model:(.+)device", file)
#     command = "taskkill /f /t /im adb.exe"
#     os.system(command)
#     for i in a:
#         print i[0].split()[0],i[1].split()[0]

# command = "appium -a 127.0.0.1 -p 4723  -U  %s  --no-reset"%file
# os.system(command)

#     b = re.findall(r"List of devices attached", file)
# print b
command = "netstat -aon|findstr 5037"
a = os.popen(command).read()
print a
with open(r"UDID.txt","r") as files:
    file = files.readlines()
    print "woshi fenge"
    for i in file:
        a = re.findall(r"LISTENING(.+)", i)
        if a != []:
            command = "tasklist | findstr %s > UDID.txt" % a[0].split()[0]
            os.system(command)
