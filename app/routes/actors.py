from flask import jsonify, request, abort
from app import app
from app.models.actor import Actor
from app.models.movie import Movie
from app.auth.auth import requires_auth

@app.route('/actors', methods=['GET'])
@requires_auth('get:actors')
def get_actors(payload):
    """Handles GET requests for actors.
    returns:
        - a list of actor objects
        - success message
    """
    actors = []
    for actor in Actor.query.all():
        actors.append(actor.to_json())
    return jsonify({
        'actors': actors,
        'success': True
    }), 200

@app.route('/actors', methods=['POST'])
@requires_auth('post:actors')
def add_actor(payload):

    body = request.get_json()
    movie = Movie.query.filter_by(id=body.get('movie')).one_or_none()
    if not movie:
        return jsonify({'message': 'Movie not found in database.'}),422
    new_actor = Actor(
        name=body.get('name'),
        bio=body.get('bio'),
        age=body.get('age'),
        gender=body.get('gender'),
        movie=body.get('movie')
    )
    new_actor.save()
    return jsonify({
        'actor': new_actor.to_json(),
        'success': True
    }), 201

@app.route('/actors/<int:id>', methods=['PATCH'])
@requires_auth('patch:actors')
def update_actor(payload, id):
    """Handles UPDATE requests for actors.
    returns:
        - actor object
        - success message
    """
    actor = Actor.query.filter_by(id=id).first()
    if not actor:
        return jsonify({'message': 'Actor not found.'})
    body = request.get_json()
    actor.name = body.get('name', actor.name)
    actor.bio = body.get('bio', actor.bio)
    actor.age = body.get('age', actor.age)
    actor.gender = body.get('gender', actor.gender)
    actor.update()
    return jsonify({
        'actor': actor.to_json(),
        'success': True
    }), 200


@app.route('/actors/<int:id>', methods=['DELETE'])
@requires_auth('delete:actors')
def delete_actor(payload, id):
    """Handles DELETE requests for actors.
    returns:
        - success message
    """
    actor = Actor.query.filter_by(id=id).first()
    if not actor:
        return jsonify({'message': 'Actor not found.'})
    actor.delete()
    return jsonify({
        'message': 'Actor Successfully deleted.',
        'success': True,
    }), 200