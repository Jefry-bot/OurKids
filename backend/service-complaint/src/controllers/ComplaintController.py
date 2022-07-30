import string
from flask import Blueprint, request
import requests

from services.ComplaintService import ComplaintServiceTxt
from ourkids.ResponseBuilder import ResponseBuilder
from ourkids.NotAuthException import NotAuthException
from entities.complaint import Complaint

class ComplaintController:
    complaint_routes: Blueprint = Blueprint("complaint_routes", __name__)
    __url: string = "/complaints"

    def __init__(self) -> None:
        global service
        service = ComplaintServiceTxt()
        
    @complaint_routes.before_request
    def verify_token_middleware():
        try:
            token = request.headers['Authorization']
            data = requests.get("http://localhost:4001/api/verify/token", headers={"Authorization": token}).json()['exp']
            if data == None:
                NotAuthException("Error")
        except KeyError:
            raise NotAuthException("Error")
        
        
    @complaint_routes.get(__url + "/<id>")
    def findById(id):
        return ResponseBuilder.success(service.findById(id))

    @complaint_routes.get(__url)
    def findAll():
        return ResponseBuilder.success(service.findAll()) 

    @complaint_routes.delete(__url + "/<id>")
    def deleteById(id):
        return ResponseBuilder.voidSuccess(service.deleteById, id)

    @complaint_routes.post(__url)
    def save():
        return ResponseBuilder.voidSuccess(service.save, request)

    @complaint_routes.put(__url + "/<id>")
    def update(id):
        complaint = Complaint(request=request)
        return ResponseBuilder.voidSuccess(service.update, {"id": id, "complaint": complaint})