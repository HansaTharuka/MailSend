import smtplib

#import config

EMAIL_ADDRESS = "moratechknights@gmail.com"
PASSWORD = "123Techknights456"

def send_email(subject, msg):
    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(EMAIL_ADDRESS, PASSWORD)
        message = 'Subject: {}\n\n{}'.format(subject, msg)
        server.sendmail(EMAIL_ADDRESS, EMAIL_ADDRESS, message)
        server.quit()
        print("Success: Email sent!")
    except:
        print("Email failed to send.")


subject = "Test subject"
msg = "Hello there, how are you today?"

send_email(subject, msg)