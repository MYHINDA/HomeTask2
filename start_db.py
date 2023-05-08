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

def insert_one_employee(employee):
        employees_documents.insert_one(employee)


def get_employee_fromDB(name):
    # get Employee from db
    return employees_documents.find_one({"name":name})


def get_employees():

    e = list(db.get_collection('Employees').find({}))
    return e
