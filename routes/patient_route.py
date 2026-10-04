from flask import Blueprint,jsonify,request
from services.patient_service import get_all_patients,get_patient_by_id,create_patient,delete_patient,update_patient,partial_update
from utils.patient_validation import validation_data
patient_bp=Blueprint('patient',__name__,url_prefix='/api/patients')
#GET ALL
@patient_bp.route('/',methods=['GET'])
def get_patients():
    patients,error=get_all_patients()
    result=[]
    if error:
        return jsonify({"error":"Internal Server Error"}),500
    if patients is None:
        return jsonify({"error":"Internal Server Error"}),500
    for patient in patients:
        result.append({
            "patient_id":patient.patient_id,
            "patient_name":patient.patient_name,
            "age":patient.age,
            "gender":patient.gender,
            "disease":patient.disease
        })
    return jsonify({"message":"Patient data retrieved successfully","patients":result}),200
#GET BY ID
@patient_bp.route('/<int:patient_id>',methods=['GET'])
def get_patient_with_id(patient_id):
    patient,error=get_patient_by_id(patient_id)
    if error:
        return jsonify({"error":"Internal server Error"}),500
    if patient is None:
        return jsonify({"error":"Patient not found"}),404

    return jsonify({
        "patient_id":patient.patient_id,
        "patient_name":patient.patient_name,
        "age":patient.age,
        "gender":patient.gender,
        "disease":patient.disease
    }),200

#POST
@patient_bp.route('/',methods=["POST"])
def add_patient():
    new_patient_data=request.get_json()
    if not new_patient_data:
        return jsonify({"error": "Patient not created"}), 400
    #data validation logic
    cleaned_data,error= validation_data(new_patient_data,partial=False)

    if error:
        return jsonify({"error": error}), 400
    created_patient,error = create_patient(
        patient_nm=cleaned_data["patient_name"],
        age=cleaned_data["age"],
        gender=cleaned_data["gender"],
        disease=cleaned_data["disease"]
    )
    if error:
        return jsonify({"error": "Internal Server Error"}), 500

    if  created_patient is None:
        return jsonify({"error":"Internal Server Error"}),500

    return jsonify({"status":"Patient added successfully",
        "patient_id":created_patient.patient_id,
        "patient_name":created_patient.patient_name,
        "age":created_patient.age,
        "gender":created_patient.gender,
        "disease":created_patient.disease

    }),201
#DELETE
@patient_bp.route('/<int:patient_id>',methods=['DELETE'])
def remove_patient(patient_id):
    #error handling
    patient,error=get_patient_by_id(patient_id)
    if error:
        return jsonify({"error":"Internal server Error"}),500
    if  patient is None:
        return jsonify({"error":"Patient not found"}),404
    deleted_patient,error = delete_patient(patient_id)
    if error:
        return jsonify({"error": "Internal Server Error"}),500
    if  deleted_patient is None:
        return jsonify({"error":"Patient not deleted"}),404
    return jsonify({"status":"Patient removed successfully","patient_id":patient_id}),200

#UPDATE
@patient_bp.route('/<int:patient_id>',methods=['PUT'])
def edit_patient(patient_id):
    patient_data=request.get_json()
    #data validation
    if not patient_data:
        return jsonify({"error": "Request body is Required"}),400
    cleaned_data, error = validation_data(patient_data, partial=False)

    if error:
        return jsonify({"error": error}), 400
    update_patiented,error = update_patient(
        patient_id=patient_id,
        patient_name=cleaned_data["patient_name"],
        age=cleaned_data["age"],
        gender=cleaned_data["gender"],
        disease=cleaned_data["disease"]
    )
    if error:
        return jsonify({"error": "Internal Server Error"}),500
    if  update_patiented is None:
        return jsonify({"error": "Patient not found"}),404
    return jsonify({"status":"Patient updated successfully","patient_id":update_patiented.patient_id}),200
#partial update
@patient_bp.route('/<int:patient_id>',methods=['PATCH'])
def partial_update_patient(patient_id):
    data=request.get_json()
    if not data:
        return jsonify({"error":"Request body is Required"}),400
    #patient name validation
    cleaned_data, error = validation_data(data, partial=True)

    if error:
        return jsonify({"error": error}), 400
    #error handling
    patient,error=partial_update(patient_id,cleaned_data)
    if error:
        return jsonify({"error":"Internal server Error"}),500
    if patient is None:
        return jsonify({"error":f"Patient with ID {patient_id} not found"}),404
    return jsonify({"message":"Patient updated successfully",
        "patient_id":patient.patient_id
    }),200
