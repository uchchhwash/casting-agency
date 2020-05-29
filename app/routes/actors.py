from flask import jsonify, request
from app import app
from app.models.actor import Actor
from app.auth import requires_auth


@app.route('/actors')
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
    """Handles POST requests for actors.
    returns:
        - actor object
        - success message
    """
    body = request.get_json()
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