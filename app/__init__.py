import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restx import Api
from flask_jwt_extended import JWTManager
from .db_manager import Db_manager

from .routes.hello_routes import hello_ns

from datetime import timedelta

api = Api()
# db = Db_manager().get_db()
migrate = Migrate()
jwt = JWTManager()

def create_app():
    app = Flask(__name__)
    # app.config["SQLALCHEMY_DATABASE_URI"] = os.environ["SQLALCHEMY_DATABASE_URI"]

    api.init_app(app)
    # db.init_app(app)
    # migrate.init_app(app, db)

    jwt.init_app(app)
    # app.config['JWT_SECRET_KEY'] = os.environ['JWT_SECRET_KEY']
    # app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(minutes=30)
    # app.config["JWT_REFRESH_TOKEN_EXPIRES"] = timedelta(hours=1)

    api.add_namespace(hello_ns)

    return app   