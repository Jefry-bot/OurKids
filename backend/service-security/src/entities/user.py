class User:
    def __init__(self, data: str = None, request = None) -> None:
        if data:
            params = data.split(",")
            self.id = int(params[0])
            self.username = params[1]
            self.password = params[2]
            self.email = params[3]
            
            if (int(params[4]) == 1 ):
                self.status = True
            else:
                self.status = False
        if request:
            json = request.get_json()
            self.username = json['username']
            self.password = json['password']
            self.email = json['email']

            if (json['status']):
                self.status = True
            else:
                self.status = False
        
    @staticmethod
    def convert_single_data(user) -> str:
        status = 0

        if user['status']:
            status = 1

        user_data = (str(user['id']) + ',' + 
                       user['username'] + ',' +
                       user['password'] + ',' + 
                       user['email'] + "," + 
                       str(status))
        return user_data
    
    @staticmethod
    def convert_data(users) -> list:
        users_data = []
        
        for index, user in enumerate(users):
            if index == (len(users) - 1):
                users_data.append(User.convert_single_data(user))
            else:     
                users_data.append(User.convert_single_data(user) + '\n')
            
        return users_data