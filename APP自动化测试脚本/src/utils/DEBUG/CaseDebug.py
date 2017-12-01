# coding=utf-8
from src.testcase.common.AppInit import *
from src.testcase.common.WidgetOperation_HW import *
from src.testcase.page.ReadAPPElement import *
from src.utils.CollectLog import *
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

print('appium -a 127.0.0.1 -p %s -bp %s -U %s --no-reset --local-timezone' % (port, bp_port, deviceName))

driver = webdriver.Remote('http://localhost:%s/wd/hub' % port, device_info['desired_caps'])

PageElement(device_list, app_os, app).wrapper()
page = device_list["page"]

ac = AppiumCommand(app_os)
check_log(device_list, deviceName)
check_debug(device_list, deviceName)
logger = device_info["logger"]
debug = device_info["debug"]
widget_check_unit = WidgetCheckUnit(driver, page, logger, debug)
widget_click = widget_check_unit.widget_click
wait_widget = widget_check_unit.wait_widget


class WidgetTest(WidgetOperationHW):
    def __init__(self):
        self.driver = driver
        self.ac = ac
        self.page = page
        self.logger = logger
        self.debug = debug
        self.widget_click = widget_click
        self.wait_widget = wait_widget


class b(WidgetTest):
    def case(self):
        self.set_power("power_on")

        self.widget_click(self.page["control_device_page"]["delay_timer"],
                          self.page["delay_timer_roll_popup"]["title"])

        now = time.strftime("%H:%M")

        delay_time_1 = ["delay", "00:02"]
        start_time_1, set_time_1 = self.create_delay_timer(now, delay_time_1)

        time.sleep(60)

        self.widget_click(self.page["control_device_page"]["power_button"],
                          self.page["control_device_page"]["power_off"])

        self.check_timer(start_time_1, set_time_1, u"电源已关闭", same_power=True)


b().case()


class fix(WidgetTest):
    pass


WidgetTest = fix
