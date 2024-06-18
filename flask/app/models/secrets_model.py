from app.extensions import db

from sqlalchemy.dialects.postgresql import UUID
import uuid

class Secrets(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    key_id = db.Column(UUID(as_uuid=True), nullable=False, default=uuid.uuid4)
    created_at = db.Column(db.DateTime, nullable=False)
    raw = db.Column(db.String(1000), nullable=False)

    # def __str__(self): 
    #     return f"id {self.id}, key_id ({self.key_id}), registered on {self.created_at}, raw: {raw}"