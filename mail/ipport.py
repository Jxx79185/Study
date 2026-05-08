import smtplib
from email.mime.text import MIMEText
from email.header import Header

smtp_obj=smtplib.SMTP_SSL('smtp.exmail.qq.com',465)
smtp_obj.iogin('1281545400@qq.com','xxawd418ds')

msg=MIMEText('Hello')
msg['From']=Header('你知道的','utf-8')
msg['To']=Header('有缘人','utf-8')
msg['subject']=Header('一封信','utf-8')

smtp_obj.sendmail('1281545400@qq.com','56128745@qq.com',msg.as_string())