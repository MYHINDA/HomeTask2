from flask import Flask, redirect, url_for, request
from bson import json_util
import json
from markupsafe import escape


import HMO
import background


app = Flask(__name__)

# get employees
@app.route('/', methods=['GET'])
def get_employees():
    # return jsonify(HMO.getEmployees())
    return json.loads(json_util.dumps(HMO.get_employees()))


#Get 1 employee by his name
@app.route("/employeeName", methods=['POST'])
def get_employee():
    
    name = request.form["name"]
    
    data = HMO.get_employee_fromDB(escape(name))
    
    return json.loads(json_util.dumps(data))


#Add new employee
@app.route('/success/<name>')
def success(name):
   return 'welcome %s' % name


@app.route('/employee', methods=['POST'])
def employee():
    employee = {}
    employee["id"] = request.form["id"]
    employee["name"] = request.form['nm']
    employee["address"] = {
        "city": request.form["city"],
        "street":request.form["street"],
        "number": request.form["number"]
        }
    employee["date"] = request.form['dateOfBirth']
    employee["tel"] = request.form['tel']
    employee["cell"] = request.form['cell']
    employee["corona"] = {
        "vaccinationsAndMnufacturers":[
            [request.form["v1"], request.form["m1"]],
            [request.form["v2"], request.form["m2"]],
            [request.form["v3"], request.form["m3"]],
            [request.form["v4"], request.form["m4"]]
        ],
        "dateOfPositiveTest": request.form["positive"],
        "recoveryDate": request.form["recovery"]
    }
    if request.form["avatar"]:
        employee["image"] = request.form["avatar"]

    HMO.insert_one_employee(employee)

    return redirect(url_for('success', name=employee["name"]))
   
app.run()
