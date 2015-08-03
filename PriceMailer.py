__author__ = 'igorchtivelband'
import smtplib
from email.mime.text import MIMEText

def sendPriceEmail(price,target_email,smtp_server,smtp_port,smtp_user,smtp_pwd):
    msg = MIMEText("Hurry up, book your flight")
    msg['Subject'] = "A flight with price "+price+" was found"
    msg['From'] = "do_not_reply@gmail.com"
    msg['To'] = target_email
    debuglevel = True
    mail = smtplib.SMTP(smtp_server, smtp_port)
    mail.set_debuglevel(debuglevel)
    mail.starttls()
    mail.login(smtp_user, smtp_pwd)
    mail.sendmail('do_not_reply@gmail.com', target_email, msg.as_string())
    mail.quit()
