from app.models.keys_model import Keys, db

from datetime import datetime
from hashlib import sha256
import uuid
from sqlalchemy import insert

def insert_key_data(email, date):
    id = str(uuid.uuid4())
    
    key = Keys(
        id = id,
        email = email,
        date = date
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
    input_str = email + date.strftime('%Y-%m-%d %H:%M:%S')
    token = sha256(input_str.encode('utf-8')).hexdigest()
    
    return token
    

def get_data(email):
    date = datetime.now()
    token = create_token(email, date)
    
    insert_key_data(email, date)
    
    id = get_id(email, date)

    response = {
        "key_id": token,
        "id": id
    }

    return response