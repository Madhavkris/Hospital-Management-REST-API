from database.connection import db
from models.patient_model import Patient
#GET ALL
def get_all_patients():
    try:
        check_patient=db.session.execute(db.select(Patient)).scalars().all()
        return check_patient,None
    except Exception as e:
        print(e)
        return None,"Database error"
#GET BY ID
def get_patient_by_id(patient_id):
    try:
        patient=db.session.get(Patient,patient_id)
        if patient is None:
            return None,None
        return patient,None
    except Exception as e:
        print(e)
        return None,"Database error"
#create patients
def create_patient(patient_nm,age,gender,disease):
    try:
        new_patient=Patient(
            patient_name=patient_nm,
            age=age,
            gender=gender,
            disease=disease
        )
        db.session.add(new_patient)
        db.session.commit()
        return new_patient,None
    except Exception as e:
        db.session.rollback()
        print(e)
        return None,"Database error"

#DELETE
def delete_patient(patient_id):
    try:
       patient,error=get_patient_by_id(int(patient_id))
       if error:
           return None,error
       if  patient is None:
           return None,None
       db.session.delete(patient)
       db.session.commit()
       return patient,None
    except Exception as e:
        db.session.rollback()
        print(repr(e))
        return None,"Database error"
#PUT/UPDATE
def update_patient(patient_id,patient_name,age,gender,disease):
    try:
        patient,error=get_patient_by_id(patient_id)
        if error:
            return None,error
        if  patient is None:
            return None,None
        patient.patient_name=patient_name
        patient.age=age
        patient.gender=gender
        patient.disease=disease
        db.session.commit()
        return patient,None
    except Exception as e:
        db.session.rollback()
        print(repr(e))
        return None,"Database error"
#PATCH ?PARTIAL UPDATE
def partial_update(patient_id,data):
    try:
        patient,error=get_patient_by_id(patient_id)
        if error:
            return None,error
        if  patient is None:
            return None,None
        if 'patient_name' in data:
            patient.patient_name=data["patient_name"]
        if 'age' in data:
            patient.age=data["age"]
        if 'gender' in data:
            patient.gender=data["gender"]
        if 'disease' in data:
            patient.disease=data["disease"]
        db.session.commit()
        return patient,None
    except Exception as e:
        db.session.rollback()
        print(repr(e))
        return None,"Database error"
