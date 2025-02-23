import os

class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'postgresql://postgres:04048922@localhost/lolApidb')
    SECRET_KEY = os.environ.get('SECRET_KEY', 'mysecretkey')

