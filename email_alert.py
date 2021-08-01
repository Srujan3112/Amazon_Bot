import smtplib
import config
class EmailAlert(object):
    def __init__(self,subject,msg):
        self.subject=subject
        self.msg=msg

    def send_email(self):
        try:
            server = smtplib.SMTP('smtp.gmail.com:587')
            server.ehlo()
            server.starttls()
            server.login(config_email.EMAIL_ADDRESS, config_email.EMAIL_PASSWORD)
            message = 'Subject :{} \n\n{}'.format(self.subject, self.msg)
            server.sendmail(config_email.EMAIL_ADDRESS, config_email.EMAIL_ADDRESS, message)
            server.quit()
            print("Success: Email sent ")
        except:
            print("Failed to send email")

