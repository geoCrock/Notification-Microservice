import os


class Config:
    PORT = os.getenv("PORT")
    EMAIL = os.getenv("EMAIL")
    DB_URI = os.getenv('DB_URL')
    SMTP_HOST = os.getenv('SMTP_HOST')
    SMTP_PORT = os.getenv('SMTP_PORT')
    SMTP_LOGIN = os.getenv('SMTP_LOGIN')
    SMTP_PASSWORD = os.getenv('SMTP_PASSWORD')
    SMTP_EMAIL = os.getenv('SMTP_EMAIL')
    SMTP_NAME = os.getenv('SMTP_NAME')



