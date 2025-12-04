# Author:Yi Sun(Tim) 2023-8-30

'''Automation Test Report'''

import unittest
# from HTMLTestRunner import HTMLTestRunner
from htmltestreport import HTMLTestReport
import time
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.header import Header
import subprocess

class send_report_ui:
    def new_report_ui(test_report):
        lists = os.listdir(test_report)
        lists.sort(key=lambda fn: os.path.getmtime(test_report + '\\' + fn))
        file_new = os.path.join(test_report, lists[-1])
        print(file_new)
        return file_new

    def send_mail_ui(file_new):
        with open(file_new, 'rb') as f:
            mail_body = f.read()

        sender = 'aa@ecogaragedoors.com'
        # receiver = 'aa@ecogaragedoors.com'
        receiver = ['aa@ecogaragedoors.com', 'bb@ecogaragedoors.com']
        subject = 'UI Automation Test Report for EGD'
        '''mail body'''
        msg = MIMEMultipart('mixed')
        msg_html1 = MIMEText(
            'Automation Test starts at 18:00 everyday, and the Report automatically sent,DO NOT reply.You can check details from the attachment,thank you!')
        msg.attach(msg_html1)
        '''mail attachement'''
        m = MIMEText(mail_body, "html", "utf-8")
        m["Content-Type"] = "application/octet-stream"
        m["Content-Disposition"] = "attachment;filename = UI_Automation_Test_Report for EGD Dev.html"
        msg.attach(m)
        msg['From'] = sender
        # msg['To'] = receiver
        msg['To'] = ";".join(receiver)
        msg['Subject'] = subject

        try:
            smtpserver = 'smtp.gmail.com'
            smtp = smtplib.SMTP(smtpserver, 587)
            smtp.ehlo()
            smtp.starttls()
            print('Connected to SMTP server successfully!')
            user = 'aa@ecogaragedoors.com'
            password = 'aabb'
            smtp.login(user, password)
            print('Start to send')
            smtp.sendmail(sender, receiver, msg.as_string())
            print('Mail send out, well done!')
            smtp.quit()
        except smtplib.SMTPException as e:
            print('Mail send error', e)

    def disconnect_wifi():
                try:
                    subprocess.run(["netsh", "wlan", "disconnect"], check=True)
                    print("WiFi disconnected")
                except subprocess.CalledProcessError as e:
                    print(f"error: {e}")

if __name__ == "__main__":
    test_dir_ui = "C:\\Users\\Yi Sun\\PycharmProjects\\EGD\\UITestCase"
    test_report_ui = "C:\\Users\\Yi Sun\\PycharmProjects\\EGD\\Report\\UI"

    discover = unittest.defaultTestLoader.discover(test_dir_ui, pattern='test_*.py')
    now = time.strftime("%Y-%m-%d_%H_%M_%S")
    filename1 = test_report_ui + '\\' + now + '_result.html'

    k = 1
    while k < 2:
        timing = time.strftime('%H_%M',time.localtime(time.time()))
        if timing == '18_00':
            print('start to run automation test')
            runner = HTMLTestReport(file_path=filename1, title='EGD_Dev_UI_Automation_Test_Report',
                                    description='Automation Test starts at 18:00 everyday, and the Report automatically '
                                                'sent,DO NOT reply.You can check details from the attachment,thank you!')
            runner.run(discover)
            print('finish running automation test')
            break
        else:
            time.sleep(60)  # check every 60 sec
            print(timing)

    new_report1 = send_report_ui.new_report_ui(test_report_ui)
    send_report_ui.send_mail_ui(new_report1)
    send_report_ui.disconnect_wifi()
