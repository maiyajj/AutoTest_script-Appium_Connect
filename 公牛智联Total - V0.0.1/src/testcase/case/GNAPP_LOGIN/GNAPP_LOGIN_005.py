# coding=utf-8
from src.testcase.case.LaunchApp import *


class GNAppLogin5(LaunchApp):
    def run(self):
        self.case_module = u"登录"  # 用例所属模块
        self.case_title = u'登录页面—成功登录后注销账号，再次进入登录页面查看'  # 用例名称
        self.zentao_id = 1900  # 禅道ID
        self.basename = os.path.basename(__file__).split(".")[0]  # 获取用例的文件名称:GNAPP_LOGIN_005
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
            data = str(conf["user_and_pwd"][self.user][0]).decode('hex').replace(" ", "")
            user_name.clear()
            self.ac.send_keys(user_name, data)
            self.logger.info(u'[APP_INPUT] ["用户名"] input success')
            time.sleep(0.5)

            login_pwd = self.widget_click(self.page["login_page"]["title"],
                                          self.page["login_page"]["password"],
                                          self.page["login_page"]["title"],
                                          1, 1, 1, 10, 0.5)

            data = str(conf["user_and_pwd"][self.user][1]).decode('hex').replace(" ", "")
            self.show_pwd(self.wait_widget(self.page["login_page"]["check_box"]))
            login_pwd.clear()
            self.ac.send_keys(login_pwd, data)
            self.logger.info(u'[APP_INPUT] ["密码"] input success')
            time.sleep(0.5)

            self.widget_click(self.page["login_page"]["title"],
                              self.page["login_page"]["login_button"],
                              self.page["device_page"]["title"],
                              1, 1, 1, 10, 0.5)

            self.widget_click(self.page["device_page"]["title"],
                              self.page["device_page"]["user_image"],
                              self.page["personal_settings_page"]["title"],
                              1, 1, 1, 10, 0.5, 0)

            self.widget_click(self.page["personal_settings_page"]["title"],
                              self.page["personal_settings_page"]["account_setting"],
                              self.page["account_setting_page"]["title"],
                              1, 1, 1, 10, 0.5, 0)

            self.widget_click(self.page["account_setting_page"]["title"],
                              self.page["account_setting_page"]["logout"],
                              self.page["logout_popup"]["title"],
                              1, 1, 1, 10, 0.5, 0)

            self.widget_click(self.page["logout_popup"]["title"],
                              self.page["logout_popup"]["confirm"],
                              self.page["login_page"]["title"],
                              1, 1, 1, 10, 0.5, 0)

            self.debug.warn("(%s)self.driver.close_app() App closed" % self.basename)
            self.logger.info(u"[APP_INF] APP退出")
            time.sleep(1)

            self.launch_app(True)
            self.logger.info(u"[APP_INF] APP重新启动")
            while True:
                try:
                    self.wait_widget(self.page["update_popup"]["title"], 3, 1)
                    self.logger.info(u"[APP_INF] APP有最新版本，可以更新")
                    self.widget_click(self.page["update_popup"]["title"],
                                      self.page["update_popup"]["cancel"],
                                      self.page["god_page"]["title"],
                                      1, 1, 1, 10, 0.5, 0)
                    self.logger.info(u"[APP_INF] 取消更新")
                except TimeoutException:
                    pass
                try:
                    self.wait_widget(self.page["login_popup"]["title"], 3, 1)
                    self.logger.info(u"[APP_INF] APP需要重新登陆，等待重新登录")
                    self.widget_click(self.page["login_popup"]["title"],
                                      self.page["login_popup"]["confirm"],
                                      self.page["login_page"]["title"],
                                      1, 1, 1, 10, 0.5, 0)
                except TimeoutException:
                    pass

                try:
                    self.wait_widget(self.page["device_page"]["title"], 3, 1)
                    self.logger.info(u"[APP_INF] APP当前页面为主页面， 错误！")
                    raise NoSuchElementException()
                except TimeoutException:
                    pass
                except NoSuchElementException:
                    raise TimeoutException()

                try:
                    self.wait_widget(self.page["login_page"]["title"], 3, 1)
                    self.logger.info(u"[APP_INF] APP当前页面为登录页面")
                    break
                except TimeoutException:
                    pass

            user_name = self.widget_click(self.page["login_page"]["title"],
                                          self.page["login_page"]["username"],
                                          self.page["login_page"]["title"],
                                          1, 1, 1, 10, 0.5)

            # 发送数据
            data = str(conf["user_and_pwd"][self.user][0]).decode('hex').replace(" ", "")
            user_name.clear()
            self.ac.send_keys(user_name, data)
            self.logger.info(u'[APP_INPUT] ["用户名"] input success')
            time.sleep(0.5)

            login_pwd = self.widget_click(self.page["login_page"]["title"],
                                          self.page["login_page"]["password"],
                                          self.page["login_page"]["title"],
                                          1, 1, 1, 10, 0.5)

            data = str(conf["user_and_pwd"][self.user][1]).decode('hex').replace(" ", "")
            self.show_pwd(self.wait_widget(self.page["login_page"]["check_box"]))
            login_pwd.clear()
            self.ac.send_keys(login_pwd, data)
            self.logger.info(u'[APP_INPUT] ["密码"] input success')
            time.sleep(0.5)

            self.widget_click(self.page["login_page"]["title"],
                              self.page["login_page"]["login_button"],
                              self.page["device_page"]["title"],
                              1, 1, 1, 10, 0.5)

            self.case_over(True)
        except TimeoutException:
            self.case_over(False)

    def output(self):
        self.run()
        return self.result()
