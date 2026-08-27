from database.connection import db
class Department(db.Model):
    __tablename__="departments"
    department_id=db.Column(db.Integer,primary_key=True)
    department_name=db.Column(db.String(100),nullable=False,unique=True)

    #relationship
    doctors = db.relationship("Doctor", back_populates="department")