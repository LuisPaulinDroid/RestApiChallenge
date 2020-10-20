from flask import Flask
import requests

app = Flask(__name__)

@app.route('/api/helloworld', methods=['GET'])
def hello_world():
    return {'message': 'Hello World!'}, 200

@app.route('/api/pokemon', methods=['GET'])
def pokemons():
    data = requests.get(url='https://pokeapi.co/api/v2/pokemon')
    return {'data': data.json()}, 200

if __name__ == "__main__":
    app.run(debug=True)