from app import db

from sqlalchemy.dialects.postgresql import UUID
import uuid

class Keys(db.Model):

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    email = db.Column(db.String(50), nullable=False)
    date = db.Column(db.DateTime, nullable=False)

    def __str__(self): 
        return f"id {self.id}, email ({self.email}), registered on {self.date}"