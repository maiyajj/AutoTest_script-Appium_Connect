# coding=utf-8
from src.testcase.case.LaunchApp import *
from src.utils.ScreenShot import *


class GNAppRegister1(LaunchApp):
    def run(self):
        self.case_module = u"注册"  # 用例所属模块
        self.case_title = u'注册页面-已有账户登录按钮，跳转页面检查'  # 用例名称
        self.zentao_id = 1888  # 禅道ID
        self.basename = os.path.basename(__file__).split(".")[0]  # 获取用例的文件名称:GNAPP_REGISTER_001
        self.logger.info('[GN_INF] <current case> [CASE_ID="%s", CASE_NAME="%s", 禅道ID="%s", CASE_MODULE="%s"]'
                         % (self.basename, self.case_title, self.zentao_id, self.case_module))  # 记录log

        try:
            self.launch_app(True)  # 启动APP
            self.case()
        except WebDriverException:
            self.debug.error(traceback.format_exc())  # Message: ***

    # 用例动作
    def case(self):
        try:
            self.widget_click(login_page["title"],
                              login_page["to_register"],
                              register_page["title"],
                              1, 1, 1, 10, 0.5)

            self.widget_click(register_page["title"],
                              register_page["to_login"],
                              login_page["title"],
                              1, 1, 1, 10, 0.5)

            self.case_over(True)
        except TimeoutException:
            self.case_over(False)

    def output(self):
        self.run()
        return self.result()
