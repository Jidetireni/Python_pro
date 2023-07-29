#!/usr/bin/python3
# This is a python script to automatically send mails  
# importing the nessecary libaries 
from email.message import EmailMessage 
import ssl
import smtplib  
import os

# defining the function with nessecary arguments for the mail 
def create_mail(sender, password, receiver, subject, body ):

    # Creating an instance for the arguments passed  
    mess= EmailMessage()
    mess['From']= sender
    mess['To']= receiver
    mess['Subject']= subject
    mess.set_content(body)

    # Create an ssl context for secure communication
    context= ssl.create_default_context()

    # Connecting SMTP server to using SSL context 
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(sender, password)
        smtp.sendmail(sender, receiver, mess.as_string())

# For security create an Environment Variable and store your passwords 
value = os.environ.get('PASSWORD')

# Assigning variables for the passed arguments and declaring the function
if __name__  == "__main__":
    email_sender= ""
    email_receiver= ""
    email_password= value
    email_subject= ""
    email_body= ""
    create_mail(email_sender, email_password, email_receiver, email_subject, email_body)