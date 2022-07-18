import json
import string
import requests
from flask import Blueprint, flash, redirect, render_template, request, url_for
from services.AuthService import Service

class AuthController:
    auth_routes: Blueprint = Blueprint("auth_routes", __name__)
    
    def __init__(self) -> None:
        global service
        service = Service()

    @auth_routes.route("/login", methods=['GET', 'POST'])
    @auth_routes.route("/login/<success>", methods=['GET', 'POST'])
    def login(success=None):
        return service.login(request, success)

    @auth_routes.route("/register", methods=['GET', 'POST'])
    def register():
        return service.register(request)