class Complaint:
    def __init__(self, data: str = None, request = None) -> None:
        if data:
            params = data.split(",")
            self.id = int(params[0])
            self.name = params[1]
            self.description = params[2]
            self.content = params[3]
            self.person = params[4]
            self.day = params[5]
            self.problem = params[6]
            self.requirement = params[7]
            self.fathers = int(params[8])
        if request:
            json = request.get_json()
            self.name = json['name']
            self.description = json['description']
            self.content = json['content']
            self.person = json['person']
            self.day = json['day']
            self.problem = json['problem']
            self.requirement = json['requirement']
            self.fathers = int(json['fathers'])
        
    @staticmethod
    def convert_single_data(complaint) -> str:
        complaint_data = (str(complaint['id']) + ',' + 
                       complaint['name'] + ',' +
                       complaint['description'] + ',' + 
                       complaint['content'] + "," + 
                       complaint['person'] + "," + 
                       complaint['day'] + "," + 
                       complaint['problem'] + "," + 
                       complaint['requirement'] + "," + 
                       str(complaint['fathers']))
        return complaint_data
    
    @staticmethod
    def convert_data(complaints) -> list:
        complaints_data = []
        
        for index, complaint in enumerate(complaints):
            if index == (len(complaints) - 1):
                complaints_data.append(Complaint.convert_single_data(complaint))
            else:     
                complaints_data.append(Complaint.convert_single_data(complaint) + '\n')
            
        return complaints_data