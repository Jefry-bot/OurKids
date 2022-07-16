import string
from flask import Blueprint, redirect, render_template, request, url_for

class ErrorController:
    error_routes: Blueprint = Blueprint("error_routes", __name__)

    @error_routes.get("/error-server")
    def error_server():
        return render_template('errors/error-server.html')
    
    @error_routes.get("/not-found")
    def not_found():
        return render_template('errors/not-found.html')
    
    @error_routes.get("/not-auth")
    def not_auth():
        return render_template('errors/not_auth.html')