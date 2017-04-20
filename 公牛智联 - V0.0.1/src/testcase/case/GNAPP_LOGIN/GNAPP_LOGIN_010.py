# coding=utf-8
from src.testcase.case.LaunchApp import *
from src.testcase.case.ToLoginPage import *


class GNAppLogin10(object):
    def __init__(self):
        self.case_module = u"登录"  # 用例所属模块
        self.case_title = u'登录页面—位数错误的数字账号，登录提示信息检查'  # 用例名称
        self.ZenTao_id = 1895  # 禅道ID
        self.basename = os.path.basename(__file__).split(".")[0]  # 获取用例的文件名称:GNAPP_LOGIN_010
        logger.info('[GN_INF] <current case> [CASE_ID="%s", CASE_NAME="%s", 禅道ID="%s", CASE_MODULE="%s"]'
                    % (self.basename, self.case_title, self.ZenTao_id, self.case_module))  # 记录log
        try:
            self.driver = launch_app()  # 启动APP
            widget_check_unit = WidgetCheckUnit(self.driver)  # 元素初始化
            self.widget_click = widget_check_unit.widget_click  # 初始化self.widget_click
            self.wait_widget = widget_check_unit.wait_widget  # 初始化self.wait_widget
            self.start_time = time.strftime("%Y-%m-%d %H:%M:%S")
            logger.info('app start [time=%s]' % self.start_time)  # 记录log，APP打开时间
            self.success = 0
            ToLoginPage()  # 使APP跳转到登录页面等待
            self.case()
        except WebDriverException:
            self.case_over("unknown")

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
            data = "1"
            user_name.send_keys(data)
            logger.info(u'[APP_INPUT] ["位数错误用户名"] input success')
            time.sleep(0.5)

            login_pwd = self.widget_click(login_page["title"],
                                          login_page["password"],
                                          login_page["title"],
                                          1, 1, 1, 10, 0.5)

            self.driver.press_keycode(29, 28672)
            self.driver.press_keycode(112)
            data = conf_login_pwd.decode('hex')
            login_pwd.send_keys(data)
            logger.info(u'[APP_INPUT] ["登录密码"] input success')
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

            # 截屏
            screen_shot_name = r"./screenshots/%s - %s - %s - [%s]-[%s].png" \
                               % (database["program_loop_time"], database["case_location"],
                                  self.ZenTao_id, self.basename, time.strftime("%Y-%m-%d %H_%M_%S"))
            database["screen_name"] = screen_shot_name

            width = self.driver.get_window_size()['width']
            height = self.driver.get_window_size()['height']
            self.width = int(width * 0.5)
            self.height = int(height * 0.66)

            self.driver.tap([(self.width, self.height)], )
            self.driver.tap([(self.width, self.height)], )
            self.driver.tap([(self.width, self.height)], )

            self.driver.save_screenshot(screen_shot_name)
            logger.info(u'[APP_OPERATE] ["屏幕截图"] screen shot success')

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
