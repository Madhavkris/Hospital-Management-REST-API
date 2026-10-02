from flask import Blueprint,jsonify,request
from services.patient_service import get_all_patients,get_patient_by_id,create_patient,delete_patient,update_patient,partial_update
from utils.patient_validation import validation_data
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
        return jsonify({"error": "Patient not created"}), 400
    #data validation logic
    cleaned_data,error= validation_data(new_patient_data,partial=False)

    if error:
        return jsonify({"error": error}), 400
    created_patient = create_patient(
        patient_nm=cleaned_data["patient_name"],
        age=cleaned_data["age"],
        gender=cleaned_data["gender"],
        disease=cleaned_data["disease"]
    )

    if not created_patient:
        return jsonify({"error":"Patient not created"}),404

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
    deleted_patient = delete_patient(patient_id)
    if not deleted_patient:
        return jsonify({"error":"Patient not deleted"}),400
    return jsonify({"status":"Patient removed successfully","patient_id":patient_id}),200


@patient_bp.route('/<int:patient_id>',methods=['PUT'])
def edit_patient(patient_id):
    patient_data=request.get_json()
    if not patient_data:
        return jsonify({"error": "Request body is Required"}),400
    cleaned_data, error = validation_data(patient_data, partial=False)

    if error:
        return jsonify({"error": error}), 400
    update_patiented = update_patient(
        patient_id=patient_id,
        patient_name=cleaned_data["patient_name"],
        age=cleaned_data["age"],
        gender=cleaned_data["gender"],
        disease=cleaned_data["disease"]
    )

    if not update_patiented:
        return jsonify({"error": "Patient not found"}), 404
    return jsonify({"status":"Patient updated successfully","patient_id":update_patiented.patient_id}),200

@patient_bp.route('/<int:patient_id>',methods=['PATCH'])
def partial_update_patient(patient_id):
    data=request.get_json()
    if not data:
        return jsonify({"error":"Request body is Required"}),400
    #patient name validation
    cleaned_data, error = validation_data(data, partial=True)

    if error:
        return jsonify({"error": error}), 400

    patient=partial_update(patient_id,cleaned_data)
    if not patient:
        return jsonify({"error":f"Patient with ID {patient_id} not found"}),404
    return jsonify({"message":"Patient updated successfully",
        "patient_id":patient.patient_id
    }),200
