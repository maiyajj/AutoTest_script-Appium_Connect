# coding=utf-8
from src.testcase.case.LaunchApp import *
from src.utils.ScreenShot import *


class GNAppRegister11(LaunchApp):
    def run(self):
        self.case_module = u"注册"  # 用例所属模块
        self.case_title = u'注册页面-用户名长度小于11位，提示信息检查'  # 用例名称
        self.zentao_id = 1838  # 禅道ID
        self.basename = os.path.basename(__file__).split(".")[0]  # 获取用例的文件名称:GNAPP_REGISTER_011
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

            user_name = self.widget_click(register_page["title"],
                                          register_page["username"],
                                          register_page["title"],
                                          1, 1, 1, 10, 0.5)

            # 29 is the keycode of 'a', 28672 is the keycode of META_CTRL_MASK
            self.driver.press_keycode(29, 28672)
            # KEYCODE_FORWARD_DEL 删除键 112
            self.driver.press_keycode(112)
            # 发送数据
            data = "1381234"
            user_name.send_keys(data)
            self.logger.info(u'[APP_INPUT] ["用户名"] input success')
            time.sleep(0.5)

            pwd = self.widget_click(register_page["title"],
                                    register_page["password"],
                                    register_page["title"],
                                    1, 1, 1, 10, 0.5)

            self.driver.press_keycode(29, 28672)
            self.driver.press_keycode(112)
            data = "123456"
            pwd.send_keys(data)
            self.logger.info(u'[APP_INPUT] ["密码"] input success')
            time.sleep(0.5)

            check_code = self.widget_click(register_page["title"],
                                           register_page["check_code"],
                                           register_page["title"],
                                           1, 1, 1, 10, 0.5)

            self.driver.press_keycode(29, 28672)
            self.driver.press_keycode(112)
            data = "123456"
            check_code.send_keys(data)
            self.logger.info(u'[APP_INPUT] ["注册验证码"] input success')
            time.sleep(0.5)

            widget_px = register_page["register_button"]
            width = int(int(self.device_info["dpi"]["width"]) * widget_px[3]["width"])
            height = int(int(self.device_info["dpi"]["height"]) * widget_px[3]["height"])
            self.driver.tap([(width, height)], )
            self.logger.info(u'[APP_CLICK] operate_widget ["%s"] success' % widget_px[2])

            while True:
                try:
                    self.wait_widget(loading_popup["title"], 0.5, 0.1)
                except TimeoutException:
                    break

                # 截屏获取设备toast消息
                ScreenShot(self.device_info, self.zentao_id, self.basename, self.logger)

            self.case_over("screen")
        except TimeoutException:
            self.case_over(False)

    def output(self):
        self.run()
        return self.result()
