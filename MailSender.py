# i have imported the os module so you can import your email and appPassword with environmental variables
import os;
import smtplib;
import MailList
count = 0
topcount = len(MailList.list)
subject = raw_input('The Subject you want >  ')
message = raw_input('The message you want to send > ')
while (count != topcount):
    print(MailList.list[count])
    Address = 'set this to your email address'
    Password = 'set this to your email appPassword you cant find that here https://myaccount.google.com/apppasswords '
    port = smtplib.SMTP('smtp.gmail.com' , 587)
    port.ehlo()
    port.starttls()
    port.ehlo()
    port.login(Address, Password)
    msg = 'Subject: {}\n\n{}'.format(subject, message)
    port.sendmail(Address, MailList.list[count], msg)
    port.close()
    count = count + 1
