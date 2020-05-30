from flask import jsonify, request, abort
from app import app
from app.models.movie import Movie
from app.auth.auth import requires_auth


# API TO GET ALL MOVIES
# ALLOWED BY EXECUTIVE-PRODEUCER/CASTING-DIRECTOR/CASTING-ACTOR
@app.route('/movies')
@requires_auth('get:movies')
def get_movies(payload):
    try:
        movies = []
        for movie in Movie.query.all():
            movies.append(movie.to_json())
        return jsonify({
            'movies': movies,
            'success': True
        }), 200

    except Exception:
        abort(500)


# ADD TO A NEW MOVIE
# ALLOWED BY CASTING-DIRECTOR
@app.route('/movies', methods=['POST'])
@requires_auth('post:movies')
def add_movie(payload):
    try:
        body = request.get_json()
        similar_movie_flag = Movie.query.filter(
            Movie.title == body.get('title')).one_or_none()
        if similar_movie_flag is not None:
            return jsonify({
                'message': 'Similar Movie Title Already Exist in Database.'
            }), 422
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

    except Exception:
        abort(500)


# API TO EDIT A EXISTING MOVIE
# ALLOWED BY EXECUTIVE-PRODEUCER/CASTING-DIRECTOR
@app.route('/movies/<int:id>', methods=['PATCH'])
@requires_auth('patch:movies')
def update_movie(payload, id):
    try:
        body = request.get_json()
        movie = Movie.query.filter(Movie.id == id).one_or_none()
        if not movie:
            return jsonify({'message': 'Movie not found.'}), 404
        if movie:
            movie_flag = Movie.query.filter(
                Movie.title == body.get('title')).one_or_none()
            if movie_flag is not None:
                return jsonify({
                    'message': 'Similar Movie Title Already Exist in Database.'
                }), 422
        movie.title = body.get('title', movie.title)
        movie.desc = body.get('desc', movie.desc)
        movie.release_date = body.get('release_date', movie.release_date)
        movie.update()
        return jsonify({
            'movie': movie.to_json(),
            'success': True
        }), 200
    except Exception:
        abort(500)


# API TO DELETE A EXISTING MOVIE
# ALLOWED BY EXECUTIVE-PRODEUCER
@app.route('/movies/<int:id>', methods=['DELETE'])
@requires_auth('delete:movies')
def delete_movies(payload, id):
    try:
        movie = Movie.query.filter_by(id=id).first()
        if not movie:
            return jsonify({'message': 'Movie not found.'}), 404
        movie.delete()
        return jsonify({
            'message': 'Movie Successfully deleted.',
            'success': True,
        }), 200

    except Exception:
        abort(500)
