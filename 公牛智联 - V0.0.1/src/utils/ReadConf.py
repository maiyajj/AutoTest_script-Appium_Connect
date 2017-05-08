# coding=utf-8
# 由Conf.py生成
import sys

import yaml

reload(sys)
sys.setdefaultencoding('utf-8')

conf = yaml.load(file(r"config/Conf.yaml"))


def modified_conf(conf):
    with open(r"config/1Conf.yaml", "w") as conf_yaml:
        conf_yaml.write("# 打开APP超时时间\n")
        conf_yaml.write("open_app_timeout: %s\n" % conf["search_device_timeout"])
        conf_yaml.write("# 搜索设备超时时间\n")
        conf_yaml.write("search_device_timeout: %s\n" % conf["search_device_timeout"])
        conf_yaml.write("# 操作响应超时时间\n")
        conf_yaml.write("request_timeout: %s\n" % conf["request_timeout"])
        conf_yaml.write("# 离线恢复超时时间\n")
        conf_yaml.write("offline_recovery_timeout: %s\n" % conf["offline_recovery_timeout"])
        conf_yaml.write("# 程序操作等待时间\n")
        conf_yaml.write("operate_wait_time: %s\n" % conf["operate_wait_time"])
        conf_yaml.write("# 待添加的设备Mac\n")
        conf_yaml.write("MAC: %s\n" % conf["MAC"])
        conf_yaml.write("# Mac地址列表选取标志位\n")
        conf_yaml.write("mac_choose_flag: %s\n" % conf["mac_choose_flag"])
        conf_yaml.write("# 错误密码\n")
        conf_yaml.write("err_pwd: %s\n" % conf["err_pwd"])
        conf_yaml.write("# wifi密码\n")
        conf_yaml.write("wifi_pwd: %s\n" % conf["wifi_pwd"])
        conf_yaml.write("# 待选择App\n")
        conf_yaml.write("App:\n")
        conf_yaml.write("  GN: [com.iotbull.android.superapp,"
                        " com.iotbull.android.superapp.activitys.regist_login.SplashActivity]\n")
        conf_yaml.write("  JD: [com.jd.smart, com.jd.smart.activity.LoadingActivity]\n")
        conf_yaml.write("# Toast消息\n")
        conf_yaml.write("Toast:\n")
        conf_yaml.write("  login_password_mistake: [40, 1570, 1040, 1750\n")
        conf_yaml.write("user_and_pwd:  # 用户名，（登录密码/旧密码）， 新密码\n")
        conf_yaml.write("  name01: ['31373020303030302030303031', '3132333435363738', '3837363534333231']\n")
        conf_yaml.write("  name02: ['31373020303030302030303032', '3132333435363738', '3837363534333231']\n")
        conf_yaml.write("  name03: ['31373020303030302030303033', '3132333435363738', '3837363534333231']\n")
        conf_yaml.write("  name04: ['31373020303030302030303034', '3132333435363738', '3837363534333231']\n")
        conf_yaml.write("  name05: ['31373020303030302030303035', '3132333435363738', '3837363534333231']\n")
        conf_yaml.write("  name06: ['31373020303030302030303036', '3132333435363738', '3837363534333231']\n")
        conf_yaml.write("  name07: ['31373020303030302030303037', '3132333435363738', '3837363534333231']\n")
        conf_yaml.write("  name08: ['31373020303030302030303038', '3132333435363738', '3837363534333231']\n")
        conf_yaml.write("  name09: ['31373020303030302030303039', '3132333435363738', '3837363534333231']\n")
        conf_yaml.write("  name10: ['31373020303030302030303130', '3132333435363738', '3837363534333231']\n")
