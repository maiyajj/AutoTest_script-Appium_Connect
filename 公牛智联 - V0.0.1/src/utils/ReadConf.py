# coding=utf-8
# 由Conf.py生成
import sys

import yaml

reload(sys)
sys.setdefaultencoding('utf-8')

conf = yaml.load(file(r"config/Conf.yaml"))


def modified_conf(config):
    with open(r"config/Conf.yaml", "w") as conf_yaml:
        conf_yaml.write("# 打开APP超时时间\n")
        conf_yaml.write("open_app_timeout: %s\n" % config["search_device_timeout"])
        conf_yaml.write("# 搜索设备超时时间\n")
        conf_yaml.write("search_device_timeout: %s\n" % config["search_device_timeout"])
        conf_yaml.write("# 操作响应超时时间\n")
        conf_yaml.write("request_timeout: %s\n" % config["request_timeout"])
        conf_yaml.write("# 离线恢复超时时间\n")
        conf_yaml.write("offline_recovery_timeout: %s\n" % config["offline_recovery_timeout"])
        conf_yaml.write("# 程序操作等待时间\n")
        conf_yaml.write("operate_wait_time: %s\n" % config["operate_wait_time"])
        conf_yaml.write("# 待添加的设备Mac\n")
        conf_yaml.write("MAC: %s\n" % config["MAC"])
        conf_yaml.write("# Mac地址列表选取标志位\n")
        conf_yaml.write("mac_choose_flag: %s\n" % config["mac_choose_flag"])
        conf_yaml.write("# 错误密码\n")
        conf_yaml.write("err_pwd: %s\n" % config["err_pwd"])
        conf_yaml.write("# wifi密码\n")
        conf_yaml.write("wifi_pwd: %s\n" % config["wifi_pwd"])
        conf_yaml.write("# 待选择App\n")
        conf_yaml.write("App:\n")
        conf_yaml.write("  GN: [com.iotbull.android.superapp,"
                        " com.iotbull.android.superapp.activitys.regist_login.SplashActivity]\n")
        conf_yaml.write("  JD: [com.jd.smart, com.jd.smart.activity.LoadingActivity]\n")
        conf_yaml.write("# Toast消息\n")
        conf_yaml.write("Toast:\n")
        conf_yaml.write("  login_password_mistake: [40, 1570, 1040, 1750\n")
        conf_yaml.write("user_and_pwd:  # 用户名，（登录密码/旧密码）， 新密码\n")
        user = config["user_and_pwd"]
        conf_yaml.write("  name01: [%s, %s, %s]\n" % (user["name01"][0], user["name01"][2], user["name01"][1]))
        conf_yaml.write("  name02: [%s, %s, %s]\n" % (user["name02"][0], user["name02"][2], user["name02"][1]))
        conf_yaml.write("  name03: [%s, %s, %s]\n" % (user["name03"][0], user["name03"][2], user["name03"][1]))
        conf_yaml.write("  name04: [%s, %s, %s]\n" % (user["name04"][0], user["name04"][2], user["name04"][1]))
        conf_yaml.write("  name05: [%s, %s, %s]\n" % (user["name05"][0], user["name05"][2], user["name05"][1]))
        conf_yaml.write("  name06: [%s, %s, %s]\n" % (user["name06"][0], user["name06"][2], user["name06"][1]))
        conf_yaml.write("  name07: [%s, %s, %s]\n" % (user["name07"][0], user["name07"][2], user["name07"][1]))
        conf_yaml.write("  name08: [%s, %s, %s]\n" % (user["name08"][0], user["name08"][2], user["name08"][1]))
        conf_yaml.write("  name09: [%s, %s, %s]\n" % (user["name09"][0], user["name09"][2], user["name09"][1]))
        conf_yaml.write("  name10: [%s, %s, %s]\n" % (user["name10"][0], user["name10"][2], user["name10"][1]))
