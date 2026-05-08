import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.utils import formataddr

# 连接服务器
smtp_obj = smtplib.SMTP_SSL('smtp.qq.com', 465)
smtp_obj.login('1281545400@qq.com', 'qzgiebdeoprmhfgc')  # 确保授权码正确！

# 构建邮件
msg = MIMEText('Hello', 'plain', 'utf-8')

# 关键修正：使用 formataddr 规范格式化 From/To 头
msg['From'] = formataddr(('你知道的', '1281545400@qq.com'))  # 自动处理编码和格式
msg['To'] = formataddr(('有缘人', '3554860748@qq.com'))
msg['Subject'] = Header('一封信', 'utf-8').encode()

# 发送邮件（注意收件人地址必须与 msg['To'] 中的实际地址一致）
smtp_obj.sendmail('1281545400@qq.com', ['3554860748@qq.com'], msg.as_string())
smtp_obj.quit()