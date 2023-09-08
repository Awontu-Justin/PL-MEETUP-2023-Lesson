from email.message import EmailMessage
import ssl
import smtplib
"""This is a pytrhon script that permit us to send an email"""
email_sender='justinawontu@gmail.com'
email_password='trdewfrqbdssfyxm'
email_receiver='wawah66707@vikinoko.com'
subject='Welcome to PL-MEETUP-2023'
body='''Please do well to attend all classes scheduled by your mentor and don't forget to do all your assignments
thank you all'''
em=EmailMessage() #Creates an instance of message
em['FROM']=email_sender#specifies source
em['TO']=email_receiver#specifies destination
em['SUBJECT']=subject
em.set_content(body)
context=ssl.create_default_context()
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
  smtp.login(email_sender,email_password)
  smtp.sendmail(email_sender, email_receiver, em.as_string())