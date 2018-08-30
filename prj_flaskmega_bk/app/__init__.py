from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config[]
app.config.from_object("config")
db = SQLAlchemy(app)

from app.views import views
from app.models import models
