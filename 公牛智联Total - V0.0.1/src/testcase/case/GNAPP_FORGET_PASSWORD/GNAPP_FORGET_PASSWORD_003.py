# coding=utf-8
from src.testcase.case.LaunchApp import *


class GNAppForgetPassword3(LaunchApp):
    def run(self):
        self.case_module = u"忘记密码"  # 用例所属模块
        self.case_title = u'忘记密码页面-点击返回登入界面"按钮，页面检查"'  # 用例名称
        self.zentao_id = 1907  # 禅道ID
        self.basename = os.path.basename(__file__).split(".")[0]  # 获取用例的文件名称:GNAPP_FORGET_PASSWORD_003
        self.logger.info('[GN_INF] <current case> [CASE_ID="%s", CASE_NAME="%s", 禅道ID="%s", CASE_MODULE="%s"]'
                         % (self.basename, self.case_title, self.zentao_id, self.case_module))  # 记录log

        try:
            self.launch_app(True)  # 启动APP
            self.case()
        except BaseException:
            self.debug.error(traceback.format_exc())  # Message: ***
            self.case_over("unknown")

    # 用例动作
    def case(self):
        try:
            self.widget_click(self.page["login_page"]["title"],
                              self.page["login_page"]["to_find_password"],
                              self.page["find_password_page"]["title"],
                              1, 1, 1, 10, 0.5)

            self.widget_click(self.page["find_password_page"]["title"],
                              self.page["find_password_page"]["to_return"],
                              self.page["login_page"]["title"],
                              1, 1, 1, 10, 0.5)

            self.case_over(True)
        except TimeoutException:
            self.case_over(False)

    def output(self):
        self.run()
        return self.result()
