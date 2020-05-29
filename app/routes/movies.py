from flask import jsonify, request
from app import app
from app.models.movie import Movie
from app.auth.auth import requires_auth


@app.route('/movies')
@requires_auth('get:movies')
def get_movies(payload):
    """Handles GET requests for movies.
    returns:
        - a list of movie objects
        - success message
    """
    movies = []
    for movie in Movie.query.all():
        movies.append(movie.to_json())
    return jsonify({
        'movies': movies,
        'success': True
    }), 200


@app.route('/movies', methods=['POST'])
@requires_auth('post:movies')
def add_movie(payload):
    """Handles POST requests for movies.
    returns:
        - movie object
        - success message
    """
    body = request.get_json()
    new_movie = Movie(
        title=body.get('title'),
        desc=body.get('desc'),
        release_date=body.get('release_date')
    )
    new_movie.save()
    return jsonify({
        'movie': new_movie.to_json(),
        'success': True
    }), 201

@app.route('/movies/<int:id>', methods=['PATCH'])
@requires_auth('patch:movies')
def update_movie(id):
    """Handles UPDATE requests for movies.
    returns:
        - movie object
        - success message
    """
    movie = Movie.query.filter_by(id=id).first()
    if not movie:
        return jsonify({'message': 'Movie not found.'})
    body = request.get_json()
    movie.title = body.get('title', movie.title)
    movie.desc = body.get('desc', movie.desc)
    movie.release_date = body.get('release_date', movie.release_date)
    movie.update()
    return jsonify({
        'movie': movie.to_json(),
        'success': True
    }), 200


@app.route('/movies/<int:id>', methods=['DELETE'])
@requires_auth('delete:movies')
def delete_movies(id):
    """Handles DELETE requests for movies.
    returns:
        - success message
    """
    movie = Movie.query.filter_by(id=id).first()
    if not movie:
        return jsonify({'message': 'Movie not found.'})
    movie.delete()
    return jsonify({
        'message': 'Movie Successfully deleted.',
        'success': True,
    }), 200