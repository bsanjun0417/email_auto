import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
from email.encoders import encode_base64 #한글깨짐방지
from email.header import Header
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart #파일첨부
from email.utils import formatdate
from email import encoders
import sqlite3


conn = sqlite3.connect('main.db')
cursor = conn.cursor()
cursor.execute('select * from email_data;')
data_list = cursor.fetchall()


nmail_id= data_list[0][1]
nmail_pw=data_list[0][2]

gmail_id = data_list[1][1]
gmail_pw = data_list[1][2]

def send1(check,to_email,title,body):
  
    if check == 'naver':
        for email in to_email:

            naver_mail(email, title, body)
    elif check == 'google':
          for email in to_email:
              g_mail(email, title, body)






def g_mail(to_email,title,body):

 
    msg = MIMEMultipart()
    msg['Subject'] = title
    msg['From'] = gmail_id
    msg['To']= to_email


    msg.attach(MIMEText(body,"plain", 'utf-8'))
    smtp = smtplib.SMTP("smtp.gmail.com",587)
    smtp.starttls()

    smtp.login(user=gmail_id,password=gmail_pw)
    smtp.sendmail(gmail_id,to_email,msg.as_string())
    smtp.close()


    


def naver_mail(to_email,title,body):
    
    msg = MIMEMultipart()
    msg['Subject'] = title
    msg['From'] = nmail_id
    msg['To']= to_email
    msg.attach(MIMEText(body,"plain", 'utf-8'))

    smtp = smtplib.SMTP("smtp.naver.com",587)
    smtp.starttls()

    smtp.login(user=nmail_id,password=nmail_pw)
    smtp.sendmail(nmail_id,to_email,msg.as_string())
    smtp.close()




def send2(check,to_email,title1,body1,path):
    if check == 'naver':
        for email in to_email:

            naver_mail2(email, title1, body1,path)
    elif check == 'google':
          for email in to_email:
              g_mail2(email, title1, body1,path)


def naver_mail2(to_email, title, body,path):
    msg = MIMEMultipart()
    msg['Subject'] = title
    msg['From'] = nmail_id
    msg['To']= to_email
    
    msg.attach(MIMEText(body,"plain", 'utf-8'))
    with open(path, "rb") as attachment:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header(
                    "Content-Disposition",
                    f"attachment; filename= {os.path.basename(path)}",
        )
        msg.attach(part)
    smtp = smtplib.SMTP("smtp.naver.com",587)
    smtp.starttls()

    smtp.login(user=nmail_id,password=nmail_pw)
    smtp.sendmail(nmail_id,to_email,msg.as_string())
    smtp.close()





def g_mail2(to_email, title, body,path):
    msg = MIMEMultipart()
    msg['Subject'] = title
    msg['From'] = gmail_id
    msg['To']= to_email
    msg.attach(MIMEText(body,"plain", 'utf-8'))
    with open(path, "rb") as attachment:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header(
                    "Content-Disposition",
                    f"attachment; filename= {os.path.basename(path)}",
        )
        msg.attach(part)

    smtp = smtplib.SMTP("smtp.gmail.com",587)
    smtp.starttls()

    smtp.login(user=gmail_id,password=gmail_pw)
    smtp.sendmail(gmail_id,to_email,msg.as_string())
    smtp.close()

