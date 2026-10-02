def validation_data(data,partial=False):
    #check required fields
    required_fields=['patient_name','age','gender','disease']
    #checked validation
    if not partial:
        for field in required_fields:
            if field not in data:
                return None,f"{field} is required"
    #return cleaned data
    cleaned_data={}
    if "patient_name" in data:
        patient_name=data["patient_name"]
        if not isinstance(patient_name,str):
            return None,"Patient name must be string"
        patient_name=patient_name.strip().capitalize()
        if not patient_name:
            return None,"Patient name cannot be empty"
        cleaned_data["patient_name"]=patient_name
    if "age" in data:
        age=data["age"]
        if   not isinstance(age,int) or   isinstance(age,bool):
            return None,"Age must be integer"
        if not 1<=age<=110:
            return None,"Age must be between 1 and 110"
        cleaned_data["age"]=age
    if "gender" in data:
        gender=data["gender"]
        if not isinstance(gender,str):
            return None,"Gender must be string"
        gender=gender.strip().capitalize()
        if not gender:
            return None,"Gender cannot be empty"
        cleaned_data["gender"]=gender
    if "disease" in data:
        disease=data['disease']
        if not isinstance(disease,str):
            return None,"Disesease must be string"
        disease=disease.strip()
        if not disease:
            return None,"Disease cannot be empty"
        cleaned_data['disease']=disease
    return cleaned_data,None




