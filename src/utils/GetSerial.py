# coding:utf-8
import datetime
import logging
import logging.handlers

import serial

from src.utils.ShellCommand import *

try:
    import Queue
except ImportError:
    import queue as Queue


# 读取串口log
class ReceiveSerial(object):
    def __init__(self, com, port):
        self.sc = ShellCommand()
        self.log_path = os.path.join(self.sc.set_appium_log_addr(), "%s" % time.strftime("%Y-%m-%d_%H.%M"), "DeviceLog")
        self.log_name = "%s_%s" % (com, port)
        self.serial_main_data_queue = Queue.Queue()
        try:
            self.serial_sever = serial.Serial(str(com), int(port), timeout=3)
            self.device_serial()
        except serial.SerialException as e:
            # e: '\\xcf\\xb5\\xcd...'
            # 需要通过decode("string-escape")转义\\，结果'\xcf\xb5\xcd...'
            py2_3 = str(e)
            try:
                exec (u'''py2_3 = re.findall(".+'(.+?)'", str(e))[0].decode("string-escape").decode("gbk")''')
            except AttributeError:
                exec (u'''py2_3 = re.findall(".+'(.+?)'", str(e))[0]''')
            print(u"%s打开失败，%s请检查串口设置。" % (com, py2_3))
            os._exit(-1)

    def receive_log(self):
        while True:
            if not self.serial_sever.is_open:
                break
            else:
                try:
                    data = self.serial_sever.readline()  # 读取数据
                    if data is '':
                        continue
                    data = data.strip()
                    data_time = datetime.datetime.now().strftime('%Y-%m-%d %X:%f')[:-3]
                    data = "[%s]%s" % (data_time, data)
                    self.serial_main_data_queue.put_nowait(data)
                    # self.serial_log.info(data)
                except AttributeError:
                    break
                except TypeError:
                    break
                except serial.SerialException:
                    break

    # 分析设备log
    def filtrate_data(self, command_queue):
        start_stop, command, serial_result_queue = False, "", ""
        while True:
            if command_queue.qsize():
                start_stop, command, serial_result_queue = command_queue.get_nowait()
                print(start_stop, command, serial_result_queue)
                if start_stop is False:
                    break
            if self.serial_main_data_queue.qsize():
                serial_main_data = self.serial_main_data_queue.get_nowait()
                for re_message, read_num in command.items():
                    if re_message in serial_main_data:
                        tmp = []
                        tmp.append(serial_main_data)
                        while read_num:
                            if self.serial_main_data_queue.qsize():
                                tmp.append(self.serial_main_data_queue.get_nowait())
                                read_num -= 1
                        serial_data = " cha_ru ".join(tmp + [""])
                        serial_result_queue.put_nowait(serial_data)
                        print("#####" + serial_data)
                        break

    # 接收控制命令，开始/结束分析设备log
    def start_stop_filtrate_data(self, command_queue):
        """
        事件驱动，接收command命令，返回log结果
        :param command_queue:
        :return:
        """
        while True:
            if command_queue.qsize():
                self.filtrate_data(command_queue)
                time.sleep(0.1)
            else:
                if not self.serial_sever.is_open:
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
