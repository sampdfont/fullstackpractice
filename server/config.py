from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__) # tells the execution that this is the main point of entry
CORS(app) # wraps the app in cors for different uris to connect

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///mydatabase.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app) # create instance of sqlalchemy - with the objects already in app - for the db