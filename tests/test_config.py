import os
import sys
import unittest
from flask import current_app
from flask_testing import TestCase

# Adding project root to python interpreter sys.path to enable
# imports searching
lib_path = os.path.abspath(os.path.join(__file__, '..', '..'))
sys.path.insert(0, lib_path)

from project import app

# Class to test enviroment variables for Development configuration
class TestDevelopmentConfig(TestCase):
    def create_app(self):
        app.config.from_object('config.DevelopmentConfig')
        return app

    def test_app_is_development(self):
        self.assertTrue(app.config['DEBUG'] is True)
        self.assertTrue(app.config['TESTING'] is True)
        self.assertFalse(current_app is None)

# Class to test enviroment variables for Testing configuration
class TestTestingConfig(TestCase):
    def create_app(self):
        app.config.from_object('config.TestingConfig')
        return app

    def test_app_is_testing(self):
        self.assertTrue(app.config['DEBUG'] is False)
        self.assertTrue(app.config['TESTING'] is True)

# Class to test enviroment variables for Production configuration
class TestProductionConfig(TestCase):
    def create_app(self):
        app.config.from_object('config.BaseConfig')
        return app

    def test_app_is_testing(self):
        self.assertTrue(app.config['DEBUG'] is False)
        self.assertTrue(app.config['TESTING'] is False)

if __name__ == '__main__':
    unittest.main()