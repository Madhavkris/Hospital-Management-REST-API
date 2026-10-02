def validation_data(data,partial=False):
    required_fields=['department_name']
    if not partial:
        for field in required_fields:
            if field not in data:
                return None,f"{field} is required"
    cleaned_data = {}
    if "department_id" in data:
        department_id = data["department_id"]
        if not isinstance(department_id,int) or isinstance(department_id,bool):
            return None,f"department ID must be integer"
        if department_id<=0:
            return None,"department ID must be greater than 0"
        cleaned_data["department_id"] = department_id
    if "department_name" in data:
        department_name = data["department_name"]
        if not isinstance(department_name,str):
            return None,f"department name must be string"
        department_name= department_name.strip()
        if not department_name:
            return None,"department name cannot be empty"
        cleaned_data["department_name"] = department_name
    return cleaned_data,None
