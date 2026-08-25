from database.connection import db

class Doctor(db.Model):
    __tablename__="doctors"
    doctor_id=db.Column(db.Integer, primary_key=True)
    doctor_name=db.Column(db.String(100),nullable=False)
    specialization=db.Column(db.String(100),nullable=False)
    department_id=db.Column(db.Integer,db.ForeignKey("departments.department_id"),nullable=False)
