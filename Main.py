# coding=utf-8
from multiprocessing import *

from src.common.AppInit import *
from src.common.LaunchAppiumServices import *
from src.suite.ScanCaseName import *
from src.testcase.WaitCase import *
from src.utils.SendMail import *

__author__ = "Maiyajj"
__version__ = ""
__build_version__ = ""


class MainFunc(object):
    def run(self, device_list, device_name, m_queue):
        """
        One process launch appium services.
        Another process launch test case.
        """
        # These two functions cannot run on the same process and can only be run with multiple processes.
        appium = Process(target=LaunchAppiumServices, args=(device_list, device_name), name=device_name)
        appium.daemon = True  # this process will be killed when 'case' is over
        appium.start()
        case = Process(target=WaitCase, args=(device_list, device_name, m_queue))
        case.start()
        case.join()

    def send_mail(self, m_queue):
        """Send mail at set time every day.
        """
        Mailer(m_queue, conf)


if __name__ == '__main__':
    scan_case = Process(target=scan_case_name)
    scan_case.start()
    # The list of information to be tested.
    # device_list: type dict.
    device_list = AppInit().app_init()
    print(device_list)
    mf = MainFunc()

    scan_case.join()

    # Create a multi-process communication channel
    # multiprocess.Queue()
    # main process can get data from child process
    m_queue = Queue()

    # Start send mail process.
    mail = Process(target=mf.send_mail, args=(m_queue,))
    mail.daemon = True
    mail.start()

    # Start app auto test process.
    # Open an equal number of processes according to the number of mobile phones.
    process = [Process(target=mf.run, args=(device_list, device_name, m_queue)) for device_name in device_list.keys()]
    for i in process:
        i.start()

    for i in process:
        i.join()
