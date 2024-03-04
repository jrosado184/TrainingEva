import os
from flask import Flask
from dotenv import load_dotenv
from pymongo import MongoClient
from routes.employee_routes import init_employee_routes

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")

app = Flask(__name__)
app.config["MONGO_URI"] = MONGO_URI

client = MongoClient(MONGO_URI)
db = client["development"]
employees = db["employees"]

init_employee_routes(app, employees)

if __name__ == "__main__":
    app.run(debug=True)
