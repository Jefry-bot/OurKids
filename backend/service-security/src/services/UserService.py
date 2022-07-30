
import string

from ourkids.database import DataBase
from entities.user import User
from ourkids.NotFoundException import NotFoundException
from flask import request
from werkzeug.security import generate_password_hash
from os.path import dirname
from entities.user import User

class UserService(DataBase):
    def __init__(self) -> None:
        super().__init__()

    def findById(self, id: int) -> dict:
        self.sql: string = "SELECT ID, USERNAME, STATUS, PASSWORD FROM USER WHERE ID = " + str(id)
        self.cursor.execute(self.sql)

        row = self.cursor.fetchone()
        
        return self.getUser(row)

    def deleteById(self, id: int) -> None:
        self.sql: string = "DELETE FROM USER WHERE ID = " + str(id)
        self.cursor.execute(self.sql)
        self.commit()

    def findAll(self):
        self.sql: string = "SELECT ID, USERNAME, STATUS, PASSWORD FROM USER"
        self.cursor.execute(self.sql)

        rows = self.cursor.fetchall()
        
        if rows != None:
            users = []

            for row in rows:
                users.append(self.getUser(row).__dict__)
        else:
            raise NotFoundException("Not found exception")
        return users   

    def save(self, request: request) -> None:
        self.sql: string = ("INSERT INTO USER(USERNAME, STATUS, PASSWORD)" + 
                            "VALUES ('{USERNAME}', {STATUS}, '{PASSWORD}')".format( 
                                      USERNAME = request.json['username'], 
                                      STATUS = request.json['status'], 
                                      PASSWORD = generate_password_hash(request.json['password'])))
        self.cursor.execute(self.sql)
        self.commit()

    def getUser(self, row) -> User:
        if row != None:
            user = User()

            if row[2] == b'\00':
                user.status = False
            else:
                user.status = True

            user.id = row[0]
            user.username = row[1]
            user.password = row[3]
        else:
            raise NotFoundException("No found exception")

        return user

class UserServiceTxt:
    def __init__(self) -> None:
        self.user_path = dirname(__file__) + '/../database/user.txt'
        self.id_path = dirname(__file__) + '/../database/id_user.txt'

    def commit(self, users):
        with open(self.user_path, 'w') as user_table:
            user_table.writelines(users)

    def id_actual(self):
        with open(self.id_path, 'r') as data:
            id = int(data.readline(4)) + 1
        with open(self.id_path, 'w') as data:
            data.write(str((id)) + "  ")
        return id

    def findAll(self):
        with open(self.user_path) as user_table:
            users = []
            users_data = user_table.readlines()
            
            for object_data in users_data:
                user = User(object_data)
                users.append(user.__dict__)
        return users
            
    def findById(self, id: int):
        users = self.findAll()
        
        for index, user in enumerate(users):
            if str(user['id']) == str(id):
                return users[index]
        raise NotFoundException("Not user found")
            
    def deleteById(self, id: int):
        users = self.findAll()
        self.findAll()
        
        for index, user in enumerate(users):
            if str(user['id']) == str(id):
                del users[index]
        self.commit(User.convert_data(users))

    def update(self, data):
        users = self.findAll()
        
        for index, user in enumerate(users):
            if str(user['id']) == str(data['id']):
                data['user'].id = data['id']
                users[index] = data['user'].__dict__
        self.commit(User.convert_data(users))
        
    def save(self, request):
        users = self.findAll()
        user = User(request=request)
        user.id = self.id_actual()
        users.append(user.__dict__)
        self.commit(User.convert_data(users))