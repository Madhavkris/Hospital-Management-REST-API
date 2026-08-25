from flask import Blueprint,jsonify
from services.doctor_service import get_all_doctors
doctor_bp=Blueprint('doctor',__name__,url_prefix='/api/doctors')
@doctor_bp.route('/',methods=['GET'])
def get_doctors():
    doctors=get_all_doctors()
    if doctors is None:
        return jsonify({"error":"Database error"}),500
    return jsonify(doctors),200
