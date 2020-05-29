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