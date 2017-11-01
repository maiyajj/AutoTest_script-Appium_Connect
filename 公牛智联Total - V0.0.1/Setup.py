# coding=utf-8
from multiprocessing import *

from src.testcase.case.WaitCase import *
from src.testcase.common.AppInit import *
from src.testcase.suite.ScanCaseName import *
from src.utils.LaunchAppiumServices import *
from src.utils.SendMail import *

__author__ = "Maiyajj"
__version__ = ""
__build_version__ = ""


class MainFunc(object):
    """
    """

    def run(self, device_list, device_name):
        """
        One process launch appium services.
        Another process launch test case.
        """
        # These two functions cannot run on the same process and can only be run with multiple processes.
        appium = Process(target=LaunchAppiumServices, args=(device_list, device_name,), name=device_name)
        appium.start()
        case = Process(target=WaitCase, args=(device_list, device_name,))
        case.start()

    def send_mail(self):
        """
        Send mail at 7 o 'clock every day.
        """
        # Receiver/Sender for mail.
        mail_list = ["chenghao@gongniu.cn",
                     "zhulei@gongniu.cn",
                     "fanrt@gongniu.cn",
                     "sunsy@gongniu.cn",
                     "dongjz@gongniu.cn"]

        kwargs = {"mail_list": mail_list,
                  "mail_pwd": conf["mail_pwd"]}

        # Get report xls from child process, is blocking!
        parent_path = database["multi_queue"].get()
        
        # Scan the root directory to get the files you want to send by mail.
        file_list = []
        for parent, dirnames, filenames in os.walk(parent_path):
            for filename in filenames:
                file_path = os.path.join(parent, filename)
                file_list.append(file_path)
        kwargs["file_path"] = file_list

        # Refresh time per second.
        # When time is 7 a.m, send the scanned files in the mail.
        while True:
            now_time = time.strftime("%H:%M:%S")
            if "07:00:00" in now_time:
                Mailer(**kwargs).send_mail()
            time.sleep(1)


if __name__ == '__main__':
    # The list of information to be tested.
    # device_list: type dict.
    device_list = AppInit().app_init()
    print device_list
    mf = MainFunc()

    # Create a multi-process communication channel
    # multiprocess.Queue()
    # main process can get data from child process
    database["multi_queue"] = Queue()
    
    scan_case = Process(target=scan_case_name)
    scan_case.start()
    scan_case.join()

    # Start send mail process.
    mail = Process(target=mf.send_mail)
    mail.start()

    # Start app auto test process.
    # Open an equal number of processes according to the number of mobile phones.
    process = [Process(target=mf.run, args=(device_list, device_name)) for device_name in device_list.keys()]
    for i in process:
        i.start()
