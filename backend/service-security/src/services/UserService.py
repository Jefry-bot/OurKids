
import string

from ourkids.database import DataBase
from entities.user import User
from ourkids.NotFoundException import NotFoundException
from flask import request
from werkzeug.security import generate_password_hash


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
