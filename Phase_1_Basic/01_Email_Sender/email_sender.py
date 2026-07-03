"""
Project 1: Email Sender
External Requirements: Google Account, App Password (Security -> 2-Step Verification -> App Passwords)
"""
from email.message import EmailMessage
import smtplib
import ssl

email_sender = 'your_email@gmail.com'
email_password = 'your_app_password'
email_receiver = 'receiver@example.com'
subject = 'Test Subject'
body = 'Test Body'

em = EmailMessage()
em['From'], em['To'], em['Subject'] = email_sender, email_receiver, subject
em.set_content(body)

context = ssl.create_default_context()
# To test, uncomment the lines below:
# with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
#     smtp.login(email_sender, email_password)
#     smtp.sendmail(email_sender, email_receiver, em.as_string())
