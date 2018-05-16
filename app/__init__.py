# app/__init__.py

from flask_api import FlaskAPI
from flask_sqlalchemy import SQLAlchemy
#from flask_migrate import Migrate
#from app import models


# local imports
from instance.config import app_config

# initialize sql-alchemy
db = SQLAlchemy()

def create_app(config_name):
    app = FlaskAPI(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    #migrate = Migrate(app, db)
    

    # # temporary route 
    # @app.route('/')
    # def hello_world():
    #     return 'Hello world guys'

    return app

