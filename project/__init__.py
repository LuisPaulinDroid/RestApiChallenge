from flask import Flask

from project.helloworld.controllers import helloworld
from project.pokemon.controllers import pokemon

# Initializing application
app = Flask(__name__)
app.config.from_object('config.BaseConfig')

# Adding imported controllers endpoints to application
app.register_blueprint(helloworld, url_prefix='/api/helloworld')
app.register_blueprint(pokemon, url_prefix='/api/pokemon')