from flask import jsonify, request
from flask_restx import Resource, fields
from app.routes.declare_namespace import v1_ns

import app.controllers.gen_key_controller as gen_key_controller
import app.controllers.get_secrets_controller as get_secrets_controller
import app.controllers.gen_secret_controller as gen_secret_controller

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

gen_secret_model = v1_ns.model('GenSecretModel', {
    'key_id': fields.String(required=True, description='Id da key gerada em /genKey'),
    "raw": fields.String(required=True, description='Texto a ser criptografado')
})
@v1_ns.route("/secrets", methods=["GET", "POST"])
class Secrets(Resource):
    def get(self):
        response = get_secrets_controller.get_data() if not request.args.get("key_id") else get_secrets_controller.get_secret_by_key_id(request.args.get("key_id"))
        return jsonify(response)
    
    @v1_ns.expect(gen_secret_model, validate=True)
    def post(self):
        key = request.headers.get("key")
        if not key or key == "":
            return {"message": "Key não informada"}, 400

        data = request.get_json()
        raw = data.get("raw")

        secret = gen_secret_controller.create_secret(signing_key=key, raw=raw)
        resp = {   
            "id": str(secret.id),
            "key_id": str(secret.key_id),
            "created_at": secret.created_at.strftime("%Y-%m-%d %H:%M:%S"),
            "raw": secret.raw
        }

        return resp, 201
