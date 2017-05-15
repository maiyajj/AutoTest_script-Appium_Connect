# coding=utf-8
from src.testcase.case.LaunchApp import *
from src.utils.ScreenShot import *


class GNAppDevicePage1(LaunchApp):
    def run(self):
        self.case_module = u"设备页"  # 用例所属模块
        self.case_title = u'默认页面信息检查'  # 用例名称
        self.zentao_id = 1773  # 禅道ID
        self.basename = os.path.basename(__file__).split(".")[0]  # 获取用例的文件名称:GNAPP_DEVICE_PAGE_001
        self.driver = self.return_driver()
        self.logger.info('[GN_INF] <current case> [CASE_ID="%s", CASE_NAME="%s", 禅道ID="%s", CASE_MODULE="%s"]'
                         % (self.basename, self.case_title, self.zentao_id, self.case_module))  # 记录log

        try:
            self.launch_app(False)  # 启动APP
            self.case()
        except WebDriverException:
            self.debug.error(traceback.format_exc())  # Message: ***

    # 用例动作
    def case(self):
        try:
            self.wait_widget(device_page["user_image"], 3, 1)

            now_time = self.wait_widget(device_page["welcome"], 3, 1).get_attribute("name")
            if 0 < int(time.strftime("%H")) < 12:
                if now_time != u"上午好":
                    raise TimeoutException()
            else:
                if now_time != u"下午好":
                    raise TimeoutException()

            if self.wait_widget(device_page["welcome"], 3, 1).get_attribute("name") != u"上海市":
                raise TimeoutException()

            self.wait_widget(device_page["weather"], 3, 1)

            self.case_over(True)
        except TimeoutException:
            self.case_over(False)

    def output(self):
        self.run()
        return self.result()
