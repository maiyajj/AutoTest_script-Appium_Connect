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

print('appium -a 127.0.0.1 -p %s -bp %s -U %s --no-reset --local-timezone' % (port, bp_port, deviceName))

driver = webdriver.Remote('http://localhost:%s/wd/hub' % port, device_info['desired_caps'])

try:
    receive_serial = ReceiveSerial(serial_com, serial_port)
    serial_sever = receive_serial.serial_sever
    serial_main_data_queue = receive_serial.serial_main_data_queue
except serial.SerialException as e:
    print e


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

        self.input_serial_command("power", "set_normal_timer", "launch_normal_timer_once")

        # 上层
        self.widget_click(self.page["control_device_page"]["up_timer"],
                          self.page["up_timer_page"]["title"])

        self.delete_normal_timer("up")

        now = time.strftime("%H:%M")

        delay_time_1 = 1
        delay_time_2 = 2
        start_time_1, set_time_1, cycle_1 = self.create_normal_timer("up_timer_page", now, delay_time_1, "power_on")
        start_time_2, set_time_2, cycle_2 = self.create_normal_timer("up_timer_page", now, delay_time_2, "power_off")

        self.widget_click(self.page["up_timer_page"]["to_return"],
                          self.page["control_device_page"]["title"])

        # 中层
        self.widget_click(self.page["control_device_page"]["mid_timer"],
                          self.page["mid_timer_page"]["title"])

        self.delete_normal_timer("mid")

        now = time.strftime("%H:%M")

        delay_time_3 = 1
        delay_time_4 = 2
        start_time_3, set_time_3, cycle_3 = self.create_normal_timer("mid_timer_page", now, delay_time_3, "power_on")
        start_time_4, set_time_4, cycle_4 = self.create_normal_timer("mid_timer_page", now, delay_time_4, "power_off")

        self.widget_click(self.page["mid_timer_page"]["to_return"],
                          self.page["control_device_page"]["title"])

        # 下层
        self.widget_click(self.page["control_device_page"]["down_timer"],
                          self.page["down_timer_page"]["title"])

        self.delete_normal_timer("down")

        now = time.strftime("%H:%M")

        delay_time_5 = 1
        delay_time_6 = 3
        start_time_5, set_time_5, cycle_5 = self.create_normal_timer("down_timer_page", now, delay_time_5, "power_on")
        start_time_6, set_time_6, cycle_6 = self.create_normal_timer("down_timer_page", now, delay_time_6, "power_off")

        while True:
            if time.time() > set_time_6 + 10:
                break
            print(time.time())
            time.sleep(1)

        #####
        btn_state_list = self.check_serial_button_state()  # 开关
        set_normal_timer_list = self.check_serial_set_normal_timer()  # 定时设置
        launch_normal_timer_once_list = self.check_serial_launch_normal_timer_once()  # 定时执行开
        timer_list = self.get_timer_id_from_set(set_normal_timer_list)
        result = self.get_layer_timer_from_launch(timer_list,
                                                  a=launch_normal_timer_once_list)
b().case()


def set_count_roll(roll_value, set_value, elem=page["add_normal_timer_page"]["roll_m"]):
    # 滚轮
    element = wait_widget(elem)
    lc, sz = element.location, element.size
    lcx, lcy, szw, szh = float(lc["x"]), float(lc["y"]), float(sz["width"]), float(sz["height"])
    pxx, pxy = elem[3]["px"]
    start_x, start_y = int(lcx + pxx * szw), int(lcy + pxy * szh)  # 获取滚轮滑动开始坐标值

    diff = set_value - roll_value
    diff_a = abs(diff)
    try:
        # 计算滚轮滑动目标坐标值
        pm_value = diff / diff_a
        if pm_value > 0:  # 往下滑
            aszh = int(szh * 1.5)
        else:  # 往上滑
            aszh = int(szh * 1.4)
        end_y = start_y - diff / diff_a * aszh
    except ZeroDivisionError:
        end_y = start_y

    swipe = ac.swipe
    swipe_time = conf["roll_time"]["GN_F1331"]
    while diff_a > 0:
        swipe(start_x, start_y, start_x, end_y, driver, percent=False)  # step=25
        print(diff_a)
        diff_a -= 1
        time.sleep(swipe_time)

    print("roll_value: %s, set_value: %s" % (roll_value, set_value))

    time.sleep(1)


class fix(WidgetTest):
    pass


WidgetTest = fix
