from flask import Flask, jsonify, request
import requests
import HMO
from bson import json_util
import json


app = Flask(__name__)


# get employees
@app.route('/', methods=['GET'])
def get_employees():
    # return jsonify(HMO.getEmployees())
    return json.loads(json_util.dumps(HMO.getEmployees()))


#Get 1 employee by his name
@app.route('/employees/<string:name>', methods=['GET'])
def get_employee(name):
    return json.loads(json_util.dumps(HMO.getEmployeeFromDB(name)))


#Add new employee
@app.route('/employees', methods=['POST'])
def add_employee():
    # r  = request.get_json()
    # resp = requests.post("https://127.0.0.1:5000", r, verify=False)
    HMO.insertOneEmployee(HMO.e2)
    return "created"


app.run()