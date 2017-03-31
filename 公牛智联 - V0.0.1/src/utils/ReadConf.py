# coding:utf-8
import sys

import yaml

reload(sys)
sys.setdefaultencoding('utf-8')

conf = yaml.load(file(r"../config/Conf.yaml"))
conf_request_timeout = conf["request_timeout"]
conf_operate_wait_time = conf["operate_wait_time"]
conf_MAC = conf["MAC"]
conf_offline_recovery_timeout = conf["offline_recovery_timeout"]
conf_open_app_timeout = conf["open_app_timeout"]
conf_search_device_timeout = conf["search_device_timeout"]
conf_mac_choose_flag = conf["mac_choose_flag"]
conf_user_name = conf["user_name"]
# 登录密码
conf_login_pwd = conf["login_pwd"]
# 旧密码
conf_old_pwd = conf["old_pwd"]
# 新密码
conf_new_pwd = conf["new_pwd"]
conf_App = conf["App"]