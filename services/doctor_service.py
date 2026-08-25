from database.connection import get_connect
def get_all_doctors():
    connection = get_connect()
    if not connection:
        return None
    cursor = connection.cursor(dictionary=True)
    query = """
        SELECT
            d.doctor_id,
            d.doctor_name,
            d.specialization,
            dep.department_name
        FROM doctors d
        JOIN departments dep
            ON d.department_id = dep.department_id
    """
    cursor.execute(query)
    doctors = cursor.fetchall()
    cursor.close()
    connection.close()
    return doctors