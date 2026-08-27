from flask import Flask
from database.connection import db
import os
from dotenv import load_dotenv
from urllib.parse import quote_plus

#importing all models

from models.doctor_model import Doctor
from models.appointments_model import Appointment
from models.department_model import Department
from models.patient_model import Patient

#importing routes
from routes.appointment_route import appointment_bp
from routes.patient_route import patient_bp
from routes.department_route import department_bp
from routes.doctor_route import doctor_bp

#returning the load_dot function
load_dotenv()
#creating flask object
app=Flask(__name__)
#converting the password @ into quotes
password=quote_plus(os.getenv("DB_PASSWORD"))
#configuring the SQLAlchemy

app.config["SQLALCHEMY_DATABASE_URI"]=(
    f"mysql+pymysql://"
    f"{os.getenv('DB_USER')}:"
    f"{password}@" #escapes @
    f"{os.getenv('DB_HOST')}:"
    f"{os.getenv('DB_PORT','3306')}/"
    f"{os.getenv('DB_DATABASE')}"
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False
db.init_app(app)
#testing the test cases

#routes
app.register_blueprint(patient_bp)
app.register_blueprint(appointment_bp)
app.register_blueprint(department_bp)
app.register_blueprint(doctor_bp)
if __name__=='__main__':
    app.run(debug=True)