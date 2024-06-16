from flask import Flask
from app import create_app, db

from app.models.keys_model import Keys
from app.models.secrets_model import Secrets

app = create_app()

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")