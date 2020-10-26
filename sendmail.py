
import smtplib
import os
from email.message import EmailMessage

EMAIL_ADDRESS =  'varaprasad.achary@gmail.com'
EMAIL_PASSWORD = 'Pesi123$'

msg = EmailMessage()
msg['Subject'] = 'Wedding Invitation'
msg['From'] = EMAIL_ADDRESS
msg['To'] = 'varaachary@gmail.com'
msg.set_content('Hello, \n\n We are cordially inviting for my brother wedding!!\n\n Date: 10th Jan 2021\n\n Thanks,\n\n VaraPrasasd Achary')

with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()
    smtp.login(EMAIL_ADDRESS,EMAIL_PASSWORD)

    #subject = 'How are you Doing?'
    #body = 'I would like to meet you and discuss about very important money matters'
    #msg = f'Subject: {subject}\n\n{body}'  
    #smtp.sendmail(EMAIL_ADDRESS,'varaachary@gmail.com',msg)

    smtp.send_message(msg)