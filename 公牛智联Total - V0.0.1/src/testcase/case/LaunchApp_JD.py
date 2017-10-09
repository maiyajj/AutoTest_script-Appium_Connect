# coding=utf-8
import inspect
from httplib import BadStatusLine
from urllib2 import URLError

from appium import webdriver

from src.testcase.case.ToDevicePage import *
from src.testcase.case.ToLoginPage import *
from src.testcase.common.WidgetCheckUnit import *
from src.utils.ScreenShot import *


def launch_fail_fix_jd(func):
    def wrapper(self):
        i = 1
        ii = 1
        while True:
            try:
                func(self)
                break
            except WebDriverException, e:
                e = "".join(str(e).split())
                if e != "Message:":
                    self.debug.error(traceback.format_exc())
                    self.debug.error("launch_app driver(WebDriverException):%s times" % i)

                    time.sleep(1)
                    if i >= 3:
                        self.http_run_app()
                    elif i >= 4:
                        self.http_run_app(True)
                        i = 0
                    i += 1
                else:
                    self.http_run_app()
            except URLError:
                self.debug.error("launch_app driver(URLError):%s times" % ii)
                ii += 1
                self.http_run_app(True)
                break
            except BadStatusLine:
                self.debug.error("launch_app driver(BadStatusLine)")
                self.http_run_app(True)
                break

    return wrapper


def decor_init_app_jd(func):
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
                # self.check_user_pwd()
                self.driver.close_app()
                self.debug.info("init_app driver(close_app success)")
                break
            except BaseException:
                self.debug.error(traceback.format_exc())

    return wrapper


def decor_launch_app_jd(func):
    def wrapper(self, page_login):
        self.driver = self.return_driver()
        self.debug.info("basename:%s" % self.basename)
        self.data_statistics(self.zentao_id)
        i = 0
        while True:
            try:
                try:
                    self.sc.kill_zombie_proc()
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
                        print "i", i
                        raise WebDriverException(traceback.format_exc())
            except BaseException:
                self.case_over("unknown")
                self.debug.error("case_over:%s" % traceback.format_exc())
                raise WebDriverException("Case launch unknown")

    return wrapper


def case_run_jd(bool):
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
                try:
                    self.case()
                except TimeoutException:
                    self.case_over(False)
                    self.debug.error("case_over:%s" % traceback.format_exc())
                database["unknown"] = 0
            except BaseException:
                self.debug.error(traceback.format_exc())  # Message: ***
                self.case_over("unknown")
                database["unknown"] += 1
                if database["unknown"] > 2:
                    database["unknown"] = 0
                    self.debug.error("Too many unknown case!:%s" % self.basename)
                    self.reset_port()

            # 记录运行结果
            return self.result()

        return _wrapper

    return wrapper


class LaunchAppJD(object):
    def __init__(self, **kwargs):
        self.device_info = kwargs["device_info"]
        self.page = kwargs["page_element"]
        self.logger = kwargs["logger"]
        self.sc = kwargs["sc"]
        self.device_name = self.device_info["udid"]
        self.port = self.device_info["port"]
        self.bp_port = self.device_info["bp_port"]
        self.wda_port = self.device_info["wda_port"]
        self.app = self.device_info["app"]
        self.ac = AppiumCommand(self.device_info["platformName"])

        self.debug = self.device_info["debug"]
        self.user = conf["user_and_pwd"][self.device_name][self.app]
        self.case_module = ""  # 用例所属模块
        self.case_title = ""  # 用例名称
        self.zentao_id = 0000  # 禅道ID
        self.basename = ""  # 用例自动化文件名称
        self.success = False  # 初始化用例执行结果
        # self.start_fail = False  # 初始化APP启动结果
        self.widget_click = None
        self.wait_widget = None
        self.start_time = None

    def reset_port(self):
        for ports in [self.port]:
            proc_pid = self.sc.find_proc_and_pid_by_port(ports)
            if proc_pid == []:  # 判断当前端口是否被占用
                print "COM %s unused" % ports
                self.debug.info("COM %s unused" % ports)
            else:
                for i in proc_pid:
                    self.sc.kill_proc_by_pid(i[1])
                    print "Kill %s" % i[0]
                    self.debug.info("Kill %s" % i[0])

    def http_run_app(self, strong_reboot=False):
        while True:
            try:
                if strong_reboot == True:
                    if self.device_info["udid"] in self.sc.get_phone_udid():
                        self.reset_port()
                    else:
                        self.debug.error("device is disconnected")
                self.check_appium_launch()
                try:
                    self.driver.quit()
                    self.debug.warn("driver quit success")
                except BaseException:
                    self.debug.warn("driver need not quit")
                self.driver = webdriver.Remote('http://localhost:%s/wd/hub' % self.device_info["port"],
                                               self.device_info["desired_caps"])  # 启动APP
                self.init_operate()
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
                self.debug.info("Appium Sever is death! %s" % time.strftime("%Y-%m-%d %H:%M:%S"))
                time.sleep(1)
            else:
                self.debug.info("Appium Sever launch Success! %s" % time.strftime("%Y-%m-%d %H:%M:%S"))
                break

    def wait_pwd_timeout(self):
        i = 1
        while i <= 31:
            time.sleep(10)
            self.driver.tap([(10, 10)])
            print "time sleep %sS" % (i * 10)
            self.logger.info("time sleep %sS" % (i * 10))
            i += 1

    @decor_init_app_jd
    @launch_fail_fix_jd
    def init_app(self):
        global driver
        with open("appium command %s.txt" % self.device_name, "a") as files:
            files.write('''driver = webdriver.Remote('http://localhost:%s/wd/hub', %s)''' % (
                self.device_info["port"], self.device_info["desired_caps"]) + "\n\n")

        driver = webdriver.Remote('http://localhost:%s/wd/hub' % self.device_info["port"],
                                  self.device_info["desired_caps"])  # 启动APP
        self.driver = driver

    def return_driver(self):
        try:
            print self.driver
        except AttributeError:
            self.driver = driver
        return self.driver

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

    @decor_launch_app_jd
    @launch_fail_fix_jd
    def launch_app(self):
        self.debug.warn("launch_app driver(ready launch)")
        try:
            self.driver.close_app()
            time.sleep(0.5)
            self.debug.info("launch_app close_app success")
        except BaseException:
            self.debug.info("launch_app close_app error success")
        self.driver.launch_app()
        time.sleep(0.5)
        self.debug.info("launch_app driver(launch_app success)")

    def show_pwd(self, element, element1=None, param="name", display=True):
        if display:
            while True:
                try:
                    if param == "name":
                        if self.ac.get_attribute(element, param) != "":
                            break
                        else:
                            if element1 is None:
                                element.click()
                            else:
                                element1.click()
                    else:
                        if self.ac.get_attribute(element, param) == "true":
                            break
                        else:
                            if element1 is None:
                                element.click()
                            else:
                                element1.click()

                except BaseException:
                    self.debug.error(traceback.format_exc())
        else:
            while True:
                try:
                    if param == "name":
                        if self.ac.get_attribute(element, param) == "":
                            break
                        else:
                            if element1 is None:
                                element.click()
                            else:
                                element1.click()
                    else:
                        if self.ac.get_attribute(element, param) == "false":
                            break
                        else:
                            if element1 is None:
                                element.click()
                            else:
                                element1.click()
                except BaseException:
                    self.debug.error(traceback.format_exc())

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

    def set_timer_roll(self, elem_h, elem_m, elem_t, et, now_time, same_fish_mode=False, leave_time=2):
        if isinstance(et, int):
            if et >= 0:
                time_seg = "int"
            else:
                time_seg = "minus"
        else:
            if et[0] == "point":
                time_seg = "point"
            elif et[0] == "delay":
                time_seg = "delay"
            else:
                time_seg = None
        # 时滚轮
        element_h = self.wait_widget(elem_h)
        pxx_h, pxy_h = elem_h[3]["px"]
        lc_h, sz_h = element_h.location, element_h.size
        lcx_h, lcy_h, szw_h, szh_h = float(lc_h["x"]), float(lc_h["y"]), float(sz_h["width"]), float(sz_h["height"])
        aszh_h = int(szh_h / 5)
        start_x_h, start_y_h = int(lcx_h + pxx_h * szw_h), int(lcy_h + pxy_h * szh_h)
        # 分滚轮
        element_m = self.wait_widget(elem_m)
        pxx_m, pxy_m = elem_m[3]["px"]
        lc_m, sz_m = element_m.location, element_m.size
        lcx_m, lcy_m, szw_m, szh_m = float(lc_m["x"]), float(lc_m["y"]), float(sz_m["width"]), float(sz_m["height"])
        aszh_m = int(szh_m / 5)
        start_x_m, start_y_m = int(lcx_m + pxx_m * szw_m), int(lcy_m + pxy_m * szh_m)

        roll_now_h, roll_now_m = self.ac.get_attribute(self.wait_widget(elem_t), "name").split(":")
        roll_now_h, roll_now_m = int(roll_now_h), int(roll_now_m)
        if roll_now_h == 0 and roll_now_m == 1:
            self.driver.swipe(start_x_h, start_y_h, start_x_h, start_y_h - aszh_h, 0)
            roll_now_h, roll_now_m = self.ac.get_attribute(self.wait_widget(elem_t), "name").split(":")
            roll_now_h, roll_now_m = int(roll_now_h), int(roll_now_m)

        now_h, now_m = now_time.split(":")
        if same_fish_mode is False:
            now_h, now_m = int(now_h), int(now_m)
        else:
            now_h, now_m = int(now_h), int(now_m) - leave_time
            now_h, now_m = (now_h + now_m / 60) % 24, now_m % 60

        if time_seg == "int":
            aet = abs(et)
            sign_aet = et / aet
            set_h, set_m = now_h + sign_aet * (aet / 60), now_m + leave_time + sign_aet * (aet % 60)
            set_h, set_m = (set_h + set_m / 60) % 24, set_m % 60
            true_h, true_m = set_h, set_m
        elif time_seg == "minus":
            aet = abs(et)
            sign_aet = et / aet
            set_h, set_m = now_h + sign_aet * (aet / 60), now_m + sign_aet * (aet % 60)
            set_h, set_m = (set_h + set_m / 60) % 24, set_m % 60
            true_h, true_m = set_h, set_m
        elif time_seg == "point":
            set_h, set_m = et[1].split(":")
            set_h, set_m = int(set_h), int(set_m)
            true_h, true_m = set_h, set_m
        elif time_seg == "delay":
            set_h, set_m = et[1].split(":")
            set_h, set_m = int(set_h), int(set_m)
            true_h, true_m = int(set_h) + now_h, int(set_m) + leave_time + now_m
            true_h, true_m = (true_h + true_m / 60) % 24, true_m % 60
        else:
            set_h, set_m = "error", "error"
            true_h, true_m = set_h, set_m

        start_h, start_m = (now_h + (now_m + leave_time) / 60) % 24, (now_m + leave_time) % 60
        start_time = "%02d:%02d" % (start_h, start_m)
        set_time = "%02d:%02d" % (set_h, set_m)
        true_time = "%02d:%02d" % (true_h, true_m)
        
        et_h = abs(set_h - roll_now_h)
        et_m = abs(set_m - roll_now_m)
        try:
            end_y_h = start_y_h - (set_h - roll_now_h) / et_h * aszh_h
        except ZeroDivisionError:
            end_y_h = start_y_h
        try:
            end_y_m = start_y_m - (set_m - roll_now_m) / et_m * aszh_m
        except ZeroDivisionError:
            end_y_m = start_y_m
        # 分钟在前，时钟在后，若为00:00，滚轮会自动加一
        while et_m > 0:
            self.driver.swipe(start_x_m, start_y_m, start_x_m, end_y_m, 0)
            et_m -= 1
        while et_h > 0:
            self.driver.swipe(start_x_h, start_y_h, start_x_h, end_y_h, 0)
            et_h -= 1

        self.logger.info("start_time: %s, set_time: %s, true_time: %s" % (start_time, set_time, true_time))
        if self.ac.get_attribute(self.wait_widget(elem_t), "name") == set_time:
            return start_time, true_time
        else:
            raise TimeoutException("timer set error")

    # 定时检查模板，用时删减
    def check_timer(self, start_time, set_time, power_state, power_same_prev=False):
        start_h, start_m = start_time.split(":")
        start_times = int(start_h) * 60 + int(start_m)
        set_h, set_m = set_time.split(":")
        set_times = int(set_h) * 60 + int(set_m)
        if start_times < set_times:
            delay_times = (set_times - start_times) * 60
        else:
            delay_times = 24 * 60 * 60 + (set_times - start_times) * 60
        self.logger.info("[APP_TIMER]Delay Time:%s" % (delay_times + 30))
        while True:
            if time.strftime("%H:%M") == start_time:
                now = time.time()
                break
            else:
                time.sleep(1)
        self.logger.info("[APP_TIMER]Now Time:%s" % time.strftime("%H:%M:%S"))
        element = self.wait_widget(self.page["control_device_page"]["power_state"])
        while True:
            if time.strftime("%H:%M") == set_time:
                if power_same_prev is False:
                    while True:
                        if self.ac.get_attribute(element, "name") == power_state:
                            self.logger.info("[APP_TIMER]End Time:%s[%s]" % (time.strftime("%H:%M:%S"), time.time()))
                            self.logger.info(u"[APP_INFO]Device Info:%s" % power_state)
                            break
                        else:
                            time.sleep(1)
                else:
                    while True:
                        time.sleep(10)
                        if self.ac.get_attribute(element, "name") == power_state:
                            self.logger.info(
                                "[APP_TIMER]End Time:%s[%s]" % (time.strftime("%H:%M:%S"), (time.time() - 10)))
                            self.logger.info(u"[APP_INFO]Device Info:%s" % power_state)
                            break
                        else:
                            time.sleep(1)
                break
            else:
                if time.time() < now + delay_times + 30:
                    time.sleep(1)
                else:
                    raise TimeoutException("Device state Error")
    
    # 删除普通定时
    def delete_normal_timer(self):
        while True:
            try:
                self.wait_widget(self.page["normal_timer_page"]["no_timer"])
                self.logger.info("It has no timer~")
                break
            except TimeoutException:
                self.logger.info("It has normal timer.")
                self.widget_click(self.page["normal_timer_page"]["timer_edit"],
                                  self.page["timer_edit_popup"]["title"])

                self.widget_click(self.page["timer_edit_popup"]["delete"],
                                  self.page["normal_timer_page"]["title"])

    # 关闭模式定时
    def close_mode_timer(self):
        element = self.wait_widget(self.page["control_device_page"]["mode_timer"])
        while True:
            attribute = self.ac.get_attribute(element, "name")
            if u"未启用" not in attribute:
                self.logger.info("[APP_INFO]Mode timer is run")
                self.widget_click(self.page["control_device_page"]["mode_timer"],
                                  self.page["mode_timer_page"]["title"])

                if u"热水器模式" in attribute:
                    self.widget_click(self.page["mode_timer_page"]["water_button"],
                                      self.page["mode_timer_page"]["title"])
                elif u"鱼缸模式" in attribute:
                    self.widget_click(self.page["mode_timer_page"]["fish_button"],
                                      self.page["mode_timer_page"]["title"])
                else:
                    self.widget_click(self.page["mode_timer_page"]["piocc_button"],
                                      self.page["mode_timer_page"]["title"])

                time.sleep(5)

                self.widget_click(self.page["mode_timer_page"]["to_return"],
                                  self.page["control_device_page"]["title"])
            else:
                self.logger.info("[APP_INFO]Mode timer don't run")
                break
