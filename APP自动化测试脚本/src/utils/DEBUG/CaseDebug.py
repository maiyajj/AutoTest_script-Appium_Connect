# coding=utf-8

from src.common.AppInit import *
from src.testcase.GN_F1331.WidgetOperation import *

device_list = AppInit().app_init()
deviceName = device_list.keys()[0]
device_info = device_list[deviceName]
device_info["port"] = 4725
device_info["bp_port"] = 4726
device_info["wda_port"] = 4727

app_os = device_info["platformName"]
app = device_info["app"]
port = device_info["port"]
bp_port = device_info["bp_port"]
wda_port = device_info["wda_port"]
device_name = device_info["udid"]
serial_port = int(conf["phone_name"][device_name]["serial_port"])
serial_com = conf["phone_name"][device_name]["serial_com"]
serial_command_queue = Queue.Queue()
serial_result_queue = Queue.Queue()
receive_serial = ReceiveSerial(serial_com, serial_port)


# print('appium -a 127.0.0.1 -p %s -bp %s -U %s --no-reset --local-timezone' % (port, bp_port, deviceName))
#
# driver = webdriver.Remote('http://localhost:%s/wd/hub' % port, device_info['desired_caps'])


def launch_receive_serial():
    receive_serial.receive_log()


def receive_serial_command():
    serial_command_queue.put_nowait((False, "", 0, 0, 0, serial_result_queue))
    receive_serial.start_stop_filtrate_data(serial_command_queue)


# page = PageElement(app_os).get_page_element()
# device_info["page"] = page
#
# ac = AppiumCommand(app_os)
# logger = check_log(device_info)
# debug = check_debug(device_info)
#
# device_info["logger"] = logger
# device_info["debug"] = debug
# widget_check_unit = WidgetCheckUnit(driver, device_info)
# widget_click = widget_check_unit.widget_click
# wait_widget = widget_check_unit.wait_widget
serial_receive_t = threading.Thread(target=launch_receive_serial)
serial_command_t = threading.Thread(target=receive_serial_command)
serial_receive_t.start()
serial_command_t.start()


# serial_command_queue.put_nowait((True, "_f133u_uart_recv_event", 1, time.time() - 30, time.time() + 30, serial_result_queue))

class WidgetTest(WidgetOperation):
    def __init__(self):
        self.serial_command_queue = serial_command_queue
        self.serial_result_queue = serial_result_queue
        self.serial_button_state()


WidgetTest()


# self.driver = driver
# self.ac = ac
# self.page = page
# self.logger = logger
# self.debug = debug
# self.widget_click = widget_click
# self.wait_widget = wait_widget
# self.serial_command_queue = serial_command_queue
# self.serial_result_queue = serial_result_queue


class b(WidgetTest):
    def case(self):
        self.set_power("main_button_off")

        tmp = 10
        while tmp > 0:
            self.widget_click(self.page["control_device_page"]["main_button"],
                              self.page["control_device_page"]["main_button_on"])
            self.logger.info(u"[APP_INFO]Device info: main button on")

            self.widget_click(self.page["control_device_page"]["main_button"],
                              self.page["control_device_page"]["main_button_off"])
            self.logger.info(u"[APP_INFO]Device info: main button off")
            tmp -= 1


b().case()


class fix(WidgetTest):
    pass


WidgetTest = fix
