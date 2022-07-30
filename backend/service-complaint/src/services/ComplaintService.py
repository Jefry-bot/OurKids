
import string

from flask import jsonify
from ourkids.database import DataBase
from entities.complaint import Complaint
from ourkids.NotFoundException import NotFoundException
from os.path import dirname
from entities.complaint import Complaint


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

class ComplaintServiceTxt:
    def __init__(self) -> None:
        self.complaint_path = dirname(__file__) + '/../database/complaint.txt'
        self.id_path = dirname(__file__) + '/../database/id_complaint.txt'

    def commit(self, complaints):
        with open(self.complaint_path, 'w') as complaint_table:
            complaint_table.writelines(complaints)

    def id_actual(self):
        with open(self.id_path, 'r') as data:
            id = int(data.readline(4)) + 1
        with open(self.id_path, 'w') as data:
            data.write(str((id)) + "  ")
        return id

    def findAll(self):
        with open(self.complaint_path) as complaint_table:
            complaints = []
            complaints_data = complaint_table.readlines()
            
            for object_data in complaints_data:
                complaint = Complaint(object_data)
                complaints.append(complaint.__dict__)
        return complaints
            
    def findById(self, id: int):
        complaints = self.findAll()
        
        for index, complaint in enumerate(complaints):
            if str(complaint['id']) == str(id):
                return complaints[index]
        raise NotFoundException("Not complaint found")
            
    def deleteById(self, id: int):
        complaints = self.findAll()
        
        for index, complaint in enumerate(complaints):
            if str(complaint['id']) == str(id):
                del complaints[index]
        self.commit(Complaint.convert_data(complaints))

    def update(self, data):
        complaints = self.findAll()
        
        for index, complaint in enumerate(complaints):
            if str(complaint['id']) == str(data['id']):
                data['complaint'].id = data['id']
                complaints[index] = data['complaint'].__dict__
        self.commit(Complaint.convert_data(complaints))
        
    def save(self, request):
        complaints = self.findAll()
        complaint = Complaint(request=request)
        complaint.id = self.id_actual()
        complaints.append(complaint.__dict__)
        self.commit(Complaint.convert_data(complaints))