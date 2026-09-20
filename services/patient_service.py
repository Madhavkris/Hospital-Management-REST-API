from database.connection import db
from models.patient_model import Patient
def get_all_patients():
    return db.session.execute(db.select(Patient)).scalars().all()
def get_patient_by_id(patient_id):
    patient=db.session.get(Patient,patient_id)
    return patient
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
        return new_patient
    except Exception as e:
        db.session.rollback()
        print(e)
        return None


def delete_patient(patient_id):
    try:
       patient=get_patient_by_id(int(patient_id))
       db.session.delete(patient)
       db.session.commit()
       return patient
    except Exception as e:
        db.session.rollback()
        print(repr(e))
        return None

def update_patient(patient_id,patient_name,age,gender,disease):
    try:
        patient=get_patient_by_id(patient_id)
        if not patient:
            return None
        patient.patient_name=patient_name
        patient.age=age
        patient.gender=gender
        patient.disease=disease
        db.session.commit()
        return patient
    except Exception as e:
        db.session.rollback()
        print(repr(e))
        return None