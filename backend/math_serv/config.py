import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'my_precious_secret_key')
    DEBUG = os.getenv('DEBUG', False)
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = os.getenv("SQLALCHEMY_TRACK_MODIFICATIONS", False)
    CELERY_BROKER_URL = os.getenv("CELERY_BROKER_URL")
    CELERY_IMPORTS = ("backend.math_serv.tasks",)
    RESULT_BACKEND = os.getenv('RESULT_BACKEND')
    CALLBACK_URL = os.getenv('CALLBACK_URL')

callback_url = Config.CALLBACK_URL