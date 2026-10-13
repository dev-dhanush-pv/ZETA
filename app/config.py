import os 
from dotenv import load_dotenv

load_dotenv()

class Config:
    db_user = os.getenv('DB_USER')
    db_port = os.getenv('DB_PORT')
    db_name = os.getenv('DB_NAME')
    db_host = os.getenv('DB_HOST')
    db_password = os.getenv('DB_PASSWORD')

    SQLALCHEMY_DATABASE_URI = f"mysql+mysqlconnector://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SECRET_KEY = os.getenv('FLASK_SECRET_KEY')