from datetime import datetime, timedelta
from os import getenv
from services.UserService import UserService
from werkzeug.security import check_password_hash
from jwt import encode, decode
from jwt import exceptions
from ourkids.NotAuthException import NotAuthException

class AuthService:
    @staticmethod
    def write_token(data: dict):
        token = encode(payload={**data, "exp": AuthService.expire_date(1)}, 
                       key=getenv('SECRET'), algorithm = "HS256")
        return token
        
    @staticmethod
    def expire_date(days: int):
        now = datetime.now()
        expire = now + timedelta(days)

        return expire

    @staticmethod
    def validate_token(token, output = False):
        if output:
            return decode(token, key=getenv('SECRET'), algorithms = ["HS256"])
        decode(token, key=getenv('SECRET'), algorithms = ["HS256"])

    @staticmethod
    def validateUser(data: any):
        service = UserService()
        users = service.findAll()

        for user in users:
            if data['username'] == user['username'] and check_password_hash(user['password'], data['password']):
                return True
        return False 
    
    @staticmethod
    def verify(request):
        try:
            token = request.headers['Authorization'].split(" ")[1]
        except KeyError:
            raise NotAuthException("Error")
        AuthService.validate_token(token, output = False)