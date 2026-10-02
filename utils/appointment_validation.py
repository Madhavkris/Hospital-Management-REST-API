from datetime import datetime,date,time
def validation_data(data,partial=False):
    required_fields=['patient_id','doctor_id','appointment_time','appointment_date','status']
    if not partial:
        for field in required_fields:
            if field not in data:
                return None,f"{field} is required"
    cleaned_data = {}
    #patient_id
    if "patient_id" in data:
        patient_id = data["patient_id"]
        if not isinstance(patient_id,int) or isinstance(patient_id,bool):
            return None,"Patient ID must be an integer"
        if patient_id<=0:
            return None,"Patient ID must be greater than 0"
        cleaned_data["patient_id"]=patient_id
    #Doctor id
    if "doctor_id" in data:
        doctor_id = data["doctor_id"]
        if not isinstance(doctor_id,int) or isinstance(doctor_id,bool):
            return None,"Doctor ID must be an integer"
        if doctor_id<=0:
            return None,"Doctor ID must be greater than 0"
        cleaned_data["doctor_id"]=doctor_id
    #time
    if "appointment_time" in data:
        appointment_time = data["appointment_time"]
        if isinstance(appointment_time,str):
            try:
                cleaned_data["appointment_time"]=datetime.strptime(appointment_time,"%H:%M").time()
            except ValueError:
                return None,"Appointment Time must be valid time string"
        elif isinstance(appointment_time,time):
            cleaned_data["appointment_time"]=appointment_time
        else:
            return None,"Appointment Time  must be a time object or a HH:MM string"
    #Date
    if "appointment_date" in data:
        appointment_date = data["appointment_date"]
        if isinstance(appointment_date,str):
            try:
                cleaned_data["appointment_date"]=datetime.strptime(appointment_date,"%Y-%m-%d").date()
            except ValueError:
                return None,"Appointment Date must be valid date string"
        elif isinstance(appointment_date,date):
            cleaned_data["appointment_date"]=appointment_date
        else:
            return None,"Appointment date must be a date object or a YYYY-MM-DD string"
    #status
    if "status" in data:
        appointment_status = data["status"]
        if  not isinstance(appointment_status,str):
            return None,"Appointment status is must be string"
        appointment_status = appointment_status.strip().capitalize()
        if not appointment_status:
            return None,"Appointment status cannot be empty"
        cleaned_data["status"]=appointment_status

    return cleaned_data,None