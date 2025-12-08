from flask import Flask, request, jsonify

app=Flask(__name__)

employees=[
    {
        "id":1,
        "first_name":"John",
        "last_name":"Doe",
        "email":"johndoe12@gmail.com",
        "position":"Software Engineer",
        "salary":50000,
    },
    {
        "id":2,
        "first_name":"Jane",
        "last_name":"Hopper",
        "email":"janehopper12@gmail.com",
        "position":"Product Manager",
        "salary":100000,
    }
]


# GET all employees
@app.route("/employees", methods=["GET"])
def get_employees():
    return jsonify(employees)

# GET employee by id
@app.route("/employees/<int:emp_id>", methods=["GET"])
def get_employee(emp_id):
    for emp in employees:
        if emp["id"] == emp_id:
            return jsonify(emp)
    return jsonify({"error": "Employee not found"}), 404

#POST add new employee
@app.route("/employees", methods=["POST"])
def add_employee():
    data = request.get_json()
    new_id = max(emp["id"] for emp in employees) + 1 if employees else 1
    data["id"] = new_id
    employees.append(data)
    return jsonify({"message": "Employee added", "employee": data}), 201


@app.route("/employees/<int:emp_id>", methods=["PUT"])
def update_employee(emp_id):
    data = request.get_json()
    for emp in employees:
        if emp["id"] == emp_id:
            emp.update(data)
            return jsonify({"message": "Employee updated", "employee": emp})
    return jsonify({"error": "Employee not found"}), 404

# DELETE employee by id
@app.route("/employees/<int:emp_id>", methods=["DELETE"])
def delete_employee(emp_id):
    for emp in employees:
        if emp["id"] == emp_id:
            employees.remove(emp)
            return jsonify({"message": "Employee deleted"})
    return jsonify({"error": "Employee not found"}), 404

if __name__=="__main__":
    app.run(debug=True)