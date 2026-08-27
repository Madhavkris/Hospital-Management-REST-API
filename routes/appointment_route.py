from flask import Blueprint,jsonify,request
from services.appointment_service import get_appointment_by_id,get_all_appointments,create_appointments

appointment_bp=Blueprint('appointment',__name__,url_prefix="/api/appointments")
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