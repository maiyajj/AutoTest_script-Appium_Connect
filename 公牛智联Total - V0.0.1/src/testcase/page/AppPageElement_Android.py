# coding=utf-8
class MainPageWidgetAndroid(object):
    # 万能页面
    def god_page(self):
        d = {}
        d["title"] = ["android.widget.FrameLayout", "class", u"万能控件",
                      {"px": {"width": 0, "height": 0}}]
        return d

    # 引导页
    def view_pager_page(self):
        d = {}
        # 标题
        d["title"] = ["com.iotbull.android.superapp:id/indicator", "id", u"引导页"]
        return d

    # 登录页
    def login_page(self):
        d = {}
        # 标题
        d["title"] = ["com.iotbull.android.superapp:id/login_btn_commit", "id", u"登录页"]
        # 页面activity
        d["activity"] = [".activitys.regist_login.LoginActivity", "activity", u"页面activity"]
        # 用户名输入框
        d["username"] = ["com.iotbull.android.superapp:id/login_et_username", "id", u"用户名输入框"]
        # 密码输入框
        d["password"] = ["com.iotbull.android.superapp:id/login_et_password", "id", u"密码输入框"]
        # 显示密码
        d["check_box"] = ["com.iotbull.android.superapp:id/login_cb_show_password", "id", u"密码可见/不可见"]
        # 忘记密码
        d["to_find_password"] = ["com.iotbull.android.superapp:id/login_tv_go_find_password", "id", u"忘记密码"]
        # 登录按钮
        d["login_button"] = ["com.iotbull.android.superapp:id/login_btn_commit", "id", u"登录按钮",
                             {"px": {"width": 0.5, "height": 0.65}}]
        # 新账号注册
        d["to_register"] = ["com.iotbull.android.superapp:id/login_tv_go_regist", "id", u"新账号注册"]
        return d

    # 忘记密码页
    def find_password_page(self):
        d = {}
        # 标题
        d["title"] = ["com.iotbull.android.superapp:id/forget_password_commit_button", "id", u"忘记密码页"]
        # 页面activity
        d["activity"] = [".activitys.regist_login.ForgetPasswordActivity", "activity", u"页面activity"]
        # 返回
        d["to_return"] = ["android.widget.ImageButton", "class", u"返回"]
        # 手机号
        d["user_name"] = ["com.iotbull.android.superapp:id/forget_password_user_name_edit_text", "id", u"手机号"]
        # 验证码
        d["check_code"] = ["com.iotbull.android.superapp:id/forget_password_check_code_edit_text", "id", u"验证码"]
        # 获取验证码
        d["get_check_code"] = ["com.iotbull.android.superapp:id/forget_password_get_check_code_text_view", "id",
                               u"获取验证码"]
        # 下一步
        d["to_next"] = ["com.iotbull.android.superapp:id/forget_password_commit_button", "id", u"下一步",
                        {"px": {"width": 0.5, "height": 0.45}}]
        return d

    # 忘记密码→重置密码页
    def new_password_page(self):
        d = {}
        # 标题
        d["title"] = ["com.iotbull.android.superapp:id/forget_password_new_password_commit_button", "id", u"忘记密码→重置密码页"]
        # 页面activity
        d["activity"] = [".activitys.regist_login.ForgetPasswordActivity", "activity", u"页面activity"]
        # 返回
        d["to_return"] = ["android.widget.ImageButton", "class", u"返回"]
        # 新密码
        d["new_pwd"] = ["com.iotbull.android.superapp:id/forget_password_new_password_password_edit_text", "id", u"新密码"]
        # 确认新密码
        d["conform_pwd"] = ["com.iotbull.android.superapp:id/forget_password_new_password_commit_password_edit_text",
                            "id", u"确认新密码"]
        # 完成
        d["commit"] = ["com.iotbull.android.superapp:id/forget_password_new_password_commit_button", "id", u"完成"]
        return d

    # 注册页
    def register_page(self):
        d = {}
        # 标题
        d["title"] = ["com.iotbull.android.superapp:id/regist_commit_button", "id", u"注册页"]
        # 页面activity
        d["activity"] = [".activitys.regist_login.RegistActivity", "activity", u"页面activity"]
        # 用户名
        d["username"] = ["com.iotbull.android.superapp:id/regist_et_username", "id", u"用户名"]
        # 密码
        d["password"] = ["com.iotbull.android.superapp:id/regist_et_password", "id", u"密码"]
        # 验证码
        d["check_code"] = ["com.iotbull.android.superapp:id/regist_et_check_code", "id", u"验证码"]
        # 获取验证码
        d["get_check_code"] = ["com.iotbull.android.superapp:id/regist_tv_get_check_code", "id", u"获取验证码"]
        # 立即注册按钮
        d["register_button"] = ["com.iotbull.android.superapp:id/regist_commit_button", "id", u"立即注册按钮",
                                {"px": {"width": 0.5, "height": 0.75}}]
        # 公牛服务协议
        d["to_protocol"] = ["com.iotbull.android.superapp:id/regist_tv_go_regist_protocol", "id", u"公牛服务协议"]
        # 已有账户登录
        d["to_login"] = ["com.iotbull.android.superapp:id/regist_tv_go_login", "id", u"已有账户登录"]
        # 密码可见/不可见
        d["check_box"] = ["com.iotbull.android.superapp:id/regist_cb_show_password", "id", u"密码可见/不可见"]
        return d

    # 用户使用协议页
    def protocol_page(self):
        d = {}
        # 标题
        d["title"] = ["com.iotbull.android.superapp:id/activity_regist_protocol", "id", u"用户使用协议页"]
        # 页面activity
        d["activity"] = [".activitys.regist_login.RegistProtocolActivity", "activity", u"页面activity"]
        # 返回
        d["to_return"] = ["android.widget.ImageButton", "class", u"返回"]
        return d

    # 设备控制页
    def device_control_page(self):
        d = {}
        pass
        return d

    # 个人设置页
    def personal_settings_page(self):
        d = {}
        # 标题
        d["title"] = ["com.iotbull.android.superapp:id/rv_item_main_setting_menu_text_view", "id", u"个人设置页"]
        # 页面activity
        d["activity"] = [".activitys.main_setting.HomeActivity", "activity", u"页面activity"]
        # 头像
        d["head_image"] = ["com.iotbull.android.superapp:id/home_setting_head_image_view", "id", u"头像"]
        # 昵称
        d["nickname"] = ["com.iotbull.android.superapp:id/menu_setting_nickname_text_view", "id", u"昵称"]
        # 账号
        d["id"] = ["com.iotbull.android.superapp:id/menu_setting_phone_text_view", "id", u"账号"]
        # 账户设置
        d["account_setting"] = ["//android.widget.LinearLayout/android.support.v7.widget.RecyclerView"
                                "/android.widget.LinearLayout", "xpath", u"账户设置"]
        # 微信链接
        d["using_help"] = ["//android.widget.LinearLayout/android.support.v7.widget.RecyclerView"
                           "/android.widget.LinearLayout[2]", "xpath", u"微信链接"]
        # 使用帮助
        d["using_help"] = ["//android.widget.LinearLayout/android.support.v7.widget.RecyclerView"
                           "/android.widget.LinearLayout[3]", "xpath", u"使用帮助"]
        # 意见反馈
        d["feedback"] = ["//android.widget.LinearLayout/android.support.v7.widget.RecyclerView"
                         "/android.widget.LinearLayout[4]", "xpath", u"意见反馈"]
        # 主题风格
        d["theme_style"] = ["//android.widget.LinearLayout/android.support.v7.widget.RecyclerView"
                            "/android.widget.LinearLayout[5]", "xpath", u"主题风格"]
        # 版本信息
        d["version_info"] = ["//android.widget.LinearLayout/android.support.v7.widget.RecyclerView"
                             "/android.widget.LinearLayout[6]", "xpath", u"版本信息"]
        # 关于我们
        d["about_us"] = ["//android.widget.LinearLayout/android.support.v7.widget.RecyclerView"
                         "/android.widget.LinearLayout[7]", "xpath", u"关于我们"]
        return d

    # 账户设置页
    def account_setting_page(self):
        d = {}
        # 标题
        d["title"] = ["com.iotbull.android.superapp:id/user_info_iv_bg", "id", u"账户设置页"]
        # 页面activity
        d["activity"] = [".activitys.main_setting.userinfo_setting.UserInfoSettingActivity", "activity", u"页面activity"]
        # 返回
        d["to_return"] = ["android.widget.ImageButton", "class", u"返回"]
        # 昵称
        d["nickname"] = ["//android.support.v7.widget.RecyclerView/android.widget.LinearLayout[1]"
                         "/android.widget.LinearLayout/android.widget.TextView", "xpath", u"昵称"]
        # 性别
        d["gender"] = ["//android.support.v7.widget.RecyclerView/android.widget.LinearLayout[2]"
                       "/android.widget.LinearLayout/android.widget.TextView", "xpath", u"性别"]
        # 地址
        d["address"] = ["//android.support.v7.widget.RecyclerView/android.widget.LinearLayout[3]"
                        "/android.widget.LinearLayout/android.widget.TextView", "xpath", u"地址"]
        # 生日
        d["birthday"] = ["//android.support.v7.widget.RecyclerView/android.widget.LinearLayout[4]"
                         "/android.widget.LinearLayout/android.widget.TextView", "xpath", u"生日"]
        # 修改密码
        d["change_pwd"] = ["//android.support.v7.widget.RecyclerView/android.widget.LinearLayout[5]"
                           "/android.widget.LinearLayout/android.widget.TextView", "xpath", u"修改密码"]
        # 退出登录
        d["logout"] = ["com.iotbull.android.superapp:id/user_info_btn_logout", "id", u"退出登录"]
        return d

    # 修改昵称页
    def change_nickname_page(self):
        d = {}
        # 标题
        d["title"] = ["com.iotbull.android.superapp:id/user_name_update_commit_button", "id", u"修改昵称页"]
        # 页面activity
        d["activity"] = [".activitys.main_setting.userinfo_setting.UserNameUpdateActivity", "activity", u"页面activity"]
        # 返回
        d["to_return"] = ["android.widget.ImageButton", "class", u"返回"]
        # 输入框
        d["nickname"] = ["com.iotbull.android.superapp:id/user_name_update_nickname_edit_text", "id", u"输入框"]
        # 完成
        d["commit"] = ["com.iotbull.android.superapp:id/user_name_update_commit_button", "id", u"完成"]
        return d

    # uiautomatorviewer没办法读取滚轮数值，暂不使用
    def gender_page(self):
        d = {}
        # 选择性别
        d["choose_gender"] = [u"选择性别", "name", u"选择性别"]
        # 取消
        d["cancel"] = [u"取消", "name", u"取消"]
        # 确定
        d["submit"] = [u"确定", "name", u"确定"]
        return d

    # 修改密码页
    def change_pwd_page(self):
        d = {}
        # 标题
        d["title"] = ["com.iotbull.android.superapp:id/user_password_update_commit_button", "id", u"修改密码页"]
        # 页面activity
        d["activity"] = [".activitys.main_setting.password_update.UserPasswordUpdateActivity", "activity",
                         u"页面activity"]
        # 返回
        d["to_return"] = ["android.widget.ImageButton", "class", u"返回"]
        # 旧密码
        d["old_pwd"] = ["com.iotbull.android.superapp:id/user_password_update_old_password_edit_text", "id", u"旧密码"]
        # 新密码
        d["new_pwd"] = ["com.iotbull.android.superapp:id/user_password_update_new_password_edit_text", "id", u"新密码"]
        # 确认新密码
        d["conform_pwd"] = ["com.iotbull.android.superapp:id/"
                            "user_password_update_new_password_commit_password_edit_text", "id", u"确认新密码"]
        # 确定
        d["commit"] = ["com.iotbull.android.superapp:id/user_password_update_commit_button", "id", u"确定",
                       {"px": {"width": 0.5, "height": 0.7}}]
        return d

    # 使用帮助页
    def app_help_page(self):
        d = {}
        # 标题
        d["title"] = ["com.iotbull.android.superapp:id/app_help_web_view", "id", u"使用帮助页"]
        # 页面activity
        d["activity"] = [".activitys.main_setting.AppHelpActivity", "activity", u"页面activity"]
        # 返回
        d["to_return"] = ["android.widget.ImageButton", "class", u"返回"]
        return d

    # 意见反馈页
    def feedback_page(self):
        d = {}
        # 标题
        d["title"] = ["com.iotbull.android.superapp:id/activity_feedback", "id", u"意见反馈页"]
        # 页面activity
        d["activity"] = [".activitys.main_setting.feedback.FeedbackActivity", "activity",
                         u"页面activity"]
        # 返回
        d["to_return"] = ["android.widget.ImageButton", "class", u"返回"]
        # 问题类型
        d["problem_types"] = ["//android.widget.RelativeLayout/android.support.v7.widget.RecyclerView"
                              "/android.widget.LinearLayout", "xpath", u"问题类型"]
        # 涉及设备
        d["involve_device"] = ["//android.widget.RelativeLayout/android.support.v7.widget.RecyclerView"
                               "/android.widget.LinearLayout[2]", "xpath", u"涉及设备"]
        # 问题描述
        d["problem_describe"] = ["com.iotbull.android.superapp:id/feedback_content_edit_text", "id", u"问题描述"]
        # 联系方式
        d["contact"] = ["com.iotbull.android.superapp:id/feedback_title_edit_text", "id", u"联系方式"]
        # 提交
        d["commit"] = ["com.iotbull.android.superapp:id/feedback_add_button", "id", u"提交"]
        return d

    # 主题风格页
    def theme_style_page(self):
        d = {}
        # 标题
        d["title"] = ["com.iotbull.android.superapp:id/activity_app_theme", "id", u"主题风格页"]
        # 页面activity
        d["activity"] = [".activitys.main_setting.AppThemeActivity", "activity", u"页面activity"]
        # 返回
        d["to_return"] = ["android.widget.ImageButton", "class", u"返回"]
        # 锦绣绿
        d["green"] = ["//android.support.v7.widget.RecyclerView/android.widget.LinearLayout[1]"
                      "//android.widget.RadioButton", "xpath", u"锦绣绿色"]
        # 激情红
        d["red"] = ["//android.support.v7.widget.RecyclerView/android.widget.LinearLayout[2]"
                    "//android.widget.RadioButton", "xpath", u"激情红色"]
        # 稻香橙
        d["orange"] = ["//android.support.v7.widget.RecyclerView/android.widget.LinearLayout[3]"
                       "//android.widget.RadioButton", "xpath", u"稻香橙色"]
        # 山水青
        d["cyan"] = ["//android.support.v7.widget.RecyclerView/android.widget.LinearLayout[4]"
                     "//android.widget.RadioButton", "xpath", u"山水青色"]
        return d

    # 版本信息
    def upgrade_page(self):
        d = {}
        # 标题
        d["title"] = ["com.iotbull.android.superapp:id/app_upgrade_check_upgrade_button", "id", u"版本信息页"]
        # 页面activity
        d["activity"] = [".activitys.main_setting.AppUpgradeActivity", "activity", u"页面activity"]
        # 返回
        d["to_return"] = ["android.widget.ImageButton", "class", u"返回"]
        # 当前版本
        d["current_version"] = ["com.iotbull.android.superapp:id/app_upgrade_current_version_text_view", "id", u"当前版本"]
        # 最新版本
        d["new_version"] = ["com.iotbull.android.superapp:id/app_upgrade_new_version_text_view", "id", u"最新版本"]
        # 立即更新
        d["upgrade_button"] = ["com.iotbull.android.superapp:id/app_upgrade_check_upgrade_button", "id", u"立即更新"]
        return d

    # 设备页
    def device_page(self):
        d = {}
        # 标题
        d["title"] = ["com.iotbull.android.superapp:id/home_nav_btn_device", "id", u"设备页"]
        # 页面activity
        d["activity"] = [".activitys.main_setting.HomeActivity", "activity", u"页面activity"]
        # 用户头像
        d["user_image"] = ["com.iotbull.android.superapp:id/device_user_image_view", "id", u"主页面头像"]
        # 上午好/下午好
        d["welcome"] = ["com.iotbull.android.superapp:id/device_tv_welcome_text", "id", u"上午好/下午好"]
        # 城市信息
        d["city"] = ["com.iotbull.android.superapp:id/device_city_name_text_view", "id", u"城市信息"]
        # 天气信息
        d["weather"] = ["com.iotbull.android.superapp:id/device_tv_weather_desc", "id", u"天气信息"]
        # 天气图标
        d["city"] = ["com.iotbull.android.superapp:id/device_iv_weather_image", "id", u"天气图标"]
        # 设备table
        d["device_table"] = ["com.iotbull.android.superapp:id/home_nav_btn_device", "id", u"设备table"]
        # 消息table
        d["message_table"] = ["com.iotbull.android.superapp:id/home_nav_btn_message", "id", u"消息table"]
        # 商城table
        d["mall_table"] = ["com.iotbull.android.superapp:id/home_nav_btn_mall", "id", u"商城table"]
        # 添加设备按钮
        d["add_device"] = ["com.iotbull.android.superapp:id/device_iv_add", "id", u"添加设备按钮"]
        # 切换九宫格
        d["change_layout"] = ["com.iotbull.android.superapp:id/device_iv_change_layout", "id", u"切换九宫格"]
        return d

    # 设备页→消息
    def home_message_page(self):
        d = {}
        # 标题
        d["title"] = ["com.iotbull.android.superapp:id/message_tab_btn_activity", "id", u"设备页→消息"]
        # 页面activity
        d["activity"] = [".activitys.main_setting.HomeActivity", "activity", u"页面activity"]
        # 返回
        d["to_return"] = ["android.widget.ImageButton", "class", u"返回"]
        # 活动
        d["message_activity"] = ["com.iotbull.android.superapp:id/message_tab_btn_activity", "id", u"活动"]
        # 设备
        d["device"] = ["com.iotbull.android.superapp:id/message_tab_btn_alert", "id", u"设备"]
        # 消息分类
        d["classify"] = ["android.widget.ImageButton", "class", u"消息分类"]
        # 设置
        d["setting"] = ["//android.support.v7.widget.LinearLayoutCompat/android.widget.TextView", "xpath", u"设置"]
        # 没有消息
        d["no_message"] = ["com.iotbull.android.superapp:id/recycler_view_empty_ll", "id", u"当前页面无消息"]
        return d

    # 设备页→消息设置
    def message_setting_page(self):
        d = {}
        # 标题
        d["title"] = ["com.iotbull.android.superapp:id/message_setting_rv_menu", "id", u"设备页→消息设置"]
        # 页面activity
        d["activity"] = [".activitys.main_setting.HomeActivity", "activity", u"页面activity"]
        # 返回
        d["to_return"] = ["android.widget.ImageButton", "class", u"返回"]
        # 清空活动历史消息
        d["clear_activity"] = ["//android.widget.FrameLayout/android.support.v7.widget.RecyclerView"
                               "/android.support.v7.widget.RecyclerView", "xpath", u"清空活动历史消息"]
        # 清空设备历史消息
        d["clear_device"] = ["//android.widget.FrameLayout/android.support.v7.widget.RecyclerView"
                             "/android.support.v7.widget.RecyclerView[2]", "xpath", u"清空设备历史消息"]
        return d

    # 消息→消息分类
    def message_classify_page(self):
        d = {}
        # 标题
        d["title"] = ["com.iotbull.android.superapp:id/message_classify_rv_device_list", "id", u"消息→消息分类"]
        # 页面activity
        d["activity"] = [".activitys.message_mall.message_classify.MessageClassifyActivity", "activity", u"页面activity"]
        # 返回
        d["to_return"] = ["android.widget.ImageButton", "class", u"返回"]
        # 全部设备
        d["all_device"] = ["//android.widget.LinearLayout[1]//android.widget.RadioButton", "xpath", u"全部设备"]
        # 展示体验数据
        d["experience_data"] = ["//android.widget.LinearLayout[2]//android.widget.RadioButton", "xpath", u"展示体验数据"]
        # A2 管理者
        d["A2"] = ["//android.widget.LinearLayout[3]//android.widget.RadioButton", "xpath", u"A2 管理者"]
        # A3 体验
        d["A3"] = ["//android.widget.LinearLayout[4]//android.widget.RadioButton", "xpath", u"A3 体验"]
        # A4 分享者
        d["A4"] = ["//android.widget.LinearLayout[5]//android.widget.RadioButton", "xpath", u"A4 分享者"]
        # A5 体验
        d["A5"] = ["//android.widget.LinearLayout[6]//android.widget.RadioButton", "xpath", u"A5 体验"]
        return d

    # 设备页→选择产品类型
    def device_add_scan_page(self):
        d = {}
        # 标题
        d["title"] = ["com.iotbull.android.superapp:id/select_product_gateway_list_view", "id", u"设备页→选择产品类型"]
        # 页面activity
        d["activity"] = [".activitys.device_scene.SelectProductActivity", "activity", u"页面activity"]
        # 返回
        d["to_return"] = ["android.widget.ImageButton", "class", u"返回"]
        # 公牛智能网关-硬件 .activitys.device_scene.device_add.PrepareSetNetworkActivity
        d["gateway_hw"] = ["//android.widget.ListView/android.widget.LinearLayout", "xpath", u"公牛智能网关-硬件"]
        # 公牛智能网关-模拟器
        d["gateway_sim"] = ["//android.widget.ListView/android.widget.LinearLayout[2]", "xpath", u"公牛智能网关-设备模拟器"]
        # 公牛Wi-Fi智能插座二代-硬件
        d["gn_wifi_hw"] = ["//android.widget.ListView/android.widget.LinearLayout[3]", "xpath", u"公牛Wi-Fi智能插座二代-硬件"]
        # 公牛Wi-Fi智能插座二代-设备模拟器
        d["gn_wifi_sim"] = ["//android.widget.ListView/android.widget.LinearLayout[4]", "xpath", u"公牛Wi-Fi智能插座二代-设备模拟器"]
        # 扫描二维码
        d["capture"] = ["//android.support.v7.widget.LinearLayoutCompat", "xpath", u"扫描二维码"]
        return d

    # 选择产品类型→配网说明
    def prepare_set_network_page(self):
        d = {}
        # 标题
        d["title"] = ["com.iotbull.android.superapp:id/prepare_next_button", "id", u"选择产品类型→配网说明"]
        # 页面activity
        d["activity"] = [".activitys.device_scene.device_add.PrepareSetNetworkActivity", "activity", u"页面activity"]
        # 返回
        d["to_return"] = ["android.widget.ImageButton", "class", u"返回"]
        # 下一步
        d["prepare_next"] = ["com.iotbull.android.superapp:id/prepare_next_button", "id", u"下一步"]
        return d

    # 配网说明→配置网络
    def set_network_page(self):
        d = {}
        # 标题
        d["title"] = ["com.iotbull.android.superapp:id/button_hiflying_smartlinker_start", "id", u"配网说明→配置网络"]
        # 页面activity
        d["activity"] = [".activitys.device_scene.device_add.SetNetworkActivity", "activity", u"页面activity"]
        # 返回
        d["to_return"] = ["android.widget.ImageButton", "class", u"返回"]
        # SSID
        d["ssid"] = ["com.iotbull.android.superapp:id/editText_hiflying_smartlinker_ssid", "id", u"SSID"]
        # WiFi密码
        d["wifi_pwd"] = ["com.iotbull.android.superapp:id/editText_hiflying_smartlinker_password", "id", u"WiFi密码"]
        # 下一步
        d["prepare_next"] = ["com.iotbull.android.superapp:id/button_hiflying_smartlinker_start", "id", u"下一步"]
        # 更换WiFi
        d["change_wifi"] = ["com.iotbull.android.superapp:id/da_set_network_btn_change_wifi", "id", u"更换WiFi"]
        return d

    # 配置网络→添加设备
    def scan_with_subscribe_page(self):
        d = {}
        # 标题
        d["title"] = ["com.iotbull.android.superapp:id/device_add_image_layout", "id", u"配置网络→添加设备"]
        # 页面activity
        d["activity"] = [".activitys.device_scene.device_add.ScanWithSubscribeActivity", "activity", u"页面activity"]
        # 返回
        d["to_return"] = ["android.widget.ImageButton", "class", u"返回"]
        return d

    # 添加设备→添加失败
    def add_device_failed_page(self):
        d = {}
        # 标题
        d["title"] = ["com.iotbull.android.superapp:id/failed_text_view", "id", u"添加设备→添加失败"]
        # 页面activity
        d["activity"] = [".activitys.device_scene.device_add.AddFailedActivity", "activity", u"页面activity"]
        # 返回
        d["to_return"] = ["android.widget.ImageButton", "class", u"返回"]
        # 重新扫描
        d["failed_rescan"] = ["com.iotbull.android.superapp:id/failed_rescan_button", "id", u"重新扫描"]
        # soft配网
        d["soft"] = [u"soft配网", "name", u"soft配网"]
        # 取消
        d["cancel"] = ["com.iotbull.android.superapp:id/failed_cancel_button", "id", u"取消"]
        return d


# .activitys.main_setting.AppAboutActivity 关于我们
# 天气 .activitys.main_setting.weather.CitySelectorActivity
# 照相机 com.google.zxing.activity.CaptureActivity
# 消息设置.activitys.message_mall.message_setting.MessageSettingActivity
# 选择产品类型 .activitys.device_scene.SelectProductActivity
# 扫描二维码 com.google.zxing.activity.CaptureActivity
# 公牛智能网关-硬件 .activitys.device_scene.device_add.PrepareSetNetworkActivity

class PopupWidgetAndroid(object):
    # 设备升级确认弹窗
    def update_popup(self):
        d = {}
        # 标题
        # d["title"] = [u"新版提示", "name", u"标题"]
        d["title"] = ["com.iotbull.android.superapp:id/alertTitle", "id", u"标题", {"text": u"新版提示"}]
        # 立即体验
        d["confirm"] = ["android:id/button1", "id", u"立即体验"]
        # 稍后更新
        d["cancel"] = ["android:id/button2", "id", u"稍后更新"]
        # 安装
        d["install"] = ["com.android.packageinstaller:id/ok_button", "id", u"安装"]
        # 取消
        d["install_cancel"] = ["com.android.packageinstaller:id/cancel_button", "id", u"稍后更新"]
        # 完成
        d["install"] = ["com.android.packageinstaller:id/done_button", "id", u"完成"]
        # 打开
        d["install_cancel"] = ["com.android.packageinstaller:id/launch_button", "id", u"打开"]
        return d

    # 设备登录页面提示弹窗
    def login_popup(self):
        d = {}
        # 标题
        # d["title"] = [u"操作失败，账号在其他手机登录，请确认是否本人使用。", "name", u"提示 - 重新登录"]
        d["title"] = ["android:id/message", "id", u"提示 - 重新登录", {"text": u"操作失败，账号在其他手机登录，请确认是否本人使用。"}]
        # 页面activity
        d["activity"] = [".activitys.regist_login.SplashActivity", "activity", u"页面activity"]
        # 登录
        d["confirm"] = ["android:id/button1", "id", u"登录"]
        # 取消
        d["cancel"] = ["android:id/button2", "id", u"取消"]
        return d

    # 退出登录确认弹窗
    def logout_popup(self):
        d = {}
        # 标题
        # d["title"] = [u"是否确认退出登录？", "name", u"退出确认"]
        d["title"] = ["android:id/message", "id", u"退出确认", {"text": u"是否确认退出登录？"}]
        # 确认
        d["confirm"] = ["android:id/button1", "id", u"确认"]
        # 取消
        d["cancel"] = ["android:id/button2", "id", u"取消"]
        return d

    # 终止添加设备
    def terminate_add_device_popup(self):
        d = {}
        # 标题
        # d["title"] = [u"是否确认终止添加设备？", "name", u"取消确认"]
        d["title"] = ["android:id/message", "id", u"取消确认", {"text": u"是否确认终止添加设备？"}]
        # 确认
        d["confirm"] = ["android:id/button1", "id", u"确认"]
        # 取消
        d["cancel"] = ["android:id/button2", "id", u"取消"]
        return d

    # 等待弹窗loading
    def loading_popup(self):
        d = {}
        # 标题
        # d["title"] = ["loading...", "name", u"正在加载中loading..."]
        d["title"] = ["android:id/message", "id", u"正在加载中loading...", {"text": "loading..."}]
        return d

    # 清空活动历史消息
    def clear_activity_popup(self):
        d = {}
        # 标题
        # d["title"] = [u"是否清除活动消息？", "name", u"清除确认"]
        d["title"] = ["android:id/message", "id", u"清除确认", {"text": u"是否清除活动消息？"}]
        # 确认
        d["confirm"] = ["android:id/button1", "id", u"确认"]
        # 取消
        d["cancel"] = ["android:id/button2", "id", u"取消"]
        return d

        # 清空活动历史消息

    def clear_device_popup(self):
        d = {}
        # 标题
        # d["title"] = [u"是否清除设备消息？", "name", u"清除确认"]
        d["title"] = ["android:id/message", "id", u"清除确认", {"text": u"是否清除设备消息？"}]
        # 确认
        d["confirm"] = ["android:id/button1", "id", u"确认"]
        # 取消
        d["cancel"] = ["android:id/button2", "id", u"取消"]
        return d
