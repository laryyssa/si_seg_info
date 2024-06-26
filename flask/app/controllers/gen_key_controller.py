from app.models.keys_model import Keys, db
from datetime import datetime
import uuid
import secrets
from Crypto.Hash import SHA256
import base64
import random

DEFAULT_TOKEN_LENGTH = 32

def insert_key_data(email, date):
    id = str(uuid.uuid4())

    key = Keys(
        id=id,
        email=email,
        date=date
    )

    db.session.add(key)
    db.session.commit()

def get_id(email, date):
    query = Keys.query\
            .with_entities(Keys.id)\
            .where(
                Keys.email == email,
                Keys.date == date
            ).all()

    uuid_value = query[0][0]
    uuid_string = str(uuid_value)

    return uuid_string

def create_token(email, date):
    email_bytes = email.encode('utf-8')
    date_bytes = date.strftime('%Y-%m-%d %H:%M:%S').encode('utf-8')
    random_bytes = str(random.random()).encode('utf-8')
    
    msg_bytes = email_bytes + date_bytes + random_bytes

    sha256_hash = SHA256.new(msg_bytes).digest()

    token = base64.urlsafe_b64encode(sha256_hash).decode('utf-8')

    while len(token) < DEFAULT_TOKEN_LENGTH:
        random_bytes = secrets.token_bytes(256)
        sha256_hash = SHA256.new(random_bytes).digest()
        token += base64.urlsafe_b64encode(sha256_hash).decode('utf-8')
    return token[:DEFAULT_TOKEN_LENGTH]

def get_data(email):
    date = datetime.now()
    token = create_token(email, date)

    insert_key_data(email, date)

    id = get_id(email, date)

    response = {
        "key": token,
        "key_id": id
    }

    return response
