# Wrong

class GmailClient:
    def send_email(self, recipient, subject, body):
        pass


class EmailService:
    def __init__(self):
        self.gmail_client = GmailClient()

    def send_email(self, recipient, subject, body):
        self.gmail_client.send_email(recipient, subject, body)


# Correct

class EmailClient:
    def send_email(self, recipient, subject, body):
        pass


class GmailClient(EmailClient):
    def send_email(self, recipient, subject, body):
        pass


class OutlookClient(EmailClient):
    def send_email(self, recipient, subject, body):
        pass


class EmailService:
    def __init__(self, email_client: EmailClient):
        self.email_client = email_client

    def send_email(self, recipient, subject, body):
        self.email_client.send_email(recipient, subject, body)
