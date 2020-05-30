from flask import jsonify, abort
from app import app


# INDEX ROUTE TO CHECK API STATUS
@app.route('/')
def index():
    return jsonify({
        'message': 'Welcome To The Casting-Agency-API',
        'success': True
    })
