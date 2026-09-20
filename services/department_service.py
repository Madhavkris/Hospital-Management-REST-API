from database.connection import db
from models.department_model import Department
def get_department_by_id(department_id):
    department=db.session.get(Department,department_id)
    return department
def get_all_departments():
    return db.session.execute(db.select(Department)).scalars().all()

#
def create_department(department_name):
    try:
        new_department = Department(
         department_name = department_name
        )
        db.session.add(new_department)
        db.session.commit()
        return new_department
    except Exception as e:
        db.session.rollback()
        print(e)
        return None

#update
def update_department(department_id, department_name):
    try:
        department=get_department_by_id(department_id)
        if not department:
            return None
        department.department_name=department_name
        db.session.commit()
        return department
    except Exception as e:
        print(repr(e))
        return None
