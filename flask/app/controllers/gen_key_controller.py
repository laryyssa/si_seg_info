from app.models.keys_model import Keys, db

from datetime import datetime
from hashlib import sha256
from sqlalchemy import insert

def insert_key_data(email, time):
    key = Keys(
        email = email,
        date = time
    )

    db.session.add(key)
    db.session.commit()

def get_key_data(token):
    query = Keys.query.with_entities(Keys.id).all()


def create_token(email, time):
    token = sha256(email+time.encode('utf-8')).hexdigest()
    
    return token
    

def get_data(email):
    time = datetime.now()
    token = create_token(email, time)
    
    insert_key_data(token, email)
    get_data(email, time)

    return True