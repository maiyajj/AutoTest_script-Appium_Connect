# coding=utf-8
import logging
import sys
import time

sys.path.append("..")
from models.function import Report


class SmartLinkFunc(Report):
    def smart_link(self):
        while True:
            app_old_time = time.time()
            # 可批量依次添加设备
            if self.mac_choose_flag == 1:
                self.mac_choose_flag = 0
            else:
                self.mac_choose_flag = 1
            logging.info("Mac地址选择标志位为：%s" % self.mac_choose_flag)
            self.program_loop_time += 1
            logging.info(u"正在一键配网第%s次" % self.program_loop_time)
            try:
                # 打开APP
                self.init_open_app()
                # 检测+号
                self.widget_add_device_button()
                self.widget_choose_add_device_mode("HISTORY")
                if self.test_tempo_flag == "SORT":
                    pass
                if self.test_tempo_flag == "HISTORY":
                    # 检测添加历史
                    self.widget_add_history_button()
                    # 检测插座型号
                    self.widget_add_history_list()
                    # 检测输入密码页面
                    self.widget_add_specification()
                    # self.widget_input_password_text()
                    self.widget_input_password_conform()
                    func_old_time = time.time()
                    # 检测搜索设备
                    self.widget_search_device_loading()
                    if self.test_tempo_flag == "SEARCH_DEVICE_SUCCESS":
                        # 搜索设备成功，检测设备状态
                        self.widget_search_device_success()
                        if self.test_tempo_flag == "BIND_DEVICE_SUCCESS":
                            # 检查设备是否离线
                            # self.check_offline()
                            # 控制电源按钮
                            # self.widget_control_power()
                            # 设备详情页面
                            self.widget_device_info()
                            # 检测检测设备是否删除成功
                            self.widget_unbind_device()
                        if self.test_tempo_flag == "BIND_DEVICE_FAIL":
                            # 绑定设备失败
                            self.widget_bind_device_fail()
                    if self.test_tempo_flag == "SEARCH_DEVICE_FAIL":
                        # 搜索设备超时
                        self.widget_search_device_fail()
                    app_new_time = time.time()
                    func_new_time = time.time()
                    logging.info(u"函数共运行%sS" % (func_new_time - func_old_time))
                    logging.info(u"主程序共运行%sS" % (app_new_time - app_old_time))
                    self.report()
            except:
                self.report()

                # 变更语句：37,47,49，选择设备为2011加强版
