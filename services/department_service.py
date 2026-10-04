from database.connection import db
from models.department_model import Department
def get_department_by_id(department_id):
   try:
       department=db.session.get(Department,department_id)
       return department,None
   except Exception as e:
       print(e)
       return None,"Database Error"
def get_all_departments():
    try:
       check_dep= db.session.execute(db.select(Department)).scalars().all()
       return check_dep,None
    except Exception as e:
        print(e)
        return None,"Database Error"
#
def create_department(department_name):
    try:
        new_department = Department(
         department_name = department_name
        )
        db.session.add(new_department)
        db.session.commit()
        return new_department,None
    except Exception as e:
        db.session.rollback()
        print(e)
        return None,"Database Error"

#update
def update_department(department_id, department_name):
    try:
        department,error=get_department_by_id(department_id)
        if error:
            return None,error
        if  department is None:
            return None,None
        department.department_name=department_name
        db.session.commit()
        return department,None
    except Exception as e:
        db.session.rollback()
        print(repr(e))
        return None,"Database Error"

#Partial Update
def partial_update(department_id,data):
    try:
       department,error=get_department_by_id(department_id)
       if error:
           return None,error
       if  department is None:
           return None,None
       if 'department_name' in data:
           department.department_name=data.get('department_name')
       db.session.commit()
       return department,None
    except Exception as e:
        db.session.rollback()
        print(repr(e))
        return None,"Database Error"

