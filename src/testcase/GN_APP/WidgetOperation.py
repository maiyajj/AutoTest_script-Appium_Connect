# coding=utf-8
from src.testcase.GN_APP.LaunchApp import *


class WidgetOperation(LaunchApp):
    # 密码框显示密码
    def show_pwd(self, element, display=True):
        while True:
            try:
                if self.ac.get_attribute(element, "checked") == str(display).lower():
                    break
                else:
                    element.click()
            except BaseException:
                self.debug.error(traceback.format_exc())

    # 等待密码超时恢复
    def wait_pwd_timeout(self):
        i = 1
        while i <= 31:
            time.sleep(10)
            print("time sleep %sS" % (i * 10))
            self.debug.info("time sleep %sS" % (i * 10))
            i += 1
