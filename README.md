
# Casting Agency Capstone

The Casting Agency models a company that is responsible for creating movies and managing and assigning actors to those movies. You are an Executive Producer within the company and are creating a system to simplify and streamline your process.

This project uses python, flask and postgresql for it's backend and is hosted on Heroku.

All backend code follows  [PEP8 style guidelines](https://www.python.org/dev/peps/pep-0008/)

No frontend is developed for this app, you can check the api using **curl** or  [Postman](https://www.postman.com/)
## Getting Started

### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by naviging to the root directory of this project and running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.
### Database Setup
With Postgres, create a database named **casting-agency**

`createdb casting-agency`

> Make sure to include the database credentials in database path in **.env**
##  Project Configuration

This project is hosted on Heroku. To run this application locally you need to configure the .env file in the project directory.
#### AUTH0 Configurations
```
AUTH0_DOMAIN = 'Put Your AUTH0 Domain Name Here'
ALGORITHMS = ['RS256']
API_AUDIENCE = 'Put Your AUTH0 API Audience Here'
```
### Production & local Database Configurations
Development Enviroment will take the `DATABASE_URL` and  Test Enviroment will take the `TEST_DATABASE_URL`
```export DATABASE_URL = 'Put Your Postgres Database Path Here'
export TEST_DATABASE_URL = 'Put Your Postgres Test Database Path Here For Test Purpose'
export SQLALCHEMY_TRACK_MODIFICATIONS = False
```
### Authentication Tokens
```
export CA_TOKEN = "Put Your Casting Agent User Access Token Here"
export CD_TOKEN = "Put Your Casting Director User Access Token Here"
export EP_TOKEN = "Put Your Executive Producer User Access Token Here"
```
### Environment
For Development Mode set `TEST_MODE = False` & for Test Mode `TEST_MODE` = True

### Running Migrations
Use the following commands to run database migrations to add tables or columns.
```bash
flask db init
flask db migrate
flask db upgrade
```
### Running the server
To run this application on local enviroment go the project directory and open the .env file and  
set `TEST_MODE = False`

Activate Your Python Virtual Enviroment
```bash
export FLASK_APP=app.py
export FLASK_ENV=development
flask run
```

The app will now run on debug mode and auto restart if any change is made.
The application runs on http://127.0.0.1:5000/ by default.

## Authentication
This project uses Auth0 for authentication.
RBAC is implemented with users and roles inside the Auth0 account.
Click on the login button and signup. Note down the access token from the URL for further use.
##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py. 

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server.

- [jose](https://python-jose.readthedocs.io/en/latest/) JavaScript Object Signing and Encryption for JWTs. Useful for encoding, decoding, and verifying JWTS.

## Users & Roles
**Casting-Agency** has 3 types of users. each user has his own privileges.
-   **Casting Assistant**
    -   Can view actors and movies
-  **Casting Director**
    -   All permissions of a Casting Assistant and…
    -   Add or delete an actor from the database
    -   Modify actors or movies
-   **Executive Producer**
    
    -   All permissions of a Casting Director and…
    -   Add or delete a movie from the database
    

## API Reference
### Endpoints

#### GET '/actors'
- Fetches a paginated list of actors.
- Request Arguments: offset: 1(default), limit: 30(default).
- Returns: list of actors ordered by id.
```

{
  'success': True,
  'actors': [
    {
      id: 1,
      name: 'Actor 1',
      age: 30,
      gender: 'male'
    }
  ]
}
```

#### GET '/movies'
- Fetches a paginated list of movies.
- Request Arguments: offset: 1(default), limit: 30(default).
- Returns: list of movies ordered by id.
```
{
  'success': True,
  'movies': [
    {
      id: 1,
      title: 'New Movie 1',
      release_date: '2021-10-1 04:22'
    }
  ]
}
```

#### POST '/actors'
- Create a new actor.
- Request Arguments: { name: String, age: Integer, gender: String }.
- Returns: An object with `success: True` and the new actor inside an array.
```
{
  'success': True,
  'actors': [
    {
      id: 2,
      name: 'Actor 2',
      age: 28,
      gender: 'Female'
    }
  ]
}
```

#### POST '/movies'
- Create a new movie.
- Request Arguments: { title: String, release_date: DateTime }.
- Returns: An object with `success: True` and the new movie inside an array.
```
{
  'success': True,
  'movies': [
    {
      id: 2,
      title: 'New Movie 2',
      release_date: '2022-10-1 04:22'
    }
  ]
}
```

#### Patch '/actors/<actor_id>'
- Update an actor.
- Request Arguments: { name: String, age: Integer, gender: String }.
- Returns: An object with `success: True` and the updated actor inside an array.
```
{
  'success': True,
  'actors': [
    {
      id: 1,
      name: 'Updated Actor',
      age: 50,
      gender: 'Male'
    }
  ]
}
```

#### Patch '/movies/<movie_id>'
- Update a movie.
- Request Arguments: { title: String, release_date: DateTime }.
- Returns: An object with `success: True` and the updated movie inside an array.
```
{
  'success': True,
  'movies': [
    {
      id: 1,
      title: 'Updated Movie 1',
      release_date: '2030-10-1 04:22'
    }
  ]
}
```

#### DELETE '/actors/<actor_id>'
- Removes an actor from the database.
- Request Parameters: question id slug.
- Returns: An object with `success: True` and the id of the deleted actor
```
{
  'success': True,
  'id': 1
}
```

#### DELETE '/movies/<movie_id>'
- Removes a movie from the database.
- Request Parameters: question id slug.
- Returns: An object with `success: True` and the id of the deleted movie
```
{
  'success': True,
  'id': 1
}
```

## Testing

#### Testing remote server using postman

- Import the postman collection `./casting agency.postman_collection.json`.
  - This collection has 3 roles that have specific permissions detailed below.
  - Roles
    - Public
      - No access
    - Casting Assistant
      - `get:actors`, `get:movies`
    - Casting Director
      - `get:actors`, `get:movies`, `post:actors`, `patch:actors`, `patch:movies`, `delete:actors`
    - Executive Producer (all permissions)
      - `get:actors`, `get:movies`, `post:actors`, `post:movies`, `patch:actors`, `patch:movies`, `delete:actors`, `delete:movies`

- Once imported, Run the collection and play around with the endpoints within folders `public`, `assistant`, `director` and `producer`.

#### Running tests locally
To run the tests from ./test_app.py, first make sure you have ran and executed the setup.sh file to set the enviorment.

After setting the enviorment start your local postgress server:
```bash
pg_ctl -D /usr/local/var/postgres start
```

Then run the follwing commands to run the tests:
```
dropdb casting_test
createdb casting_test
psql casting_test < casting_test.psql
python test_app.py
```# Casting Agency Capstone

The Casting Agency API models a company that is responsible for creating movies and managing/assigning actors to those movies.
This api is responsible for checking permissions and handling CRUD for an Actor and Movie model/
## Getting Started

### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by naviging to the root directory of this project and running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

After installing the dependencies, execute the bash file `setup.sh` to set the user jwts, auth0 credentials and the remote database url by naviging to the root directory of this project and running:

```bash
source setup.sh
```

##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py. 

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server.

- [jose](https://python-jose.readthedocs.io/en/latest/) JavaScript Object Signing and Encryption for JWTs. Useful for encoding, decoding, and verifying JWTS.

## Running the server

From within the root directory first ensure you are working using your created virtual environment.

To run the server, execute:

```bash
export FLASK_APP=app.py
export FLASK_ENV=development
flask run
```

Setting the `FLASK_ENV` variable to `development` will detect file changes and restart the server automatically.

Setting the `FLASK_APP` variable to `flaskr` directs flask to use the `flaskr` directory and the `__init__.py` file to find the application. 

## API Reference

### Endpoints

-   GET '/actors'
-   GET '/movies'
-   POST '/actors'
-   POST '/movies'
-   PATCH '/actors/int:id'
-   PATCH '/movies/int:id'
-   DELETE '/actors/int:id'
-   DELETE '/movies/int:id'
#### GET '/movies'
- Fetches List of all Movies.
- Returns: List of Movies ordered by ID
```
{
  "movies": [
    {
      "desc": "Full Action Movie", 
      "id": 1, 
      "release_date": "2020-01-01", 
      "title": "Terminator 25"
    }
  ], 
  "success": true
}
```
#### GET '/actors'
- Fetches  List of all Actors.
- Returns: List of Actors ordered by ID
```
{
  "actors": [
    {
      "age": 25, 
      "bio": "Awesome Bio", 
      "created_on": "Sat, 30 May 2020 23:28:36 GMT", 
      "gender": "MALE", 
      "id": 1, 
      "movie": 1, 
      "name": "John Baker", 
      "updated_on": "Sat, 30 May 2020 23:28:36 GMT"
    }
  ], 
  "success": true
}
```
#### POST '/movies'
- Create a new movie.
- Request Arguments: { title: String, release_date: DateTime, desc: String }.
- Returns: An object with `success: True` and the new movie inside an array.
```
{
  "movie": {
    "desc": "Full Action Movie", 
    "id": 1, 
    "release_date": "2020-01-01", 
    "title": "Terminator 25"
  }, 
  "success": true
}
```
#### POST '/actors'
- Create a new actor.
- Request Arguments: { name: String, age: Integer, gender: String, bio: String, movie: Int(Foreign_Key) }.
- Returns: An object with `success: True` and the new actor inside an array.
```
{
  "actor": {
    "age": 25, 
    "bio": "Awesome Bio", 
    "created_on": "Sat, 30 May 2020 23:28:36 GMT", 
    "gender": "MALE", 
    "id": 1, 
    "movie": 1, 
    "name": "John Baker", 
    "updated_on": "Sat, 30 May 2020 23:28:36 GMT"
  }, 
  "success": true
}
```
#### Patch '/movies/<movie_id>'
- Update a movie.
- Request Arguments: { title: String, release_date: DateTime, desc: String }.
- Returns: An object with `success: True` and the updated movie inside an array.
```
{
  "movie": {
    "desc": "Full thriller movie", 
    "id": 1, 
    "release_date": "2020-11-11", 
    "title": "Transformers"
  }, 
  "success": true
}
```

#### Patch '/actors/<actor_id>'
- Update an actor.
- Request Arguments: { name: String, age: Integer, gender: String, bio: String, movie: Int(Foreign_Key) }.
- Returns: An object with `success: True` and the updated actor inside an array.
```
{
  "actor": {
    "age": 30, 
    "bio": "Extra Oridinary Bio", 
    "created_on": "Sat, 30 May 2020 23:28:36 GMT", 
    "gender": "MALE", 
    "id": 1, 
    "movie": 1, 
    "name": "Baker Bhai", 
    "updated_on": "Sat, 30 May 2020 23:28:36 GMT"
  }, 
  "success": true
}
```
#### DELETE '/movies/<movie_id>'
- Removes a movie from the database.
- Request Parameters: Movie ID
- Returns: An object with `success: True` and the id of the deleted movie
```
{
  "id": 1, 
  "message": "Movie Successfully deleted.", 
  "success": true
}
```
#### DELETE '/actors/<actor_id>'
- Removes an Actor from the database.
- Request Parameters: Actor ID
- Returns: An object with `success: True` and the id of the deleted actor
```
{
  "id": 1, 
  "message": "Actor Successfully deleted.", 
  "success": true
}
```
### Error Handling

Errors are returned as JSON objects in the following format:

```
{
    "success": False, 
    "error": 404,
    "message": "Resource not found."
}

```

The API will return  error types with multiple different error messages when requests fails:
-   422: Unprocessble
-   404: Not Found
-   405: Method Not Allowed
-   401: Unauthorized! Permissions error
-   400: 
	-   Permissions were not included in the JWT.
	-   400: Bad Request
	-   400: Unable to parse authentication token.
	    
	-   400: Unable to parse authentication token.
- 401:
	    
	-   401: Authorization header is expected.
	    
	-   401: Authorization header must start with "Bearer".
    
	-   401: Token expired.
	    
	-   401: Incorrect claims. Please, check the audience and issuer.
    
-   403: Permission denied.
    
-   404: Resource Not Found.
- 500: Internal server error
## Testing

### Testing remote/local server using postman

- Import the postman collection `./casting-agency.postman_collection.json`.
  - This collection has 3 roles that have specific permissions detailed below.
  - Roles
    - Public
      - No access
    - Casting Assistant
      - `get:actors`, `get:movies`
    - Casting Director
      - `get:actors`, `get:movies`, `post:actors`, `patch:actors`, `patch:movies`, `delete:actors`
    - Executive Producer (All Permissions)
      - `get:actors`, `get:movies`, `post:actors`, `post:movies`, `patch:actors`, `patch:movies`, `delete:actors`, `delete:movies`

Postman Collection has Development & Production Enviroment. Configure the domain url as your need.
>**From Auth0 Register 3 Users with this Roles  and Get Healthy Access Tokens and Update them on Postman Collection**
Run the collection and play around with the endpoints within folders `executive-producer`, `casting-director` and `casting-assisant`.

### Running the Unit Tests
To run the unit tests from test_app.py, first make sure you have configured the .env file properly and set the 
`TEST_MODE = True` in .env file.
Make sure to set a Local Postgres Database path on  TEST_DATABASE_URL in the .env file as well.
After setting eveything up run your python virtual enviroment and run 
``` 
python test_app.py
```

Then run the follwing commands to run the tests:
> At the beginning this test_file will drop all the tables in the test database and create all the tables again.
> Then this test_app will run total 26 test cases. 

## Production Deployment
We are using Heroku for deployment.
* Install heroku in your machine.
* Login to heroku
```bash
heroku login
```
* Create an app
```bash
heroku create appname
```
* Create 2 databases by running the following command twice. One for application and other one to use during the test.
```bash
heroku addons:create heroku-postgresql:hobby-dev --app appname
```

* Initialize git in the project directory
```bash
git init
git remote add heroku https://git.heroku.com/appname.git
```
* Push it to heroku
```bash
git add .
git commit -am "make it better"
git push heroku master
```
Run Application & Migrations
```
heroku run python manage.py db upgrade --app name_of_your_application
```
> If there is any issue, use `heroku restart` to restart the app.

### Author
[Uchchhwash Chakraborty](https://www.linkedin.com/in/uchchhwash)

### Acknowledgements
* The incredible team at Udacity.