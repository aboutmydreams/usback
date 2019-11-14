import requests
import time
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from flask_mail import Mail, Message
import sys


def iemail(QQ_num, data, em_name):
    # 第三方 SMTP 服务
    # name = str(data[0])
    # price = str(data[1])
    # change = str(data[2])
    # change1 = str(data[3])
    # print(change1)
    mail_host = "smtp.qq.com"  # 设置服务器

    # mail_user = "2491189079@qq.com"  # 用户名
    # mail_pass = "hsokuuoiiacjeccj"  # 口令
    # sender = '2491189079@qq.com'

    # mail_user = "1097977702@qq.com"
    # mail_pass = "xqrtdrqudrmtihee"
    # sender = "1097977702@qq.com"

    mail_user = "ncuhomer@qq.com"
    mail_pass = "fyicicjdfuwwchcg"
    sender = "ncuhomer@qq.com"

    receivers = ['{}@qq.com'.format(QQ_num)]  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

    message = MIMEText("""
    <p>{}, Happy BirthDay !,</p>
                       
                       <img src="https://cdn.nlark.com/yuque/0/2019/png/164272/1557753081523-e8bb33c3-9453-465c-8452-a3e340847f65.png">
    """.format(str(data)),
                       'html', 'utf-8')  # 正文
    message['From'] = Header("robot_hao", 'ascii')  # 发件人名字
    message['To'] = Header("测试", 'utf-8')

    subject = '{}'.format(em_name)  # 邮件名字
    message['Subject'] = Header(subject, 'ascii')

    server = smtplib.SMTP_SSL(mail_host, 465)  # SMTP协议默认端口是25
    server.set_debuglevel(1)
    server.login(mail_user, mail_pass)
    server.sendmail(sender, receivers, str(message))
    server.quit()
    print("邮件发送成功", QQ_num, data)


iemail(QQ_num="1474121785@qq.com", data="Dear Xinzhi love you", em_name="可爱的家园人")
