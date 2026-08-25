from database.connection import db

class Appointments(db.Model):
    __tablename__='appointments'
    appointment_id=db.Column(db.Integer,primary_key=True)
    patient_id=db.Column(db.Integer,db.ForeignKey("patients.patient_id"),nullable=False)
    doctor_id=db.Column(db.Integer,db.ForeignKey("doctors.doctor_id"),nullable=False)
    appointment_date=db.Column(db.Date,nullable=False)
    appointment_time=db.Column(db.Time,nullable=False)
    status=db.Column(db.String(20),nullable=False,default="Booked")
