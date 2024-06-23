from datetime import datetime
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes
from app.models.secrets_model import Secrets
from app.extensions import db

def create_secret(signing_key: str, raw: str, key_id: str) -> Secrets:
    key = signing_key.encode('utf-8')
    
    iv = get_random_bytes(16)
    
    cipher = AES.new(key, AES.MODE_CBC, iv)
    
    padded_data = pad(raw.encode('utf-8'), AES.block_size)
    
    encrypted_data = cipher.encrypt(padded_data)
    
    encrypted_content = iv + encrypted_data
    
    new_secret = Secrets(
        key_id=key_id,
        created_at=datetime.now(),
        raw=encrypted_content.hex()
    )
    
    db.session.add(new_secret)
    db.session.commit()
    
    return new_secret

def update_secret(signing_key: str, raw: str, key_id: str) -> Secrets:
    secret = Secrets.query.filter_by(key_id=key_id).first()
    if not secret:
        raise ValueError("Secret não encontrado ou não existe")

    # Criptografar os dados novos
    key = signing_key.encode('utf-8')
    iv = bytes.fromhex(secret.raw[:32])  # Usar o IV existente
    cipher = AES.new(key, AES.MODE_CBC, iv)
    padded_data = pad(raw.encode('utf-8'), AES.block_size)
    encrypted_data = cipher.encrypt(padded_data)
    encrypted_content = iv.hex() + encrypted_data.hex()

    secret.raw = encrypted_content
    secret.created_at = datetime.now()  # Atualizar a data de modificação
    db.session.commit()

    return secret

