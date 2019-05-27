#!/usr/bin/python
# -*- coding: UTF-8 -*-

from smtplib import SMTP
from email.header import Header
from email.mime.text import MIMEText

def main():
    sender = '66666@qq.com'
    receivers = ['99999@163.com']
    message = MIMEText('用python发送邮件的示例代码', 'plain', 'utf-8')
    message['From'] = Header('枯木逢春', 'utf-8')
    message['To']   = Header('暖意洋洋', 'utf-8')
    message['Subject'] = Header('示例代码实验邮件', 'utf-8')
    #该处要根据发送邮件是啥邮件来设置
    smtper = SMTP('smtp.qq.com')
    #该secretpass不是邮箱登录密码，是开启pop/smtp设置的一个客户端授权码
    smtper.login(sender, 'secretpass')
    smtper.sendmail(sender, receivers, message.as_string())
    print('邮件发送完成')

if __name__ == '__main__':
    main()

