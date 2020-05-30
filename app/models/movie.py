from app import db
from .base import Base
from .helpers import ModelHelpers


class Movie(Base, ModelHelpers):
    """Movies model."""

    __tablename__ = 'movies'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), unique=True)
    desc = db.Column(db.String(250))
    release_date = db.Column(db.String(120))
    actors = db.relationship('Actor', backref='movies', lazy=True)

    def __init__(self, title, desc, release_date):
        self.title = title
        self.desc = desc
        self.release_date = release_date

    def to_json(self):
        return {
            'id': self.id,
            'title': self.title,
            'desc': self.desc,
            'release_date': self.release_date
        }

    def __repr__(self):
        return f'<Movie {self.title}>'
