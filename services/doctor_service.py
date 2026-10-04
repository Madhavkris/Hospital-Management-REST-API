from database.connection import db
from models.doctor_model import Doctor
def get_all_doctors():
    try:
      check_doctor= db.session.execute(db.select(Doctor)).scalars().all()
      return check_doctor,None
    except Exception as e:
        print(e)
        return None,"Database Error"
def get_doctor_by_id(doctor_id):
    try:
        doctor=db.session.get(Doctor,doctor_id)
        if doctor is None:
            return None,None
        return doctor,None
    except Exception as e:
        print(e)
        return None,"Database Error"
def create_doctor(doctor_name,specialization,department_id):
    try:
        new_doctor=Doctor(
            doctor_name=doctor_name,
            specialization=specialization,
            department_id=department_id
        )
        db.session.add(new_doctor)
        db.session.commit()
        return new_doctor,None
    except Exception as e:
        db.session.rollback()
        print(e)
        return None,"Database Error"

def delete_doctor(doctor_id):
    try:
       doctor,error=get_doctor_by_id(doctor_id)
       if error:
           return None,error
       if doctor is None:
           return None,None
       db.session.delete(doctor)
       db.session.commit()
       return doctor,None
    except Exception as e:
        db.session.rollback()
        print(e)
        return None,"Database Error"

def update_doctor(doctor_id,doctor_name,specialization,department_id):
    try:
        doctor,error=get_doctor_by_id(doctor_id)
        if error:
            return None,error
        if doctor is None:
            return None,None
        doctor.doctor_name=doctor_name
        doctor.specialization=specialization
        doctor.department_id=department_id
        db.session.commit()
        return doctor,None
    except Exception as e:
        print(repr(e))
        db.session.rollback()
        return None,"Database Error"

def partial_update(doctor_id,data):
    try:
        doctor,error=get_doctor_by_id(doctor_id)
        if error:
            return None,error
        if doctor is None:
            return None,None
        if 'doctor_name' in data:
            doctor.doctor_name=data.get('doctor_name')
        if 'specialization'  in data:
            doctor.specialization=data.get('specialization')
        if 'department_id'  in data:
            doctor.department_id=data.get('department_id')
        db.session.commit()
        return doctor,None
    except Exception as e:
        db.session.rollback()
        print(repr(e))
        return None,"Database Error"