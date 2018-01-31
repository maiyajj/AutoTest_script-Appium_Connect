# coding:utf-8
import datetime
import logging
import logging.handlers

import serial
import multiprocessing, traceback,psutil

from src.utils.ShellCommand import *

try:
    import Queue
except ImportError:
    import queue as Queue


# 读取串口log
class ReceiveSerial(object):
    def __init__(self):
        self.sc = ShellCommand()
        self.main_pid = os.getpid()
        self.log_path = os.path.join(self.sc.set_appium_log_addr(), "%s" % time.strftime("%Y-%m-%d_%H.%M"), "DeviceLog")

    def open_serial(self):
        self.log_name = "%s_%s" % (self.com, self.port)
        try:
            self.serial_sever = serial.Serial(str(self.com), int(self.port), timeout=3)
            print(u"serial open success")
            self.device_serial()
        except serial.SerialException as e:
            # e: '\\xcf\\xb5\\xcd...'
            # 需要通过decode("string-escape")转义\\，结果'\xcf\xb5\xcd...'
            py2_3 = str(e)
            try:
                # Python3 报错，Pycharm针对decode关键词会提示 Unresolved attribute reference 'decode' for class 'str'。
                # 使用exec语法避免提示错误，无其他含义
                exec(u'''py2_3 = re.findall(".+'(.+?)'", str(e))[0].decode("string-escape").decode("gbk")''')
            except AttributeError:
                exec(u'''py2_3 = re.findall(".+'(.+?)'", str(e))[0]''')
            print(u"%s打开失败，%s请检查串口设置。" % (self.com, py2_3))
            os._exit(-1)

    def receive_log(self, com, port, serial_main_data_queue):
        self.com = com
        self.port = port
        self.open_serial()
        while True:
            if not self.serial_sever.is_open:
                break
            else:
                try:
                    try:
                        data = self.serial_sever.readline().decode("utf-8")  # 读取数据
                    except BaseException as e:
                        self.serial_log.info(str(e))
                        data = ""
                    if data is '':
                        continue
                    data = data.strip()
                    data_time = datetime.datetime.now().strftime('%Y-%m-%d %X:%f')[:-3]
                    data = "[%s]%s" % (data_time, data)
                    serial_main_data_queue.put_nowait(data)
                    self.serial_log.info(data)
                except AttributeError:
                    break
                except TypeError:
                    break
                except serial.SerialException:
                    break

    # 解析串口数据
    def analysis_data(self, serial_main_data, command):
        for re_message, read_num in command.items():
            if re_message in serial_main_data:
                tmp = []
                tmp.append(serial_main_data)
                while read_num:
                    try:
                        tmp.append(self.serial_main_data_queue.get_nowait())
                        read_num -= 1
                    except Queue.Empty:
                        pass
                serial_data = " cha_ru ".join(tmp + [""])
                self.serial_result_queue.put_nowait(serial_data)
                print("#####" + serial_data)
                break

    # 分析设备log
    def filtrate_data(self):
        start_stop, command = False, ""
        while True:
            try:
                start_stop, command = self.serial_command_queue.get_nowait()
                print(start_stop, command)
                if start_stop is False:
                    break
            except Queue.Empty:
                pass
            except BaseException:
                print(traceback.format_exc())
            try:
                serial_main_data = self.serial_main_data_queue.get_nowait()
                self.analysis_data(serial_main_data, command)
            except Queue.Empty:
                pass
            except BaseException:
                print(traceback.format_exc())

    # 接收控制命令，开始/结束分析设备log
    def start_stop_filtrate_data(self, com, port, serial_command_queue, serial_result_queue):
        """
        事件驱动，接收command命令，返回log结果
        :param self.serial_command_queue:
        :return:
        """
        self.serial_command_queue = serial_command_queue
        self.serial_result_queue = serial_result_queue
        self.serial_main_data_queue = multiprocessing.Queue()
        print(os.getpid())
        print([i for i in psutil.Process(self.main_pid).children() if i.pid != os.getpid()][0])

        open_serial = multiprocessing.Process(target=self.receive_log, args=(com, port, self.serial_main_data_queue))
        open_serial.daemon = True
        open_serial.start()
        while True:
            if self.serial_command_queue.qsize():
                self.filtrate_data()
            else:
                if not [i for i in psutil.Process(self.main_pid).children() if i.pid != os.getpid()][0].is_running():
                    print(222)
                    break
                while True:
                    try:
                        self.serial_main_data_queue.get_nowait()
                    except Queue.Empty:
                        break
            time.sleep(0.1)

    def init_log(self, log):
        file_path = os.path.join(self.log_path, "%s.log" % self.log_name)
        logging.basicConfig(level=logging.INFO)  # 设置打印级别
        formatter = logging.Formatter("%(message)s")  # log文件写入内容，此处为正文
        handler = logging.FileHandler(file_path, encoding="utf-8")
        handler.setFormatter(formatter)
        log.addHandler(handler)  # 初始化完毕
        return log

    def device_serial(self):
        if os.path.exists(self.log_path) is False:
            try:
                os.makedirs(self.log_path)
            except OSError:
                pass

        self.serial_log = self.init_log(logging.getLogger(self.log_name))  # 初始化完毕

        logging.shutdown()


# serial_command_queue = multiprocessing.Queue()
# serial_result_queue = multiprocessing.Queue()
# rs = ReceiveSerial()
# def sa():

if __name__ == "__main__":
    print(os.getpid())
    serial_command_queue = multiprocessing.Queue()
    serial_result_queue = multiprocessing.Queue()
    rs = ReceiveSerial()

    serial_command_queue.put_nowait((False, {"_f133u_uart_recv_event": 1}))

    # rs.start_stop_filtrate_data("COM12", 115200, serial_command_queue, serial_result_queue)
    ss = multiprocessing.Process(target=rs.start_stop_filtrate_data, args=(
        "COM12", 115200, serial_command_queue, serial_result_queue))
    # ss = multiprocessing.Process(target=sa)
    ss.daemon = True
    ss.start()
    ss.join()
