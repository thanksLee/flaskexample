import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get("SECERT_KEY") or "1234567890!@#$%^&*()abcdefghijklmnopqrstuvwxyz"
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL") or "mysql+pymysql://devpythontest:Devpythontest0!@localhost:3306/dev_pythontest_db?charset=utf8"
    SQLALCHEMY_ECHO=True
    SQLALCHEMY_TRACK_MODIFICATIONS=False
