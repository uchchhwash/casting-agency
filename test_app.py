import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from app import app
# from models import Movie, Actor


CA_TOKEN = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjdJVzdaUEZLWXBpdS1qZjAzOTJibiJ9.eyJpc3MiOiJodHRwczovL3VjaC1kZXYuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDVlYzUzZDNmY2RmYjNjMGM3ZTQzZGYxOSIsImF1ZCI6ImNhc3RpbmctYWdlbmN5IiwiaWF0IjoxNTkwNzY1MjI4LCJleHAiOjE1OTA4NTE2MTksImF6cCI6IjRoZjRONExJc1RlVUpEYWg5akZ6c2QyY0pwaU1nbk9LIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyJdfQ.iR-h6qjk0zbKoysOf_KNwBZMTEQmjCXGWO0mN4uRWBQO6Vzk-mgH400wMdcyck3pkHQc0L1xwa3JTnaiHqH5NxM4H1yNCrBo_S7XfUmZOyLcqUTgXU2X4x33IuQAPEt2jMmFcb-Sk0cX1rl-bPcsLY-iRaoOit7I4Tnrub5BuEtr4pjeXpffFRciY9K5M4VoFTWjPB-83oTaEaxJzUbUu62ZK0d9jtNav_zz5e5g7uRzEo2iLBXUo7jnL-751o7f4-FmpI62gK1N5RkBF7IasEZg4ocgY21Fy9wP_iRqUXJGhUZLoliIWSaC4I8yGpckhm1dEnsU7Hj-J482EcMfEQ"
CD_TOKEN = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjdJVzdaUEZLWXBpdS1qZjAzOTJibiJ9.eyJpc3MiOiJodHRwczovL3VjaC1kZXYuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDVlYzU0MjA2NzlkN2EyMGM4MmViYzJlZiIsImF1ZCI6ImNhc3RpbmctYWdlbmN5IiwiaWF0IjoxNTkwNzY1MTU0LCJleHAiOjE1OTA4NTE1NDUsImF6cCI6IjRoZjRONExJc1RlVUpEYWg5akZ6c2QyY0pwaU1nbk9LIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3JzIiwiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiLCJwYXRjaDphY3RvcnMiLCJwYXRjaDptb3ZpZXMiLCJwb3N0OmFjdG9ycyJdfQ.jnAQmviHK0opdojPY-__CUfzVW1qo4mjSZASQd-wmliDerOwvfKE-Of1uoIbVXNXBMMBpgyDo2a8IOfpJ8O096e8n3tTtyurKI35SNaOa4IyxDDFTjCIOdwHQbtqhKXGBLbSrNlkUSgN6Q8_514RW1rHMvd5x-bXg1qzAWPTizy7zvBN9FkSIlgEPDl7bCei_2TmuHEXtdoB-Syo0f731uWBXUIwx5IMwUljCyNl1SJlvOEsdfdrg9tGbxI2o4ASXr4caKfRsVa0qoLNZM0w_LMVtdCfUnZJeXNWHz5OVk-aU86U2KdX7CZBZU5s03H6lBElTTiL5zriYHC92f0Cdg"
EP_TOKEN = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjdJVzdaUEZLWXBpdS1qZjAzOTJibiJ9.eyJpc3MiOiJodHRwczovL3VjaC1kZXYuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDVlZDBjOWRhNDc5YWI4MGMwYWE5ZmYwMCIsImF1ZCI6ImNhc3RpbmctYWdlbmN5IiwiaWF0IjoxNTkwNzY1MzI1LCJleHAiOjE1OTA4NTE3MTYsImF6cCI6IjRoZjRONExJc1RlVUpEYWg5akZ6c2QyY0pwaU1nbk9LIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3JzIiwiZGVsZXRlOm1vdmllcyIsImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIiwicGF0Y2g6YWN0b3JzIiwicGF0Y2g6bW92aWVzIiwicG9zdDphY3RvcnMiLCJwb3N0Om1vdmllcyJdfQ.Fyk1X9nYcdHkHDDhpDFm0M-zdUoIdKfx1szslZODe9Z4L8Q8UPtKjEtbTXpjGd5MtJy3iVGNbn0gqZb7X0Y2FFbnIW__xs_UCyd59FmdjhFuNlJmY80dkOtjxeN2q2NU_whEzx3SmaQe5-QlU48NQxvlpBYSI78tXVgaZVOJP6c-A48yaVKowi8UrVACtdi7keIXS-Sf5iJ7PBbzTLcYK5MAU9_gu2m6cN9wOutZekGjKFb8osg4inmkHkba9TpR-eMHWmnYcbe3n_tkRE05ttAzf8L4Qpp6bRyw2KmJGIWaQfdzHguYrqgVPshmdVeXxt8c44wgi5JPryTV5ZgN1A"

CA_TOKEN = os.environ.get('CA_TOKEN')
CD_TOKEN = os.environ.get('CD_TOKEN')
EP_TOKEN = os.environ.get('EP_TOKEN')
class CapstoneTestCase(unittest.TestCase):
    """This class represents the casting agency test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = app
        self.client = self.app.test_client

    def tearDown(self):
        """Executed after reach test"""
        pass

    #CASTING DIRECTOR CREATE ACTOR
    def test_create_actor_by_casting_director(self):
        payload = {
           	"name": "actor1",
            "bio": "Fine Bio",
            "age": 21,
            "gender": "MALE",
            "movie": 3
        }
        response = self.client().post(
            '/actors',
            json=payload, headers={
                "Authorization":
                    "Bearer {}".format(CD_TOKEN)
            })
        self.assertEqual(response.status_code, 201)

    def test_get_actors_by_casting_director(self):

        response = self.client().get(
            '/actors',
            headers={
                "Authorization":
                    "Bearer {}".format(CD_TOKEN)
            }
        )
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)

    # def test_delete_movies_with_no_permission_fails(self):
    #     response = self.client().delete(
    #         '/movies/5',
    #         headers={
    #             "Authorization":
    #                 "Bearer {}".format(self.casting_director_token)
    #         })
    #     self.assertEqual(response.status_code, 401)


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()