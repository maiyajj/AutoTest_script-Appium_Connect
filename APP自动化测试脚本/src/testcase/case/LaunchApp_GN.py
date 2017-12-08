# coding=utf-8
import inspect
from httplib import BadStatusLine
from urllib2 import URLError

import psutil
from appium import webdriver

from src.testcase.case.ToDevicePage import *
from src.testcase.case.ToLoginPage import *
# from src.testcase.common.WidgetCheckUnit import *
from src.utils.ScreenShot import *


# launch()启动APP
def decor_launch_app(func):
    def wrapper(self, page_login):
        self.debug.info("basename: %s" % self.basename)
        self.data_statistics(self.zentao_id)  # 初始化数据统计
        i = 0
        while True:
            try:
                self.sc.kill_zombie_proc()  # 杀死多余进程，在Mac中运行，僵尸进程可能会使系统卡死造成脚本执行缓慢
                func(self)  # 执行 self.launch_fail_fix()
                self.init_operate()  # 初始化控件操作
                self.start_time = time.strftime("%Y-%m-%d %X")
                log_tmp = 'app start [time=%s]' % self.start_time
                self.logger.info(log_tmp)  # 记录log，APP打开时间
                self.debug.info(log_tmp)  # 记录log，APP打开时间
                self.success = False  # 初始化用例执行结果

                if page_login is True:  # 执行用例前使APP进入登录页面
                    ToLoginPage(self.driver, self.device_info)  # 使APP跳转到登录页面等待
                    break
                elif page_login is False:  # 执行用例前使APP进入APP主页面
                    ToDevicePage(self.driver, self.device_info)  # 使APP跳转到设备主页面等待
                    break
                else:  # 待定
                    pass
            except BaseException, e:
                self.debug.error("case_over: %s" % traceback.format_exc())  # 出了错误就一定要记录
                i += 1
                if i >= 3:  # 启动3次失败
                    self.case_over("unknown")
                    raise WebDriverException(e)

    return wrapper


# 启动失败修复，保证启动成功
def launch_fail_fix(func):
    def wrapper(self):
        i = 1
        ii = 1
        while True:
            try:
                func(self)  # 启动APP相关，launch()启动或http启动
                break
            except WebDriverException, e:  # 抛出WebDriverException可能是偶然启动失败
                e = "".join(str(e).split())
                # 错误信息只有"Message:"则表示Appium服务已停止，手机端发送信息无返回
                # "Message: A session is either terminated or not started"表示PC与手机的连接已变更，Launch_App无法启动
                if e == "Message:" or e == "Message: A session is either terminated or not started":
                    self.debug.error(traceback.format_exc())  # 记录错误信息
                    self.http_run_app(True)  # 关闭Appium和手机端对应端口来终止Appium服务
                else:  # 有详细错误信息表示Appium仍在运行
                    self.debug.error(traceback.format_exc())  # 记录错误信息
                    self.debug.error("launch_app driver(WebDriverException): %s times" % i)
                    time.sleep(1)
                    if i == 3:
                        self.http_run_app()  # 不做任何操作重新启动APP
                    elif i >= 4:
                        self.http_run_app(True)  # 重置Appium服务后重新启动APP
                        i = 0
                    i += 1
            except URLError:  # 抛出URLError说明Appium服务已停止运行
                self.debug.error("launch_app driver(URLError): %s times" % ii)
                ii += 1
                self.http_run_app(True)  # 重置Appium服务后重新启动APP
                break
            except BadStatusLine:  # 抛出BadStatusLine说明Appium服务在运行中发生了严重错误
                self.debug.error("launch_app driver(BadStatusLine)")
                self.http_run_app(True)  # 重置Appium服务后重新启动APP
                break
            except BaseException:
                self.debug.error(traceback.format_exc())

    return wrapper


# 用例执行
def case_run(bool):
    def wrapper(func):
        def _wrapper(self):
            func(self)  # 用例相关所属模块，标题，禅道ID
            self.basename = re.findall(r"\((.+?)\)", inspect.stack()[2][4][0])[0]  # 获取用例的文件名称:GNAPP_LOGIN_001
            self.logger.info('[GN_INF] <current case> [CASE_ID="%s", CASE_NAME="%s", 禅道ID="%s", CASE_MODULE="%s"]'
                             % (self.basename, self.case_title, self.zentao_id, self.case_module))  # 记录log
            try:
                self.launch_app(bool)  # 启动APP并使APP跳转到指定页面
                try:
                    self.case()  # 执行测试用例
                    self.case_over(True)  # 用例执行成功
                except TimeoutException:
                    self.case_over(False)  # 用例执行失败
                    self.debug.error("case_over: %s\n" % traceback.format_exc())  # 记录错误信息
                    self.debug.error("Now page source: \n%s" % self.driver.page_source)
                database["unknown"] = 0  # 用例有执行成功过说明Appium服务运行正常，次数归零
            except BaseException:
                self.case_over("unknown")  # 用例执行错误
                self.debug.error("case_error: %s\n" % traceback.format_exc())  # Message: ***
                self.debug.error("Now page source: \n%s" % self.driver.page_source)
                database["unknown"] += 1  # 用例执行错误次数+1
                if database["unknown"] > 5:  # 执行错误次数大于5次重置Appium服务
                    database["unknown"] = 0
                    self.debug.error("Too many unknown case!: %s" % self.basename)
                    self.reset_port()
            finally:
                try:
                    self.driver.close_app()  # 关闭APP
                    self.driver.quit()  # 用例执行结束关闭断开连接
                    self.debug.warn("driver quit success")
                except BaseException:
                    self.debug.warn("driver need not quit")

            # 记录运行结果
            return self.result()

        return _wrapper

    return wrapper


class LaunchAppGN(object):
    def __init__(self, device_info):
        self.device_info = device_info  # 设备信息表
        self.page = device_info["page"]  # APP页面元素库
        self.logger = device_info["logger"]  # log日志实例化
        self.debug = device_info["debug"]  # debug日志实例化
        self.device_name = device_info["udid"]  # 设备名称
        self.udid = device_info["udid"]  # 设备udid
        self.port = device_info["port"]  # appium服务端口
        self.bp_port = device_info["bp_port"]  # appium返回Android端口
        self.wda_port = device_info["wda_port"]  # appium返回iOS端口
        self.app = device_info["app"]  # APP型号
        self.desired_caps = device_info["desired_caps"]  # APP参数
        self.sc = device_info["sc"]  # ShellCommand实例化
        self.ac = AppiumCommand(device_info["platformName"])  # AppiumCommand实例化
        device_info["ac"] = self.ac

        self.user = conf["user_and_pwd"][self.device_name][self.app]  # APP配置
        self.case_module = ""  # 用例所属模块
        self.case_title = ""  # 用例名称
        self.zentao_id = 0000  # 禅道ID
        self.basename = ""  # 用例自动化文件名称
        self.success = False  # 初始化用例执行结果
        self.main_pid = psutil.Process(os.getpid()).parent().parent().pid  # 主进程pid
        self.widget_click = None  # 初始化
        self.wait_widget = None  # 初始化
        self.start_time = None  # 初始化

    # 关闭占用端口来停止相应服务
    def reset_port(self):
        for ports in [self.port]:
            proc_pid = self.sc.find_proc_and_pid_by_port(ports)
            if proc_pid == []:  # 判断当前端口是否被占用
                self.debug.info("COM %s unused" % ports)
            else:
                for i in proc_pid:
                    self.sc.kill_proc_by_pid(i[1])
                    self.debug.info("Kill %s" % i[0])

    # 重新连接PC和手机
    def http_run_app(self, strong_reboot=False):
        while True:
            try:
                if strong_reboot is True:  # 重置端口后再启动Appium服务
                    if self.device_info["udid"] in self.sc.get_phone_udid():  # 判断手机是否还跟PC保持正常连接
                        self.reset_port()  # 重置端口
                    else:
                        self.debug.error("device is disconnected")
                self.check_appium_launch()  # 判断Appium服务是否已启动
                try:
                    self.driver.quit()  # 关闭残余连接
                    self.debug.warn("driver quit success")
                except BaseException:
                    self.debug.warn("driver need not quit")
                self.driver = webdriver.Remote('http://localhost:%s/wd/hub' % self.port, self.desired_caps)  # 启动APP
                self.init_operate()  # 初始化操作
                break
            except WebDriverException:
                # 再次启动失败只能用例判执行错误
                self.debug.error("URLError driver(WebDriverException)")
                break
            except URLError:
                # 再次启动失败只能用例判执行错误
                self.debug.error("URLError driver(URLError)")
                break

    # 检查Appium服务是否已启动
    def check_appium_launch(self):
        """
        启动Appium服务后会占用相应端口，故轮询检测端口是否被占用来判断Appium服务是否已启动
        """
        end_time = time.time() + 10
        while True:
            # 主进程崩溃后有残留子进程，关闭当前子进程
            if not psutil.pid_exists(self.main_pid):
                psutil.Process(os.getpid()).kill()
                self.debug.info("launch_app_port: pid %s" % os.getpid())
            try:
                self.sc.find_proc_and_pid_by_port(self.port)[0]
            except IndexError:
                self.debug.info("Appium Sever is death! %s" % time.strftime("%Y-%m-%d %X"))
                time.sleep(1)
                if time.time() > end_time:  # 启动失败重置端口
                    self.reset_port()  # 不能使用self.http_run_app(True),会递归调用错误
            else:
                self.debug.info("Appium Sever launch Success! %s" % time.strftime("%Y-%m-%d %X"))
                break

    # 实例化用例操作
    def init_operate(self):
        widget_check_unit = WidgetCheckUnit(self.driver, self.device_info)  # 元素初始化
        self.widget_click = widget_check_unit.widget_click  # 初始化self.widget_click
        self.wait_widget = widget_check_unit.wait_widget  # 初始化self.wait_widget
        self.debug.info("driver(init_operate success)")

    # 数据统计
    def data_statistics(self, zentao_id):
        self.debug.info("zentao_id: %s" % zentao_id)
        if zentao_id in database[self.device_name].keys():
            pass
        else:
            database[self.device_name][zentao_id] = {}
            database[self.device_name][zentao_id]["test_count"] = 0  # 总用例数
            database[self.device_name][zentao_id]["test_pass"] = 0  # 执行成功用例数
            database[self.device_name][zentao_id]["test_fail"] = 0  # 执行失败用例数
            database[self.device_name][zentao_id]["test_error"] = 0  # 执行错误用例数
            database[self.device_name][zentao_id]["test_wait"] = 0  # 待手动检查用例数
            database[self.device_name][zentao_id]["ZenTao"] = zentao_id  # 禅道ID
            database[self.device_name][zentao_id]["case_title"] = self.case_title  # 用例标题
        self.debug.info("case_title: %s" % self.case_title)

    # launch()启动APP
    @decor_launch_app
    @launch_fail_fix
    def launch_app(self):
        self.check_appium_launch()  # 判断Appium服务是否已启动
        # 记录调试信息
        with open("appium command %s.log" % self.device_name, "a") as files:
            files.write('''driver = webdriver.Remote('http://localhost:%s/wd/hub', %s)''' % (
                self.port, self.desired_caps) + "\n\n")
        self.driver = webdriver.Remote('http://localhost:%s/wd/hub' % self.port, self.desired_caps)  # 启动APP

    # 用例执行完毕
    def case_over(self, success):
        self.success = success
        database[self.device_name][self.zentao_id]["test_count"] += 1

    # 记录用例执行结果
    def result(self):
        d_result = {True: ["success", "test_pass"],
                    False: ["failed", "test_fail"],
                    "unknown": ["unknown", "test_error"],
                    "screen": ["wait", "test_wait"]}
        result = d_result[self.success]
        self.logger.info('[GN_INF] <current case> [CASE_TITLE="%s"] %s!' % (self.case_title, result[0]))
        database[self.device_name][self.zentao_id][result[1]] += 1
        return self.zentao_id, "%s,%s" % (result[0], " " * (7 - len(result[0]))), self.case_title, self.start_time
