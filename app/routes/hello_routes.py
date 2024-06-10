from flask import request
from flask_restx import Resource
from app.routes.declare_namespace import hello_ns

import app.controllers.hello_controller as hello_controller

@hello_ns.route("/")
class Hello(Resource):
    def get(self):
        response = hello_controller.get_data()
        return response