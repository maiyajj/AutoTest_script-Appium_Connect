# coding=utf-8
from src.testcase.case.LaunchApp import *
from src.utils.ScreenShot import *


class GNAppRegister7(LaunchApp):
    def run(self):
        self.case_module = u"注册"  # 用例所属模块
        self.case_title = u'注册页面-验证码为中文字符时，提示信息检查'  # 用例名称
        self.zentao_id = 1880  # 禅道ID
        self.basename = os.path.basename(__file__).split(".")[0]  # 获取用例的文件名称:GNAPP_REGISTER_007
        self.logger.info('[GN_INF] <current case> [CASE_ID="%s", CASE_NAME="%s", 禅道ID="%s", CASE_MODULE="%s"]'
                         % (self.basename, self.case_title, self.zentao_id, self.case_module))  # 记录log

        try:
            self.launch_app(True)  # 启动APP
            self.case()
        except WebDriverException:
            pass  # Message: ***

    # 用例动作
    def case(self):
        try:
            self.widget_click(login_page["title"],
                              login_page["to_register"],
                              register_page["title"],
                              1, 1, 1, 10, 0.5)

            check_code = self.widget_click(register_page["title"],
                                           register_page["check_code"],
                                           register_page["title"],
                                           1, 1, 1, 10, 0.5)

            self.driver.press_keycode(29, 28672)
            self.driver.press_keycode(112)
            data = u"测试"
            check_code.send_keys(data)
            self.logger.info(u'[APP_INPUT] ["注册验证码"] input success')
            time.sleep(0.5)

            check_code = self.wait_widget(register_page["check_code"], 1, 0.5).get_attribute("name")
            if len(check_code) != 0:
                raise TimeoutException()

            self.case_over(True)
        except TimeoutException:
            self.case_over(False)

    def output(self):
        self.run()
        return self.result()
