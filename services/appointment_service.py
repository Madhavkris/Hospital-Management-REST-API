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
       print("Appointment Error:",repr(e))
       return None
def delete_appointment(appointment_id):
    try:
       appointment = get_appointment_by_id(appointment_id)
       db.session.delete(appointment)
       db.session.commit()
       return appointment
    except Exception as e:
        db.session.rollback()
        print("Appointment Error:",repr(e))
        return None
#update
def update_appointments(appointment_id,patient_id,doctor_id,appointment_date,appointment_time,status):
    try:
        appointment = get_appointment_by_id(appointment_id)
        if not appointment:
            return None
        appointment.patient_id=patient_id
        appointment.doctor_id=doctor_id
        appointment.appointment_date = appointment_date
        appointment.appointment_time = appointment_time
        appointment.status = status
        db.session.commit()
        return appointment
    except Exception as e:
        db.session.rollback()
        print(repr(e))
        return None

def partial_update(appointment_id,data):
    try:
        appointment = get_appointment_by_id(appointment_id)
        if not appointment:
            return None
        if 'patient_id' in data:
            appointment.patient_id = data.get('patient_id')
        if 'doctor_id' in data:
            appointment.doctor_id = data.get('doctor_id')
        if 'appointment_date' in data:
            appointment.appointment_date = data.get('appointment_date')
        if 'appointment_time' in data:
            appointment.appointment_time = data.get('appointment_time')
        if 'status' in data:
            appointment.status = data.get('status')
        db.session.commit()
        return appointment
    except Exception as e:
        db.session.rollback()
        print(repr(e))
        return None
