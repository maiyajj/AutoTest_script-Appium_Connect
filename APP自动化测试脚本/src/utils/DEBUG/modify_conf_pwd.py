# coding=utf-8
# 由Conf.py生成
import sys

import yaml

reload(sys)
sys.setdefaultencoding('utf-8')

conf_path = r"../../../config/Conf.yaml"
pwd_path = r"../../../config/pwd.yaml"
conf = dict(yaml.load(file(conf_path)), **yaml.load(file(pwd_path)))


# for i in conf["user_and_pwd"].keys():
#     conf["user_and_pwd"][i]["GN_F1331"] = {'precise_pwd': ['', ''], 'new_pwd': '', 'login_pwd': '', 'user_name': ''}

def modified_conf():
    with open(conf_path, "w") as conf_yaml:
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

        conf_yaml.write("# 滚轮滑动等待时间\n")
        conf_yaml.write("roll_time:\n")
        for k, v in conf["roll_time"].items():
            conf_yaml.write("    %s: '%s'\n" % (k, v))

        conf_yaml.write("# 待添加的设备Mac\n")
        conf_yaml.write("MAC:\n")
        for k, v in conf["MAC"].items():
            conf_yaml.write("  %s:\n" % k)
            for v1, v2 in v.items():
                conf_yaml.write("    '%s': '%s'\n" % (v1, v2))

        conf_yaml.write("# 电量计量设备备注名\n")
        conf_yaml.write("Elec_stat_mac: %s\n" % conf["Elec_stat_mac"])

        conf_yaml.write("# 错误密码\n")
        conf_yaml.write("err_pwd: '%s'\n" % conf["err_pwd"])

        conf_yaml.write("# wifi密码\n")
        conf_yaml.write("wifi_pwd: '%s'\n" % conf["wifi_pwd"])

        conf_yaml.write("# 待选择App\n")
        conf_yaml.write("App:\n")
        for k, v in conf["App"].items():
            conf_yaml.write("  %s:\n" % k)
            for v1, v2 in v.items():
                conf_yaml.write("    %s: '%s'\n" % (v1, v2))

        conf_yaml.write("# Toast消息\n")
        conf_yaml.write("Toast:\n")
        conf_yaml.write("  login_password_mistake: [40, 1570, 1040, 1750]\n")

        conf_yaml.write("# 待测APP名称和设备名称\n")
        conf_yaml.write("app_device_name:\n")
        for k, v in conf["app_device_name"].items():
            conf_yaml.write("  %s:\n" % k)
            for v1, v2 in v.items():
                conf_yaml.write("    %s: '%s'\n" % (v1, v2))

        conf_yaml.write("# 手机型号及待运行APP\n")
        conf_yaml.write("phone_name:\n")
        for k, v in conf["phone_name"].items():
            conf_yaml.write("  %s:\n" % k)
            for v1, v2 in v.items():
                conf_yaml.write("    %s: '%s'\n" % (v1, v2))


def modified_pwd():
    with open(pwd_path, "w") as conf_yaml:
        conf_yaml.write("# 邮箱用户名密码\n")
        conf_yaml.write("mail_pwd:\n")
        for k, v in conf["mail_pwd"].items():
            try:
                int(k)
                conf_yaml.write("  '%s':\n" % k)
            except BaseException:
                conf_yaml.write("  %s:\n" % k)
            for v1, v2 in v.items():
                conf_yaml.write("    %s: '%s'\n" % (v1, v2))

        conf_yaml.write("# 用户名，（登录密码/旧密码）， 新密码\n")
        conf_yaml.write("user_and_pwd:\n")
        for k, v in conf["user_and_pwd"].items():
            conf_yaml.write("  %s:\n" % k)
            for v1, v2 in v.items():
                conf_yaml.write("    %s:\n" % v1)
                for v3, v4 in v2.items():
                    if "precise_pwd" in v3:
                        conf_yaml.write('      %s: %s\n' % (v3, v4))
                    else:
                        conf_yaml.write("      %s: '%s'\n" % (v3, v4))


modified_conf()
modified_pwd()
