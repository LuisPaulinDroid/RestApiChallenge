import requests
from flask import Blueprint

pokemon = Blueprint('pokemon', __name__)

@pokemon.route('', methods=['GET'])
def index():
    # Returning pokemon list from PokeApi
    data = requests.get(url='https://pokeapi.co/api/v2/pokemon')
    if data.ok:
        return {'data': data.json()}, data.status_code
    else:
        return {'message': data.text}, data.status_code

@pokemon.route('/<name_or_id>', methods=['GET'])
def get(name_or_id):
    # Returning pokemon with specified by name or id
    data = requests.get(
        url='https://pokeapi.co/api/v2/pokemon/{0}'.format(name_or_id)
    )
    if data.ok:
        return {'data': data.json()}, data.status_code
    else:
        return {'message': data.text}, data.status_code