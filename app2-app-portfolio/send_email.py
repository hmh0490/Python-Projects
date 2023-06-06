# standard email library
import smtplib, ssl
import os


def send_email(message):
    host = "smtp.gmail.com"
    port = 465
    username = "hajni0490@gmail.com"
    # create environment variable -> only my computer stores this password
    password = os.getenv("PASSWORD")

    receiver = "hajni0490@gmail.com"
    # to send emails securely
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)

