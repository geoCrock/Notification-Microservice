import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from app.config import Config


class EmailSender:
    def __init__(self):
        self.smtp_host = Config.SMTP_HOST
        self.smtp_port = Config.SMTP_PORT
        self.smtp_login = Config.SMTP_LOGIN
        self.smtp_password = Config.SMTP_PASSWORD
        self.smtp_email = Config.SMTP_EMAIL

    def send_email(self, to_email, subject, body):
        message = MIMEMultipart()
        message["From"] = self.smtp_email
        message["To"] = to_email
        message["Subject"] = subject

        # Add body for email
        message.attach(MIMEText(body, "plain"))

        try:
            with smtplib.SMTP(self.smtp_host, self.smtp_port) as server:
                server.starttls()
                server.login(self.smtp_login, self.smtp_password)
                server.sendmail(self.smtp_email, to_email, message.as_string())
            return True
        except Exception as e:
            print(f"Error sending email: {e}")
            return False
