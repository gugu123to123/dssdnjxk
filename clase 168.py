class Citizen:
    def __init__(self,name,age,dob,id_number):
        self.citizen_name = name
        self.citizen_age = age
        self.citizen_dob = dob
        self.citizen_id = id_number
        
    def add_citizen(self):
        print("Name: "+self.citizen_name)
        print("Age: "+str(self.citizen_age))
        print("Date of birth: "+self.citizen_dob)
        print("Citizen Id: "+self.citizen_id)
        print("Citizen Added")
        
citizen1 = Citizen("chuchitanuel",1000000000,"23 de enero del 1","23")
citizen1.add_citizen()