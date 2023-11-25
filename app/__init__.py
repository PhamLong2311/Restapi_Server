from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager
from flask_oauthlib.provider import OAuth2Provider
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
  pass


app = Flask(__name__)
oauth=OAuth2Provider(app)
@app.route('/')
def home():
    return '<div style="text-align: center; font-size: 24px;">Hello!</div>'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users_sql.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'your_jwt_secret_key'
app.config['OAUTH2_PROVIDER_ERROR_ENDPOINT']='oauth/error'
app.config['OAUTH2_PROVIDER_TOKEN_EXPRIES_IN']=3600
app.app_context().push()
api = Api(app)
jwt = JWTManager(app)
db = SQLAlchemy(model_class=Base)
oauth.init_app(app)
db.init_app(app)

from app.user import *

api.add_resource(UserRegistration, '/register')
api.add_resource(UserLogin, '/login')
api.add_resource(ProtectedResource, '/protected')
api.add_resource(GetUser, '/user')
  

