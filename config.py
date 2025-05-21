import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    if (SQLALCHEMY_DATABASE_URI):
        print("Database: ", SQLALCHEMY_DATABASE_URI)
    else:
        print("URL data not found")
