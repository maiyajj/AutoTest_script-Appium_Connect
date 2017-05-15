# coding=utf-8
from src.testcase.case.LaunchApp import *
from src.utils.ScreenShot import *


class GNAppLogin8(LaunchApp):
    def run(self):
        self.case_module = u"登录"  # 用例所属模块
        self.case_title = u'登录页面—密码输入超过5次后，信息检查'  # 用例名称
        self.zentao_id = 1898  # 禅道ID
        self.basename = os.path.basename(__file__).split(".")[0]  # 获取用例的文件名称:GNAPP_LOGIN_008
        self.driver = self.return_driver()
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
            user_name = self.widget_click(login_page["title"],
                                          login_page["username"],
                                          login_page["title"],
                                          1, 1, 1, 10, 0.5)

            # 29 is the keycode of 'a', 28672 is the keycode of META_CTRL_MASK
            self.driver.press_keycode(29, 28672)
            # KEYCODE_FORWARD_DEL 删除键 112
            self.driver.press_keycode(112)
            # 发送数据
            data = str(conf["user_and_pwd"][self.user][0]).decode('hex')
            user_name.send_keys(data)
            self.logger.info(u'[APP_INPUT] ["用户名"] input success')
            time.sleep(0.5)

            count = 1
            while count > 0:
                login_pwd = self.widget_click(login_page["title"],
                                              login_page["password"],
                                              login_page["title"],
                                              1, 1, 1, 10, 0.5)

                self.driver.press_keycode(29, 28672)
                self.driver.press_keycode(112)
                data = str(conf["err_pwd"]).decode('hex')
                login_pwd.send_keys(data)
                self.logger.info(u'[APP_INPUT] ["错误密码"] input success')
                time.sleep(0.5)

                self.widget_click(login_page["title"],
                                  login_page["login_button"],
                                  god_page["title"],
                                  1, 1, 1, 10, 0.5)

                while True:
                    try:
                        self.wait_widget(loading_popup["title"], 1, 0.5)
                    except TimeoutException:
                        break

                count -= 1

            login_pwd = self.widget_click(login_page["title"],
                                          login_page["password"],
                                          login_page["title"],
                                          1, 1, 1, 10, 0.5)

            self.driver.press_keycode(29, 28672)
            self.driver.press_keycode(112)
            data = str(conf["user_and_pwd"][self.user][1]).decode('hex')
            login_pwd.send_keys(data)
            self.logger.info(u'[APP_INPUT] ["正确密码"] input success')
            time.sleep(0.5)

            widget_px = login_page["login_button"]
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
