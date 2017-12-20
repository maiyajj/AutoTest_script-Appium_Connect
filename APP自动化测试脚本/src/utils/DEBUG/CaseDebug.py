# coding=utf-8
from src.common.AppInit import *
from src.testcase.GN_F1331.WidgetOperation import *
from src.testcase.GN_F1331.page.ReadAPPElement import *
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

page = PageElement(app_os).get_page_element()
device_list["page"] = page

ac = AppiumCommand(app_os)
check_log(device_info)
check_debug(device_info)
logger = device_info["logger"]
debug = device_info["debug"]
widget_check_unit = WidgetCheckUnit(driver, device_info)
widget_click = widget_check_unit.widget_click
wait_widget = widget_check_unit.wait_widget


class WidgetTest(WidgetOperation):
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
        self.choose_home_device(conf["MAC"][self.app][self.device_mac])

        self.set_power("main_button_on")

        tmp = 10
        while tmp > 0:
            self.widget_click(self.page["control_device_page"]["main_button"])
            self.wait_widget(self.page["control_device_page"]["main_button_on"])
            self.logger.info(u"[APP_INFO]Device info: main button on")

            self.widget_click(self.page["control_device_page"]["main_button"])
            self.wait_widget(self.page["control_device_page"]["main_button_off"])
            self.logger.info(u"[APP_INFO]Device info: main button off")
            tmp -= 1


b().case()


class fix(WidgetTest):
    pass


WidgetTest = fix
