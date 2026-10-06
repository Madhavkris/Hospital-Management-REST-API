def serialize_patient(patient):
    return {
        "patient_id":patient.patient_id,
        "patient_name":patient.patient_name,
        "age":patient.age,
        "gender":patient.gender,
        "disease":patient.disease
    }
#doctors
def serialize_doctor(doctor):
    return{
        "doctor_id": doctor.doctor_id,
        "doctor_name": doctor.doctor_name,
        "specialization": doctor.specialization,
        "department": doctor.department.department_name
    }

#appointments
def serialize_appointment(appointment):
    return{
        "appointment_id": appointment.appointment_id,
        "patient_name": appointment.patient.patient_name,
        "doctor_name": appointment.doctor.doctor_name,
        "specialization": appointment.doctor.specialization,
        "department_name": appointment.doctor.department.department_name,
        "appointment_date": str(appointment.appointment_date),
        "appointment_time": str(appointment.appointment_time),
        "status": appointment.status
    }

#department
def serialize_department(department):
    return {
        "department_id": department.department_id,
        "department_name": department.department_name,
        "doctors": [doctor.doctor_name for doctor in department.doctors]
    }