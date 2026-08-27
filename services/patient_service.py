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


