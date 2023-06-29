from dotenv import load_dotenv
import os

DEBUG = True

USERNAME = os.getenv('USERNAME')
PASSWORD = os.getenv('PASSWORD')
SERVER = os.getenv('SERVER')
DB = os.getenv('DB')
SECRET_KEY = os.getenv('SECRET_KEY')

SQLALCHEMY_DATABASE_URI = f'postgresql://{USERNAME}:{PASSWORD}@{SERVER}/{DB}'
SQLALCHEMY_TRACK_MODIFICATIONS = True
