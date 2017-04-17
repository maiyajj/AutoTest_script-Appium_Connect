# coding=utf-8
# 由Conf.py生成
import sys

import yaml

reload(sys)
sys.setdefaultencoding('utf-8')

conf = yaml.load(file(r'config/Conf.yaml'))
# 打开APP超时时间
conf_open_app_timeout = conf["open_app_timeout"]
# 搜索设备超时时间
conf_search_device_timeout = conf["search_device_timeout"]
# 操作响应超时时间
conf_request_timeout = conf["request_timeout"]
# 离线恢复超时时间
conf_offline_recovery_timeout = conf["offline_recovery_timeout"]
# 程序操作等待时间
conf_operate_wait_time = conf["operate_wait_time"]
# 待添加的设备Mac
conf_MAC = conf["MAC"]
# Mac地址列表选取标志位
conf_mac_choose_flag = conf["mac_choose_flag"]
# 用户名
conf_user_name = conf["user_name"]
# 登录密码
conf_login_pwd = conf["login_pwd"]
# 旧密码
conf_old_pwd = conf["old_pwd"]
# 新密码
conf_new_pwd = conf["new_pwd"]
# 错误密码
conf_err_pwd = conf["err_pwd"]
# WiFi密码
conf_wifi_pwd = conf["wifi_pwd"]
# 待启动APP
conf_App = conf["App"]
# 提示消息
conf_Toast = conf["Toast"]
