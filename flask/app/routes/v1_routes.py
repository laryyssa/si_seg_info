from flask import request
from flask_restx import Resource, fields
from app.routes.declare_namespace import v1_ns

import app.controllers.gen_key_controller as gen_key_controller
import app.controllers.get_secrets_controller as get_secrets_controller

gen_key_model = v1_ns.model('GenKeyModel', {
    'email': fields.String(required=True, description='Email do usuário')
})
@v1_ns.route("/genKey", methods=["POST","GET"])
class genKey(Resource):
    @v1_ns.expect(gen_key_model, validate=True)
    def post(self):
        data = request.get_json()

        email = data.get("email")

        response = gen_key_controller.get_data(email)
        return response

@v1_ns.route("/secrets")
class Secrets(Resource):
    def get(self):
        response = get_secrets_controller.get_data()
        return response