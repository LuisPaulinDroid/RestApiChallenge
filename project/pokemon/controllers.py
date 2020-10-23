import requests
from flask import Blueprint

pokemon = Blueprint('pokemon', __name__)

@pokemon.route('', methods=['GET'])
def index():
    # Returning third'party pokemon request
    data = requests.get(url='https://pokeapi.co/api/v2/pokemon')
    return {'data': data.json()}, 200