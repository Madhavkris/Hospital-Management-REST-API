from flask import Blueprint,jsonify
from services.appointment_service import get_all_appointments,get_appointment_by_id
appointment_bp=Blueprint('appointment',__name__,url_prefix="/api/appointments")
@appointment_bp.route('/',methods=['GET'])
def get_appointments():
    result=get_all_appointments()
    if result is None:
        return jsonify({'error':'Database error'}),500
    return jsonify(result),200
@appointment_bp.route('/<int:appointment_id>',methods=['GET'])
def get_appointment(appointment_id):
    try:
        result=get_appointment_by_id(appointment_id)
        if result is None:
            return jsonify({'error':'Database error'}),500
        return jsonify(result),200
    except Exception as e:
        return jsonify({'error':'Database error'}),500