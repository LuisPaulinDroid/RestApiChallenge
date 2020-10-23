import json
import os
import sys
import unittest
from flask import current_app

# Adding project root to python interpreter sys.path to enable
# imports searching
lib_path = os.path.abspath(os.path.join(__file__, '..', '..'))
sys.path.insert(0, lib_path)

from project import app
from tests.base import BaseTestCase

# Class to group unit tests for Pokemon Controller
class TestPokemonController(BaseTestCase):
    
    # Testing call to Pokemon index endpoint
    def test_index(self):
        with self.client:
            response = self.client.get(
                '/api/pokemon'
            )
            data = json.loads(response.data.decode())

            # Response as expected
            self.assertEqual(response.status_code, 200)
            self.assertTrue(response.content_type == 'application/json')

if __name__ == "__main__":
    unittest.main()