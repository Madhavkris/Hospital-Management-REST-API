from database.connection import db
from models.appointments_model import Appointment

#get appointment by id
def get_appointment_by_id(appointment_id):
    return db.session.get(Appointment, appointment_id)


#get all appointments
def get_all_appointments():
    return db.session.execute(db.select(Appointment)).scalars().all()

def create_appointments(patient_id,doctor_id,appointment_date,appointment_time,status):
   try:
     new_appointment = Appointment(
         patient_id=patient_id,
         doctor_id=doctor_id,
         appointment_date=appointment_date,
         appointment_time=appointment_time,
         status=status
     )
     db.session.add(new_appointment)
     db.session.commit()
     return new_appointment
   except Exception as e:
       db.session.rollback()
       print(e)
       return None
