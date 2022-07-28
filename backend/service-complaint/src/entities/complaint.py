
import email
import string

class Complaint:
    id: int
    name: string 
    status: bool 
    description: string

    def __init__(self, id: int = None, 
                       name: string = None, 
                       status: bool = None, 
                       description: string = None) -> None:
        self.id = id
        self.name = name
        self.status = status
        self.description = description