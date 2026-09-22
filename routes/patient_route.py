from urllib import request
from flask import Blueprint,jsonify,request
from services.patient_service import get_all_patients,get_patient_by_id,create_patient,delete_patient,update_patient,partial_update

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

@patient_bp.route('/<int:patient_id>',methods=['DELETE'])
def remove_patient(patient_id):
    patient=get_patient_by_id(patient_id)
    if not patient:
        return jsonify({"error":"Patient not found"}),404
    target_id=patient_id
    deleted_patient = delete_patient(patient_id)
    if not deleted_patient:
        return jsonify({"error":"Patient not deleted"}),400
    return jsonify({"status":"Patient removed successfully","patient_id":target_id}),200


@patient_bp.route('/<int:patient_id>',methods=['PUT'])
def edit_patient(patient_id):
    patient=request.get_json()
    if not patient:
        return jsonify({"error":"Request body is Required"}),400
    updated_patient_name=patient.get('patient_name')
    updated_age=patient.get('age')
    updated_gender=patient.get('gender')
    updated_disease=patient.get('disease')
    updated_patient = update_patient(
        patient_id=patient_id,
        patient_name=updated_patient_name,
        age=updated_age,
        gender=updated_gender,
        disease=updated_disease
    )
    if not updated_patient:
        return jsonify({"error":"Patient not updated"}),400
    return jsonify({"status":"Patient updated successfully","patient_id":updated_patient.patient_id}),200

@patient_bp.route('/<int:patient_id>',methods=['PATCH'])
def partial_update_patient(patient_id):
    data=request.get_json()
    if not data:
        return jsonify({"error":"Request body is Required"}),400
    patient=partial_update(patient_id,data)
    if not patient:
        return jsonify({"error":f"Patient with ID {patient_id} not found"}),404
    return jsonify({"message":"Patient updated successfully",
        "patient_id":patient.patient_id
    }),200
