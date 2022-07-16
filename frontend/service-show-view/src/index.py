import os
import requests
from ourkids_f.load import load_env
load_env(os.path.dirname(__file__))
from flask import Flask
from ourkids_f import config
from constant.controllers import CONTROLLERS

template_folder_app = os.path.dirname(__file__) + "/../resourses/templates"
static_folder_app = os.path.dirname(__file__) + "/../resourses/static"

app = Flask(__name__, template_folder=template_folder_app, static_folder=static_folder_app)

if __name__ == '__main__':
    config(app, CONTROLLERS)
    
    app.run(debug=True, port=3000)