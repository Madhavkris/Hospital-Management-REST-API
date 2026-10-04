from flask import Blueprint,jsonify,request
from services.department_service import get_all_departments,get_department_by_id,create_department,update_department,partial_update
from utils.department_validation import validation_data
department_bp=Blueprint('department',__name__,url_prefix='/api/departments')
@department_bp.route('/',methods=['GET'])
def get_departments():
    departments,error=get_all_departments()
    if error:
        return jsonify({"error":"Internal Server Error"}),500
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
    department,error=get_department_by_id(department_id)
    if error:
        return jsonify({"error":"Internal Server Error"}),500
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
    cleaned_data,error=validation_data(new_department,partial=False)
    if error:
        return jsonify({"error":error}),400
    created_department,error=create_department(department_name=cleaned_data['department_name'])
    if error:
        return jsonify({"error":"Internal Server Error"}),500
    if created_department is None:
        return jsonify({"error":"Internal Server Error"}),500
    return jsonify({
        "status":"Department created",
        "department_name":created_department.department_name,}),201


#update
@department_bp.route('/<int:department_id>',methods=['PUT'])
def edit_department(department_id):
    department=request.get_json()
    if not department:
        return jsonify({"Error":"Request body is required"}),400
    cleaned_data,error=validation_data(department,partial=False)
    if error:
        return jsonify({"error":error}),400
    updated_department,error=update_department(
        department_id=department_id,
        department_name=cleaned_data['department_name']
    )
    if error:
        return jsonify({"error":"Internal Server Error"}),500
    if  updated_department is None:
        return jsonify({"Error":"Department not found"}),404
    return jsonify({"status":"Department updated successfully"}),200

@department_bp.route("/<int:department_id>",methods=['PATCH'])
def partial_update_department(department_id):
    data=request.get_json()
    if not data:
        return jsonify({"Error":"Request body is required"}),400
    cleaned_data,error=validation_data(data,partial=True)
    if error:
        return jsonify({"error":error}),400
    department,error=partial_update(department_id,cleaned_data)
    if error:
        return jsonify({"error":"Internal Server Error"}),500
    if  department is None:
        return jsonify({"Error":"Department not found"}),404
    return jsonify({"status":"Department Partial Updated successfully"}),200

