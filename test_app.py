import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from app import app
from app import db_drop_and_create_all
# from models import Movie, Actor

CA_TOKEN = os.environ.get('CA_TOKEN')
CD_TOKEN = os.environ.get('CD_TOKEN')
EP_TOKEN = os.environ.get('EP_TOKEN')


class CapstoneTestCase(unittest.TestCase):
    db_drop_and_create_all()
    """This class represents the casting agency test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = app
        self.client = self.app.test_client

        self.actor_id = 1
        self.movie_id = 1

        self.actor_info = {
            "name": "Bred Pit",
            "age": 20,
            "gender": "Male",
            "bio": "Fine Bio",
            "movie": self.movie_id
        }

        self.update_actor_info = {
            "name": "Clara Fymin",
            "age": 20,
            "gender": "Female",
            "bio": "Excellent Bio",
            "movie": self.movie_id
        }

        self.movie_info = {
            "title": "Batman ",
            "desc": "Full action movie",
            "release_date": "2021-10-1 04:22"
        }

        self.update_movie_info = {
            "title": "Spiderman ",
            "desc": "Full thriller movie",
            "release_date": "2021-10-1 04:22"
        }

    def add_movie(self):
        response = self.client().post(
            '/movies',
            json=self.movie_info, headers={
                "Authorization":
                "Bearer {}".format(EP_TOKEN)
            })

    def add_actor(self):
        response = self.client().post(
            '/actors',
            json=self.movie_info, headers={
                "Authorization":
                    "Bearer {}".format(EP_TOKEN)
            })

    def tearDown(self):
        """Executed after reach test"""
        pass

    def test_api_status_check(self):
        response = self.client().get('/')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data["message"], "Udacity capstone project.")
        self.assertEqual(data["success"], True)

    def test_authorization_header_check(self):
        response = self.client().get('/movies')
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 401)
        self.assertEqual(data["message"], "Authorization header is expected")

    # TEST CASES FOR ALL OPERATIONS OF EXECUTIVE PRODUCER
    # CREATE A NEW MOVIE - EXECUTIVE PRODUCER
    def test_01_create_movies_by_executive_producer(self):
        response = self.client().post(
            '/movies',
            json=self.movie_info, headers={
                "Authorization":
                    "Bearer {}".format(EP_TOKEN)
            })
        self.assertEqual(response.status_code, 201)

    # CREATE A NEW ACTOR - EXECUTIVE PRODUCER

    def test_02_create_actor_by_executive_producer(self):
        response = self.client().post(
            '/actors',
            json=self.actor_info, headers={
                "Authorization":
                    "Bearer {}".format(EP_TOKEN)
            })
        self.assertEqual(response.status_code, 201)

    # GET ALL ACTORS - EXECUTIVE PRODUCER

    def test_03_get_actors_by_executive_producer(self):
        response = self.client().get(
            '/actors',
            headers={
                "Authorization":
                    "Bearer {}".format(EP_TOKEN)
            })
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(data['success'])
        self.assertTrue(len(data['actors']) >= 0)

    # GET ALL MOVIES - EXECUTIVE PRODUCER

    def test_04_get_movies_by_executive_producer(self):
        response = self.client().get(
            '/movies',
            headers={
                "Authorization":
                    "Bearer {}".format(EP_TOKEN)
            })
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(data['success'])
        self.assertTrue(len(data['movies']) >= 0)

    # UPDATE A ACTOR INFORMATION - EXECUTIVE PRODUCER

    def test_05_update_actor_by_executive_producer(self):
        response = self.client().patch(
            '/actors/' + str(self.actor_id),
            json=self.update_actor_info, headers={
                "Authorization":
                "Bearer {}".format(EP_TOKEN)
            })
        data = json.loads(response.data)
        self.assertTrue(data['success'])
        self.assertTrue(data['actor'] is not None)

    # UPDATE A MOVIE INFORMATION - EXECUTIVE PRODUCER

    def test_06_update_movies_executive_producer(self):
        response = self.client().patch(
            '/movies/' + str(self.movie_id),
            json=self.update_movie_info, headers={
                "Authorization":
                "Bearer {}".format(EP_TOKEN)
            })
        data = json.loads(response.data)
        self.assertTrue(data['success'])
        self.assertTrue(data['movie'] is not None)

    # DELETE AN ACTOR - EXECUTIVE PRODUCER

    def test_07_delete_actor_by_executive_producer(self):
        response = self.client().delete(
            '/actors/' + str(self.actor_id),
            headers={
                "Authorization":
                    "Bearer {}".format(EP_TOKEN)
            })
        self.assertEqual(response.status_code, 200)

    # DELETE A MOVIE - EXECUTIVE PRODUCER

    def test_08_delete_movie_by_executive_producer(self):
        response = self.client().delete(
            '/movies/' + str(self.movie_id),
            headers={
                "Authorization":
                    "Bearer {}".format(EP_TOKEN)
            })
        self.assertEqual(response.status_code, 200)

    # TEST CASES FOR ALL OPERATIONS OF CASTING DIRECTOR

    # CREATE A NEW MOVIE - CASTING DIRECTOR

    def test_09_create_movies_by_casting_director(self):
        response = self.client().post(
            '/movies',
            json=self.movie_info, headers={
                "Authorization":
                    "Bearer {}".format(CD_TOKEN)
            })
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.status, "401 UNAUTHORIZED")

    # CREATE A NEW ACTOR - CASTING DIRECTOR

    def test_10_create_actor_by_casting_director(self):
        db_drop_and_create_all()
        self.add_movie()
        response = self.client().post(
            '/actors',
            json=self.actor_info, headers={
                "Authorization":
                    "Bearer {}".format(CD_TOKEN)
            })
        self.assertEqual(response.status_code, 201)

    # GET ALL ACTORS - CASTING DIRECTOR

    def test_11_get_actors_by_casting_director(self):
        response = self.client().get(
            '/actors',
            headers={
                "Authorization":
                    "Bearer {}".format(CD_TOKEN)
            })
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(data['success'])
        self.assertTrue(len(data['actors']) >= 0)

    # GET ALL MOVIES - CASTING DIRECTOR

    def test_12_get_movies_by_casting_director(self):
        response = self.client().get(
            '/movies',
            headers={
                "Authorization":
                    "Bearer {}".format(CD_TOKEN)
            })
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(data['success'])
        self.assertTrue(len(data['movies']) >= 0)

    # UPDATE A ACTOR INFORMATION - CASTING DIRECTOR

    def test_13_update_actor_by_casting_director(self):
        response = self.client().patch(
            '/actors/' + str(self.actor_id),
            json=self.update_actor_info, headers={
                "Authorization":
                "Bearer {}".format(CD_TOKEN)
            })
        data = json.loads(response.data)
        self.assertTrue(data['success'])
        self.assertTrue(data['actor'] is not None)

    # UPDATE A MOVIE INFORMATION - CASTING DIRECTOR

    def test_14_update_movies_by_casting_director(self):
        response = self.client().patch(
            '/movies/' + str(self.movie_id),
            json=self.update_movie_info, headers={
                "Authorization":
                "Bearer {}".format(CD_TOKEN)
            })
        data = json.loads(response.data)
        self.assertTrue(data['success'])
        self.assertTrue(data['movie'] is not None)

    # DELETE AN ACTOR - CASTING DIRECTOR

    def test_15_delete_actor_by_casting_director(self):
        response = self.client().delete(
            '/actors/' + str(self.actor_id),
            headers={
                "Authorization":
                    "Bearer {}".format(CD_TOKEN)
            })
        self.assertEqual(response.status_code, 200)

    # DELETE A MOVIE - CASTING DIRECTOR

    def test_16_delete_movie_by_casting_director(self):
        response = self.client().delete(
            '/movies/' + str(self.movie_id),
            headers={
                "Authorization":
                    "Bearer {}".format(CD_TOKEN)
            })
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.status, "401 UNAUTHORIZED")

    # TEST CASES FOR ALL OPERATIONS OF CASTING ASSISTANT
    # CREATE A NEW MOVIE -  CASTING ASSISTANT

    def test_17_create_movies_by_casting_assistance(self):
        db_drop_and_create_all()
        self.add_movie()
        response = self.client().post(
            '/movies',
            json=self.movie_info, headers={
                "Authorization":
                    "Bearer {}".format(CA_TOKEN)
            })
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.status, "401 UNAUTHORIZED")

    # CREATE A NEW ACTOR - CASTING DIRECTOR

    def test_18_create_actor_by_casting_assistance(self):
        self.add_actor()
        response = self.client().post(
            '/actors',
            json=self.actor_info, headers={
                "Authorization":
                    "Bearer {}".format(CA_TOKEN)
            })
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.status, "401 UNAUTHORIZED")

    # GET ALL ACTORS - CASTING DIRECTOR

    def test_19_get_actors_by_casting_assistance(self):
        response = self.client().get(
            '/actors',
            headers={
                "Authorization":
                    "Bearer {}".format(CA_TOKEN)
            })
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(data['success'])
        self.assertTrue(len(data['actors']) >= 0)

    # GET ALL MOVIES - CASTING DIRECTOR

    def test_20_get_movies_by_casting_assistance(self):
        response = self.client().get(
            '/movies',
            headers={
                "Authorization":
                    "Bearer {}".format(CA_TOKEN)
            })
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(data['success'])
        self.assertTrue(len(data['movies']) >= 0)

    # UPDATE A ACTOR INFORMATION - CASTING DIRECTOR

    def test_21_update_actor_by_casting_assistance(self):
        response = self.client().patch(
            '/actors/' + str(self.actor_id),
            json=self.update_actor_info, headers={
                "Authorization":
                "Bearer {}".format(CA_TOKEN)
            })
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.status, "401 UNAUTHORIZED")

    # UPDATE A MOVIE INFORMATION - CASTING DIRECTOR

    def test_22_update_movies_by_casting_assistance(self):
        response = self.client().patch(
            '/movies/' + str(self.movie_id),
            json=self.update_movie_info, headers={
                "Authorization":
                "Bearer {}".format(CA_TOKEN)
            })
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.status, "401 UNAUTHORIZED")

    # DELETE AN ACTOR - CASTING DIRECTOR

    def test_23_delete_actor_by_casting_assistance(self):
        response = self.client().delete(
            '/actors/' + str(self.actor_id),
            headers={
                "Authorization":
                    "Bearer {}".format(CA_TOKEN)
            })
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.status, "401 UNAUTHORIZED")

    # DELETE A MOVIE - CASTING DIRECTOR

    def test_24_delete_movie_by_casting_assistance(self):
        response = self.client().delete(
            '/movies/' + str(self.movie_id),
            headers={
                "Authorization":
                    "Bearer {}".format(CA_TOKEN)
            })
        self.assertEqual(response.status_code, 401)
        self.assertEqual(response.status, "401 UNAUTHORIZED")


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
