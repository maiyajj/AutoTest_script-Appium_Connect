# coding:utf-8
import sys

import yaml

reload(sys)
sys.setdefaultencoding('utf-8')

conf = yaml.load(file(r"../config/Conf.yaml"))
request_timeout = conf["request_timeout"]
operate_wait_time = conf["operate_wait_time"]
MAC = conf["MAC"]
offline_recovery_timeout = conf["offline_recovery_timeout"]
open_app_timeout = conf["open_app_timeout"]
search_device_timeout = conf["search_device_timeout"]
mac_choose_flag = conf["mac_choose_flag"]
App = conf["App"]
