import smtplib
import ssl

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from notification_repository import get_notifications, update_notification


def process_email():
    list_notification = get_notifications()
    for item in list_notification:
        print(item)
        send_email(item)
        update_notification(item['_id'])
    return "ok"


def send_email(email):
    sender_email = email['Sender']  # "suporte@ingressosaqui.com"
    receiver_email = email['To']  # "roberthenrrique@gmail.com"
    password = "a1b2c3d4e7*AB"

    message = MIMEMultipart("alternative")
    message["Subject"] = email['Subject']
    message["From"] = sender_email
    message["To"] = receiver_email

    # Turn these into plain/html MIMEText objects
    part2 = MIMEText(email['Body'].replace('\r\n', ''), "html")

    # Add HTML/plain-text parts to MIMEMultipart message
    # The email client will try to render the last part first
    message.attach(part2)

    # Create secure connection with server and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.hostinger.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(
            sender_email, receiver_email, message.as_string()
        )
    return "ok"
