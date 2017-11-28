# coding:utf-8
import os
import subprocess


def start_Appium(port, bootstrap_port):  # device_uid,
    # appium -p 4723 -bp 4724 -U 22238e79 --command-timeout 600
    errormsg = ""
    appium_server_url = ""
    try:
        if True:
            cmd = 'start /b appium -a 127.0.0.1' + ' -p ' + str(port) + ' --bootstrap-port ' + str(
                bootstrap_port) + ' --command-timeout 600'  # ' -U '+ device_uid+
            print cmd
            # p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE) #stdout=PIPE, stderr=PIPE)
            p = subprocess.call(cmd, shell=True, stdout=open('D:/logs.log', 'w'), stderr=subprocess.STDOUT)
            print p
            appium_server_url = 'http://127.0.0.1' + ':' + str(port) + '/wd/hub'
            print appium_server_url
        else:
            print "port:%d is used!" % (port)
    except Exception, msg:
        errormsg = str(msg)
    return appium_server_url, errormsg


def get_port(Appium_url):
    pass


def stop_Appium(Appium_url):
    cmd = 'StopAppium.bat %s' % (get_port(Appium_url))
    # print cmd
    p = os.popen(cmd)
    print p.read()


Appium_url = start_Appium(4723, 4725)[0]
