from datetime import datetime

from flask import Blueprint,jsonify,request
from services.appointment_service import get_appointment_by_id,get_all_appointments,create_appointments,delete_appointment,update_appointments,partial_update
from utils.appointment_validation import validation_data
from utils.serializers import serialize_appointment
appointment_bp=Blueprint('appointment',__name__,url_prefix="/api/appointments")
#READ ALL/GET ALL
@appointment_bp.route('/',methods=['GET'])
def all_appointments():
    #query parameters
        doctor_id=request.args.get('doctor_id')
        patient_id=request.args.get('patient_id')
        status=request.args.get('status')
        appointment_date=request.args.get('appointment_date')

        parsed_patient_id=patient_id
        parsed_doctor_id=doctor_id
        parsed_appointment_date=appointment_date
        # pagination
        page = request.args.get('page')
        per_page = request.args.get('per_page')
        parsed_page = 1
        parsed_per_page = 10
        if page is not None:
            try:
                parsed_page = int(page)
                if parsed_page < 1:
                    return ValueError
            except ValueError:
                return jsonify({"error": "Page must be an greater than 1"}),400
        if per_page is not None:
            try:
                parsed_per_page = int(per_page)
                if not (1 <= parsed_per_page <= 100):
                    raise ValueError
            except ValueError:
                return jsonify({"error": " Per Page must be an integer between 1 and 100"}),400
        if doctor_id is not None:
            try:
                parsed_doctor_id=int(doctor_id)
            except ValueError:
                return jsonify({"Error":"Doctor ID must be INTEGER"}),400
        if patient_id is not None:
            try:
                parsed_patient_id=int(patient_id)
            except ValueError:
                return jsonify({"Error":"Patient ID must be INTEGER"}),400
        if appointment_date is not None:
            try:
                parsed_appointment_date=datetime.strptime(appointment_date,"%Y-%m-%d").date()
            except ValueError:
                return jsonify({"Error":"Appointment date must be YYYY-MM-DD"}),400
        appointments,error=get_all_appointments(patient_id=parsed_patient_id,doctor_id=parsed_doctor_id,appointment_date=parsed_appointment_date,status=status,page=parsed_page,per_page=parsed_per_page)
        if error:
            return jsonify({"error":"Internal Server Error"}),500
        if  not appointments:
            return jsonify([]),200
        result=[serialize_appointment(appointment) for appointment in appointments]
        return jsonify(result),200


#Read BY ID/GET BY ID
@appointment_bp.route('/<int:appointment_id>',methods=['GET'])
def get_appointment(appointment_id):
    try:
        appointment,error=get_appointment_by_id(appointment_id)
        if error:
            return jsonify({"error":"Internal Server Error"}),500
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

#Create (POST)
@appointment_bp.route('/',methods=['POST'])
def add_appointment():
    new_appointment=request.get_json()
    if not new_appointment:
        return jsonify({"error":"Appointment is not created"}),400
    cleaned_data,errors=validation_data(new_appointment,partial=False)
    if errors:
        return jsonify({"error":errors}),400
    created_appointment,error=create_appointments(
      patient_id=cleaned_data['patient_id'],
      doctor_id=cleaned_data['doctor_id'],
      appointment_date=cleaned_data['appointment_date'],
      appointment_time=cleaned_data['appointment_time'],
      status=cleaned_data['status']
    )
    if error:
        return jsonify({"error":"Internal Server Error"}),500
    if created_appointment is None:
        return jsonify({"error":"Appointment is not created"}),500
    return jsonify({"message":"Appointment created successfully",
                    "appointment_id":created_appointment.appointment_id}),201
#delete
@appointment_bp.route('/<int:appointment_id>',methods=['DELETE'])
def remove_appointment(appointment_id):
    appointment,error=get_appointment_by_id(appointment_id)
    if error:
        return jsonify({"error":"Internal Server Error"}),500
    if  appointment is None:
        return jsonify({"error":"Appointment is not found"}),404
    deleted_appointment,error=delete_appointment(appointment_id)
    if error:
        return jsonify({"error":"Internal Server Error"}),500
    if  deleted_appointment is None:
        return jsonify({"error":"Appointment is not deleted"}),404
    return jsonify({"message":"Appointment deleted successfully","appointment ID":deleted_appointment.appointment_id}),200

#UPDATE(PUT)
@appointment_bp.route('/<int:appointment_id>',methods=['PUT'])
def edit_appointments(appointment_id):
    appointment=request.get_json()
    if not appointment:
        return jsonify({"Error":"Request Body is required"}),400
    cleaned_data,error=validation_data(appointment,partial=False)
    if error:
        return jsonify({"error":error}),400

    updated_appointment,error=update_appointments(
        appointment_id=appointment_id,
        doctor_id=cleaned_data["doctor_id"],
        patient_id=cleaned_data["patient_id"],
        appointment_time=cleaned_data["appointment_time"],
        appointment_date=cleaned_data["appointment_date"],
        status=cleaned_data['status']
    )
    if error:
        return jsonify({"error":"Internal Server Error"}),500
    if  updated_appointment is None:
        return jsonify({"error":"Appointment is not updated"}),404
    return jsonify({"status":"Appointment is updated"}),200

#Partial Update (PATCH)
@appointment_bp.route('/<int:appointment_id>',methods=['PATCH'])
def partial_update_appointment(appointment_id):
    data=request.get_json()
    if not data:
        return jsonify({"error":"Request Body is required"}),400
    cleaned_data,error=validation_data(data,partial=True)
    if error:
        return jsonify({"error":error}),400
    appointment,error=partial_update(appointment_id,cleaned_data)
    if error:
        return jsonify({"error":"Internal Server Error"}),500
    if  appointment is None:
        return jsonify({"error":"Appointment is not updated"}),404
    return jsonify({"message":"Appointment updated successfully"}),200
