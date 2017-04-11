# coding:utf-8
from src.testcase.case.INPUT_CASE.GNAppDevicePage import *
from src.testcase.case.INPUT_CASE.GNAppForgetPassword import *
from src.testcase.case.INPUT_CASE.GNAppLogin import *
from src.testcase.case.INPUT_CASE.GNAppMessageClassify import *
from src.testcase.case.INPUT_CASE.GNAppPersonalSettings import *
from src.testcase.case.INPUT_CASE.GNAppRegister import *

CaseTitle = {
    u'默认页面信息检查': GNAppDevicePage1,
    u'设备配网过程中，返回按钮功能检查': GNAppDevicePage2,
    u'设备配网过程中，弹出终止配网提示框，取消按钮功能检查': GNAppDevicePage3,
    u'忘记密码页面-点击"返回"按钮，页面检查': GNAppForgetPassword1,
    u'登录页面—新用户注册页面跳转': GNAppLogin1,
    u'登录页面—忘记密码页面跳转': GNAppLogin2,
    u'登录页面—登录功能检查': GNAppLogin3,
    u'消息分类页面信息检查': GNAppMessageClassify1,
    u'账户设置-修改密码页面，"返回"按钮功能检查': GNAppPersonalSettings1,
    u'账户设置-密码修改后页面跳转确认': GNAppPersonalSettings2,
    u'账户设置-退出当前账号后，取消按钮功能检查': GNAppPersonalSettings3,
    u'使用帮助-返回按钮功能确认': GNAppPersonalSettings4,
    u'注册页面-已有账户登录按钮，跳转页面检查': GNAppRegister1,
    'over': 'yes'}
