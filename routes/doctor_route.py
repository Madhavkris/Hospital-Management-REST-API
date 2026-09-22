from flask import Blueprint,jsonify,request
from services.doctor_service import get_all_doctors,get_doctor_by_id,create_doctor,delete_doctor,update_doctor,partial_update
doctor_bp=Blueprint('doctor',__name__,url_prefix='/api/doctors')
#GET ALL
@doctor_bp.route('/',methods=['GET'])
def get_doctors():
    doctors=get_all_doctors()
    if doctors is None:
        return jsonify({"error":"Database error"}),500
    result=[]
    for doctor in doctors:
        result.append({
            "doctor_id":doctor.doctor_id,
            "doctor_name":doctor.doctor_name,
            "specialization":doctor.specialization,
            "department":doctor.department.department_name
        })
    return jsonify(result),200
#GET BY ID
@doctor_bp.route('/<int:doctor_id>',methods=['GET'])
def get_doctor_with_id(doctor_id):
    doctor=get_doctor_by_id(doctor_id)
    if doctor is None:
        return jsonify({"error":"Doctor not found"}),404
    return jsonify({
        "doctor_id": doctor.doctor_id,
        "doctor_name": doctor.doctor_name,
        "specialization": doctor.specialization,
        "department": doctor.department.department_name
    }),200
#CREATE
@doctor_bp.route('/',methods=['POST'])
def add_doctor():
    new_doctor=request.get_json()
    if new_doctor is None:
        return jsonify({"error":"Doctor is not added"}),400
    created_doctor=create_doctor(
        doctor_name=new_doctor.get("doctor_name"),
        specialization=new_doctor.get("specialization"),
        department_id=new_doctor.get("department_id")
    )
    if created_doctor is None:
        return jsonify({"error":"Doctor is not created"}),400
    return jsonify({
        "status":"Doctor is added successfully",
        "doctor_id": created_doctor.doctor_id,
        "specialization": created_doctor.specialization,
        "department_id": created_doctor.department.department_id

    }),201
#DELETE
@doctor_bp.route('/<int:doctor_id>',methods=['DELETE'])
def remove_doctor(doctor_id):
    doctor=get_doctor_by_id(doctor_id)
    if doctor is None:
        return jsonify({"error":"Doctor not found"}),404
    target=doctor.doctor_id
    deleted_doctor=delete_doctor(doctor_id)
    if not deleted_doctor:
        return jsonify({"error":"Doctor not deleted"}),400
    return jsonify({"status":"Doctor removed successfully","doctor_id":target}),200
#UPDATE
@doctor_bp.route('/<int:doctor_id>',methods=['PUT'])
def edit_doctor(doctor_id):
    doctor=request.get_json()
    if doctor is None:
        return jsonify({"error":"Request body is required"}),400
    updated_doctor_name=doctor.get('doctor_name')
    updated_specialization=doctor.get('specialization')
    updated_department=doctor.get("department_id")
    updated=update_doctor(
        doctor_id=doctor_id,
        doctor_name=updated_doctor_name,
        specialization=updated_specialization,
        department_id=updated_department
    )
    if updated is None:
        return jsonify({"error":"Doctor not updated"}),400
    return jsonify({"status":"Doctor updated successfully"}),200
#PARTISL UPDATED
@doctor_bp.route('/<int:doctor_id>',methods=['PATCH'])
def partial_update_doctor(doctor_id):
    data=request.get_json()
    if not data:
        return jsonify({"error":"Request body is required"}),400
    doctor=partial_update(doctor_id,data)
    if doctor is None:
        return jsonify({"error":f"Doctor with ID {doctor_id} not found"}),404
    return jsonify({"status":"Doctor updated successfully"}),200
