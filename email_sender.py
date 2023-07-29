#!/usr/bin/python3
from email.message import EmailMessage 
import ssl
import smtplib  

def create_mail(sender, password, receiver, subject, body ):
    mess= EmailMessage()
    mess['From']= sender
    mess['To']= receiver
    mess['Subject']= subject
    mess.set_content(body)

    context= ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(sender, password)
        smtp.sendmail(sender, receiver, mess.as_string())

if __name__  == "__main__":
    email_sender= ""
    email_receiver= ""
    email_password= ""
    email_subject= ""
    email_body= ""
    create_mail(email_sender, email_password, email_receiver, email_subject, email_body)