import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_email(subject, content, email_address, password):
    from_addr = email_address
    to_addr = email_address
    msg = MIMEMultipart()
    msg['From'] = from_addr
    msg['To'] = to_addr
    msg['Subject'] = subject

    msg.attach(MIMEText(content, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(from_addr, password)
    text = msg.as_string()
    server.sendmail(from_addr, to_addr, text)
    server.quit()


def send_multiple_email(subject, content, from_addr, recipients_list, password):
    msg = MIMEMultipart()
    msg['From'] = from_addr
    msg['To'] = ", ".join(recipients_list)
    msg['Subject'] = subject

    msg.attach(MIMEText(content, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(from_addr, password)
    text = msg.as_string()
    server.sendmail(from_addr, recipients_list, text)
    server.quit()
