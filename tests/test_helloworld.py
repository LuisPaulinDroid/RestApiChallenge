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

# Class to group unit tests for Helloworld Controller
class TestHelloworldController(BaseTestCase):

    # Testing call to Helloworld index endpoint
    def test_index(self):
        with self.client:
            response = self.client.get(
                '/api/helloworld'
            )
            data = json.loads(response.data.decode())

            # Response as expected
            self.assertEqual(response.status_code, 200)
            self.assertTrue(response.content_type == 'application/json')
            self.assertTrue(data['message'] == 'Hello World!')

if __name__ == "__main__":
    unittest.main()