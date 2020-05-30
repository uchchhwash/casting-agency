import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from app import app
from app import db
# from models import Movie, Actor

CA_TOKEN = os.environ.get('CA_TOKEN')
CD_TOKEN = os.environ.get('CD_TOKEN')
EP_TOKEN = os.environ.get('EP_TOKEN')

class CapstoneTestCase(unittest.TestCase):
    db.drop_all()
    db.create_all()
    """This class represents the casting agency test case"""
    def setUp(self):

        """Define test variables and initialize app."""
        self.app = app
        self.client = self.app.test_client
        

    def tearDown(self):
        """Executed after reach test"""
        pass

    #CASTING DIRECTOR CREATE ACTOR
    def test_01_create_movies_by_executive_producer(self):
        payload = {
            "title": "Terminator2",
            "desc": "Full action movie",
            "release_date" : "2020-01-01"
        }
        response = self.client().post(
            '/movies',
            json=payload, headers={
                "Authorization":
                    "Bearer {}".format(EP_TOKEN)
            })
        self.assertEqual(response.status_code, 201)
    

    def test_02_create_actor_by_executive_producer(self):
        payload = {
            "name": "actor1",
            "bio": "Fine Bio",
            "age": 21,
            "gender": "MALE",
            "movie": 1
        }
        response = self.client().post(
            '/actors',
            json=payload, headers={
                "Authorization":
                    "Bearer {}".format(EP_TOKEN)
            })
        self.assertEqual(response.status_code, 201)


    def test_03_get_movies_by_executive_producer(self):
        response = self.client().get(
            '/movies',
            headers={
                "Authorization":
                    "Bearer {}".format(EP_TOKEN)
            }
        )
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)
   
   
    def test_04_get_actors_by_executive_producer(self):
        response = self.client().get(
            '/actors',
            headers={
                "Authorization":
                    "Bearer {}".format(EP_TOKEN)
            }
        )
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)


    def test_05_delete_actor_by_executive_producer(self):
        response = self.client().delete(
            '/actors/1',
            headers={
                "Authorization":
                    "Bearer {}".format(EP_TOKEN)
            })
        self.assertEqual(response.status_code, 200)

    def test_06_delete_movie_by_executive_producer(self):
        response = self.client().delete(
            '/movies/1',
            headers={
                "Authorization":
                    "Bearer {}".format(EP_TOKEN)
            })
        self.assertEqual(response.status_code, 200)


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()