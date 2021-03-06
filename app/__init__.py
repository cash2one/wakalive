from flask import Flask
from flask.ext.login import LoginManager
from flask.ext.sqlalchemy import SQLAlchemy
import os,re
from . import lecloud,leancloud

#initiate the app
app = Flask(__name__)
app.config.from_object('config')

#initiate the sqlalchemy
db = SQLAlchemy(app)

#initiate the LoginManager
login_manager = LoginManager(app)

#initiate the Lecloud
lecloud = lecloud.WakaLive(app.config['LECLOUD_USERID'],app.config['LECLOUD_SECRETKEY'])

#initiate the leancloud
leancloud = leancloud.LeanCloud(app.config['LEANCLOUD_APPID'],app.config['LEANCLOUD_APPKEY'])

from app import views,models
if not os.path.exists(app.config['SQLALCHEMY_DATABASE_PATH']):
    db.create_all()
