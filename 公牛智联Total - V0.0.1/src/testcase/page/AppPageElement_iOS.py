# coding=utf-8
class MainPageWidgetIos(object):
    # 万能页面
    def god_page(self):
        d = {}
        d["title"] = ["//XCUIElementTypeStatusBar", "xpath", u"万能控件",
                      {"px": {"width": 0, "height": 0}}]
        return d

    # 引导页
    def view_pager_page(self):
        d = {}
        # 标题
        d["title"] = ["com.iotbull.android.superapp:id/indicator", "accessibility_id", u"引导页"]
        return d

    # 登录页
    def login_page(self):
        d = {}
        # 标题
        d["title"] = [u"登  录", "accessibility_id", u"登录页"]
        # 页面activity
        # d["activity"] = [".activitys.regist_login.LoginActivity", "activity", u"页面activity"]
        # 用户名输入框
        d["username"] = ["//XCUIElementTypeOther/XCUIElementTypeTextField", "xpath", u"用户名输入框"]
        # 密码输入框
        d["password"] = ["//XCUIElementTypeOther/XCUIElementTypeSecureTextField", "xpath", u"密码输入框"]
        # 显示密码
        d["check_box"] = ["eye close", "accessibility_id", u"密码可见/不可见"]
        # 忘记密码
        d["to_find_password"] = [u"忘记密码？", "accessibility_id", u"忘记密码"]
        # 登录按钮
        d["login_button"] = [u"登  录", "accessibility_id", u"登录按钮",
                             {"px": {"width": 0.5, "height": 0.65}}]
        # 新账号注册
        d["to_register"] = [u"新用户注册", "accessibility_id", u"新账号注册"]
        return d

    # 忘记密码页
    def find_password_page(self):
        d = {}
        # 标题
        d["title"] = [u"密码找回", "accessibility_id", u"忘记密码页"]
        # 页面activity
        # d["activity"] = [".activitys.regist_login.ForgetPasswordActivity", "activity", u"页面activity"]
        # 返回
        d["to_return"] = ["//XCUIElementTypeButton", "xpath", u"返回"]
        # 手机号
        d["user_name"] = ["//XCUIElementTypeOther/XCUIElementTypeTextField", "xpath", u"手机号"]
        # 验证码
        d["check_code"] = ["//XCUIElementTypeOther/XCUIElementTypeTextField[2]", "xpath", u"验证码"]
        # 获取验证码
        d["get_check_code"] = ["//XCUIElementTypeTextField[2]/XCUIElementTypeButton", "xpath", u"获取验证码"]
        # 下一步
        d["to_next"] = [u"下一步", "accessibility_id", u"下一步",
                        {"px": {"width": 0.5, "height": 0.45}}]
        return d

    # 忘记密码→重置密码页
    def new_password_page(self):
        d = {}
        # 标题
        d["title"] = [u"新密码设置", "accessibility_id", u"忘记密码→重置密码页"]
        # 页面activity
        # d["activity"] = [".activitys.regist_login.ForgetPasswordActivity", "activity", u"页面activity"]
        # 返回
        d["to_return"] = ["//XCUIElementTypeButton", "xpath", u"返回"]
        # 新密码
        d["new_pwd"] = ["//XCUIElementTypeOther/XCUIElementTypeSecureTextField", "xpath", u"新密码"]
        # 确认新密码
        d["conform_pwd"] = ["//XCUIElementTypeOther/XCUIElementTypeSecureTextField[2]", "xpath", u"确认新密码"]
        # 完成
        d["commit"] = ["//XCUIElementTypeOther/XCUIElementTypeButton", "xpath", u"完成"]
        return d

    # 注册页
    def register_page(self):
        d = {}
        # 标题
        d["title"] = [u"立即注册", "accessibility_id", u"注册页"]
        # 页面activity
        # d["activity"] = [".activitys.regist_login.RegistActivity", "activity", u"页面activity"]
        # 用户名
        d["username"] = ["//XCUIElementTypeOther/XCUIElementTypeTextField", "xpath", u"用户名"]
        # 密码
        d["password"] = ["//XCUIElementTypeOther/XCUIElementTypeSecureTextField", "xpath", u"密码"]
        # 验证码
        d["check_code"] = ["//XCUIElementTypeOther/XCUIElementTypeTextField[2]", "xpath", u"验证码"]
        # 获取验证码
        d["get_check_code"] = [u"获取验证码", "accessibility_id", u"获取验证码"]
        # 立即注册按钮
        d["register_button"] = [u"立即注册", "accessibility_id", u"立即注册按钮",
                                {"px": {"width": 0.5, "height": 0.75}}]
        # 公牛服务协议
        d["to_protocol"] = ["//XCUIElementTypeOther/XCUIElementTypeButton[2]", "xpath", u"公牛服务协议"]
        # 已有账户登录
        d["to_login"] = [u"已有账户登录", "accessibility_id", u"已有账户登录"]
        # 密码可见/不可见
        d["check_box"] = ["eye close", "accessibility_id", u"密码可见/不可见"]
        return d

    # 用户使用协议页
    def protocol_page(self):
        d = {}
        # 标题
        d["title"] = [u"用户协议", "accessibility_id", u"用户使用协议页"]
        # 页面activity
        # d["activity"] = [".activitys.regist_login.RegistProtocolActivity", "activity", u"页面activity"]
        # 返回
        d["to_return"] = ["//XCUIElementTypeButton", "xpath", u"返回"]
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
        d["title"] = [u"账户设置", "accessibility_id", u"个人设置页"]
        # 页面activity
        # d["activity"] = [".activitys.main_setting.HomeActivity", "activity", u"页面activity"]
        # 头像
        d["head_image"] = ["None", "accessibility_id", u"头像"]
        # 昵称
        d["nickname"] = ["//XCUIElementTypeOther/XCUIElementTypeStaticText", "xpath", u"昵称"]
        # 账号
        d["accessibility_id"] = ["//XCUIElementTypeOther/XCUIElementTypeStaticText[2]", "xpath", u"账号"]
        # 账户设置
        d["account_setting"] = ["//XCUIElementTypeCell", "xpath", u"账户设置"]
        # 使用帮助
        d["using_help"] = ["//XCUIElementTypeCell[2]", "xpath", u"使用帮助"]
        # 意见反馈
        d["feedback"] = ["//XCUIElementTypeCell[3]", "xpath", u"意见反馈"]
        # 主题风格
        d["theme_style"] = ["//XCUIElementTypeCell[4]", "xpath", u"主题风格"]
        # 版本信息
        d["version_info"] = ["//XCUIElementTypeCell[5]", "xpath", u"版本信息"]
        # 关于我们
        d["about_us"] = ["//XCUIElementTypeCell[6]", "xpath", u"关于我们"]
        return d

    # 账户设置页
    def account_setting_page(self):
        d = {}
        # 标题
        d["title"] = [u"退出登录", "accessibility_id", u"账户设置页"]
        # 页面activity
        # d["activity"] = [".activitys.main_setting.userinfo_setting.UserInfoSettingActivity", "activity", u"页面activity"]
        # 返回
        d["to_return"] = ["//XCUIElementTypeButton", "xpath", u"返回"]
        # 昵称
        d["nickname"] = ["//XCUIElementTypeOther[2]//XCUIElementTypeTable/XCUIElementTypeCell", "xpath", u"昵称"]
        # 性别
        d["gender"] = ["//XCUIElementTypeOther[2]//XCUIElementTypeTable/XCUIElementTypeCell[2]", "xpath", u"性别"]
        # 地址
        d["address"] = ["//XCUIElementTypeOther[2]//XCUIElementTypeTable/XCUIElementTypeCell[3]", "xpath", u"地址"]
        # 生日
        d["birthday"] = ["//XCUIElementTypeOther[2]//XCUIElementTypeTable/XCUIElementTypeCell[4]", "xpath", u"生日"]
        # 修改密码
        d["change_pwd"] = ["//XCUIElementTypeOther[2]//XCUIElementTypeTable/XCUIElementTypeCell[5]", "xpath", u"修改密码"]
        # 退出登录
        d["logout"] = [u"退出登录", "accessibility_id", u"退出登录"]
        return d

    # 修改昵称页
    def change_nickname_page(self):
        d = {}
        # 标题
        d["title"] = [u"修改昵称", "accessibility_id", u"修改昵称页"]
        # 页面activity
        # d["activity"] = [".activitys.main_setting.userinfo_setting.UserNameUpdateActivity", "activity", u"页面activity"]
        # 返回
        d["to_return"] = ["//XCUIElementTypeButton", "xpath", u"返回"]
        # 输入框
        d["nickname"] = ["//XCUIElementTypeOther[2]//XCUIElementTypeTextField", "xpath", u"输入框"]
        # 完成
        d["commit"] = [u"完 成", "accessibility_id", u"完成"]
        return d

    # uiautomatorviewer没办法读取滚轮数值，暂不使用
    def gender_page(self):
        d = {}
        # 标题
        d["title"] = ["//XCUIElementTypeOther[2]//XCUIElementTypeOther[2]"
                      "//XCUIElementTypeOther/XCUIElementTypeButton", "xpath", u"选择性别"]
        # 男
        d["title"] = ["//XCUIElementTypeOther[2]//XCUIElementTypeOther[2]"
                      "//XCUIElementTypeOther/XCUIElementTypeButton", "xpath", u"男"]
        # 女
        d["submit"] = ["//XCUIElementTypeOther[2]//XCUIElementTypeOther[2]"
                       "//XCUIElementTypeOther[3]/XCUIElementTypeButton", "xpath", u"女"]
        # 取消
        d["cancel"] = ["//XCUIElementTypeOther[2]//XCUIElementTypeOther[2]"
                       "/XCUIElementTypeOther[2]//XCUIElementTypeButton", "xpath", u"取消"]

        return d

    # 修改密码页
    def change_pwd_page(self):
        d = {}
        # 标题
        d["title"] = [u"修改密码", "accessibility_id", u"修改密码页"]
        # 页面activity
        # d["activity"] = [".activitys.main_setting.password_update.UserPasswordUpdateActivity", "activity",
        #                  u"页面activity"]
        # 返回
        d["to_return"] = ["//XCUIElementTypeButton", "xpath", u"返回"]
        # 旧密码
        d["old_pwd"] = ["//XCUIElementTypeOther[2]//XCUIElementTypeSecureTextField", "xpath", u"旧密码"]
        # 新密码
        d["new_pwd"] = ["//XCUIElementTypeOther[2]//XCUIElementTypeSecureTextField[2]", "xpath", u"新密码"]
        # 确认新密码
        d["conform_pwd"] = ["//XCUIElementTypeOther[2]//XCUIElementTypeSecureTextField[3]", "xpath", u"确认新密码"]
        # 确定
        d["commit"] = [u"确  定", "accessibility_id", u"确定",
                       {"px": {"width": 0.5, "height": 0.7}}]
        return d

    # 使用帮助页
    def app_help_page(self):
        d = {}
        # 标题
        d["title"] = [u"使用帮助", "accessibility_id", u"使用帮助页"]
        # 页面activity
        # d["activity"] = [".activitys.main_setting.AppHelpActivity", "activity", u"页面activity"]
        # 返回
        d["to_return"] = ["//XCUIElementTypeButton", "xpath", u"返回"]
        return d

    # 意见反馈页
    def feedback_page(self):
        d = {}
        # 标题
        d["title"] = [u"意见反馈", "accessibility_id", u"意见反馈页"]
        # 页面activity
        # d["activity"] = [".activitys.main_setting.feedback.FeedbackActivity", "activity",
        #                  u"页面activity"]
        # 返回
        d["to_return"] = ["//XCUIElementTypeButton", "xpath", u"返回"]
        # 问题类型
        d["problem_types"] = ["//XCUIElementTypeOther[2]//XCUIElementTypeCell/XCUIElementTypeStaticText",
                              "xpath", u"问题类型"]
        # 涉及设备
        d["involve_device"] = ["//XCUIElementTypeOther[2]//XCUIElementTypeCell[2]/XCUIElementTypeStaticText",
                               "xpath", u"相关设备"]
        # 问题描述
        d["problem_describe"] = ["//XCUIElementTypeOther[2]//XCUIElementTypeTextView", "xpath", u"问题描述"]
        # 联系方式
        d["contact"] = ["//XCUIElementTypeOther[2]//XCUIElementTypeTextField", "xpath", u"联系方式"]
        # 提交
        d["commit"] = [u"提交", "accessibility_id", u"提交"]
        return d

    # 主题风格页
    def theme_style_page(self):
        d = {}
        # 标题
        d["title"] = [u"主题风格", "accessibility_id", u"主题风格页"]
        # 页面activity
        # d["activity"] = [".activitys.main_setting.AppThemeActivity", "activity", u"页面activity"]
        # 返回
        d["to_return"] = ["//XCUIElementTypeButton", "xpath", u"返回"]
        # 锦绣绿
        d["green"] = ["select_off_green", "accessibility_id", u"锦绣绿色"]
        # 激情红
        d["red"] = ["select_off_red", "accessibility_id", u"激情红色"]
        # 稻香橙
        d["orange"] = ["select_off_orange", "accessibility_id", u"稻香橙色"]
        # 山水青
        d["cyan"] = ["select_off_purple", "accessibility_id", u"山水青色"]
        return d

    # 版本信息
    def upgrade_page(self):
        d = {}
        # 标题
        d["title"] = [u"版本信息", "accessibility_id", u"版本信息页"]
        # 页面activity
        # d["activity"] = [".activitys.main_setting.AppUpgradeActivity", "activity", u"页面activity"]
        # 返回
        d["to_return"] = ["//XCUIElementTypeButton", "xpath", u"返回"]
        # 当前版本
        d["current_version"] = ["//XCUIElementTypeOther[2]//XCUIElementTypeStaticText[2]", "xpath", u"当前版本"]
        # 最新版本
        d["new_version"] = ["//XCUIElementTypeOther[2]//XCUIElementTypeStaticText[4]", "xpath", u"最新版本"]
        # 立即更新
        d["upgrade_button"] = [u"立即更新", "xpath", u"立即更新"]
        return d

    # 设备页
    def device_page(self):
        d = {}
        # 标题
        d["title"] = ["//XCUIElementTypeOther[2]/XCUIElementTypeTabBar/XCUIElementTypeButton", "xpath", u"设备页"]
        # 页面activity
        # d["activity"] = [".activitys.main_setting.HomeActivity", "activity", u"页面activity"]
        # 用户头像
        d["user_image"] = ["//XCUIElementTypeOther[2]/XCUIElementTypeOther/XCUIElementTypeOther"
                           "/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeOther"
                           "/XCUIElementTypeOther/XCUIElementTypeOther/XCUIElementTypeImage", "xpath", u"主页面头像"]
        # 上午好/下午好
        d["welcome"] = ["//XCUIElementTypeOther[2]//XCUIElementTypeStaticText", "xpath", u"上午好/下午好"]
        # 城市信息
        d["city"] = ["//XCUIElementTypeOther[2]//XCUIElementTypeButton", "xpath", u"城市信息"]
        # 天气信息
        d["weather"] = ["//XCUIElementTypeOther[2]//XCUIElementTypeStaticText[2]", "xpath", u"天气信息"]
        # 天气图标
        d["city"] = ["//XCUIElementTypeOther[2]//XCUIElementTypeImage/XCUIElementTypeImage", "xpath", u"天气图标"]
        # 设备table
        d["device_table"] = ["//XCUIElementTypeOther[2]/XCUIElementTypeTabBar/XCUIElementTypeButton",
                             "xpath", u"设备table"]
        # 消息table
        d["message_table"] = ["//XCUIElementTypeOther[2]/XCUIElementTypeTabBar/XCUIElementTypeButton[2]",
                              "xpath", u"消息table"]
        # 商城table
        d["mall_table"] = ["//XCUIElementTypeOther[2]/XCUIElementTypeTabBar/XCUIElementTypeButton[3]",
                           "xpath", u"商城table"]
        # 添加设备按钮
        d["add_device"] = ["//XCUIElementTypeOther[2]//XCUIElementTypeOther/XCUIElementTypeButton",
                           "xpath", u"添加设备按钮"]
        # 切换九宫格
        d["change_layout"] = ["//XCUIElementTypeOther[2]//XCUIElementTypeOther/XCUIElementTypeButton[2]",
                              "xpath", u"切换九宫格"]
        return d

    # 设备页→消息
    def home_message_page(self):
        d = {}
        # 标题
        d["title"] = [u"活 动", "accessibility_id", u"设备页→消息"]
        # 页面activity
        # d["activity"] = [".activitys.main_setting.HomeActivity", "activity", u"页面activity"]
        # 返回
        d["to_return"] = ["//XCUIElementTypeButton", "xpath", u"返回"]
        # 活动
        d["message_activity"] = ["//XCUIElementTypeOther[2]/XCUIElementTypeImage/XCUIElementTypeButton",
                                 "xpath", u"活动"]
        # 设备
        d["device"] = ["//XCUIElementTypeOther[2]/XCUIElementTypeImage/XCUIElementTypeButton[2]",
                       "xpath", u"设备"]
        # 消息分类
        d["classify"] = ["//XCUIElementTypeOther[2]//XCUIElementTypeNavigationBar/XCUIElementTypeButton",
                         "xpath", u"消息分类"]
        # 设置
        d["setting"] = ["//XCUIElementTypeOther[2]//XCUIElementTypeNavigationBar/XCUIElementTypeButton",
                        "xpath", u"设置"]
        # 没有消息
        d["no_message"] = [u"暂时还没有内容哦", "accessibility_id", u"当前页面无消息"]
        return d

    # 设备页→消息设置
    def message_setting_page(self):
        d = {}
        # 标题
        d["title"] = [u"消息设置", "accessibility_id", u"设备页→消息设置"]
        # 页面activity
        # d["activity"] = [".activitys.main_setting.HomeActivity", "activity", u"页面activity"]
        # 返回
        d["to_return"] = ["//XCUIElementTypeButton", "xpath", u"返回"]
        # 清空活动历史消息
        d["clear_activity"] = [u"清空活动历史消息", "accessibility_id", u"清空活动历史消息"]
        # 清空设备历史消息
        d["clear_device"] = [u"清空设备历史消息", "accessibility_id", u"清空设备历史消息"]
        return d

    # 消息→消息分类
    def message_classify_page(self):
        d = {}
        # 标题
        d["title"] = [u"设备分类", "accessibility_id", u"消息→消息分类"]
        # 页面activity
        # d["activity"] = [".activitys.message_mall.message_classify.MessageClassifyActivity", "activity", u"页面activity"]
        # 返回
        d["to_return"] = ["//XCUIElementTypeButton", "xpath", u"返回"]
        # 全部设备
        d["all_device"] = ["//XCUIElementTypeOther[2]//XCUIElementTypeCell", "xpath", u"全部设备"]
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
        d["title"] = [u"添加设备", "accessibility_id", u"设备页→添加设备"]
        # 页面activity
        # d["activity"] = [".activitys.device_scene.SelectProductActivity", "activity", u"页面activity"]
        # 返回
        d["to_return"] = ["//XCUIElementTypeButton", "xpath", u"返回"]
        # 公牛智能网关
        d["gateway_hw"] = ["//XCUIElementTypeOther[2]//XCUIElementTypeCell", "xpath", u"公牛智能网关"]
        # 智能LED灯
        d["smart_led"] = ["//XCUIElementTypeOther[2]//XCUIElementTypeCell[2]", "xpath", u"智能LED灯"]
        # 公牛Wi-Fi智能插座二代-硬件
        d["gn_wifi_hw"] = [u"公牛Wi-Fi智能插座二代-硬件", "accessibility_id", u"公牛Wi-Fi智能插座二代-硬件"]
        # 公牛Wi-Fi智能插座二代-设备模拟器
        d["gn_wifi_sim"] = [u"公牛Wi-Fi智能插座二代-设备模拟器", "accessibility_id", u"公牛Wi-Fi智能插座二代-设备模拟器"]
        # 扫描二维码
        d["capture"] = ["//XCUIElementTypeOther[2]//XCUIElementTypeButton[2]", "xpath", u"扫描二维码"]
        return d

    # 选择产品类型→配网说明
    def prepare_set_network_page(self):
        d = {}
        # 标题
        d["title"] = [u"添加网关", "accessibility_id", u"选择产品类型→配网说明"]
        # 页面activity
        # d["activity"] = [".activitys.device_scene.device_add.PrepareSetNetworkActivity", "activity", u"页面activity"]
        # 返回
        d["to_return"] = ["//XCUIElementTypeButton", "xpath", u"返回"]
        # 下一步
        d["prepare_next"] = [u"下一步", "accessibility_id", u"下一步"]
        return d

    # 配网说明→配置网络
    def set_network_page(self):
        d = {}
        # 标题
        d["title"] = [u"添加网关", "accessibility_id", u"配网说明→配置网络"]
        # 页面activity
        # d["activity"] = [".activitys.device_scene.device_add.SetNetworkActivity", "activity", u"页面activity"]
        # 返回
        d["to_return"] = ["//XCUIElementTypeButton", "xpath", u"返回"]
        # SSID
        d["ssid"] = ["//XCUIElementTypeOther[2]//XCUIElementTypeOther[2]/XCUIElementTypeTextField",
                     "xpath", u"SSID"]
        # WiFi密码
        d["wifi_pwd"] = ["//XCUIElementTypeOther[2]//XCUIElementTypeOther[2]/XCUIElementTypeTextField[2]",
                         "xpath", u"WiFi密码"]
        # 下一步
        d["prepare_next"] = [u"下一步", "accessibility_id", u"下一步"]
        # 更换WiFi
        d["change_wifi"] = [u"设置WIFI", "accessibility_id", u"更换WiFi"]
        return d

    # 配置网络→添加设备
    def scan_with_subscribe_page(self):
        d = {}
        # 标题
        d["title"] = [u"添加设备", "accessibility_id", u"配置网络→添加设备"]
        # 页面activity
        # d["activity"] = [".activitys.device_scene.device_add.ScanWithSubscribeActivity", "activity", u"页面activity"]
        # 返回
        d["to_return"] = ["//XCUIElementTypeButton", "xpath", u"返回"]
        return d

    # 添加设备→添加失败
    def add_device_failed_page(self):
        d = {}
        # 标题
        d["title"] = [u"添加网关", "accessibility_id", u"添加设备→添加失败"]
        # 页面activity
        # d["activity"] = [".activitys.device_scene.device_add.AddFailedActivity", "activity", u"页面activity"]
        # 返回
        d["to_return"] = ["//XCUIElementTypeButton", "xpath", u"返回"]
        # 重新扫描
        d["failed_rescan"] = [u"重新扫描", "accessibility_id", u"重新扫描"]
        # soft配网
        d["soft"] = [u"高级配网", "accessibility_id", u"soft配网"]
        return d


# .activitys.main_setting.AppAboutActivity 关于我们
# 天气 .activitys.main_setting.weather.CitySelectorActivity
# 照相机 com.google.zxing.activity.CaptureActivity
# 消息设置.activitys.message_mall.message_setting.MessageSettingActivity
# 选择产品类型 .activitys.device_scene.SelectProductActivity
# 扫描二维码 com.google.zxing.activity.CaptureActivity
# 公牛智能网关-硬件 .activitys.device_scene.device_add.PrepareSetNetworkActivity

class PopupWidgetIos(object):
    # 设备升级确认弹窗
    def update_popup(self):
        d = {}
        # 标题
        d["title"] = [u"新版提示", "accessibility_id", u"标题"]
        # 立即体验
        d["confirm"] = ["android:id/button1", "accessibility_id", u"立即体验"]
        # 稍后更新
        d["cancel"] = ["android:id/button2", "accessibility_id", u"稍后更新"]
        # 安装
        d["install"] = ["com.android.packageinstaller:id/ok_button", "accessibility_id", u"安装"]
        # 取消
        d["install_cancel"] = ["com.android.packageinstaller:id/cancel_button", "accessibility_id", u"稍后更新"]
        # 完成
        d["install"] = ["com.android.packageinstaller:id/done_button", "accessibility_id", u"完成"]
        # 打开
        d["install_cancel"] = ["com.android.packageinstaller:id/launch_button", "accessibility_id", u"打开"]
        return d

    # 设备登录页面提示弹窗
    def login_popup(self):
        d = {}
        # 标题
        d["title"] = [u"您的账号在其他设备上登录了", "accessibility_id", u"提示 - 重新登录"]
        # 页面activity
        # d["activity"] = [".activitys.regist_login.SplashActivity", "activity", u"页面activity"]
        # 登录
        d["confirm"] = ["//XCUIElementTypeOther[4]/XCUIElementTypeButton", "xpath", u"确定"]
        return d

    # 退出登录确认弹窗
    def logout_popup(self):
        d = {}
        # 标题
        d["title"] = [u"是否确认退出登录？", "accessibility_id", u"退出确认"]
        # 确认
        d["confirm"] = [u"确定", "accessibility_id", u"确定"]
        # 取消
        d["cancel"] = [u"取消", "accessibility_id", u"取消"]
        return d

    # 终止添加设备
    def terminate_add_device_popup(self):
        d = {}
        # 标题
        d["title"] = [u"是否确认终止添加设备？", "accessibility_id", u"取消确认"]
        # 确认
        d["confirm"] = [u"退出", "accessibility_id", u"确认"]
        # 取消
        d["cancel"] = [u"取消", "accessibility_id", u"取消"]
        return d

    # 等待弹窗loading
    def loading_popup(self):
        d = {}
        # 标题
        d["title"] = ["loading...", "accessibility_id", u"正在加载中loading..."]
        return d

    # 清空活动历史消息
    def clear_activity_popup(self):
        d = {}
        # 标题
        d["title"] = [u"是否清除活动消息？", "accessibility_id", u"清除确认"]
        # 确认
        d["confirm"] = ["android:id/button1", "accessibility_id", u"确认"]
        # 取消
        d["cancel"] = ["android:id/button2", "accessibility_id", u"取消"]
        return d

        # 清空活动历史消息

    def clear_device_popup(self):
        d = {}
        # 标题
        d["title"] = [u"是否清除设备消息？", "accessibility_id", u"清除确认"]
        # 确认
        d["confirm"] = ["android:id/button1", "accessibility_id", u"确认"]
        # 取消
        d["cancel"] = ["android:id/button2", "accessibility_id", u"取消"]
        return d
