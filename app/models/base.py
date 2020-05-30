from datetime import datetime
from app import db


class Base(db.Model):
    """Base model."""

    __abstract__ = True

    created_on = db.Column(db.DateTime, default=datetime.utcnow)
    updated_on = db.Column(db.DateTime, default=datetime.utcnow)
