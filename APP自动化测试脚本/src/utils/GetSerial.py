# coding:utf-8
import Queue
import datetime
import logging
import logging.handlers

import serial

from src.utils.ShellCommand import *


# 读取串口log
class ReceiveSerial(object):
    def __init__(self, com, port):
        self.sc = ShellCommand()
        self.log_path = os.path.join(self.sc.set_appium_log_addr(), "%s" % time.strftime("%Y-%m-%d_%H.%M"), "DeviceLog")
        self.log_name = "%s_%s" % (com, port)
        self.serial_queue = Queue.Queue()
        self.serial_sever = serial.Serial(str(com), int(port), timeout=3)
        self.device_serial()

    def receive_log(self):
        self.serial_log.info("receive_log %s " % self.serial_queue)
        while True:
            if not self.serial_sever.is_open:
                break
            else:
                try:
                    data = self.serial_sever.readline()  # 读取数据
                    if data is '':
                        data_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S:%f')[:-3]
                        data = "[%s]%s" % (data_time, data)
                        continue
                    data = data.strip()
                    data_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S:%f')[:-3]
                    data = "[%s]%s" % (data_time, data)
                    self.serial_queue.put_nowait(data)
                    # self.serial_log.info(data)
                except AttributeError:
                    break
                except TypeError:
                    break
                except serial.SerialException:
                    break

    # 分析设备log
    def filtrate_data(self, re_serial, read_num, st=0, et=0):
        while True:
            now = time.time()
            if st > now:
                if not self.serial_sever.is_open:
                    break
                while True:  # 清空消息队列
                    if not self.serial_queue.qsize():
                        break
                    self.serial_queue.get_nowait()
                time.sleep(0.1)
            elif st <= now < et:
                if self.serial_queue.qsize():
                    serial_data = self.serial_queue.get_nowait()
                    if re.findall(re_serial, serial_data):
                        while read_num:
                            if self.serial_queue.qsize():
                                serial_data = self.serial_queue.get_nowait()
                                read_num -= 1
                        return serial_data
                else:
                    if not self.serial_sever.is_open:
                        break
                    time.sleep(0.1)
            else:
                if not self.serial_sever.is_open:
                    break
                while True:
                    if not self.serial_queue.qsize():
                        break
                    self.serial_queue.get_nowait()
                time.sleep(0.1)

    # 接收控制命令，开始/结束分析设备log
    def start_stop_filtrate_data(self, command_queue):
        self.serial_log.info("start_stop_filtrate_data %s " % self.serial_queue)
        while True:
            if command_queue.qsize():
                start_stop, re_serial, read_num, st, et, serial_result_queue = command_queue.get_nowait()
                if start_stop:
                    serial_result_queue.put_nowait(self.filtrate_data(re_serial, read_num, st, et))
                elif start_stop is False:
                    time.sleep(0.5)
                else:
                    break
            else:
                if not self.serial_sever.is_open:
                    break
                while True:
                    if not self.serial_queue.qsize():
                        break
                    self.serial_queue.get_nowait()
                time.sleep(0.1)

    def init_log(self, log):
        file_path = os.path.join(self.log_path, "%s.log" % self.log_name)
        logging.basicConfig(level=logging.INFO)  # 设置打印级别
        formatter = logging.Formatter("%(message)s")  # log文件写入内容，此处为正文
        handler = logging.FileHandler(file_path)
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
