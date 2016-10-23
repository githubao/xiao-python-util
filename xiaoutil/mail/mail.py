# -*- coding: utf-8 -*-
__author__ = 'BaoQiang'

import smtplib
import time
import traceback
from email.header import Header
from email import encoders
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.utils import parseaddr, formataddr

"""
发送邮件
"""

# from_address = "anno_bar@163.com"
# # password = "Turn1234"
# auth_code = "anno1234"
# smtp_server = "smtp.163.com"

# from_address = "baoqiang@uzoo.cn"
# auth_code = "Fullengage2"
# smtp_server = "smtp.exmail.qq.com"

from_address = "anno_bar@sina.com"
auth_code = "Turn1234"
smtp_server = "smtp.sina.com"

to_address = []

mail_subject = "这是一封邮件"
mail_text = """
很抱歉对您的打扰，108U，108#{种子}，108#{电影}。<br><br>
有意，请扫二维码,加微信好友。<br><br>
<html><body><p><img src="cid:0"></p> </body></html>'<br><br>
***此邮件由Python程序自动发出，再次申明，如果对您有任何打扰，深感抱歉。***
"""

server = smtplib.SMTP(smtp_server, 25)


def login():
    # server.set_debuglevel(1)
    server.login(from_address, auth_code)


def send_mail():
    msg = MIMEMultipart()

    msg.attach(MIMEText(mail_text, 'html', 'utf-8'))
    # msg['From'] = format_address(u'匿名者 <%s>' % from_address)
    msg['From'] = format_address(u'匿名者 <%s>' % from_address)
    msg['To'] = format_address(u'亲爱的 <%s>' % to_address)
    msg['Subject'] = Header(mail_subject, 'utf-8').encode()

    add_jpg(msg)

    server.sendmail(from_address, to_address, msg.as_string())


def add_jpg(msg):
    with open('D:\\mnt\\others\\resources\\qrcode.png', 'rb') as f:
        # 设置附件的MIME和文件名，这里是png类型:
        mime = MIMEBase('image', 'png', filename='qrcode.png')
        # 加上必要的头信息:
        mime.add_header('Content-Disposition', 'attachment', filename='test.png')
        mime.add_header('Content-ID', '<0>')
        mime.add_header('X-Attachment-Id', '0')
        # 把附件的内容读进来:
        mime.set_payload(f.read())
        # 用Base64编码:
        encoders.encode_base64(mime)
        # 添加到MIMEMultipart:
        msg.attach(mime)


def logout():
    server.quit()


def format_address(s):
    name, address = parseaddr(s)
    return formataddr((
        Header(name, 'utf-8').encode(),
        address))


def send_list():
    login()

    f_w = open("D:\\mnt\\others\\resources\\mail-fail-list.txt", "a")
    f_w.write("*" * 50 + "\n" + time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())) + "\n")

    count = 0
    with open("D:\\mnt\\others\\resources\\mail-to-list.txt") as f:
        mail = f.readline().strip("\n")

        while True:
            if mail.startswith("#"):
                mail = f.readline().strip("\n")
                continue

            to_address.append(mail)

            try:
                send_mail()
                time.sleep(2)
                f_w.write(str(to_address).strip("[").strip("]") + "\t success!\n")
                count += 1
            except Exception as e:
                print(e)
                traceback.print_exc()
                f_w.write(str(to_address).strip("[").strip("]") + "\t is reject!\n")
                time.sleep(5)

            to_address.clear()
            mail = f.readline().strip("\n")

            if not mail:
                break

    f_w.write("[" + str(count) + "] succeed\n")
    f_w.close()

    logout()


if __name__ == "__main__":
    send_list()
