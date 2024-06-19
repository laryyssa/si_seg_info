from flask import request
from flask_restx import Resource
from app.routes.declare_namespace import v1_ns

import app.controllers.get_secrets_controller as get_secrets_controller

@v1_ns.route("/secrets")
class Hello(Resource):
    def get(self):
        response = get_secrets_controller.get_data()
        return response