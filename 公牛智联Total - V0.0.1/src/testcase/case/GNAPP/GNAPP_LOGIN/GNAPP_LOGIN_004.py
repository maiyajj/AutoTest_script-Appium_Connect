# coding=utf-8
from src.testcase.case.LaunchApp_GN import *


class GNAppLogin4(LaunchAppGN):
    @case_run_gn(True)
    def run(self):
        self.case_module = u"登录"  # 用例所属模块
        self.case_title = u'登录页面—成功登录后杀掉APP，再次开启APP的状态查看'  # 用例名称
        self.zentao_id = 1903  # 禅道ID

    # 用例动作
    def case(self):
        try:
            user_name = self.widget_click(self.page["login_page"]["title"],
                                          self.page["login_page"]["username"],
                                          self.page["login_page"]["title"])

            # 发送数据
            data = self.user["user_name"]
            data = str(data).decode('hex').replace(" ", "")
            user_name.clear()
            self.ac.send_keys(user_name, data, self.driver)
            self.logger.info(u'[APP_INPUT] ["用户名"] input success')
            time.sleep(0.5)

            self.show_pwd(self.wait_widget(self.page["login_page"]["check_box"]))
            login_pwd = self.widget_click(self.page["login_page"]["title"],
                                          self.page["login_page"]["password"],
                                          self.page["login_page"]["title"])

            data = self.user["login_pwd"]
            data = str(data).decode('hex').replace(" ", "")
            login_pwd.clear()
            self.ac.send_keys(login_pwd, data, self.driver)
            self.logger.info(u'[APP_INPUT] ["密码"] input success')
            time.sleep(0.5)

            self.widget_click(self.page["login_page"]["title"],
                              self.page["login_page"]["login_button"],
                              self.page["device_page"]["title"])

            self.driver.close_app()  # 关闭App
            self.debug.warn("(%s)self.driver.close_app() App close" % self.basename)
            self.logger.info(u"[APP_INF] APP退出")
            time.sleep(1)

            self.launch_app(None)
            self.logger.info(u"[APP_INF] APP重新启动")
            while True:
                try:
                    self.wait_widget(self.page["update_popup"]["title"])
                    self.logger.info(u"[APP_INF] APP有最新版本，可以更新")
                    self.widget_click(self.page["update_popup"]["title"],
                                      self.page["update_popup"]["cancel"],
                                      self.page["god_page"]["title"],
                                      log_record=0)
                    self.logger.info(u"[APP_INF] 取消更新")
                except TimeoutException:
                    pass
                try:
                    self.wait_widget(self.page["login_popup"]["title"])
                    self.logger.info(u"[APP_INF] APP需要重新登陆，等待重新登录")
                    self.widget_click(self.page["login_popup"]["title"],
                                      self.page["login_popup"]["confirm"],
                                      self.page["login_page"]["title"],
                                      log_record=0)
                except TimeoutException:
                    pass

                try:
                    self.wait_widget(self.page["login_page"]["title"])
                    self.logger.info(u"[APP_INF] APP当前页面为登录页面， 错误！")
                    raise NoSuchElementException()
                except TimeoutException:
                    pass
                except NoSuchElementException:
                    raise TimeoutException()

                try:
                    self.wait_widget(self.page["device_page"]["title"])
                    self.logger.info(u"[APP_INF] APP当前页面为主页面")
                    break
                except TimeoutException:
                    pass

            self.case_over(True)
        except TimeoutException:
            self.case_over(False)
