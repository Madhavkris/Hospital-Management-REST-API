from flask import Blueprint,jsonify,request
from services.department_service import get_all_departments,get_department_by_id,create_department,update_department,partial_update
department_bp=Blueprint('department',__name__,url_prefix='/api/departments')
@department_bp.route('/',methods=['GET'])
def get_departments():
    departments=get_all_departments()
    if departments is None:
        return jsonify([]),200
    result=[]
    for department in departments:
        result.append({
            "department_id":department.department_id,
            "department_name":department.department_name,
            "doctors":[ doctor.doctor_name for doctor in department.doctors ]        })
    return jsonify(result),200

@department_bp.route('/<int:department_id>',methods=['GET'])
def get_department_with_id(department_id):
    department=get_department_by_id(department_id)
    if department is None:
        return jsonify({"error":"Department not found"}),404
    return jsonify({"department_id":department.department_id,
                    "department_name":department.department_name,
                    "doctors":[doctor.doctor_name for doctor in department.doctors ] }),200

#
@department_bp.route('/',methods=['POST'])
def add_department():
    new_department=request.get_json()
    if not new_department:
        return jsonify({"error":"Department not created"}),400
    created_department=create_department(department_name=new_department.get('department_name'))

    if not created_department:
        return jsonify({"error":"Department not created"}),400
    return jsonify({
        "status":"Department created",
        "department_name":created_department.department_name,}),201


#update
@department_bp.route('/<int:department_id>',methods=['PUT'])
def edit_department(department_id):
    department=request.get_json()
    if not department:
        return jsonify({"Error":"Request body is required"}),400
    update_department_name=department.get('department_name')
    updated_department=update_department(
        department_id=department_id,
        department_name=update_department_name
    )
    if not updated_department:
        return jsonify({"Error":"Department not found"}),404
    return jsonify({"status":"Department updated successfully"}),200

@department_bp.route("/<int:department_id>",methods=['PATCH'])
def partial_update_department(department_id):
    data=request.get_json()
    if not data:
        return jsonify({"Error":"Request body is required"}),400
    department=partial_update(department_id,data)
    if not department:
        return jsonify({"Error":"Department not found"}),404
    return jsonify({"status":"Department Partial Updated successfully"}),200

