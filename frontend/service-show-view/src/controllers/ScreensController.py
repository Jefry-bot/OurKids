import string
from flask import Blueprint, render_template, request
from ourkids_f.NotAuthException import NotAuthException

class ScreensController:
    screens_routes: Blueprint = Blueprint("screens_routes", __name__)
    
    @screens_routes.get('/home')
    def Home():
        return render_template('screens/home.html')