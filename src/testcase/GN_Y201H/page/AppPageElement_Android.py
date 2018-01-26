# coding=utf-8
import sys

if sys.version_info[:1] > (2,):  # python3
    xrange = range


class MainPageWidgetAndroid(object):
    # APP主页面
    def app_home_page(self):
        d = {}
        # 标题
        d["title"] = [u"//android.widget.TextView[@text='智家']", "xpath", u"App主页面"]
        # +号
        d["add_device"] = ["com.huawei.smarthome:id/myhome__tool_bar", "id", u"+号"]
        # 账户管理
        d["account_setting"] = [u"//android.widget.TextView[@text='我的']", "xpath", u"账户管理"]
        # 设备
        device = {}
        for i in xrange(20):
            device[i] = ("//android.support.v7.widget.RecyclerView/android.widget.FrameLayout[%s]//"
                         "android.widget.TextView" % (i + 1))
        d["device"] = [device, "xpath", u"待控设备"]
        return d

    # 添加设备页面
    def add_device_page(self):
        d = {}
        # 标题
        d["title"] = ["com.huawei.smarthome:id/hand_device_btn_come", "id", u"添加设备页面"]
        # 手动添加
        d["add_hand"] = ["com.huawei.smarthome:id/hand_device_btn_come", "id", u"手动添加"]
        # 正在添加
        d["loading"] = [u"//android.widget.TextView[@text='正在扫描…']", "xpath", u"正在添加"]
        # 重新扫描
        d["retry"] = ["com.huawei.smarthome:id/add_device_scan_btn", "id", u"重新扫描"]
        # 未发现设备
        d["no_device"] = [u"//android.widget.TextView[@text='未发现设备']", "xpath", u"未发现设备"]
        # 设备
        d["device"] = ["//android.widget.ListView//android.widget.TextView", "xpath", u"设备"]
        # 返回
        d["to_return"] = ["com.huawei.smarthome:id/common_title_back", "id", u"返回"]
        return d

    # 进入输入密码页面
    def input_wifi_password_page(self):
        d = {}
        # 标题
        d["title"] = [u"//android.widget.TextView[@text='认证']", "xpath", u"进入输入密码页面"]
        # WiFi名称
        d["wifi_name"] = ["com.huawei.smarthome:id/add_device_outh_wifi_name", "id", u"WiFi名称"]
        # 下一步
        d["next"] = ["com.jd.smart:id/tv_action", "id", u"确认wifi密码按钮"]
        # 记住密码
        d["remind_pwd"] = ["com.huawei.smarthome:id/remind_cb", "id", u"记住密码"]
        # wifi密码输入框
        d["password"] = ["com.huawei.smarthome:id/add_device_outh_password", "id", u"wifi密码输入框"]
        # 密码显示关闭
        d["check_box"] = ["com.huawei.smarthome:id/add_device_outh_password_switch_img", "id", u"密码显示关闭"]
        return d

    # 设备名称及位置
    def set_name_addr_page(self):
        d = {}
        # 标题
        d["title"] = [u"//android.widget.TextView[@text='设置设备名称及位置']", "xpath", u"设备名称及位置"]
        # 备注
        d["nickname"] = ["//android.widget.EditText", "xpath", u"备注"]
        # 摆放位置
        d["addr"] = ["//android.widget.ListView//android.widget.ImageView", "xpath", u"摆放位置客厅"]
        # 下一步
        d["next"] = ["com.huawei.smarthome:id/device_loc_next", "id", u"设备"]
        # 返回
        d["to_return"] = ["com.huawei.smarthome:id/common_ui_new_title_back", "id", u"返回"]
        return d

    # 设备控制页面
    def control_device_page(self):
        d = {}
        # 标题
        d["title"] = ["com.huawei.smarthome:id/device_control_btn_title", "id", u"设备控制页面"]
        # 设备信息进入按钮
        d["device_setting"] = ["com.huawei.smarthome:id/base_device_layout_title_setting", "id", u"设备信息进入按钮"]
        # 设备离线标志
        d["offline"] = [u"设备不在线", "name", u"设备离线标志"]
        # 电源开关
        d["power_button"] = ["com.huawei.smarthome:id/device_control_btn_title", "id", u"电源开关"]
        # 电源状态
        d["power_state"] = ["com.huawei.smarthome:id/device_control_socket_new_state", "id", u"电源状态"]
        # 电源开启
        d["power_on"] = [u"//android.widget.TextView[@text='电源已开启']", "xpath", u"电源开启"]
        # 电源关闭
        d["power_off"] = [u"//android.widget.TextView[@text='电源已关闭']", "xpath", u"电源关闭"]
        # 普通定时
        d["normal_timer"] = [u"//android.widget.TextView[@text='定时']", "xpath", u"普通定时"]
        # 延迟定时
        d["delay_timer"] = [u"//android.widget.TextView[@text='倒计时']", "xpath", u"延迟定时"]
        # 指示灯
        d["led"] = [u"//android.widget.TextView[@text='指示灯']", "xpath", u"指示灯"]
        # 返回
        d["to_return"] = ["com.huawei.smarthome:id/hw_otherdevice_title_back", "id", u"返回"]
        return d

    # 设备设置页面
    def device_setting_page(self):
        d = {}
        # 标题
        d["title"] = [u"//android.widget.TextView[@text='设置']", "xpath", u"设备设置页面"]
        # 删除设备按钮
        d["unbind"] = ["com.huawei.smarthome:id/hw_otherdevice_setting_delete_device", "id", u"删除设备按钮"]
        # 编辑设备备注
        d["nickname"] = ["com.huawei.smarthome:id/setting_item_value", "id", u"编辑设备备注"]
        # 设备信息
        d["device_info"] = [u"//android.widget.TextView[@text='设备信息']", "xpath", u"编辑设备备注"]
        # 返回按钮
        d["to_return"] = ["com.huawei.smarthome:id/common_ui_new_title_back", "id", u"返回"]
        return d

    # 设备信息页面
    def device_info_page(self):
        d = {}
        # 标题
        d["title"] = [u"//android.widget.TextView[@text='设备信息']", "xpath", u"设备信息页面"]
        # Mac地址
        d["mac"] = ["//android.widget.TextView[contains(@text, ':')]", "xpath", u"删除设备按钮"]
        # 序列号
        d["serial_number"] = ["//android.widget.RelativeLayout[4]//android.widget.TextView[2]", "xpath", u"序列号"]
        # 设备型号
        d["device_model"] = ["//android.widget.RelativeLayout[5]//android.widget.TextView[2]", "xpath", u"设备型号"]
        # 固件版本
        d["bin_ver"] = ["//android.widget.RelativeLayout[6]//android.widget.TextView[2]", "xpath", u"固件版本"]
        # 返回按钮
        d["to_return"] = ["com.huawei.smarthome:id/hw_other_device_detail_back", "id", u"返回"]
        return d

    # 普通定时页面
    def normal_timer_page(self):
        d = {}
        # 标题
        d["title"] = [u"//android.widget.TextView[@text='定时']", "xpath", u"普通定时页面"]
        # 添加定时
        d["add_timer"] = ["com.huawei.smarthome:id/device_time_add", "id", u"添加定时按钮"]
        # 编辑定时
        d["timer_edit"] = ["com.huawei.smarthome:id/time_normal_item_time", "id", u"编辑定时"]
        # 无定时
        d["no_timer"] = [u"//android.widget.TextView[@text='没有定时任务']", "xpath", u"无定时"]
        # 返回
        d["to_return"] = ["com.huawei.smarthome:id/device_time_back", "id", u"返回"]
        return d

    # 新建普通定时页面
    def add_normal_timer_page(self):
        d = {}
        # 标题
        d["title"] = [u"//android.widget.TextView[@text='新增定时']", "xpath", u"新建普通定时页面"]
        # 重复
        d["repeat"] = ["com.huawei.smarthome:id/setting_item_value", "id", u"重复"]
        # 定时开按钮
        d["button_on"] = ["com.huawei.smarthome:id/device_control_time_config_open_switch", "id", u"定时开按钮"]
        # 定时关按钮
        d["button_off"] = ["com.huawei.smarthome:id/device_control_time_config_close_switch", "id", u"定时关按钮"]
        # 开启时间
        d["time_on"] = ["//android.widget.RelativeLayout[3]//android.widget.TextView[2]", "xpath", u"开启时间"]
        # 关闭时间
        d["time_off"] = ["//android.widget.RelativeLayout[5]//android.widget.TextView[2]", "xpath", u"关闭时间"]
        # 取消按钮
        d["cancel"] = ["com.huawei.smarthome:id/device_time_config_cancle", "id", u"取消"]
        # 保存按钮
        d["saved"] = ["com.huawei.smarthome:id/device_time_config_ok", "id", u"保存按钮"]
        # 删除
        d["delete"] = [u"//android.widget.Button[@text='删除']", "xpath", u"删除"]
        return d


class PopupWidgetAndroid(object):
    # 页面广告
    def ad_popup(self):
        d = {}
        # 有广告
        d["title"] = ["com.huawei.smarthome:id/tv_inSkip", "id", u"有广告"]
        # 跳过
        d["skip"] = ["com.huawei.smarthome:id/tv_inSkip", "id", u"跳过"]
        # 稍后提醒
        d["cancel"] = [u"//android.widget.Button[@text='以后再说']", "xpath", u"稍后提醒"]
        return d

    # app升级确认弹窗
    def update_popup(self):
        d = {}
        # app升级确认弹窗
        d["title"] = [u"//android.widget.TextView[@text='发现新版本']", "xpath", u"有更新"]
        # 更新
        d["confirm"] = [u"//android.widget.Button[@text='立即更新']", "xpath", u"更新"]
        # 稍后提醒
        d["cancel"] = [u"//android.widget.Button[@text='以后再说']", "xpath", u"稍后提醒"]
        return d

    # 解绑设备
    def unbind_device_popup(self):
        d = {}
        # 删除设备弹窗
        d["title"] = [u"//android.widget.TextView[contains(@text, '此操作会清除手机')]", "xpath", u"删除设备弹窗"]
        # 确认
        d["confirm"] = ["com.huawei.smarthome:id/common_user_confirm_dialog_btn_comfirm", "id", u"确认"]
        # 取消
        d["cancel"] = ["com.huawei.smarthome:id/common_user_confirm_dialog_btn_cancle", "id", u"取消"]
        return d

    # 页面加载
    def loading_popup(self):
        d = {}
        # com.huawei.smarthome:id/load_dialog_msg 正在删除…
        # com.huawei.smarthome:id/load_dialog_msg 正在创建…
        # com.huawei.smarthome:id/title_loading 设备正在控制中...
        # com.huawei.smarthome:id/wating_dialog_msg 正在发送网络配置信息
        # com.huawei.smarthome:id/wating_dialog_msg 设备注册中
        # com.huawei.smarthome:id/wating_dialog_msg
        # com.huawei.smarthome:id/load_dialog_msg
        # 弹窗消息
        d["title"] = ["//android.widget.TextView[contains(@resource-id, 'dialog_msg')]", "xpath", u"弹窗消息"]
        # 设备正在控制中
        d["control"] = ["//android.widget.TextView[contains(@resource-id, 'title_loading')]", "xpath", u"设备正在控制中"]
        return d

    # 修改设备备注弹窗
    def change_nickname_popup(self):
        d = {}
        # 标题
        d["title"] = ["com.huawei.smarthome:id/common_ui_name_edittext", "id", u"修改设备备注弹窗"]
        # 备注输入框
        d["nickname"] = ["com.huawei.smarthome:id/common_ui_name_edittext", "id", u"备注输入框"]
        # 确认
        d["confirm"] = ["com.huawei.smarthome:id/common_user_confirm_dialog_btn_comfirm", "id", u"确认"]
        # 取消
        d["cancel"] = ["com.huawei.smarthome:id/common_user_confirm_dialog_btn_cancle", "id", u"取消"]
        return d

    # 定时重复页面
    def timer_repeat_popup(self):
        d = {}
        # 标题
        d["title"] = [u"//android.widget.TextView[@text='重复']", "xpath", u"定时重复页面"]
        # 执行一次
        d["once"] = [u"//android.widget.TextView[@text='执行一次']", "xpath", u"执行一次"]
        # 每天
        d["everyday"] = [u"//android.widget.TextView[@text='每天']", "xpath", u"每天"]
        # 工作日
        d["workday"] = [u"//android.widget.TextView[contains(@text, '工作日')]", "xpath", u"工作日"]
        # 周末
        d["weekend"] = [u"//android.widget.TextView[@text='周末']", "xpath", u"周末"]
        # 自定义
        d["define"] = [u"//android.widget.TextView[@text='自定义']", "xpath", u"自定义"]
        # 周一
        d["monday"] = [u"//android.widget.TextView[@text='周一']", "xpath", u"周一"]
        # 周二
        d["tuesday"] = [u"//android.widget.TextView[@text='周二']", "xpath", u"周二"]
        # 周三
        d["wednesday"] = [u"//android.widget.TextView[@text='周三']", "xpath", u"周三"]
        # 周四
        d["thursday"] = [u"//android.widget.TextView[@text='周四']", "xpath", u"周四"]
        # 周五
        d["friday"] = [u"//android.widget.TextView[@text='周五']", "xpath", u"周五"]
        # 周六
        d["saturday"] = [u"//android.widget.TextView[@text='周六']", "xpath", u"周六"]
        # 周日
        d["weekday"] = [u"//android.widget.TextView[@text='周日']", "xpath", u"周日"]
        # 完成
        d["confirm"] = ["com.huawei.smarthome:id/device_timer_custom_repeat_finish_btn", "id", u"完成"]
        # 取消
        d["cancel"] = ["com.huawei.smarthome:id/device_timer_config_repeat_default_canclebutton", "id", u"取消"]
        return d

    # 普通定时时间设置滚轮
    def normal_timer_roll_popup(self):
        d = {}
        # 标题
        d["title"] = [u"//android.widget.TextView[contains(@text, '时间')]", "xpath", u"设置时间"]
        # 时间滚轮,时
        d["roll_h"] = ["com.huawei.smarthome:id/device_hour_min_dialog_hour_wheel", "id",
                       u"时间滚轮,时", {"px": [0.5, 0.5]}]
        # 时间滚轮,分
        d["roll_m"] = ["com.huawei.smarthome:id/device_hour_min_dialog_minute_wheel", "id",
                       u"时间滚轮,分", {"px": [0.5, 0.5]}]
        # 确定
        d["confirm"] = ["com.huawei.smarthome:id/base_device_dialog_btn_ok", "id", u"确定"]
        # 取消
        d["cancel"] = ["com.huawei.smarthome:id/base_device_dialog_btn_cancle", "id", u"取消"]
        return d

    # 延时定时时间设置滚轮
    def delay_timer_roll_popup(self):
        d = {}
        # 标题
        d["title"] = [u"//android.widget.TextView[contains(@text, '倒计时')]", "xpath", u"设置时间"]
        # 时间滚轮,时
        d["roll_h"] = ["com.huawei.smarthome:id/device_control_delay_dialog_hour", "id",
                       u"时间滚轮,时", {"px": [0.5, 0.5]}]
        # 时间滚轮,分
        d["roll_m"] = ["com.huawei.smarthome:id/device_control_delay_dialog_min", "id",
                       u"时间滚轮,分", {"px": [0.5, 0.5]}]
        # 确定
        d["confirm"] = ["com.huawei.smarthome:id/device_control_delay_dialog_btn_horizontal_ok", "id", u"确定"]
        # 取消
        d["cancel"] = ["com.huawei.smarthome:id/device_control_delay_dialog_btn_horizontal_cancle", "id", u"取消"]
        # 关闭确定
        d["c_confirm"] = ["com.huawei.smarthome:id/device_control_delay_dialog_btn_vertical_ok", "id", u"关闭确定"]
        # 关闭取消
        d["c_cancel"] = ["com.huawei.smarthome:id/device_control_delay_dialog_btn_vertical_cancel", "id", u"关闭取消"]
        # 停止
        d["stop"] = ["com.huawei.smarthome:id/device_control_delay_dialog_btn_vertical_stop", "id", u"关闭停止"]
        return d
