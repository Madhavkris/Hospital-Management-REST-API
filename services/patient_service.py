from database.connection import get_connect
def get_all_patients():
    connection = get_connect()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM patients")
    results=cursor.fetchall()
    cursor.close()
    connection.close()
    return results
