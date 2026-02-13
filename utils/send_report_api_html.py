# Author:Yi Sun(Tim) 2022-9-07

'''Automation Test Report'''

import unittest
from HTMLTestRunner import HTMLTestRunner
import time
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.header import Header

def new_report(test_report):
    lists = os.listdir(test_report)
    lists.sort(key=lambda fn: os.path.getmtime(test_report + '\\' + fn))
    file_new = os.path.join(test_report, lists[-1])
    print(file_new)
    return file_new

def send_mail(file_new):
    with open(file_new, 'rb') as f:
        mail_body = f.read()

    sender = 'aa@ecogaragedoors.com'
    # receiver = 'aa@ecogaragedoors.com'
    receiver = ['aa@ecogaragedoors.com', 'bb@ecogaragedoors.com']
    subject = 'Automation API Test Report for EGD'
    '''mail body'''
    msg = MIMEMultipart('mixed')
    msg_html1 = MIMEText(mail_body, 'html', 'utf-8')
    msg.attach(msg_html1)
    '''mail attachement'''
    m = MIMEText(mail_body, "html", "utf-8")
    m["Content-Type"] = "application/octet-stream"
    m["Content-Disposition"] = "attachment;filename = Automation_API_Test_Report for EGD.html"
    msg.attach(m)
    msg['From'] = sender
    msg['To'] = receiver
    # msg['To'] = ";".join(receiver)
    msg['Subject'] = subject

    try:
        smtpserver = 'smtp.office365.com'
        smtp = smtplib.SMTP(smtpserver, 587)
        smtp.ehlo()
        smtp.starttls()
        user = 'aa@ecogaragedoors.com'
        password = 'aabb'
        smtp.login(user, password)
        print('Start to send')
        smtp.sendmail(sender, receiver, msg.as_string())
        print('Mail send out, well done!')
        smtp.quit()
    except smtplib.SMTPException:
        print('Mail send error')

if __name__ == "__main__":
    test_dir_ui = "xxxx\\APITestCase"
    test_report_ui = "xxxx\\Report"
    discover = unittest.defaultTestLoader.discover(test_dir_api, pattern='test_*.py')
    now = time.strftime("%Y-%m-%d_%H_%M_%S")
    filename = test_report_api + '\\' + now + '_result.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner(stream=fp, title='EGD_Automation_API_Test_Report',
                            description='''
                            API Automation Test Report automatically sends everyday,DO NOT reply.
                            You can check details from the attachment,thank you!''')
    runner.run(discover)
    fp.close()
    new_report1 = new_report(test_report_api)
    send_mail(new_report1)

