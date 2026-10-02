def validation_data(data,partial=False):
    required_fields=['doctor_name','specialization','department_id']
    if not partial:
        for field in required_fields:
            if field not in data:
                return None,f"{field} is required"
    cleaned_data={}
    #doctor nmae
    if "doctor_name" in data:
        doctor_name=data["doctor_name"]
        if not isinstance(doctor_name,str):
            return None,"Doctor name must be string"
        doctor_name=doctor_name.strip().capitalize()
        if not doctor_name:
            return None,"Doctor name cannot be empty"
        cleaned_data['doctor_name']=doctor_name
    #specialization
    if "specialization" in data:
        specialization=data["specialization"]
        if not isinstance(specialization,str):
            return None,"Specialization must be string"
        specialization=specialization.strip()
        if not specialization:
            return None,"Specialization cannot be empty"
        cleaned_data['specialization']=specialization
    #department_id
    if "department_id" in data:
        department_id=data["department_id"]
        if not isinstance(department_id,int) or isinstance(department_id,bool):
            return None,"Department id must be integer"
        if department_id<=0:
            return None,"Department ID must be greater than 0"
        cleaned_data['department_id']=department_id
    return cleaned_data,None
