# coding=utf-8
from src.testcase.case.LaunchApp import *
from src.testcase.case.ToLoginPage import *


class GNAppRegister5(object):
    def __init__(self):
        self.case_module = u"注册"  # 用例所属模块
        self.case_title = u'注册页面-正确的用户名和密码，小于6位数字验证码，注册验证'  # 用例名称
        self.ZenTao_id = 1882  # 禅道ID
        self.basename = os.path.basename(__file__).split(".")[0]  # 获取用例的文件名称:GNAPP_REGISTER_005
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
            data = conf_user_name.decode('hex')
            user_name.send_keys(data)
            logger.info(u'[APP_INPUT] ["用户名"] input success')
            time.sleep(0.5)

            pwd = self.widget_click(register_page["title"],
                                    register_page["password"],
                                    register_page["title"],
                                    1, 1, 1, 10, 0.5)

            self.driver.press_keycode(29, 28672)
            self.driver.press_keycode(112)
            data = "123456"
            pwd.send_keys(data)
            logger.info(u'[APP_INPUT] ["注册密码"] input success')
            time.sleep(0.5)

            check_code = self.widget_click(register_page["title"],
                                           register_page["check_code"],
                                           register_page["title"],
                                           1, 1, 1, 10, 0.5)

            self.driver.press_keycode(29, 28672)
            self.driver.press_keycode(112)
            data = "1234"
            check_code.send_keys(data)
            logger.info(u'[APP_INPUT] ["注册验证码"] input success')
            time.sleep(0.5)

            self.widget_click(register_page["title"],
                              register_page["register_button"],
                              register_page["title"],
                              1, 1, 1, 10, 0.5)

            # 截屏
            screen_shot_name = r"./screenshots/%s - %s - %s - [%s]-[%s].png" \
                               % (database["program_loop_time"], database["case_location"],
                                  self.ZenTao_id, self.basename, time.strftime("%Y-%m-%d %H_%M_%S"))
            database["screen_name"] = screen_shot_name

            width = self.driver.get_window_size()['width']
            height = self.driver.get_window_size()['height']
            self.width = int(width * 0.5)
            self.height = int(height * 0.75)

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
