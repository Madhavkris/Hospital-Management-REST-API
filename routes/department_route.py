from flask import Blueprint,jsonify
from services.department_service import get_all_departments
department_bp=Blueprint('department',__name__,url_prefix='/api/departments')
@department_bp.route('/',methods=['GET'])
def get_departments():
    departments=get_all_departments()
    if departments is None:
        return jsonify({"error":"Database error"}),500
    return jsonify(departments),200
