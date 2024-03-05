from flask import jsonify, Blueprint, request, current_app
from models import Employee

employee_bp = Blueprint("employee_bp", __name__, url_prefix="/api/employees")

@employee_bp.route("/", methods=["GET"])
def get_employees():
    employees = current_app.mongo.db.employees.find({})
    return jsonify(list(employees)), 200

@employee_bp.route("/<id>", methods=["GET"])
def get_employee(id):
        employee = current_app.mongo.db.employees.find_one({"_id": id})
        if employee:
            return jsonify(employee), 200
        else:
            return jsonify({"error": " " + f"employee with id {id} not found"}), 400

@employee_bp.route("/", methods=["POST"])
def insert_employee():
        body_request = request.get_json()
        if not body_request:
            return jsonify("Please provide all required fields"), 400
        
        new_employee = Employee(
            body_request.get("employee_id"),
            body_request.get("employee_name"),
            body_request.get("assigned_job"),
        ).to_dict()
        
        current_app.mongo.db.employees.insert_one(new_employee)
        return jsonify(new_employee), 201

def init_employee_routes_blueprint(app):
    app.register_blueprint(employee_bp)
