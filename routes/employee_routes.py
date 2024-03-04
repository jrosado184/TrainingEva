from flask import jsonify, request
from models import Employee

def init_employee_routes(app, employees):
    def get_employees():
        return jsonify(list(employees.find({}))), 200

    def get_employee(id):
        employee = employees.find_one({"_id": id})
        if employee:
            return jsonify(employee), 200
        else:
            return jsonify({"error": " " + f"employee with id {id} not found"}), 400

    def insert_employee():
        body_request = request.get_json()
        if not body_request:
            return jsonify("Please provide all required fields"), 400
        
        new_employee = Employee(
            body_request.get("employee_id"),
            body_request.get("employee_name"),
            body_request.get("assigned_job"),
        ).to_dict()
        
        employees.insert_one(new_employee)
        return jsonify(new_employee), 201

    app.add_url_rule("/employees", view_func=get_employees, methods=["GET"])
    app.add_url_rule("/employees/<id>", view_func=get_employee, methods=["GET"])
    app.add_url_rule("/employees", view_func=insert_employee, methods=["POST"])
