# coding:utf-8
import datetime, Queue, threadpool, re, serial, time

serial_data_queue = Queue.Queue()
pool = threadpool.ThreadPool(3)

serial_sever = serial.Serial("COM6", 115200, timeout=3)  # 串口参数初始化
# 读取串口log
def receive_log():
    while True:
        if not serial_sever.is_open:
            break
        else:
            try:
                data = serial_sever.readline()  # 读取数据
                if data is '':
                    data_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S:%f')[:-3]
                    data = "[%s]%s" % (data_time, data)
                    print(data)
                    continue
                data = data.strip()
                data_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S:%f')[:-3]
                data = "[%s]%s" % (data_time, data)
                serial_data_queue.put_nowait(data)
            except AttributeError:
                break
            except TypeError:
                break
            except serial.SerialException:
                break


def filtrate_data(re_serial, read_num=1):
    while True:
        num = read_num
        if serial_data_queue.qsize():
            serial_data = serial_data_queue.get_nowait()
            if re.findall(re_serial, serial_data):
                while num:
                    if serial_data_queue.qsize():
                        serial_data = serial_data_queue.get_nowait()
                        num -= 1
                return serial_data
        else:
            time.sleep(0.1)


def check_data():
    while True:
        btn_state = bin(int(filtrate_data("_f133u_uart_recv_event", 1)[34:36], 16)).ljust(6, "0")[2:5]
        up_btn, middle_btn, down_btn = btn_state
        up_btn, middle_btn, down_btn = int(up_btn), int(middle_btn), int(down_btn)
        print(up_btn, middle_btn, down_btn)
        serial_sever.close()


def test():
    while True:
        print 1
        time.sleep(1)
def pool_func(func):
    func()


request = threadpool.makeRequests(pool_func, [receive_log, check_data])  # 创建线程池任务列表
[pool.putRequest(req) for req in request]

# request = threadpool.makeRequests(receive_log, ["useless_args"])
# request.append(threadpool.makeRequests(check_data, [(["_f133u_uart_recv_event", 1, 5], None)])[0])

new_thread = threadpool.makeRequests(pool_func, [test])[0]
pool.putRequest(new_thread)

pool.wait()
# def hello(m, n, o):
#     """"""
#     print "m = %s, n = %s, o = %s" % (m, n, o)
# 
# 
# if __name__ == '__main__':
#     # 方法1
#     lst_vars_1 = ['1', '2', '3']
#     lst_vars_2 = ['4', '5', '6']
#     func_var = [(lst_vars_1, None), (lst_vars_2, None)]
#     print(func_var)
#     # 方法2
#     dict_vars_1 = {'m': '1', 'n': '2', 'o': '3'}
#     dict_vars_2 = {'m': '4', 'n': '5', 'o': '6'}
#     func_var = [(None, dict_vars_1), (None, dict_vars_2)]
# 
#     pool = threadpool.ThreadPool(2)
#     requests = threadpool.makeRequests(hello, func_var)
#     [pool.putRequest(req) for req in requests]
#     pool.wait()
