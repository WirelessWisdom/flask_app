from unittest import TestCase
from app import app
import json


class TestHome(TestCase):
    def test_home(self):
        with app.test_client() as c:
            resp = c.get('/')

            self.assertAlmostEqual(resp.status_code, 200)
            self.assertEqual(json.loads(resp.get_data()), {'message': 'Hello world!'})

