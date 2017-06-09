# coding=utf-8
from src.testcase.case.LaunchApp import *


class GNAppLogin10(LaunchApp):
    def run(self):
        self.case_module = u"登录"  # 用例所属模块
        self.case_title = u'登录页面—位数错误的数字账号，登录提示信息检查'  # 用例名称
        self.zentao_id = 1895  # 禅道ID
        self.basename = os.path.basename(__file__).split(".")[0]  # 获取用例的文件名称:GNAPP_LOGIN_010
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
            user_name = self.widget_click(self.page["login_page"]["title"],
                                          self.page["login_page"]["username"],
                                          self.page["login_page"]["title"],
                                          1, 1, 1, 10, 0.5)

            # 发送数据
            data = "1"
            user_name.clear()
            self.ac.send_keys(user_name, data)
            self.logger.info(u'[APP_INPUT] ["位数错误用户名"] input success')
            time.sleep(0.5)

            login_pwd = self.widget_click(self.page["login_page"]["title"],
                                          self.page["login_page"]["password"],
                                          self.page["login_page"]["title"],
                                          1, 1, 1, 10, 0.5)

            data = conf["user_and_pwd"][self.user]["login_pwd"]
            data = str(data).decode('hex').replace(" ", "")
            self.show_pwd(self.wait_widget(self.page["login_page"]["check_box"]))
            login_pwd.clear()
            self.ac.send_keys(login_pwd, data)
            self.logger.info(u'[APP_INPUT] ["登录密码"] input success')
            time.sleep(0.5)

            widget_px = self.page["login_page"]["login_button"][3]["px"]
            width = int(int(self.device_info["dpi"]["width"]) * widget_px["width"])
            height = int(int(self.device_info["dpi"]["height"]) * widget_px["height"])
            self.driver.tap([(width, height)], )
            self.logger.info(u'[APP_CLICK] operate_widget ["%s"] success' % widget_px[2])

            while True:
                try:
                    self.wait_widget(self.page["loading_popup"]["title"], 0.5, 0.1)
                except TimeoutException:
                    break

                # 截屏获取设备toast消息
                ScreenShot(self.device_info, self.zentao_id, self.basename, self.logger)

            try:
                login_pwd = self.widget_click(self.page["login_page"]["title"],
                                              self.page["login_page"]["password"],
                                              self.page["login_page"]["title"],
                                              1, 1, 1, 10, 0.5)

                data = conf["user_and_pwd"][self.user]["login_pwd"]
                data = str(data).decode('hex').replace(" ", "")
                self.show_pwd(self.wait_widget(self.page["login_page"]["check_box"]))
                login_pwd.clear()
                self.ac.send_keys(login_pwd, data)
                self.logger.info(u'[APP_INPUT] ["正确密码"] input success')
                self.widget_click(self.page["login_page"]["title"],
                                  self.page["login_page"]["login_button"],
                                  self.page["device_page"]["title"],
                                  1, 1, 1, 10, 0.5)
            except TimeoutException:
                i = 1
                while i <= 33:
                    time.sleep(10)
                    widget_px = self.page["god_page"]["title"][3]["px"]
                    width = int(int(self.device_info["dpi"]["width"]) * widget_px["width"])
                    height = int(int(self.device_info["dpi"]["height"]) * widget_px["height"])
                    self.driver.tap([(width, height)], )
                    print "time sleep %sS" % (i * 10)
                    i += 1
                self.widget_click(self.page["login_page"]["title"],
                                  self.page["login_page"]["login_button"],
                                  self.page["device_page"]["title"],
                                  1, 1, 1, 10, 0.5)

            self.case_over("screen")
        except TimeoutException:
            self.case_over(False)

    def output(self):
        self.run()
        return self.result()
