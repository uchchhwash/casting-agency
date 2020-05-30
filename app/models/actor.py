from app import db
from .base import Base
from .helpers import ModelHelpers


class Actor(Base, ModelHelpers):
    """Actors model."""

    __tablename__ = 'actors'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    bio = db.Column(db.String(250))
    age = db.Column(db.Integer)
    gender = db.Column(db.String(10))
    movie = db.Column(db.Integer, db.ForeignKey('movies.id'))

    def __init__(self, name, bio, age, gender, movie):
        self.name = name
        self.bio = bio
        self.age = age
        self.gender = gender
        self.movie = movie

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'bio': self.bio,
            'age': self.age,
            'gender': self.gender,
            'movie': self.movie,
            'created_on': self.created_on,
            'updated_on': self.updated_on
        }

    def __repr__(self):
        return f'<Actor {self.name}>'
