from database.connection import get_connect
def get_all_departments():
    connection=get_connect()
    if not connection:
        return None
    cursor=connection.cursor(dictionary=True)
    cursor.execute("select * from departments")
    results=cursor.fetchall()
    cursor.close()
    connection.close()
    return results