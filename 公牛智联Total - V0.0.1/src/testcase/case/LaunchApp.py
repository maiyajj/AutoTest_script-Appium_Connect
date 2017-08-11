# coding=utf-8
import inspect
import traceback
from httplib import BadStatusLine
from urllib2 import URLError

from appium import webdriver

from src.testcase.case.ToDevicePage import *
from src.testcase.case.ToLoginPage import *
from src.testcase.common.WidgetCheckUnit import *
from src.utils.ScreenShot import *


def launch_fail_fix(func):
    def wrapper(self):
        i = 1
        ii = 1
        while True:
            try:
                func(self)
                break
            except WebDriverException:
                self.debug.error(traceback.format_exc())
                self.debug.error("launch_app driver(WebDriverException):%s times" % i)
                i += 1
                time.sleep(1)
                if i == 3:
                    self.http_run_app()
                    i = 0
            except URLError:
                self.debug.error("launch_app driver(URLError):%s times" % ii)
                ii += 1
                self.http_run_app()
                break
            except BadStatusLine:
                self.debug.error("launch_app driver(BadStatusLine)")
                self.http_run_app()
                break

    return wrapper


def decor_init_app(func):
    def wrapper(self):
        while True:
            try:
                self.check_appium_launch()
                try:
                    self.driver.quit()
                    self.debug.warn("driver quit success")
                except BaseException:
                    self.debug.warn("driver need not quit")
                func(self)
                self.check_user_pwd()
                self.driver.close_app()
                self.debug.info("init_app driver(close_app success)")
                break
            except BaseException:
                self.debug.error(traceback.format_exc())

    return wrapper


def decor_launch_app(func):
    def wrapper(self, page_login):
        self.driver = self.return_driver()
        self.debug.info("basename:%s" % self.basename)
        self.data_statistics(self.zentao_id)
        i = 0
        while True:
            try:
                try:
                    func(self)
                    self.init_operate()
                    self.start_time = time.strftime("%Y-%m-%d %H:%M:%S")
                    self.logger.info('app start [time=%s]' % self.start_time)  # 记录log，APP打开时间
                    self.success = False

                    if page_login is True:
                        ToLoginPage(self.driver, self.logger, self.device_info, self.page)  # 使APP跳转到登录页面等待
                        break
                    elif page_login is False:
                        ToDevicePage(self.driver, self.logger, self.device_info, self.page)  # 使APP跳转到设备主页面等待
                        break
                    elif page_login is None:
                        pass
                        break
                    i = 0
                except BaseException:
                    i += 1
                    if i == 3:
                        i = 0
                        raise WebDriverException(traceback.format_exc())
            except BaseException:
                self.case_over("unknown")
                self.debug.error("case_over:%s" % traceback.format_exc())
                raise WebDriverException("Case launch unknown")

    return wrapper


def case_run(bool):
    def wrapper(func):
        def _wrapper(self):
            func(self)
            self.basename = re.findall(r"\((.+?)\)", inspect.stack()[2][4][0])[0]
            # self.basename = os.path.basename(__file__).split(".")[0]  # 获取用例的文件名称:GNAPP_LOGIN_001
            self.logger.info('[GN_INF] <current case> [CASE_ID="%s", CASE_NAME="%s", 禅道ID="%s", CASE_MODULE="%s"]'
                             % (self.basename, self.case_title, self.zentao_id, self.case_module))  # 记录log

            try:
                self.launch_app(bool)  # 启动APP
                # battery = self.wait_widget(self.page["god_page"]["battery"], 3, 1).get_attribute("name")
                # self.logger.warn(u"手机%s" % battery)
                self.case()
            except BaseException:
                self.debug.error(traceback.format_exc())  # Message: ***
                self.case_over("unknown")

            # 记录运行结果
            return self.result()

        return _wrapper
    return wrapper

class LaunchApp(object):
    conf = conf

    def __init__(self, **kwargs):
        self.device_info = kwargs["device_info"]
        self.page = kwargs["page_element"]
        self.logger = kwargs["logger"]
        self.sc = kwargs["sc"]
        self.device_name = self.device_info["udid"]
        self.port = self.device_info["port"]
        self.bp_port = self.device_info["bp_port"]
        self.wda_port = self.device_info["wda_port"]
        self.ac = AppiumCommand(self.device_info["platformName"])

        self.debug = self.device_info["debug"]
        self.user = self.device_name
        self.case_module = ""  # 用例所属模块
        self.case_title = ""  # 用例名称
        self.zentao_id = 0000  # 禅道ID
        self.basename = ""  # 用例自动化文件名称
        self.success = False  # 初始化用例执行结果
        # self.start_fail = False  # 初始化APP启动结果
        self.widget_click = None
        self.wait_widget = None
        self.start_time = None

    def http_run_app(self):
        global driver
        while True:
            try:
                self.check_appium_launch()
                try:
                    self.driver.quit()
                    self.debug.warn("driver quit success")
                except BaseException:
                    self.debug.warn("driver need not quit")
                driver = webdriver.Remote('http://localhost:%s/wd/hub' % self.device_info["port"],
                                          self.device_info["desired_caps"])  # 启动APP
                self.driver = driver
                break
            except WebDriverException:
                self.debug.error("URLError driver(WebDriverException)")
                break
            except URLError:
                self.debug.error("URLError driver(URLError)")
                break

    def check_appium_launch(self):
        while True:
            try:
                self.sc.find_proc_and_pid_by_port(self.port)[0]
            except IndexError:
                time.sleep(1)
            else:
                self.debug.info("Appium Sever launch Success! %s" % time.strftime("%Y-%m-%d %H:%M:%S"))
                break

    def wait_pwd_timeout(self):
        i = 1
        while i <= 31:
            time.sleep(10)
            widget_px = self.page["god_page"]["title"]
            width = int(int(self.device_info["dpi"]["width"]) * widget_px[3]["px"]["width"])
            height = int(int(self.device_info["dpi"]["height"]) * widget_px[3]["px"]["height"])
            self.driver.tap([(width, height)], )
            print "time sleep %sS" % (i * 10)
            self.logger.info("time sleep %sS" % (i * 10))
            i += 1

    def check_user_pwd(self):
        self.init_operate()
        ToLoginPage(self.driver, self.logger, self.device_info, self.page)
        while True:
            try:
                user_name = self.widget_click(self.page["login_page"]["title"],
                                              self.page["login_page"]["username"],
                                              self.page["login_page"]["title"])

                # 发送数据
                data = conf["user_and_pwd"][self.device_info["udid"]]["user_name"]
                data = str(data).decode('hex').replace(" ", "")
                user_name.clear()
                self.ac.send_keys(user_name, data, self.driver)
                time.sleep(0.5)

                precise_pwd = conf["user_and_pwd"][self.device_info["udid"]]["precise_pwd"]
                for x in xrange(len(precise_pwd)):
                    self.show_pwd(self.wait_widget(self.page["login_page"]["check_box"]))
                    login_pwd = self.widget_click(self.page["login_page"]["title"],
                                                  self.page["login_page"]["password"],
                                                  self.page["login_page"]["title"])

                    data = str(precise_pwd[x]).decode('hex').replace(" ", "")
                    login_pwd.clear()
                    self.ac.send_keys(login_pwd, data, self.driver)
                    try:
                        self.widget_click(self.page["login_page"]["title"],
                                          self.page["login_page"]["login_button"],
                                          self.page["device_page"]["title"])
                        if x == 0:
                            conf["user_and_pwd"][self.device_info["udid"]]["login_pwd"] = precise_pwd[0]
                            conf["user_and_pwd"][self.device_info["udid"]]["new_pwd"] = precise_pwd[1]
                        else:
                            conf["user_and_pwd"][self.device_info["udid"]]["login_pwd"] = precise_pwd[1]
                            conf["user_and_pwd"][self.device_info["udid"]]["new_pwd"] = precise_pwd[0]
                        break
                    except TimeoutException:
                        if x != len(precise_pwd) - 1:
                            pass
                        else:
                            raise TimeoutException()
                modified_conf(conf)
                break
            except TimeoutException:
                self.wait_pwd_timeout()
                self.debug.error("init_app:%s" % traceback.format_exc())

    @decor_init_app
    @launch_fail_fix
    def init_app(self):
        global driver
        driver = webdriver.Remote('http://localhost:%s/wd/hub' % self.device_info["port"],
                                  self.device_info["desired_caps"])  # 启动APP
        self.driver = driver

    def init_operate(self):
        widget_check_unit = WidgetCheckUnit(self.driver, self.page, self.logger)  # 元素初始化
        self.widget_click = widget_check_unit.widget_click  # 初始化self.widget_click
        self.wait_widget = widget_check_unit.wait_widget  # 初始化self.wait_widget
        self.debug.info("driver(init_operate success)")

    def data_statistics(self, zentao_id):
        self.debug.info("zentao_id:%s" % zentao_id)
        if zentao_id in database[self.device_name].keys():
            pass
        else:
            database[self.device_name][zentao_id] = {}
            database[self.device_name][zentao_id]["test_count"] = 0
            database[self.device_name][zentao_id]["test_pass"] = 0
            database[self.device_name][zentao_id]["test_fail"] = 0
            database[self.device_name][zentao_id]["test_error"] = 0
            database[self.device_name][zentao_id]["test_wait"] = 0
            database[self.device_name][zentao_id]["ZenTao"] = zentao_id
            database[self.device_name][zentao_id]["case_title"] = self.case_title
        self.debug.info("case_title:%s" % self.case_title)

    @decor_launch_app
    @launch_fail_fix
    def launch_app(self):
        self.debug.warn("launch_app driver(ready launch)")
        try:
            self.driver.close_app()
            self.debug.info("launch_app close_app success")
        except BaseException:
            self.debug.info("launch_app close_app error success")
        self.driver.launch_app()
        self.debug.info("launch_app driver(launch_app success)")

    def return_driver(self):
        return driver

    def show_pwd(self, element, bool=True):
        if bool:
            while True:
                try:
                    if self.ac.get_attribute(element, "checked") == "true":
                        break
                    else:
                        element.click()
                except BaseException:
                    self.debug(traceback.format_exc())
        else:
            while True:
                try:
                    if self.ac.get_attribute(element, "checked") == "false":
                        break
                    else:
                        element.click()
                except BaseException:
                    self.debug(traceback.format_exc())

    def case_over(self, success):
        self.success = success
        database[self.device_name][self.zentao_id]["test_count"] += 1

    # 记录运行结果
    def result(self):
        d_result = {True: ["success", "test_pass"],
                    False: ["failed", "test_fail"],
                    "unknown": ["unknown", "test_error"],
                    "screen": ["wait", "test_wait"]}
        result = d_result[self.success]
        self.logger.info('[GN_INF] <current case> [CASE_TITLE="%s"] %s!' % (self.case_title, result[0]))
        database[self.device_name][self.zentao_id][result[1]] += 1
        return "%s" % result[0], self.zentao_id, self.case_title, self.start_time
