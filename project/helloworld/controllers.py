import requests

from flask import Blueprint

helloworld = Blueprint('helloworld', __name__)

@helloworld.route('', methods=['GET'])
def index():
    return {'message': 'Hello World!'}, requests.codes.ok