
import string

class User:
    id: int
    username: string 
    status: bool 
    password: string

    def __init__(self, id: int = None, 
                       username: string = None, 
                       status: bool = None, 
                       password: string = None) -> None:
        self.id = id
        self.username = username
        self.status = status
        self.password = password