# Here, we add a secret key and initializing the Flask app

from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ecf6e975838a2f7bf3c5dbe7d55ebe5b'

from flaskApp import routes
