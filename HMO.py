import json
from start_db import client, db, get_employee_fromDB, insert_one_employee, get_employees


class Employee:
    
    def __init__(self, name, id, address, dateOfBirth, tel, cel, corona, dateOfPositiveTest, recoveryDate) -> None:
        self.name = name
        self.id = id
        self.adrress = {
            "city" : address["city"],
            "street" : address["street"],
            "number" : address["number"]
        }
        self.dateOfBirth = dateOfBirth
        self.tel = tel
        self.cel = cel
        self.corona = list(zip(corona["vaccinations"], corona["manufacturer"], strict=True))
        self.dateOfPositiveTest = dateOfPositiveTest
        self.recoveryDate = recoveryDate


    def normelize(self):
        obj = {
            "name": self.name,
            "id": self.id,
            "address": {
                "city": self.adrress["city"],
                "street": self.adrress["street"],
                "number": self.adrress["number"]
            },
            "dateOfBirth": self.dateOfBirth,
            "Tel": self.tel,
            "CELL": self.cel,
            "corona": {
                "vaccinationsAndMnufacturers" :self.corona,
                "dateOfPositiveTest": self.dateOfPositiveTest,
                "recoveryDate": self.recoveryDate
            }
        }
        return obj


    def add_employee(self):
        ob = self.normelize()
        insert_one_employee(ob)
    

    def get_employee(self, name):
        return get_employee_fromDB(name)


    def get_employee(self): 
        return get_employees()
    

# import from json to db
def import_employees():
    
    collection = db["New_data"]

    with open("data.json", 'r') as f:
        my_data = json.load(f)
        if isinstance(my_data, list):
            collection.insert_many(my_data)
        else:
            collection.insert_one(my_data)


# export data from db to json
def export_employees():
    employees = client.get_database('HMO').get_collection('Emploeeys').find()

    data = [e for e in employees]
    
    fileName = "./export_data.json"
    with open(fileName, 'w', encoding='utf_8') as file:
        file.write("{ \"employees\": ")
        file.write(json.dumps(data, indent=2, default=str))
        file.write("}")
