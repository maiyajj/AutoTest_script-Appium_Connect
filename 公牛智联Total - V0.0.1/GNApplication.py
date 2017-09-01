# coding=utf-8
from multiprocessing import *

import psutil
from src.testcase.case.WaitCase import *
from src.testcase.suite.ScanCaseName import *
from src.utils.LaunchAppiumServices import *
from src.utils.SendMail import *

_main_version = ""
_build_version = ""


def run(device_list, device_name):
    run_appium = 1
    run_case = 1
    while True:
        if run_appium == 1:
            run_appium = 0
            appium = Process(target=LaunchAppiumServices, args=(device_list, device_name,), name=device_name)
            appium.start()
        if run_case == 1:
            run_case = 0
            case = Process(target=WaitCase, args=(device_list, device_name,))
            case.start()
        while True:
            if appium.is_alive() is False:
                run_appium = 1
                print appium.pid
                time.sleep(1)
                break
            elif case.is_alive() is False:
                run_case = 1
                print case.pid
                time.sleep(1)
                break
            else:
                print appium.name
                time.sleep(1)


def check_port(device_list):
    port = {}
    for k, v in device_list.items():
        port[k] = []
        port[k].append(v['port'])
        port[k].append(v['bp_port'])
        port[k].append(v['wda_port'])
    with open(r"./node_mem_%s.log" % time.strftime("%Y-%m-%d %H:%M:%S"), "w") as files:
        while True:
            try:
                for k, v in port.items():
                    for i in v:
                        command = 'lsof -i:%s' % i
                        find_pid = re.findall(r"(.+?) .+?(\d+).+LISTEN.+?", os.popen(command).read())
                        if find_pid != []:
                            proc = find_pid[0][0]
                            pid = int(find_pid[0][1])
                            mem = psutil.Process(pid).memory_info().rss / 1024 / 1024
                            p = psutil.virtual_memory()
                            rest = (p.total * (100 - p.percent) / 100) / 1024 / 1024
                            print "\n***************[%s]|[%s][%s]:[%sM][all_remain:%sM]-----------------[%s]***********************\n" % (
                                i, time.strftime("%Y-%m-%d %H:%M:%S"), proc, mem, rest, k)
                            files.write("[%s]|[%s][%s]:[%sM][all_remain:%sM]-----------------[%s]\n" % (
                                i, time.strftime("%Y-%m-%d %H:%M:%S"), proc, mem, rest, k))
                time.sleep(1)
            except BaseException:
                files.write(traceback.format_exc())


def check_proc():
    with open(r"./2.log", "w") as files:
        while True:
            print len(psutil.pids())
            time.sleep(1)
            files.write("\n************%s***************" % len(psutil.pids()))


def scan_files():
    file_list = []
    mail_list = ["chenghao@gongniu.cn", "zhulei@gongniu.cn", "fanrt@gongniu.cn", "sunsy@gongniu.cn"]
    mail_title = 'Hey subject'
    mail_content = 'Hey this is content'
    while True:
        try:
            file_path = os.path.join(ShellCommand().set_appium_log_addr(), "temp.log")
            with open(file_path, "r") as files:
                parent_path = files.read()
                os.remove(file_path)
                break
        except OSError:
            time.sleep(1)
    for parent, dirnames, filenames in os.walk(parent_path):
        for filename in filenames:
            file_path = os.path.join(parent, filename)
            file_list.append(file_path)
    kwargs = {"mail_list": mail_list,
              "mail_title": mail_title,
              "mail_content": mail_content,
              "file_path": file_list}
    return kwargs

def send_mail():
    while True:
        now_time = str(time.strftime("%Y-%m-%d %H:%M:%S"))
        print now_time
        if "12:00:00" in now_time:
            kwargs = scan_files()
            Mailer(**kwargs).send_mail()
        elif "14:00:00" in now_time:
            kwargs = scan_files()
            Mailer(**kwargs).send_mail()
        elif "16:00:00" in now_time:
            kwargs = scan_files()
            Mailer(**kwargs).send_mail()
        elif "18:00:00" in now_time:
            kwargs = scan_files()
            Mailer(**kwargs).send_mail()
        time.sleep(1)


if __name__ == '__main__':
    device_list = AppInit().app_init()
    print device_list
    port = Process(target=check_port, args=(device_list,))
    # port.start()
    proc = Process(target=check_proc)
    # proc.start()
    scan_case = Process(target=scan_case_name)
    # scan_case.start()
    # scan_case.join()
    mail = Process(target=send_mail)
    mail.start()

    process = [Process(target=run, args=(device_list, device_name)) for device_name in device_list.keys()]
    for i in process:
        i.start()
