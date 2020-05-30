from dotenv import load_dotenv
load_dotenv()
from flask import Flask, jsonify
from config import Config, Test_Config, DEVELOPMENT_MODE
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .auth.auth import AuthError

app = Flask(__name__)

#DEVELOPMENT MODE FALSE INTIALIZE PRODUCTION & TRUE INTIALIZE LOCAL DATABASE 
if DEVELOPMENT_MODE.lower() == 'false':
    app.config.from_object(Config)
    print("activated production database")
else :
    app.config.from_object(Test_Config)
    print("activated local database")


db = SQLAlchemy(app)
migrate = Migrate(app, db)


# Drop DB and Creat DB
def db_drop_and_create_all():
    db.drop_all()
    db.create_all()


from app.models import actor, movie
from app.routes import index, actors, movies

# Error Handling

#db_drop_and_create_all()

@app.errorhandler(AuthError)
def auth_error(error):
    return jsonify({
        "success": False,
        "error": error.status_code,
        "message": error.error['description']
    }), error.status_code 


@app.errorhandler(422)
def unprocessable(error):
    return jsonify({
        "success": False,
        "error": 422,
        "message": "unprocessable"
    }), 422


@app.errorhandler(404)
def not_found(error):
    return jsonify({
        "success": False,
        "error": 404,
        "message": "Not Found."
    }), 404


@app.errorhandler(405)
def method_not_allowed(error):
    return jsonify({
        "success": False,
        "error": 405,
        "message": error.description
    }), 405


@app.errorhandler(401)
def permissions_error(error):
    return jsonify({
        "success": False,
        "error": 401,
        "message": "Unauthorized! Permissions error."
    }), 401


@app.errorhandler(400)
def user_error(error):
    return jsonify({
        "success": False,
        "error": 400,
        "message": error.description
    }), 400


@app.errorhandler(401)
def invalid_claims(error):
    return jsonify({
        "success": False,
        "error": 401,
        "message": error.__dict__
    }), 401