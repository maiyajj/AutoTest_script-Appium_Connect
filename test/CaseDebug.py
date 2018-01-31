# coding=utf-8
try:
    from importlib import reload
except ImportError:
    pass

from src.common.AppInit import *
from src.testcase.GN_F1331.input_case.GN_F1331_Input_Case import *
from src.testcase.GN_F1331.page.ReadAPPElement import *
from src.utils.Debug import *

device_list = AppInit().app_init()
print(device_list)
deviceName = list(device_list.keys())[0]
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
phone_model = device_info["deviceName"]
serial_port = int(conf["phone_name"][device_name]["serial_port"])
serial_com = conf["phone_name"][device_name]["serial_com"]
device_mac = conf["phone_name"][device_name]["devices_mac"]
user = conf["user_and_pwd"][device_name][app]

print('appium -a 127.0.0.1 -p %s -bp %s -U %s --no-reset --local-timezone' % (port, bp_port, deviceName))

driver = webdriver.Remote('http://localhost:%s/wd/hub' % port, device_info['desired_caps'])

page = PageElement(app_os).get_page_element()
device_info["page"] = page

ac = AppiumCommand(app_os)
device_info["ac"] = ac

sc = ShellCommand()
device_info["sc"] = sc

debug = check_debug(device_info)
device_info["debug"] = debug

widget_check_unit = WidgetCheckUnit(driver, device_info)
widget_click = widget_check_unit.widget_click
wait_widget = widget_check_unit.wait_widget

receive_serial = ReceiveSerial()
serial_command_queue = multiprocessing.Queue()
serial_result_queue = multiprocessing.Queue()
device_info["serial_command_queue"] = serial_command_queue
device_info["serial_result_queue"] = serial_result_queue

serial_command_queue.put_nowait((False, ""))
alive = multiprocessing.Value('b', True)
# 接收设备串口log
serial_receive_t = multiprocessing.Process(target=receive_serial.start_stop_filtrate_data, args=(
    serial_com, serial_port, serial_command_queue, serial_result_queue, alive))

serial_receive_t.start()

device_info["serial_command_queue"] = serial_command_queue
device_info["serial_result_queue"] = serial_result_queue

import src.testcase.GN_F1331.case.GN_F1331_ELECTRICITY.GN_F1331_ELECTRICITY_001 as tc

reload(tc)
case = tc.GNF1331Electricity1(device_info)
case.widget_click = widget_click
case.wait_widget = wait_widget
case.driver = driver
case.page = page
case.ac = ac
case.sc = sc
case.case()
