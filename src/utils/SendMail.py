# coding=utf-8
import smtplib
from email.header import Header
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr

from .ShellCommand import *


class Mailer(object):
    """
    The function of sending an email.
    """

    def __init__(self, m_queue, alive, conf, send_now=False, sendTo="all"):
        # Receiver/Sender for mail.
        mail_list = ["chenghao@gongniu.cn",
                     "zhulei@gongniu.cn",
                     "fanrt@gongniu.cn",
                     "sunsy@gongniu.cn",
                     "dongjz@gongniu.cn"]

        if sendTo == "all":
            self.mail_list = mail_list
        else:
            if isinstance(sendTo, list):
                self.mail_list = sendTo
            else:
                self.mail_list = [sendTo]

        self.mail_pwd = conf["mail_pwd"]
        self.mail_host = "smtp.163.com"
        self.mail_user = bytearray.fromhex(self.mail_pwd["163"]["user_name"]).decode("utf-8")
        self.mail_pass = bytearray.fromhex(self.mail_pwd["163"]["pwd"]).decode("utf-8")
        self.mail_postfix = self.mail_user.split("@")[1]

        self.sc = ShellCommand()

        log_tmp = os.path.join(self.sc.set_appium_log_addr(), "AutoTestGNApp/%s" % time.strftime("%Y-%m-%d %H-%M"))
        self.mail_error = os.path.join(log_tmp, "mail_error.log")

        # Get report xls from child process, is blocking!
        parent_path = m_queue.get()
        m_queue.put(parent_path)

        # Scan the root directory to get the files you want to send by mail.
        f = lambda x: os.path.join(parent_path, x)
        while True:  # create root directory is faster than create files, maybe no files in mail.
            try:
                self.file_path = os.listdir(parent_path)
                if self.file_path:
                    self.file_path = list(map(f, self.file_path))
                    break
            except BaseException:
                time.sleep(1)

        # Refresh time per second.
        # When time is 7 a.m, send the scanned files in the mail.
        if send_now:
            self.send_mail()
        else:
            while True:
                now_time = time.strftime("%X")
                if "07:00:00" in now_time or not alive.value:
                    self.send_mail()
                time.sleep(1)

    def send_mail(self):
        me = "%s<%s@%s>" % (self.mail_user, self.mail_user, self.mail_postfix)
        msg = MIMEMultipart()
        msg['Subject'] = u'自动化测试结果输出'
        msg['From'] = self.format_addr(u'自动化测试 <%s>' % me)
        msg['To'] = self.format_addr(u'管理员 <%s>' % ";".join(self.mail_list))

        # puretext = MIMEText('<h1>你好，<br/>'+self.mail_content+'</h1>','html','utf-8')
        puretext = MIMEText(u'Dear All:\n'
                            u'    如下是自动测试结果输出，请各位审阅，谢谢。若附件部分内容缺失请用本地应用打开附件即可\n',
                            'plain', 'utf-8')
        msg.attach(puretext)

        # 文本类型的附件
        for i in self.file_path:
            name = os.path.basename(i)
            jpgpart = MIMEApplication(open(r'%s' % i, 'rb').read())
            jpgpart.add_header('Content-Disposition', 'attachment', filename=name)
            msg.attach(jpgpart)

        # jpg类型的附件
        # jpgpart = MIMEApplication(open('D:/test.log', 'rb').read())
        # jpgpart.add_header('Content-Disposition', 'attachment', filename='test.log')
        # msg.attach(jpgpart)

        # xlsx类型的附件
        # xlsxpart = MIMEApplication(open('test.xlsx', 'rb').read())
        # xlsxpart.add_header('Content-Disposition', 'attachment', filename='test.xlsx')
        # msg.attach(xlsxpart)

        # mp3类型的附件
        # mp3part = MIMEApplication(open('kenny.mp3', 'rb').read())
        # mp3part.add_header('Content-Disposition', 'attachment', filename='benny.mp3')
        # msg.attach(mp3part)

        # pdf类型附件
        # part = MIMEApplication(open('foo.pdf', 'rb').read())
        # part.add_header('Content-Disposition', 'attachment', filename="foo.pdf")
        # msg.attach(part)

        try:
            s = smtplib.SMTP()  # 创建邮件服务器对象
            s.connect(self.mail_host)  # 连接到指定的smtp服务器。参数分别表示smpt主机和端口
            s.login(self.mail_user, self.mail_pass)  # 登录到你邮箱
            s.sendmail(me, self.mail_list, msg.as_string())  # 发送内容
            s.close()
            print("send mail success !!")
            return True
        except Exception as e:
            with open(self.mail_error, "a", encoding="utf-8") as files:
                files.write(str(e))
            return False

    def format_addr(self, s):
        name, addr = parseaddr(s)
        return formataddr((Header(name, 'utf-8').encode("utf-8"), addr))
