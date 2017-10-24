# coding=utf-8
from multiprocessing import *

from src.testcase.case.WaitCase import *
from src.testcase.common.AppInit import *
from src.testcase.suite.ScanCaseName import *
from src.utils.LaunchAppiumServices import *
from src.utils.SendMail import *

_main_version = ""
_build_version = ""


class MainFunc(object):
    def run(self, device_list, device_name):
        appium = Process(target=LaunchAppiumServices, args=(device_list, device_name,), name=device_name)
        appium.start()
        case = Process(target=WaitCase, args=(device_list, device_name,))
        case.start()

    def scan_files(self, parent_path):
        file_list = []
        mail_list = ["chenghao@gongniu.cn",
                     "zhulei@gongniu.cn",
                     "fanrt@gongniu.cn",
                     "sunsy@gongniu.cn",
                     "dongjz@gongniu.cn"]
        # mail_list = ["1045373828@qq.com"]
        mail_title = 'Hey subject'
        mail_content = 'Hey this is content'
        for parent, dirnames, filenames in os.walk(parent_path):
            for filename in filenames:
                file_path = os.path.join(parent, filename)
                file_list.append(file_path)
        kwargs = {"mail_list": mail_list,
                  "mail_title": mail_title,
                  "mail_content": mail_content,
                  "file_path": file_list}

        return kwargs

    def send_mail(self):
        file_path = os.path.join(ShellCommand().set_appium_log_addr(), "temp.log")
        while True:
            try:
                with open(file_path, "r") as files:
                    parent_path = files.read()
                    os.remove(file_path)
                    break
            except BaseException:
                time.sleep(1)
        while True:
            now_time = str(time.strftime("%Y-%m-%d %H:%M:%S"))
            if "07:00:00" in now_time:
                Mailer(**self.scan_files(parent_path)).send_mail()
            time.sleep(1)


if __name__ == '__main__':
    device_list = AppInit().app_init()
    print device_list
    mf = MainFunc()
    
    scan_case = Process(target=scan_case_name)
    scan_case.start()
    scan_case.join()

    mail = Process(target=mf.send_mail)
    mail.start()

    process = [Process(target=mf.run, args=(device_list, device_name)) for device_name in device_list.keys()]
    for i in process:
        i.start()
