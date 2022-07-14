
import string

from flask import jsonify
from ourkids.database import DataBase
from entities.complaint import Complaint
from ourkids.NotFoundException import NotFoundException


class ComplaintService(DataBase):
    def __init__(self) -> None:
        super().__init__()

    def findById(self, id: int) -> dict:
        self.sql: string = "SELECT ID, NAME, STATUS, DESCRIPTION FROM COMPLAINT WHERE ID = " + str(id)
        self.cursor.execute(self.sql)

        row = self.cursor.fetchone()
        
        return self.getComplaint(row)

    def deleteById(self, id: int) -> None:
        self.sql: string = "DELETE FROM COMPLAINT WHERE ID = " + str(id)
        self.cursor.execute(self.sql)
        self.commit()

    def findAll(self) -> dict:
        self.sql: string = "SELECT ID, NAME, STATUS, DESCRIPTION FROM COMPLAINT"
        self.cursor.execute(self.sql)

        rows = self.cursor.fetchall()
        
        if rows != None:
            complaints = []

            for row in rows:
                complaints.append(self.getComplaint(row).__dict__)
        else:
            raise NotFoundException("Not found exception")
        
        return complaints   

    def save(self, request) -> None:
        self.sql: string = "INSERT INTO COMPLAINT(NAME, STATUS, DESCRIPTION) VALUES ('{NAME}', {STATUS}, '{DESCRIPTION}')".format(NAME = request.json['name'], STATUS = request.json['status'], DESCRIPTION = request.json['description'])
        self.cursor.execute(self.sql)
        self.commit()

    def getComplaint(self, row) -> Complaint:
        if row != None:
            complaint = Complaint()

            if row[2] == b'\00':
                complaint.status = False
            else:
                complaint.status = True

            complaint.id = row[0]
            complaint.name = row[1]
            complaint.description = row[3]
        else:
            raise NotFoundException("Not found exception")

        return complaint

