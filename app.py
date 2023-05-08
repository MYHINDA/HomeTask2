from flask import Flask, redirect, url_for, request
import HMO
from bson import json_util
import json


app = Flask(__name__)


# get employees
@app.route('/', methods=['GET'])
def get_employees():
    # return jsonify(HMO.getEmployees())
    return json.loads(json_util.dumps(HMO.get_employees()))


#Get 1 employee by his name
@app.route('/employees/<string:name>', methods=['GET'])
def get_employee(name):
    return json.loads(json_util.dumps(HMO.get_employee_fromDB(name)))


#Add new employee

@app.route('/success/<name>')
def success(name):
   return 'welcome %s' % name


@app.route('/employee', methods=['POST'])
def employee():
    employee = {}
    employee["id"] = request.form["id"]
    employee["name"] = request.form['nm']
    employee["tel"] = request.form['tel']
    HMO.insert_one_employee(employee)

    return redirect(url_for('success', name=employee["id"]))
   
app.run(debug=True)
