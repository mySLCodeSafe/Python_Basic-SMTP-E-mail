#! /usr/bin/python
# Author: ShamiLakhani@hotmail.com
# Version:  0.1 - Draft.
# Objective: Example on how to send a basic level e-mail through Python. 

import smtplib
sender = "<info@welcometothejungle.com>"
receivers = "<someone@gmail.com>"

message = """From: <info@welcometothejungle.com>
To: <someone@gmail.com>
Subject: Info from the wild Jungle !
Hello - its a retail jungle out there.
"""
try:
   smtpObj = smtplib.SMTP('smtp.mailgun.org', 25)
   smtpObj.login('postmaster@welcometothejungle.com','password')
   smtpObj.sendmail(sender, receivers, message)   
   print (sender, receivers, message)      
   print ("Successfully sent email")
   smtpObj.close()
except SMTPException:
   print ("Error: unable to send email")
   smtpObj.close()