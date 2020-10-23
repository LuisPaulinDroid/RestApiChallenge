import os
import sys
from flask_testing import TestCase

# Adding project root to python interpreter sys.path to enable
# imports searching
lib_path = os.path.abspath(os.path.join(__file__, '..', '..'))
sys.path.insert(0, lib_path)

from project import app

# Class to group tests common actions
class BaseTestCase(TestCase):

    def create_app(self):
        app.config.from_object('config.TestingConfig')
        return app