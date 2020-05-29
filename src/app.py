import os, json
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import exc
from flask_cors import CORS
from .database.models import db_drop_and_create_all, setup_db
# from .auth.auth import AuthError, requires_auth

def create_app(test_config=None):
  # create and configure the app
  app = Flask(__name__)
  setup_db(app)
  CORS(app)



  # Uncomment the following line to initialize the database.
  db_drop_and_create_all()

  # ROUTES
  @app.route('/', methods=['GET'])
  def health_check():
      return jsonify({
          "success": True,
          "message":"Application Running Successfully"
      }), 200

  
  
  return app

app = create_app()
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
