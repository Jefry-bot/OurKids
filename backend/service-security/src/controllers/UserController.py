import string
from flask import Blueprint, request
from ourkids.NotAuthException import NotAuthException
from services.AuthService import AuthService

from services.UserService import UserServiceTxt
from ourkids.ResponseBuilder import ResponseBuilder
from entities.user import User

class UserController:
    user_routes: Blueprint = Blueprint("user_routes", __name__)
    __url: string = "/users"

    def __init__(self) -> None:
        global service
        service = UserServiceTxt()

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

    @user_routes.put(__url + "/<id>")
    def update(id):
        user = User(request=request)
        return ResponseBuilder.voidSuccess(service.update, {"id": id, "user": user})