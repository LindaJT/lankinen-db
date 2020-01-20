from flask import Flask
app = Flask(__name__)

from flask_sqlalchemy import SQLAlchemy
app.config["SQLALCHEMY_DATABASE_URI"] = "sqllite:///dbs.db"
app.config["SQLALCHEMY_ECHO"] = True

db = SQLAlchemy(app)

from src import views

from src.databases import models
from src.databases import views

db.create_all()