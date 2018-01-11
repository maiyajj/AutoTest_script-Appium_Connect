# coding=utf-8
import threading

from src.common.AppInit import *
from src.testcase.GN_F1331.WidgetOperation import *
from src.testcase.GN_F1331.page.ReadAPPElement import *
from src.utils.Debug import *

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
device_mac = conf["phone_name"][device_name]["devices_mac"]
serial_command_queue = Queue.Queue()
serial_result_queue = Queue.Queue()
receive_serial = ReceiveSerial(serial_com, serial_port)
serial_sever = receive_serial.serial_sever
serial_main_data_queue = receive_serial.serial_main_data_queue

print('appium -a 127.0.0.1 -p %s -bp %s -U %s --no-reset --local-timezone' % (port, bp_port, deviceName))

driver = webdriver.Remote('http://localhost:%s/wd/hub' % port, device_info['desired_caps'])


def launch_receive_serial():
    receive_serial.receive_log()


def receive_serial_command():
    serial_command_queue.put_nowait((False, "", ""))
    receive_serial.start_stop_filtrate_data(serial_command_queue)


page = PageElement(app_os).get_page_element()
device_info["page"] = page

ac = AppiumCommand(app_os)
debug = check_debug(device_info)

device_info["debug"] = debug
widget_check_unit = WidgetCheckUnit(driver, device_info)
widget_click = widget_check_unit.widget_click
wait_widget = widget_check_unit.wait_widget
serial_receive_t = threading.Thread(target=launch_receive_serial)
serial_command_t = threading.Thread(target=receive_serial_command)
serial_receive_t.start()
serial_command_t.start()


class WidgetTest(WidgetOperation):
    def __init__(self):
        self.ac = ac
        self.app = app
        self.page = page
        self.driver = driver
        self.debug = debug
        self.widget_click = widget_click
        self.wait_widget = wait_widget
        self.device_mac = device_mac
        self.serial_command_queue = serial_command_queue
        self.serial_result_queue = serial_result_queue


class b(WidgetTest):
    def case(self):
        self.choose_home_device(conf["MAC"][self.app][self.device_mac])

        self.delete_out_date_timer()

        self.set_power("main_button_off")

        self.input_serial_command("device_info")
        device_info_state_list = self.check_device_info_state(True)
        time_0 = time.time()
        safe_memory_0 = self.get_device_info_state(device_info_state_list, time_0)[1]

        self.input_serial_command("power", "device_info")

        self.ac.swipe(0.5, 0.9, 0.5, 0.6, self.driver)

        if safe_memory_0 == "1":
            self.widget_click(self.page["control_device_page"]["memory_mode"])
            time_1 = time.time()

            self.widget_click(self.page["control_device_page"]["safe_mode"])
            time_2 = time.time()
        else:
            self.widget_click(self.page["control_device_page"]["safe_mode"])
            time_1 = time.time()

            self.widget_click(self.page["control_device_page"]["memory_mode"])
            time_2 = time.time()

        device_info_state_list = self.check_device_info_state()
        device_info_state_1_list = self.get_device_info_state(device_info_state_list, time_1)
        device_info_state_2_list = self.get_device_info_state(device_info_state_list, time_2)
        self.debug.info(u"[APP_INFO]device state: \n"
                        u"device_info_state_list: %s;\n"
                        u"device_info_state_1_list: %s;\n"
                        u"device_info_state_2_list: %s;"
                        % (device_info_state_list, device_info_state_1_list, device_info_state_2_list))

        if safe_memory_0 == "1":
            # 记忆模式
            safe_memory_1 = device_info_state_1_list[1]
            result = [safe_memory_1 == "0"]
            if False in result:
                raise TimeoutException("device state error, current: %s, result: %s" % (safe_memory_1, result))

            # 安全模式
            safe_memory_2 = device_info_state_2_list[1]
            result = [safe_memory_2 == "1"]
            if False in result:
                raise TimeoutException("device state error, current: %s, result: %s" % (safe_memory_2, result))
        else:
            # 安全模式
            safe_memory_1 = device_info_state_1_list[1]
            result = [safe_memory_1 == "1"]
            if False in result:
                raise TimeoutException("device state error, current: %s, result: %s" % (safe_memory_1, result))

            # 记忆模式
            safe_memory_2 = device_info_state_2_list[1]
            result = [safe_memory_2 == "0"]
            if False in result:
                raise TimeoutException("device state error, current: %s, result: %s" % (safe_memory_2, result))


b().case()


class fix(WidgetTest):
    pass


WidgetTest = fix
