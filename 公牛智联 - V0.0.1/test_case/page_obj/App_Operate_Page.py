# coding=utf-8
import sys

sys.path.append("..")
from models.driver import ReadInfo


class MainPageWidget(ReadInfo):
    def class_mainpage_init(self):
        self.login_page()
        self.find_password_page()
        self.register_page()
        self.procotol_page()
        self.account_setting_page()

    def login_page(self):
        # 用户名输入框
        username = ["com.iotbull.android.superapp:id/loginUserNameEditText", "id"]
        # 密码输入框
        password = ["com.iotbull.android.superapp:id/loginPasswordEditText", "id"]
        # 忘记密码
        to_find_password = ["com.iotbull.android.superapp:id/loginFindPasswordTextView", "id"]
        # 登录按钮
        login_button = ["com.iotbull.android.superapp:id/loginCommitButton", "id"]
        # 新账号注册
        to_register = ["com.iotbull.android.superapp:id/loginToRegistTextView", "id"]

    def find_password_page(self):
        # 返回
        to_return = ["android.widget.ImageButton", "class"]
        # 手机号
        user_name = ["com.iotbull.android.superapp:id/forget_password_user_name_edit_text", "id"]
        # 验证码
        check_code = ["com.iotbull.android.superapp:id/forget_password_check_code_edit_text", "id"]
        # 获取验证码
        get_check_code = ["com.iotbull.android.superapp:id/forget_password_get_check_code_text_view", "id"]
        # 下一步
        to_next = ["com.iotbull.android.superapp:id/forget_password_commit_button", "id"]

    def register_page(self):
        # 用户名
        username = ["com.iotbull.android.superapp:id/registUserNameEditText", "id"]
        # 密码
        password = ["com.iotbull.android.superapp:id/registPasswordEditText", "id"]
        # 验证码
        check_code = ["com.iotbull.android.superapp:id/registCheckCodeEditText", "id"]
        # 获取验证码
        get_check_code = ["com.iotbull.android.superapp:id/registGetCheckCodeTextView", "id"]
        # 立即注册按钮
        register_button = ["com.iotbull.android.superapp:id/regist_commit_button", "id"]
        # 公牛服务协议
        to_protocol = ["com.iotbull.android.superapp:id/registToRegistProtocolTextView", "id"]
        # 已有账户登录
        to_login = ["com.iotbull.android.superapp:id/registToLoginTextView", "id"]
        # 密码可见/不可见
        check_box = ["com.iotbull.android.superapp:id/checkBox", "id"]

    def procotol_page(self):
        # 返回
        to_return = ["android.widget.ImageButton", "class"]

    def devices_page(self):
        pass

    def personal_settings(self):
        # 头像
        head_image = ["com.iotbull.android.superapp:id/home_setting_head_image_view", "id"]
        # 昵称
        nickname = ["com.iotbull.android.superapp:id/menu_setting_nickname_text_view", "id"]
        # 账号
        id = ["com.iotbull.android.superapp:id/menu_setting_phone_text_view", "id"]
        # 账户设置
        account_setting = [u"账户设置", "name"]
        # 使用帮助
        using_help = [u"使用帮助", "name"]
        # 意见反馈
        feedback = [u"意见反馈", "name"]
        # 主题风格
        theme_style = [u"主题风格", "name"]
        # 版本信息
        version_info = [u"版本信息", "name"]
        # 关于我们
        about_us = [u"关于我们", "name"]

    def account_setting_page(self):
        # 标题
        title = [u"账户设置", "name"]
        # 返回
        to_return = ["android.widget.ImageButton", "class"]
        # 昵称
        nickname = [u"昵称", "name"]
        # 性别
        gender = [u"性别", "name"]
        # 地址
        address = [u"地址", "name"]
        # 生日
        birthday = [u"生日", "name"]
        # 修改密码
        change_pwd = [u"修改密码", "name"]
        # 退出登录
        logout = ["com.iotbull.android.superapp:id/user_info_btn_logout", "id"]

    def change_nickname(self):
        # 标题
        title = [u"修改昵称", "name"]
        # 返回
        to_return = ["android.widget.ImageButton", "class"]
        # 输入框
        nickname = ["com.iotbull.android.superapp:id/user_name_update_nickname_edit_text", "id"]
        # 完成
        commit = ["com.iotbull.android.superapp:id/user_name_update_commit_button", "id"]

    # uiautomatorviewer没办法读取滚轮数值，暂不使用
    def gender_page(self):
        # 选择性别
        choose_gender = [u"选择性别", "name"]
        # 取消
        cancel = [u"取消", "name"]
        # 确定
        submit = [u"确定", "name"]
        # 男

    def change_pwd_page(self):
        # 标题
        title = [u"修改密码", "name"]
        # 返回
        to_return = ["android.widget.ImageButton", "class"]
        # 旧密码
        old_pwd = ["com.iotbull.android.superapp:id/user_password_update_old_password_edit_text", "id"]
        # 新密码
        new_pwd = ["com.iotbull.android.superapp:id/user_password_update_new_password_edit_text", "id"]
        # 确认新密码
        conform_pwd = ["com.iotbull.android.superapp:id/user_password_update_new_password_commit_password_edit_text", "id"]
        # 确定
        commit = ["com.iotbull.android.superapp:id/user_password_update_commit_button", "id"]

    def feedback_page(self):
        # 标题
        title = [u"意见反馈", "name"]
        # 返回
        to_return = ["android.widget.ImageButton", "class"]
        # 问题类型
        problem_types = [u"问题类型", "name"]
        # 涉及设备
        involve_device = [u"涉及设备", "name"]
        # 问题描述
        problem_describe = ["com.iotbull.android.superapp:id/feedback_content_edit_text", "id"]
        # 联系方式
        contact = ["com.iotbull.android.superapp:id/feedback_title_edit_text", "id"]
        # 提交
        commit = ["com.iotbull.android.superapp:id/feedback_add_button", "id"]

    def device_page(self):
        # 设备table
        device_table = []
        # 消息table

        # 商城table
