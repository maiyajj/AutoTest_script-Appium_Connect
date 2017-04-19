# coding=utf-8
from src.testcase.case.LaunchApp import *
from src.testcase.case.ToLoginPage import *


class GNAppLogin5(object):
    def __init__(self):
        self.case_module = u"登录"  # 用例所属模块
        self.case_title = u'登录页面—成功登录后注销账号，再次进入登录页面查看'  # 用例名称
        self.ZenTao_id = 1900  # 禅道ID
        self.basename = os.path.basename(__file__).split(".")[0]  # 获取用例的文件名称:GNAPP_LOGIN_005
        logger.info('[GN_INF] <current case> [CASE_ID="%s", CASE_NAME="%s", 禅道ID="%s", CASE_MODULE="%s"]'
                    % (self.basename, self.case_title, self.ZenTao_id, self.case_module))  # 记录log
        try:
            self.driver = launch_app()  # 启动APP
            widget_check_unit = WidgetCheckUnit(self.driver)  # 元素初始化
            self.widget_click = widget_check_unit.widget_click  # 初始化self.widget_click
            self.wait_widget = widget_check_unit.wait_widget  # 初始化self.wait_widget
        except WebDriverException:
            self.case_over("unknown")
        self.start_time = time.strftime("%Y-%m-%d %H:%M:%S")
        logger.info('app start [time=%s]' % self.start_time)  # 记录log，APP打开时间
        self.success = 0
        ToLoginPage()  # 使APP跳转到登录页面等待
        self.case()

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
            data = conf_user_name.decode('hex')
            user_name.send_keys(data)
            logger.info(u'[APP_INPUT] ["用户名"] input success')
            time.sleep(0.5)

            login_pwd = self.widget_click(login_page["title"],
                                          login_page["password"],
                                          login_page["title"],
                                          1, 1, 1, 10, 0.5)

            self.driver.press_keycode(29, 28672)
            self.driver.press_keycode(112)
            data = conf_login_pwd.decode('hex')
            login_pwd.send_keys(data)
            logger.info(u'[APP_INPUT] ["密码"] input success')
            time.sleep(0.5)

            self.widget_click(login_page["title"],
                              login_page["login_button"],
                              device_page["title"],
                              1, 1, 1, 10, 0.5)

            self.widget_click(device_page["title"],
                              device_page["user_image"],
                              personal_settings_page["title"],
                              1, 1, 1, 10, 0.5, 0)

            self.widget_click(personal_settings_page["title"],
                              personal_settings_page["account_setting"],
                              account_setting_page["title"],
                              1, 1, 1, 10, 0.5, 0)

            self.widget_click(account_setting_page["title"],
                              account_setting_page["logout"],
                              logout_popup["title"],
                              1, 1, 1, 10, 0.5, 0)

            self.widget_click(logout_popup["title"],
                              logout_popup["confirm"],
                              login_page["activity"],
                              1, 1, 1, 10, 0.5, 0)

            self.driver.quit()  # 退出appium服务
            logger.info(u"[APP_INF] APP退出")
            time.sleep(1)

            try:
                self.driver = launch_app()  # 启动APP
                widget_check_unit = WidgetCheckUnit(self.driver)  # 元素初始化
                self.widget_click = widget_check_unit.widget_click  # 初始化self.widget_click
                self.wait_widget = widget_check_unit.wait_widget  # 初始化self.wait_widget
            except WebDriverException:
                self.case_over("unknown")

            logger.info(u"[APP_INF] APP重新启动")
            while True:
                if self.driver.current_activity == login_popup["activity"][0]:
                    try:
                        self.wait_widget(update_popup["title"], 3, 1)
                        logger.info(u"[APP_INF] APP有最新版本，可以更新")
                        self.widget_click(update_popup["title"],
                                          update_popup["cancel"],
                                          god_page["title"],
                                          1, 1, 1, 10, 0.5, 0)
                        logger.info(u"[APP_INF] 取消更新")
                    except TimeoutException:
                        pass
                    try:
                        self.wait_widget(login_popup["title"], 3, 1)
                        logger.info(u"[APP_INF] APP需要重新登陆，等待重新登录")
                        self.widget_click(login_popup["title"],
                                          login_popup["confirm"],
                                          login_page["title"],
                                          1, 1, 1, 10, 0.5, 0)
                    except TimeoutException:
                        pass

                if self.driver.current_activity == device_page["activity"][0]:
                    logger.info(u"[APP_INF] APP当前页面为主页面, 错误！")
                    raise TimeoutException()

                if self.driver.current_activity == login_page["activity"][0]:
                    logger.info(u"[APP_INF] APP当前页面为登录页面")
                    break

            user_name = self.widget_click(login_page["title"],
                                          login_page["username"],
                                          login_page["title"],
                                          1, 1, 1, 10, 0.5)

            # 29 is the keycode of 'a', 28672 is the keycode of META_CTRL_MASK
            self.driver.press_keycode(29, 28672)
            # KEYCODE_FORWARD_DEL 删除键 112
            self.driver.press_keycode(112)
            # 发送数据
            data = conf_user_name.decode('hex')
            user_name.send_keys(data)
            logger.info(u'[APP_INPUT] ["用户名"] input success')
            time.sleep(0.5)

            login_pwd = self.widget_click(login_page["title"],
                                          login_page["password"],
                                          login_page["title"],
                                          1, 1, 1, 10, 0.5)

            self.driver.press_keycode(29, 28672)
            self.driver.press_keycode(112)
            data = conf_login_pwd.decode('hex')
            login_pwd.send_keys(data)
            logger.info(u'[APP_INPUT] ["密码"] input success')
            time.sleep(0.5)

            self.widget_click(login_page["title"],
                              login_page["login_button"],
                              device_page["title"],
                              1, 1, 1, 10, 0.5)

            self.case_over(True)
        except TimeoutException:
            self.case_over(False)

    def case_over(self, success):
        self.success = success
        time.sleep(1)
        self.driver.close_app()  # 关闭APP
        self.driver.quit()  # 退出appium服务
        logger.info('app closed [time=%s]' % time.strftime("%Y-%m-%d %H:%M:%S"))

    def result(self):
        if self.success is True:
            logger.info('[GN_INF] <current case> [CASE_TITLE="%s"] success!' % self.case_title)  # 记录运行结果
            return "success", self.case_title, self.start_time
        elif self.success is False:
            logger.info('[GN_INF] <current case> [CASE_TITLE="%s"] failed!' % self.case_title)
            return "failed", self.case_title, self.start_time
        elif self.success == "unknown":
            logger.info('[GN_INF] <current case> [CASE_TITLE="%s"] unknown!' % self.case_title)
            return "unknown", self.case_title, self.start_time
