import string
from flask import Blueprint, redirect, render_template, request, url_for

class ErrorController:
    error_routes: Blueprint = Blueprint("error_routes", __name__)

    @error_routes.get("/error-servers")
    def login():
        return render_template('errors/error-server.html')