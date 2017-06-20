# coding=utf-8
from src.testcase.case.LaunchApp import *


class GNAppLogin4(LaunchApp):
    def run(self):
        self.case_module = u"登录"  # 用例所属模块
        self.case_title = u'登录页面—成功登录后杀掉APP，再次开启APP的状态查看'  # 用例名称
        self.zentao_id = 1903  # 禅道ID
        self.basename = os.path.basename(__file__).split(".")[0]  # 获取用例的文件名称:GNAPP_LOGIN_004
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
                              self.page["login_page"]["login_button"],
                              self.page["device_page"]["title"],
                              1, 1, 1, 10, 0.5)

            self.driver.close_app()  # 关闭App
            self.debug.warn("(%s)self.driver.close_app() App close" % self.basename)
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
                    self.wait_widget(self.page["login_page"]["title"], 3, 1)
                    self.logger.info(u"[APP_INF] APP当前页面为登录页面， 错误！")
                    raise NoSuchElementException()
                except TimeoutException:
                    pass
                except NoSuchElementException:
                    raise TimeoutException()

                try:
                    self.wait_widget(self.page["device_page"]["title"], 3, 1)
                    self.logger.info(u"[APP_INF] APP当前页面为主页面")
                    break
                except TimeoutException:
                    pass

            self.case_over(True)
        except TimeoutException:
            self.case_over(False)

    def output(self):
        self.run()
        return self.result()
