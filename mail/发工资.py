from openpyxl import load_workbook
import smtplib
from email.mime.text import MIMEText
from email.header import Header
import os
from email.utils import formataddr

path=os.path.join(os.path.dirname(os.path.abspath(__file__)),'2.xlsx')
wb=load_workbook(path)
ws=wb['Sheet1']

count=0
table_col_html="<thead>"
for row in ws:
    smtp_obj=smtplib.SMTP_SSL('smtp.qq.com',465)
    smtp_obj.login('1281545400@qq.com','qzgiebdeoprmhfgc')
    row_text=''
    count+=1
    if count==1:   
        for col in row:
            table_col_html+=f"<th>{col.value}</th>"
        table_col_html+="</thead>"
    else:
        row_text='<tr>'
        for cell in row:
            row_text+=f'<td>{cell.value}</td>'
        row_text+="</tr>"
        name=row[0].value
        addr=row[3].value
        mail_body_context=f'''
            <table border="1px solid black">
            {table_col_html}
            {row_text}
            </table>
        '''
        msg=MIMEText(mail_body_context,'html','utf-8')
        msg['From']=formataddr(('二年级年级组','1281545400@qq.com'))
        msg['To']=formataddr((f'{name}',addr))
        msg['subject']=Header('二年级成绩','utf-8')
        smtp_obj.sendmail('1281545400@qq.com',[addr],msg.as_string())
        print('发送成功')
        smtp_obj.quit()

     
