# RestApiChallenge
 
This project demonstrates basic implementation of a REST API using Python3 with Flask framework.
 
## Installing and running application
 
This project can be run as a container based on the Dockerfile included as the image in order to facilitate the environment setup process.
 
### Prerequisites
 
- Docker 19.03.12 version or later. You can follow the instructions in official site to [get Docker](https://docs.docker.com/get-docker/) in any supported OS.
 
### Run application
 
1. Clone or download this project from [GitHub](https://github.com/LuisPaulinDroid/RestApiChallenge)
2. Follow the steps in your Docker installation to build an image based on the Dockerfile included in the project. (The following steps are for Ubuntu):
 ```
 # Navigate to the downloaded folder
 cd /path/to/RestApiChallenge
  # Build the image
 docker build -t rest_api_challenge ./
 ```
3. Run a container based on built image:
 ```
 docker run -p 5000:5000 --name restapichallenge rest_api_challenge
 ```
 You will see an output from Flask application indicating the listening hostname and port. Now you can make requests as described in [Using the API](#-using-the-api)
  The container runs with `python run.py` by default, but you can specify another command to run with the container as follows:
  ```
 # Example running 'python tests/test_config.py' inside the docker container
 # instead of 'python run.py'
 docker run -p 5000:5000 --name restapichallenge rest_api_challenge python tests/test_config.py
 ```
 
## Using the API
 
There are two endpoints you can consume with url http://localhost:5000/api/{endpoint}:
 
 - "helloworld": Accepting GET method only and retrieves a "Hello World!" message in json format.
 - "pokemon": Accepting GET method only and retrieves a Pokémon list according to third party service from [PokéApi](https://pokeapi.co/).