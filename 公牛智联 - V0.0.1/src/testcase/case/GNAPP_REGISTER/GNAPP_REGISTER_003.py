# coding=utf-8
from src.testcase.case.LaunchApp import *
from src.utils.ScreenShot import *


class GNAppRegister3(LaunchApp):
    def run(self):
        self.case_module = u"注册"  # 用例所属模块
        self.case_title = u'注册页面-正确的用户名和密码，验证码大于6位，注册验证'  # 用例名称
        self.zentao_id = 1884  # 禅道ID
        self.basename = os.path.basename(__file__).split(".")[0]  # 获取用例的文件名称:GNAPP_REGISTER_003
        self.logger.info('[GN_INF] <current case> [CASE_ID="%s", CASE_NAME="%s", 禅道ID="%s", CASE_MODULE="%s"]'
                         % (self.basename, self.case_title, self.zentao_id, self.case_module))  # 记录log

        try:
            self.launch_app(True)  # 启动APP
            self.case()
        except WebDriverException:
            pass  # Message: ***
        except BaseException, e:
            self.debug.error("%s:%s" % (self.basename, e))

    # 用例动作
    def case(self):
        try:
            self.widget_click(login_page["title"],
                              login_page["to_register"],
                              register_page["title"],
                              1, 1, 1, 10, 0.5)  # 点击“新用户注册按钮”

            user_name = self.widget_click(register_page["title"],
                                          register_page["username"],
                                          register_page["title"],
                                          1, 1, 1, 10, 0.5)  # 点击用户名输入框

            # 29 is the keycode of 'a', 28672 is the keycode of META_CTRL_MASK
            self.driver.press_keycode(29, 28672)
            # KEYCODE_FORWARD_DEL 删除键 112
            self.driver.press_keycode(112)
            # 发送数据
            data = conf["user_and_pwd"][self.user][0].decode('hex')
            user_name.send_keys(data)  # 输入用户名
            self.logger.info(u'[APP_INPUT] ["用户名"] input success')
            time.sleep(0.5)

            pwd = self.widget_click(register_page["title"],
                                    register_page["password"],
                                    register_page["title"],
                                    1, 1, 1, 10, 0.5)  # 点击密码输入框

            self.driver.press_keycode(29, 28672)
            self.driver.press_keycode(112)
            data = "123456"
            pwd.send_keys(data)
            self.logger.info(u'[APP_INPUT] ["密码"] input success')
            time.sleep(0.5)

            check_code = self.widget_click(register_page["title"],
                                           register_page["check_code"],
                                           register_page["title"],
                                           1, 1, 1, 10, 0.5)  # 点击验证码输入框

            self.driver.press_keycode(29, 28672)
            self.driver.press_keycode(112)
            data = "1234567"  # 传入超过6位的验证码
            check_code.send_keys(data)
            self.logger.info(u'[APP_INPUT] ["注册验证码"] input success')
            time.sleep(0.5)

            check_code = self.wait_widget(register_page["check_code"], 1, 0.5).get_attribute("name")
            if len(check_code) != 6:  # 检测验证码长度
                raise TimeoutException()

            self.case_over(True)
        except TimeoutException:
            self.case_over(False)

    def output(self):
        self.run()
        return self.result()
