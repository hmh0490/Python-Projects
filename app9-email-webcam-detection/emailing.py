import smtplib
# metadata about images
import imghdr
from email.message import EmailMessage
import os

PASSWORD = os.getenv("PASSWORD")
SENDER = "hajni0490@gmail.com"
RECEIVER = "hajni0490@gmail.com"
def send_email(image_path):
    print("emailing started")
    email_message = EmailMessage()
    email_message["Subject"] = "New customer showed up!"
    email_message.set_content("Hey, we just saw a new customer!")

    with open(image_path, "rb") as file:
        content = file.read()
    email_message.add_attachment(content, maintype="image", subtype=imghdr.what(None, content))

    gmail = smtplib.SMTP("smtp.gmail.com", 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(SENDER, PASSWORD)
    gmail.sendmail(SENDER, RECEIVER, email_message.as_string())
    gmail.quit()
    print("emailing ended")

if __name__ == "__main__":
    send_email(image_path="images/215.png")
