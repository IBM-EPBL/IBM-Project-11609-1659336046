import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail


def sendgrid(To_Address):

    message = Mail(
        from_email='jagadeeshpoy08@gmail.com',
        to_emails=To_Address,
        subject='Sending with Twilio SendGrid is Fun',
        html_content='<strong>and easy to do anywhere, even with Python</strong>')
    try:
        sg = SendGridAPIClient(os.environ.get(
            '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'))
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(e.message)
