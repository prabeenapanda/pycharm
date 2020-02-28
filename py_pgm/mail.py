import smtplib

sender = 'prabeena.panda@gssinfotech.com'
receivers = ['sanjib.jena@gssinfotech.com']# list is must IF Multiple rcvr write them inside a list

message = """From: From Person <from@fromdomain.com>
To: To Person <to@todomain.com>
Subject: SMTP e-mail test

This is a test e-mail message.
"""

try:
   smtpObj = smtplib.SMTP('localhost')
   smtpObj.sendmail(sender, receivers, message)
   print("Successfully sent email")
except SMTPException:
   print("Error: unable to send email")