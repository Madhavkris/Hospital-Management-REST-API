from database.connection import get_connect
def get_all_appointments():
    connection=get_connect()
    if not connection:
        return None
    cursor=connection.cursor(dictionary=True)
    query="""select  a.appointment_id, p.patient_name,d.doctor_name, d.specialization,dep.department_name,a.appointment_date,a.appointment_time,a.status from appointments a join patients p on a.patient_id=p.patient_id join doctors d on a.doctor_id=d.doctor_id join departments dep on d.department_id=dep.department_id"""
    cursor.execute(query)
    appointments=cursor.fetchall()
    for appointment in appointments:
        if appointment["appointment_time"] is not None:
            appointment["appointment_time"]=str(appointment["appointment_time"])
    cursor.close()
    connection.close()
    return appointments
def get_appointment_by_id(appointment_id):
    connection=get_connect()
    if not connection:
        return None
    cursor=connection.cursor(dictionary=True)
    query="""select  a.appointment_id, p.patient_name,d.doctor_name, d.specialization,
              dep.department_name,a.appointment_date,a.appointment_time,a.status
              from appointments a join patients p on a.patient_id=p.patient_id join doctors d on a.doctor_id=d.doctor_id join departments dep on d.department_id=dep.department_id where a.appointment_id=%s """
    values=(appointment_id,)
    cursor.execute(query,(appointment_id,))
    appointment=cursor.fetchone()
    if appointment["appointment_time"] is not None:
        appointment["appointment_time"]=str(appointment["appointment_time"])

    cursor.close()
    connection.close()
    return appointment
