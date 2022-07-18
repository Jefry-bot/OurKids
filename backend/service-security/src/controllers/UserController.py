import string
from flask import Blueprint, request
from ourkids.NotAuthException import NotAuthException
from services.AuthService import AuthService

from services.UserService import UserService
from ourkids.ResponseBuilder import ResponseBuilder

class UserController:
    user_routes: Blueprint = Blueprint("user_routes", __name__)
    __url: string = "/users"

    def __init__(self) -> None:
        global service
        service = UserService()

    @user_routes.get(__url + "/<id>")
    def findById(id):
        AuthService.verify(request)
        return ResponseBuilder.success(service.findById(id))

    @user_routes.get(__url)
    def findAll():
        AuthService.verify(request)
        return ResponseBuilder.success(service.findAll()) 

    @user_routes.delete(__url + "/<id>")
    def deleteById(id):
        AuthService.verify(request)
        return ResponseBuilder.voidSuccess(service.deleteById, id)

    @user_routes.post(__url)
    def save():
        return ResponseBuilder.voidSuccess(service.save, request)