from flask import jsonify, abort
from app import app


@app.route('/')
def index():
    """Handles GET requests for sample ping.
    This is used to test whether the app is set up well.
    returns:
        - success message
    """
    return jsonify({
        'message': 'Udacity capstone project.',
        'success': True
    })