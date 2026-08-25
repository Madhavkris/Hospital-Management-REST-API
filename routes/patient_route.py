from urllib import request

from flask import Blueprint,jsonify
from services.patient_service import get_all_patients
patient_bp=Blueprint('patient',__name__,url_prefix='/api/patients')
@patient_bp.route('/',methods=['GET'])
def get_patients():
    patients=get_all_patients()
    if patients is None:
        return jsonify({"error":"Database error"}),500
    return ({"message":"Patient data is retrive successfully","patients":patients}),200
@patient_bp.route('/',methods=['POST'])
def create_patient():
    new_data=request.get_json()
    patient=["patient_name",""]
    if new_data is None:
        return jsonify({"message":"Data fields are missing"}),400
    missing_fields=[]
    for field in patient:
        if field not in new_data:
            missing_fields.append(field)

