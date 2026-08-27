from urllib import request

from flask import Blueprint,jsonify,request
from services.patient_service import get_all_patients,get_patient_by_id,create_patient
patient_bp=Blueprint('patient',__name__,url_prefix='/api/patients')
@patient_bp.route('/',methods=['GET'])
def get_patients():
    patients=get_all_patients()
    result=[]
    if patients is None:
        return jsonify({"error":"Patient not found"}),404
    for patient in patients:
        result.append({
            "patient_id":patient.patient_id,
            "patient_name":patient.patient_name,
            "age":patient.age,
            "gender":patient.gender,
            "disease":patient.disease
        })
    return jsonify({"message":"Patient data retrieved successfully","patients":result}),200

@patient_bp.route('/<int:patient_id>',methods=['GET'])
def get_patient_with_id(patient_id):
    patient=get_patient_by_id(patient_id)
    if patient is None:
        return jsonify({"error":"Patient not found"}),404
    return jsonify({
        "patient_id":patient.patient_id,
        "patient_name":patient.patient_name,
        "age":patient.age,
        "gender":patient.gender,
        "disease":patient.disease
    }),200
@patient_bp.route('/',methods=["POST"])
def add_patient():
    new_patient_data=request.get_json()

    if not new_patient_data:
        return jsonify({"error":"Patient not created"}),400
    created_patient = create_patient(
        patient_nm=new_patient_data.get('patient_name'),
        age=new_patient_data.get('age'),
        gender=new_patient_data.get('gender'),
        disease=new_patient_data.get('disease')
    )

    if not created_patient:
        return jsonify({"error":"Patient not created"}),400

    return jsonify({"status":"Patient added successfully",
        "patient_id":created_patient.patient_id,
        "patient_name":created_patient.patient_name,
        "age":created_patient.age,
        "gender":created_patient.gender,
        "disease":created_patient.disease

    }),201