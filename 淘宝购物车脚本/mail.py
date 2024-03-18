import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

def sendMail(mail_content,recv_address):
    # param mail_content 邮件内容
    # param recv_address 接收邮箱
    sender_address = 'jdsxjh@gmail.com'
    sender_pass = 'lfxxykidvtrkouaf'
    # 怎么申请应用密码可以往下看
    message = MIMEMultipart() #message结构体初始化
    message['From'] = sender_address #你自己的邮箱
    message['To'] = recv_address #要发送邮件的邮箱
    message['Subject'] = 'taobao提醒'
    # mail_content,发送内容,这个内容可以自定义,'plain'表示文本格式
    message.attach(MIMEText(mail_content,'plain'))
    # 这里是smtp网站的连接,可以通过谷歌邮箱查看,步骤请看下边
    session = smtplib.SMTP('smtp.gmail.com',587)
    # 连接tls
    session.starttls()
    # 登陆邮箱
    session.login(sender_address,sender_pass)
    # message结构体内容传递给text,变量名可以自定义
    text = message.as_string()
    # 主要功能,发送邮件
    session.sendmail(sender_address,recv_address,text)
    # 打印显示发送成功
    print("send {} successfully".format(recv_address))
    # 关闭连接
    session.quit()