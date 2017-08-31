# coding=utf-8
from LaunchApp_GN import *
from LaunchApp_JD import *
from src.testcase.common.WidgetCheckUnit import *


def case_run(bool):
    def wrapper(func):
        def _wrapper(self):
            func(self)
            self.init_operate()
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
                database["unknown"] += 1
                if database["unknown"] > 1:
                    database["unknown"] = 0
                    self.debug.error("Too many unknown case!:%s" % self.basename)
                    self.reset_port()

            # 记录运行结果
            return self.result()

        return _wrapper
    return wrapper


# def case_run(bool):
#     def wrapper(func):
#         def _wrapper(self):
#             func(self)
#             if self.app == "GN":
#                 WaitCaseGN(device_list, device_name)
#             elif self.app == "JD":
#                 WaitCaseJD(device_list, device_name)
#             else:
#                 raise KeyError("%s:The App not support" % self.app)
#
#         return _wrapper
#     return wrapper
class LaunchApp(object):
    # def __init__(self, **kwargs):
    #     self.kwargs = kwargs
    #     self.app = kwargs["app"]
    #
    # def launch_app(self):
    #     if self.app == "GN":
    #         return LaunchAppGN(**self.kwargs).init_app()
    #     elif self.app == "JD":
    #         return LaunchAppJD(**self.kwargs).init_app()
    #     else:
    #         raise KeyError("%s:No such App!" % self.app)
    def __init__(self, **kwargs):
        self.kwargs = kwargs
        self.app = kwargs["device_info"]["app"]
        self.lgn = LaunchAppGN(**kwargs)
        self.ljd = LaunchAppJD(**kwargs)

    def reset_port(self):
        if self.app == "GN":
            self.lgn.reset_port()
        elif self.app == "JD":
            self.ljd.reset_port()
        else:
            raise KeyError("The app does not support")

    def http_run_app(self, strong_reboot=False):
        global driver
        if self.app == "GN":
            driver = self.lgn.http_run_app(strong_reboot)
        elif self.app == "JD":
            driver = self.ljd.http_run_app(strong_reboot)
        else:
            raise KeyError("The app does not support")

    def check_appium_launch(self):
        if self.app == "GN":
            self.lgn.check_appium_launch()
        elif self.app == "JD":
            self.ljd.check_appium_launch()
        else:
            raise KeyError("The app does not support")
    def wait_pwd_timeout(self):
        if self.app == "GN":
            self.lgn.wait_pwd_timeout()
        elif self.app == "JD":
            self.ljd.wait_pwd_timeout()
        else:
            raise KeyError("The app does not support")

    def check_user_pwd(self):
        if self.app == "GN":
            self.lgn.check_user_pwd()
        elif self.app == "JD":
            self.ljd.check_user_pwd()
        else:
            raise KeyError("The app does not support")

    def init_app(self):
        # global driver
        if self.app == "GN":
            return self.lgn.init_app()
        elif self.app == "JD":
            return self.ljd.init_app()
        else:
            raise KeyError("The app does not support")

    def init_operate(self):
        if self.app == "GN":
            self.lgn.init_operate()
        elif self.app == "JD":
            self.ljd.init_operate()
        else:
            raise KeyError("The app does not support")

    def data_statistics(self, zentao_id):
        if self.app == "GN":
            self.lgn.data_statistics(zentao_id)
        elif self.app == "JD":
            self.ljd.data_statistics(zentao_id)
        else:
            raise KeyError("The app does not support")

    def launch_app(self):
        if self.app == "GN":
            self.lgn.launch_app()
        elif self.app == "JD":
            self.ljd.launch_app()
        else:
            raise KeyError("The app does not support")

    def return_driver(self):
        return driver

    def show_pwd(self, element, bool=True):
        if self.app == "GN":
            self.lgn.show_pwd(element, bool)
        elif self.app == "JD":
            self.ljd.show_pwd(element, bool)
        else:
            raise KeyError("The app does not support")

    def case_over(self, success):
        if self.app == "GN":
            self.lgn.case_over(success)
        elif self.app == "JD":
            self.ljd.case_over(success)
        else:
            raise KeyError("The app does not support")

    # 记录运行结果
    def result(self):
        if self.app == "GN":
            self.lgn.result()
        elif self.app == "JD":
            self.ljd.result()
        else:
            raise KeyError("The app does not support")
