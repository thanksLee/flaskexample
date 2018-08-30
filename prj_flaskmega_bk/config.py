import os
basedir = os.path.abspath(os.path.dirname(__file__))

WTF_CSRF_ENABLED=True
SECRET_KEY="1234567890abcdefghijklmnopqrstuvwxyz!@#$%^&*()_+"

OPENID_PROVIDERS = [
    {'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id'},
    {'name': 'Yahoo', 'url': 'https://me.yahoo.com'},
    {'name': 'AOL', 'url': 'http://openid.aol.com/<username>'},
    {'name': 'Flickr', 'url': 'http://www.flickr.com/<username>'},
    {'name': 'MyOpenID', 'url': 'https://www.myopenid.com'}]


SQLALCHEMY_DATABASE_URI="mysql+pymysql://devpythontest:Devpythontest0!@localhost:3306/dev_pythontest_db?charset=utf8"
SQLALCHEMY_MIGRATE_REPO=os.path.join(basedir, "db_repository")
SQLALCHEMY_ECHO=True
SQLALCHEMY_TRACK_MODIFICATIONS=True
