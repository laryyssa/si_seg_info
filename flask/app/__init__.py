import os

from flask import Flask, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from flask_restx import Api

from .extensions import db

from .routes.v1_routes import v1_ns

api = Api(doc="/docs")

def create_app():
    app = Flask(__name__)

    app.route("/")(lambda : handle_static_files())

    
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://{username}:{password}@{host}:{port}/{database}'.format(
            username=os.environ['RDS_USERNAME'],
            password=os.environ['RDS_PASSWORD'],
            host=os.environ['RDS_HOSTNAME'],
            port=os.environ['RDS_PORT'],
            database=os.environ['RDS_DB_NAME'],
        )
    


    db.init_app(app)
    api.init_app(app)


    api.add_namespace(v1_ns)

    return app   


def handle_static_files():
    return send_from_directory("static", "index.html")