import os

basedir = os.path.abspath(os.path.dirname(__name__))

class Config:
    # create your own .env file to match what's here
    FLASK_APP = os.environ.get('FLASK_APP') #app (or run.py if using shell context processors)
    FLASK_DEBUG = os.environ.get('FLASK_DEBUG') #bool True
    SECRET_KEY = os.environ.get('SECRET_KEY')
    # see README for directions on creating a database with correct structure
    # production DB uri will only be shared at the discretion of CTA instructors
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
