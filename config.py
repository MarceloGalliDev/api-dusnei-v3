from dotenv import load_dotenv
import os

load_dotenv()

DEBUG = True

# USERNAME = os.getenv('USERNAME')
# PASSWORD = quote_plus(os.getenv('PASSWORD'))
# SERVER = os.getenv('SERVER')
# DB = os.getenv('DB')
# SECRET_KEY = os.getenv('SECRET_KEY')
# SQLALCHEMY_DATABASE_URI = f"postgresql://{USERNAME}:{PASSWORD}@{SERVER}/{DB}"

SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')

SQLALCHEMY_TRACK_MODIFICATIONS = True

