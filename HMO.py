import json
from start_db import client, getEmployeeFromDB, insertOneEmployee, getEmployees


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
    

    def addEmployee(self):
        ob = self.normelize()
        insertOneEmployee(ob)
    

    def getEmployee(self, name):
        return getEmployeeFromDB(name)

    def getEmployee(self): 
        return getEmployees()
    


# import from json to db
def importEmployees():
    
    db = client["New_data"]
    collection = db["New_data"]

    file_name = input("Enter file data name: ")
    with open("./" + file_name + ".json", 'r') as f:

        my_data = json.load(f)
        if isinstance(my_data, list):
            collection.insert_many(my_data)
        else:
            collection.insert_one(my_data)


# export data from db to json
def exportEmployees():
    employees = client.get_database('HMO').get_collection('Emploeeys').find()
    data = [e for e in employees]
    fileName = "./exportData.json"
    with open(fileName, 'w', encoding='utf_8') as file:
        file.write("{ \"employees\": ")
        file.write(json.dumps(data, indent=2, default=str))
        file.write("}")









corona = {"vaccinations":['01/01/1000', '02/02/2000',
                          '03/03/3000', '04/04/4000'], "manufacturer":["aa", "bb", "cc", "dd"]}
address = {
    "city": "TLV",
    "street": "begin",
    "number": 111
}

e = Employee("name", 123, address, "01/01/2000", 8856, 5271,\
             corona, '01/02/3000', '02/03/4000')
e1 = Employee("name1", 456, address, "01/01/2000", 8856, 5271,
             corona, '01/02/3000', '02/03/4000')
e2 = Employee("name2", 789, address, "01/01/2000", 8856, 5271,
              corona, '01/02/3000', '02/03/4000')

e.addEmployee()
e1.addEmployee()

# em = e.getEmployee(e.name)
# print(em)

# exportEmployees()

# importEmployees()

# getEmployees()
