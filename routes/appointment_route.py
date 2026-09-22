from flask import Blueprint,jsonify,request
from services.appointment_service import get_appointment_by_id,get_all_appointments,create_appointments,delete_appointment,update_appointments,partial_update

appointment_bp=Blueprint('appointment',__name__,url_prefix="/api/appointments")
#READ ALL/GET ALL
@appointment_bp.route('/',methods=['GET'])
def all_appointments():
        appointments=get_all_appointments()

        if  not appointments:
            return jsonify([]),200
        result=[]
        for appointment in appointments:
            result.append({
                "appointment_id": appointment.appointment_id,
                "patient_name": appointment.patient.patient_name,
                "doctor_name": appointment.doctor.doctor_name,
                "specialization": appointment.doctor.specialization,
                "department_name": appointment.doctor.department.department_name,
                "appointment_date": str(appointment.appointment_date),
                "appointment_time": str(appointment.appointment_time),
                "status": appointment.status
            })
        return jsonify(result),200


#Read BY ID/GET BY ID
@appointment_bp.route('/<int:appointment_id>',methods=['GET'])
def get_appointment(appointment_id):
    try:
        appointment=get_appointment_by_id(appointment_id)
        if appointment is None:
            return jsonify({'error':'Appointment not found'}),404
        return jsonify({
            "appointment_id":appointment.appointment_id,
            "patient_name": appointment.patient.patient_name,
            "doctor_name": appointment.doctor.doctor_name,
            "specialization":appointment.doctor.specialization,
            "department_name": appointment.doctor.department.department_name,
            "appointment_date":str(appointment.appointment_date),
            "appointment_time":str(appointment.appointment_time),
            "status":appointment.status
        }), 200
    except Exception as e:
        print(e)
        return jsonify({'error':str(e)}),500

#Create
@appointment_bp.route('/',methods=['POST'])
def add_appointment():
    new_appointment=request.get_json()
    if not new_appointment:
        return jsonify({"error":"Appointment is not created"}),400
    created_appointment=create_appointments(
      patient_id=new_appointment.get('patient_id'),
      doctor_id=new_appointment.get('doctor_id'),
      appointment_date=new_appointment.get('appointment_date'),
      appointment_time=new_appointment.get('appointment_time'),
      status=new_appointment.get('status')
    )
    if created_appointment is None:
        return jsonify({"error":"Appointment is not created"}),400
    return jsonify({"message":"Appointment created successfully",
                    "appointment_id":created_appointment.appointment_id}),201
#delete
@appointment_bp.route('/<int:appointment_id>',methods=['DELETE'])
def remove_appointment(appointment_id):
    appointment=get_appointment_by_id(appointment_id)
    if not appointment:
        return jsonify({"error":"Appointment is not found"}),404
    deleted_appointment=delete_appointment(appointment_id)
    if not deleted_appointment:
        return jsonify({"error":"Appointment is not deleted"}),400
    return jsonify({"message":"Appointment deleted successfully","appointment ID":deleted_appointment.appointment_id}),200

#UPDATE
@appointment_bp.route('/<int:appointment_id>',methods=['PUT'])
def edit_appointments(appointment_id):
    appointment=request.get_json()
    if not appointment:
        return jsonify({"Error":"Request Body is required"}),400
    doctor_id = appointment.get('doctor_id')
    patient_id = appointment.get('patient_id')
    update_appointment_time=appointment.get('appointment_time')
    update_appointment_date=appointment.get('appointment_date')
    update_appointment_status=appointment.get('status')

    updated_appointment=update_appointments(
        appointment_id=appointment_id,
        doctor_id=doctor_id,
        patient_id=patient_id,
        appointment_time=update_appointment_time,
        appointment_date=update_appointment_date,
        status=update_appointment_status
    )
    if not updated_appointment:
        return jsonify({"error":"Appointment is not updated"}),404
    return jsonify({"status":"Appointment is updated"}),200

@appointment_bp.route('/<int:appointment_id>',methods=['PATCH'])
def partial_update_appointment(appointment_id):
    data=request.get_json()
    if not data:
        return jsonify({"error":"Request Body is required"}),400
    appointment=partial_update(appointment_id,data)
    if not appointment:
        return jsonify({"error":"Appointment is not updated"}),404
    return jsonify({"message":"Appointment updated successfully"}),200
