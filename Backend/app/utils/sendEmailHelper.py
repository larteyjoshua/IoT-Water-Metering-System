import sendgrid
import os
from sendgrid.helpers.mail import Mail, Email, To, Content
from app.utils.config import settings

def sendMail(emails:str, message: str, subject: str):
    sg = sendgrid.SendGridAPIClient(api_key=settings.SENDGRID_APIKEY)
    from_email = Email("larteyjoshua@gmail.com")  # Change to your verified sender
    to_email = To(emails)  # Change to your recipient
    content = Content("text/html", message)
    mail = Mail(from_email, to_email, subject, content)

    # Get a JSON-ready representation of the Mail object
    mail_json = mail.get()

    # Send an HTTP POST request to /mail/send
    response = sg.client.mail.send.post(request_body=mail_json)
    return response