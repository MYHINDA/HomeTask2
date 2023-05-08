from pymongo import MongoClient


client = MongoClient(port=27017)
 

def start_db():

    global db
    db_name = "HMO"
    db = client[db_name]

    collection_emploeeys = "Employees"
    
    collection_names = db.list_collection_names()


    if collection_emploeeys in collection_names:
        db.drop_collection(collection_emploeeys)
    db.create_collection(collection_emploeeys)

    global employees_documents
    employees_documents = db[collection_emploeeys]


start_db()

def insertOneEmployee(employee):
        employees_documents.insert_one(employee)


def getEmployeeFromDB(name):
    # get Employee from db
    return employees_documents.find_one({"name":name})


def getEmployees():

    e = list(db.get_collection('Emploeeys').find({}))
    
    return e


# test to insert employees:

# import requests

# resp = requests.get( "https://jsonplaceholder.typicode.com/users", verify=False)
# employees = resp.json()
# for e in employees:
#     employees_documents.insert_one(e)
