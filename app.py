import os
from flask import Flask
from dotenv import load_dotenv
from flask_pymongo import PyMongo
from routes.employee_routes import init_employee_routes_blueprint

load_dotenv()

def create_app():
    app = Flask(__name__)
    app.config["MONGO_URI"] = os.environ.get("MONGO_URI")

    mongo = PyMongo(app)
    app.mongo = mongo

    init_employee_routes_blueprint(app)

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
