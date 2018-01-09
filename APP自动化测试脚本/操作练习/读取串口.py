# coding:utf-8
import Queue
import datetime
import re
import time

import serial
import threadpool


# 读取串口log
class ReceiveSerial(object):
    def __init__(self, com, port):
        self.serial_data_queue = Queue.Queue()
        self.btn_state = Queue.Queue()
        self.pool = threadpool.ThreadPool(2)
        self.serial_sever = serial.Serial(str(com), int(port), timeout=3)

    def receive_log(self, tmp):
        while True:
            if not self.serial_sever.is_open:
                break
            else:
                try:
                    data = self.serial_sever.readline()  # 读取数据
                    if data is '':
                        data_time = datetime.datetime.now().strftime('%Y-%m-%d %X:%f')[:-3]
                        data = "[%s]%s" % (data_time, data)
                        continue
                    data = data.strip()
                    data_time = datetime.datetime.now().strftime('%Y-%m-%d %X:%f')[:-3]
                    data = "[%s]%s" % (data_time, data)
                    self.serial_data_queue.put_nowait(data)
                except AttributeError:
                    break
                except TypeError:
                    break
                except serial.SerialException:
                    break
            # print(data)
            # print(self.serial_data_queue.qsize())

    def filtrate_data(self, re_serial, read_num, timeout):
        end_time = time.time() + timeout
        while True:
            num = read_num
            if self.serial_data_queue.qsize():
                serial_data = self.serial_data_queue.get_nowait()
                if re.findall(re_serial, serial_data):
                    while num:
                        if self.serial_data_queue.qsize():
                            serial_data = self.serial_data_queue.get_nowait()
                            num -= 1
                    return serial_data
            else:
                if not self.serial_sever.is_open:
                    break
                time.sleep(0.1)
                if timeout is not None:
                    if time.time() < end_time:
                        time.sleep(0.1)
                    else:
                        self.serial_sever.close()
                        break

    def check_data(self, re_serial, read_num, timeout=None):
        btn_state = bin(int(self.filtrate_data(re_serial, read_num, timeout)[34:36], 16)).ljust(6, "0")[2:5]
        up_btn, middle_btn, down_btn = btn_state
        up_btn, middle_btn, down_btn = int(up_btn), int(middle_btn), int(down_btn)
        self.btn_state.put_nowait((up_btn, middle_btn, down_btn))
        self.serial_sever.close()


rs = ReceiveSerial("com6", 115200)
request = threadpool.makeRequests(rs.receive_log, ["useless_args"])
request.append(threadpool.makeRequests(rs.check_data, [(["_f133u_uart_recv_event", 1, 100], None)])[0])  # 创建线程池任务列表
[rs.pool.putRequest(req) for req in request]
rs.pool.wait()
up_btn, middle_btn, down_btn = rs.btn_state.get_nowait()
print(up_btn, middle_btn, down_btn)
