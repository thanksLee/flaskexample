import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get("SECERT_KEY") or "1234567890!@#$%^&*()abcdefghijklmnopqrstuvwxyz"
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL") or "mysql+pymysql://devpythontest:Devpythontest0!@localhost:3306/dev_pythontest_db?charset=utf8"
    SQLALCHEMY_ECHO=True
    SQLALCHEMY_TRACK_MODIFICATIONS=False

    MAIL_SERVER = os.environ.get("MAIL_SERVER")
    MAIL_PORT = int(os.environ.get("MAIL_PORT") or 25)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    ADMINS = ["dmzone75@gmail.com"]

    POSTS_PER_PAGE=10

    LANGUAGES = ["en", "es"]

    MS_TRANSLATOR_KEY = os.environ.get('MS_TRANSLATOR_KEY')