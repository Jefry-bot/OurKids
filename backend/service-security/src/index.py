import os
from flask import Flask
from flask_cors import CORS
from ourkids.Settings import config
from ourkids.load import load_env
load_env(os.path.dirname(__file__))

from constant.controllers import CONTROLLERS

app = Flask(__name__)

cors = CORS(app, resources={r"/api/*": {"origins": {"http://localhost:3000"}}})

if __name__ == '__main__':
    config(app, CONTROLLERS)
    
    app.run(port=4001)