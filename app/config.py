import os
from dotenv import load_dotenv

# import env
load_dotenv()

class Config:
    PORT = os.environ.get("PORT")
    EMAIL = os.environ.get("EMAIL")
    DB_URI = os.environ.get('DB_URL')
    SMTP_HOST = os.environ.get('SMTP_HOST')
    SMTP_PORT = os.environ.get('SMTP_PORT')
    SMTP_LOGIN = os.environ.get('SMTP_LOGIN')
    SMTP_PASSWORD = os.environ.get('SMTP_PASSWORD')
    SMTP_EMAIL = os.environ.get('SMTP_EMAIL')
    SMTP_NAME = os.environ.get('SMTP_NAME')
    
