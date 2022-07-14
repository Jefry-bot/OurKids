import string
from flask import Blueprint, request
from ourkids.NotFoundException import NotFoundException

from services.AuthService import AuthService

class AuthController:
    auth_routes: Blueprint = Blueprint("auth_routes", __name__)

    @auth_routes.post("/login")
    def login():
        data = request.get_json()

        if AuthService.validateUser(data):
            return AuthService.write_token(data)
        else:
            raise NotFoundException

    @auth_routes.get("/verify/token")
    def verify():
        token = request.headers['Authorization'].split(" ")[1]
        return AuthService.validate_token(token, output = True)