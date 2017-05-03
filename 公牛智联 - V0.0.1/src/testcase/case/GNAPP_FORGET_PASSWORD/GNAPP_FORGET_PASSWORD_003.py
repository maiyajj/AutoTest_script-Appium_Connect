# coding=utf-8
import os

from src.testcase.case.LaunchApp import *
from src.utils.ScreenShot import *


class GNAppForgetPassword3(LaunchApp):
    def run(self):
        self.case_module = u"忘记密码"  # 用例所属模块
        self.case_title = u'忘记密码页面-点击返回登入界面"按钮，页面检查"'  # 用例名称
        self.ZenTao_id = 1907  # 禅道ID
        self.basename = os.path.basename(__file__).split(".")[0]  # 获取用例的文件名称:GNAPP_FORGET_PASSWORD_003

        self.launch_app(Login_page=True)  # 启动APP
        self.case()

    # 用例动作
    def case(self):
        try:
            self.widget_click(login_page["title"],
                              login_page["to_find_password"],
                              find_password_page["title"],
                              1, 1, 1, 10, 0.5)

            self.widget_click(find_password_page["title"],
                              find_password_page["to_return"],
                              login_page["title"],
                              1, 1, 1, 10, 0.5)

            self.case_over(True)
        except TimeoutException:
            self.case_over(False)

    def output(self):
        self.run()
        return self.result()
