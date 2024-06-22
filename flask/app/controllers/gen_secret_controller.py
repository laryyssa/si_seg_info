from datetime import datetime
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes
from app.models.secrets_model import Secrets
from app.extensions import db
import uuid

def create_secret(signing_key: str, raw: str) -> Secrets:
    key = signing_key.encode('utf-8')
    
    iv = get_random_bytes(16)
    
    cipher = AES.new(key, AES.MODE_CBC, iv)
    
    padded_data = pad(raw.encode('utf-8'), AES.block_size)
    
    encrypted_data = cipher.encrypt(padded_data)
    
    encrypted_content = iv + encrypted_data
    
    new_secret = Secrets(
        key_id=uuid.uuid4(),
        created_at=datetime.now(),
        raw=encrypted_content.hex()
    )
    
    db.session.add(new_secret)
    db.session.commit()
    
    return new_secret
